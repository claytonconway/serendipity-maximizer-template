"""Discovery, recombination, scoring, and registers.

Core of the Serendipity Maximizer 'secret sauce'.
"""

from .recombination import recombine
from .register import IdeaRegister
from .scoring import score_idea

__all__ = ["score_idea", "recombine", "IdeaRegister"]
