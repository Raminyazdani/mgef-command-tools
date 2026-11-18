# MGEF command tools

Small offline Python utilities that extract MGEF form IDs from text and generate
`playerenchantobject` command lines. No third-party Python dependencies or network
access are required. Python 3.10 or newer is recommended.

## Quick start

Run the following from the repository root with Python 3.10+ and a POSIX shell.
The bundled `examples/effects.txt` contains two fictional records.

```text
MGEF Example One (00000001)
MGEF Example Two (00000002)
```

Print single-effect commands and their one possible pair for a sample item.

```sh
python mgef_tools.py examples/effects.txt --item 0006B46B --pairs
```

Expected standard output is three lines.

```text
playerenchantobject 0006B46B 00000001
playerenchantobject 0006B46B 00000002
playerenchantobject 0006B46B 00000001 00000002
```

To save those lines, choose a new filename in an existing directory.

```sh
demo_dir="$(mktemp -d)"
python mgef_tools.py examples/effects.txt --item 0006B46B --pairs --output "$demo_dir/commands.txt"
cat "$demo_dir/commands.txt"
```

The generator writes the three lines to the file. Running the same command
again with that output path exits with status 2 and leaves the file intact.

Run the isolated tests from the repository root.

```sh
python -I -S -B -m unittest discover -s tests
```

Input records begin with `MGEF` and contain an eight-digit hexadecimal ID in
parentheses. Other lines are ignored. The CLI validates, normalizes, deduplicates
and sorts IDs. Use `--limit` to cap the total number of commands (default 10,000).
The example verifies the generated text. Game-engine behavior is untested.

## Preserved original scripts

The scripts in `legacy/` read from their current working directory.
`create_files.py` attempts to read every file and writes `maani_add.txt`
and `mgef_add.txt`. `ench_robe.py` scans `.txt` files and writes `ench_robe.txt`.
Both can overwrite existing outputs. Run them only in a separate scratch directory
containing disposable inputs. Use `mgef_tools.py` for explicit input and exclusive
output creation. Original record collections and generated outputs are excluded.

## Provenance and license

This repository imports a preserved local snapshot and adds an explicit-input,
validated CLI and seven isolated tests. Commits record the actual import and
improvement work on 2026-10-30; no historical timeline is reconstructed.
Original code is proprietary; see `LICENSE`. Existing external rights are retained.
