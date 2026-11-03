"""`python -m atlas_engine`: this engine as a process. PlumCraft starts it with
`PLUMCRAFT_ENGINE_SOCKET` and `PLUMCRAFT_ENGINE_TOKEN` set; `--listen 127.0.0.1:7311` serves HTTP,
for Engine › Attach and `plumcraft-engine run --attach`."""

import sys

from atlas_engine import AtlasEngine


def main() -> int:
    return AtlasEngine.serve()


if __name__ == "__main__":
    sys.exit(main())
