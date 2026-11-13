# AI Contributions — Atlas for PlumCraft

*About AI slop.* Fair enough: a machine generated this, and its generator was written by a machine too. Call it instant ramen: fast, cheap, genuinely edible, and nobody should pretend it simmered on a stove all afternoon. The honest answer isn't a claim about quality. It's the record below: what the maintainer asked for, what the model did, and what went wrong, including the defects that the test suite and PlumCraft's conformance suite caught. Bon appétit, but mind the sodium content.

Tracks what AI helpers contributed to Atlas versus the human maintainer.

## Human maintainer

The maintainer wrote PlumCraft and its Python engine SDK, and directed the `plumcraft-engine new` generator that made this project. Atlas is that generator's output with every type it offers (scalars, text, table, array, SVG, image, audio, list, any): a sample engine, and a starting point to copy. Its nodes are the template's examples.

## Contributions

### 2026-11-13 — The SDK pin moved to PlumCraft 0.7.0: commonkit's hash switch (Claude Opus 5.5)

**What the maintainer asked for:** the commonkit hash facade, layer 3 (plum `docs/plans/2026-11-12-commonkit-hash-facade.md` §3.8, the maintainer's D23 1a): move the PlumCraft dependents onto the release that hashes through commonkit's facade, so every handle is in one algorithm, chosen by commonkit's `HASH` (the store's `.policy.json`, then `COMMONKIT_HASH`, then `b3`).

**What the AI did:**
- `pyproject.toml` (1+1 lines): the SDK's `rev` moves from `81dd28f` to `34f6aea`, the commit tagged `plumcraft-v0.7.0`. `uv.lock` (+99 −6): `plumcraft-engine` 0.2.0, `pyuncommonkit` 0.2.0 and `blake3` 1.0.11.
- `tests/test_hash.py` (85 lines, the same in the three engines): under md5 and then b3, each in a child process with a fresh `COMMONKIT_STORE_ROOT`, `COMMONKIT_HASH` and `COMMONKIT_MARK_DIR`, the engine's hello reports exactly `[algo]`, commonkit's stderr line names the algorithm and its source, every handle the demo returns and an array published through the SDK's data plane are `<algo>:` with the algorithm's length, and no `shm_*` marker is left.

The engine has no hashing of its own: every handle comes from the SDK.

**Tests failed before the code:** at `81dd28f` the test fails in the child with `KeyError: 'algos'` (the old hello has no `data.algos`); checked on opencv-engine.

**Checked** (through plum's `hf2_env.py`, a fresh store per run): `uv run pytest` under md5 and under b3 (31 passed each), and `scripts/conform` under both with PlumCraft 0.7.0's `plumcraft` binary on `PLUMCRAFT_BIN` (14 of 14 cases; this repo's script runs only the Python half); `ruff check` and `ruff format --check`. No marker but `.started` in any run.

**Defects in AI-written code:** the first draft of the test published its array with no inline budget and no shared store, which the SDK refuses; caught by running it.

### 2026-11-04 — The SDK pin moved to PlumCraft's Windows support (Claude Opus 5.5)

The maintainer installed this engine from PlumCraft's editor on Windows. It registered and appeared, then died on start: `module 'socket' has no attribute 'AF_UNIX'`. The SDK was pinned to PlumCraft `3995cb7`, from before PlumCraft ran on Windows, and Windows Python has no Unix sockets. The maintainer: "bump the engine pins".

The AI moved the pin to PlumCraft `81dd28f` (`main`, merging PR #19, "PlumCraft on Windows"). There the SDK also reads a `tcp:127.0.0.1:<port>` locator, which the host offers on Windows. `uv.lock` was regenerated. `scripts/check` passes: ruff, format, and 29 tests on macOS.

The same SDK had already been tried on Windows: on `win11-dev`, with the installed OpenCV engine's SDK swapped for the checkout. A fresh install there with this pin hasn't been tried.

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
