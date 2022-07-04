#!/usr/bin/env python3

"""
Script that outputs a modified version of a passed INI file based on the changes
it's told to make.

This can be used from chezmoi's modify_*.tmpl scripts as follows:
#!/bin/bash
TO_ADD='
{
    "SECTION NAME": {
        "KEY": "NEW VALUE"
    }
}
'
{{ joinPath .chezmoi.sourceDir "lib/modify_ini_file.py" }} "$TO_ADD"
"""

import json
import re
import sys

SECTIONS_TO_MODIFY = json.loads(sys.argv[1])

section_name_pattern = "|".join(re.escape(name) for name in SECTIONS_TO_MODIFY)
SECTION_PATTERN_RE = re.compile(rf"\[({section_name_pattern})\]\n[\s\S]*?\n(?=\n|$)")

original_contents = sys.stdin.read()
FOUND_SECTIONS = set()


def repl(match: re.Match[str]) -> str:
    FOUND_SECTIONS.add(match.group(1))
    found_keys = set()
    to_add = SECTIONS_TO_MODIFY[match.group(1)]
    lines = match.group(0).splitlines(keepends=True)
    for idx, line in enumerate(lines):
        key, _, value = line.partition("=")
        if not value:
            continue
        found_keys.add(key)
        new_value = to_add.get(key)
        if new_value is not None:
            lines[idx] = f"{key}={to_add[key]}\n"

    for key, value in to_add.items():
        if key not in found_keys:
            lines.append(f"{key}={value}\n")

    return f"{''.join(lines)}"


if original_contents:
    lines = SECTION_PATTERN_RE.sub(repl, original_contents).splitlines(keepends=True)
else:
    lines = []

for section_name, to_add in SECTIONS_TO_MODIFY.items():
    if section_name in FOUND_SECTIONS:
        continue
    lines.append(f"[{section_name}]\n")
    for key, value in to_add.items():
        lines.append(f"{key}={value}\n")
    lines.append("\n")
lines.pop()
print("".join(lines), end="")
