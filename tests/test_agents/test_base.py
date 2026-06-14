"""Basic agent structure tests."""

from src.serendipity_maximizer.agents.base import BaseSpecialist
from src.serendipity_maximizer.agents.scoring import ImpactScorer
from src.serendipity_maximizer.agents.serendipity import SerendipityDiscoverer


def test_specialists_are_instantiable_and_buildable():
    disc = SerendipityDiscoverer()
    ImpactScorer()  # ensure instantiable (scorer not used beyond construction in this smoke test)

    assert isinstance(disc, BaseSpecialist)
    assert disc.name == "serendipity_discoverer"

    # Build should return something callable (demo impl returns fn with .name)
    built = disc.build(model=None)
    assert callable(built) or hasattr(built, "invoke") or hasattr(built, "ainvoke")
