# AI Contributions — Atlas for PlumCraft

*About AI slop.* Fair enough: a machine generated this, and its generator was written by a machine too. Call it instant ramen: fast, cheap, genuinely edible, and nobody should pretend it simmered on a stove all afternoon. The honest answer isn't a claim about quality. It's the record below: what the maintainer asked for, what the model did, and what went wrong, including the defects that the test suite and PlumCraft's conformance suite caught. Bon appétit, but mind the sodium content.

Tracks what AI helpers contributed to Atlas versus the human maintainer.

## Human maintainer

The maintainer wrote PlumCraft and its Python engine SDK, and directed the `plumcraft-engine new` generator that made this project. Atlas is that generator's output with every type it offers (scalars, text, table, array, SVG, image, audio, list, any): a sample engine, and a starting point to copy. Its nodes are the template's examples.

## Contributions

### 2026-11-03 — Published, with `register` (Claude Opus 5.5)

The maintainer: "Let's get the python engines (duckdb, opencv, ?) into one or more public repos". They chose one repo per engine, named `plumcraft-<name>-engine`, and the SDK pinned to PlumCraft's pushed `headless-write-files` commit until a release.

The AI:

- pinned the SDK to that commit over https, in place of a path on the maintainer's machine;
- added the MIT and Apache 2.0 licences, PlumCraft's;
- put `examples/` in the wheel, so `register` finds the demo;
- wrote the Install section: `uv tool install git+…`, then `<engine> register`.

The tests and ruff passed against the SDK fetched from GitHub.

### 2026-10-30 — Generated (Claude Opus 5.5)

The project was made by `plumcraft-engine new` with every type, in an AI session testing the generator. No code was written by hand.
