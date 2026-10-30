# MGEF command tools

Small offline Python utilities that extract MGEF form IDs from text and generate
`playerenchantobject` command lines. No third-party Python dependencies or network
access are required. Python 3.10 or newer is recommended.

```sh
python mgef_tools.py examples/effects.txt
python mgef_tools.py examples/effects.txt --item 0006B46B --pairs --output new_commands.txt
python -I -S -B -m unittest discover -s tests
```

Input records begin with `MGEF` and contain an eight-digit hexadecimal ID in
parentheses. Other lines are ignored. IDs are validated, normalized, deduplicated
and sorted. Pair generation has a configurable command-count cap. Output files
are created exclusively; an existing file is never overwritten by the new CLI.
The generated commands were tested as text only, not in any game engine.

## Preserved original scripts

`legacy/create_files.py` and `legacy/ench_robe.py` preserve the original scripts.
They scan their current working directory and can overwrite output text files.
If needed, run them only in a separate scratch directory. The new CLI is the
recommended entry point. Original record collections and generated outputs are
deliberately excluded; the example records are fictional.

## Provenance and license

This repository imports a preserved local snapshot and adds an explicit-input,
validated CLI and seven isolated tests. Commits record the actual import and
improvement work on 2026-10-30; no historical timeline is reconstructed.
Original code is proprietary; see `LICENSE`. Existing external rights are retained.
