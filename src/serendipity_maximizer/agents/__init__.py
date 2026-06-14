"""Agent definitions and base classes for the Serendipity Maximizer.

Per AI-RULES: Production agent code lives here (orchestrators call these).
YAML packs live at top-level agents/packs/.
"""

from .base import BaseSpecialist
from .scoring import ImpactScorer
from .serendipity import SerendipityDiscoverer

__all__ = ["BaseSpecialist", "SerendipityDiscoverer", "ImpactScorer"]
