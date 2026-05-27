#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

LIST_FILE = Path(__file__).resolve().parent.parent / "apps-direct-domains.list"

RULE_RE = re.compile(
    r"^(DOMAIN-SUFFIX|DOMAIN|DOMAIN-KEYWORD),"
    r"([A-Za-z0-9](?:[A-Za-z0-9.\-]*[A-Za-z0-9])?),"
    r"(DIRECT|REJECT|PROXY)$"
)

DOMAIN_LABEL_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


def validate_domain(domain: str) -> str | None:
    if len(domain) > 253:
        return "domain too long (>253 chars)"
    if domain.startswith(".") or domain.endswith("."):
        return "leading or trailing dot"
    if ".." in domain:
        return "double dot"
    labels = domain.split(".")
    if len(labels) < 2:
        return "needs at least one dot (e.g. example.com, not just 'localhost')"
    for label in labels:
        if not DOMAIN_LABEL_RE.match(label):
            return f"invalid label '{label}'"
    return None


def main() -> int:
    if not LIST_FILE.exists():
        print(f"❌ Rule file not found: {LIST_FILE}", file=sys.stderr)
        return 1

    text = LIST_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    errors: list[str] = []
    warnings: list[str] = []
    seen: dict[tuple[str, str], int] = {}
    rule_count = 0
    category_counts: dict[str, int] = defaultdict(int)
    current_category = "(uncategorized)"

    for lineno, raw in enumerate(lines, 1):
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("#"):
            cat_match = re.match(r"^#\s*===\s*(.+?)\s*===\s*$", stripped)
            if cat_match:
                current_category = cat_match.group(1)
            continue

        if line != line.rstrip():
            warnings.append(f"line {lineno}: trailing whitespace")

        match = RULE_RE.match(stripped)
        if not match:
            errors.append(f"line {lineno}: malformed rule: {stripped!r}")
            continue

        rule_type, domain, target = match.groups()

        domain_error = validate_domain(domain)
        if domain_error:
            errors.append(f"line {lineno}: {domain_error}: {domain!r}")
            continue

        key = (rule_type, domain.lower())
        if key in seen:
            errors.append(
                f"line {lineno}: duplicate {rule_type},{domain} "
                f"(first at line {seen[key]})"
            )
            continue
        seen[key] = lineno

        rule_count += 1
        category_counts[current_category] += 1

    print(f"✓ Validated {LIST_FILE.name}")
    print(f"  Total rules: {rule_count}")
    print(f"  Categories ({len(category_counts)}):")
    for cat, n in sorted(category_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"    - {cat}: {n}")

    if warnings:
        print(f"\n⚠ {len(warnings)} warning(s):")
        for w in warnings:
            print(f"  {w}")

    if errors:
        print(f"\n❌ {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1

    print("\n✓ All checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
