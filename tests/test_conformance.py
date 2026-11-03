"""PlumCraft's conformance checks: what every engine must do, in process and over HTTP."""

from plumcraft_engine.conformance import assert_conformant

from atlas_engine import AtlasEngine


def test_the_engine_is_conformant(demo):
    assert_conformant(AtlasEngine, demo=demo, slow="atlas.slow")
