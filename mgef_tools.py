"""Generate console commands from MGEF records without overwriting outputs."""
import argparse
import itertools
from pathlib import Path
import re

FORM_ID = re.compile(r"^[0-9A-Fa-f]{8}$")
RECORD = re.compile(r"^\s*MGEF.*?\(([^()]*)\)")


def parse_effects(lines):
    effects = set()
    for number, line in enumerate(lines, 1):
        if not line.lstrip().startswith("MGEF"):
            continue
        match = RECORD.search(line)
        if not match or not FORM_ID.fullmatch(match.group(1).strip()):
            raise ValueError(f"Invalid MGEF form ID on line {number}")
        effects.add(match.group(1).strip().upper())
    return sorted(effects)


def commands(effects, item, pairs=False, limit=10000):
    if not FORM_ID.fullmatch(item):
        raise ValueError("Item ID must contain exactly eight hexadecimal digits")
    count = len(effects) + (len(effects) * (len(effects) - 1) // 2 if pairs else 0)
    if count > limit:
        raise ValueError(f"Command count {count} exceeds limit {limit}")
    for effect in effects:
        yield f"playerenchantobject {item.upper()} {effect}"
    if pairs:
        for first, second in itertools.combinations(effects, 2):
            yield f"playerenchantobject {item.upper()} {first} {second}"


def write_new(path, lines):
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        for line in lines:
            stream.write(line + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--item", default="000139A3")
    parser.add_argument("--pairs", action="store_true")
    parser.add_argument("--limit", type=int, default=10000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.input.stat().st_size > 8 * 1024 * 1024:
        parser.error("Input exceeds 8 MiB")
    try:
        effects = parse_effects(args.input.read_text(encoding="utf-8-sig").splitlines())
        result = list(commands(effects, args.item, args.pairs, args.limit))
        if args.output:
            write_new(args.output, result)
        else:
            print("\n".join(result))
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
