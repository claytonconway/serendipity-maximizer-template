"""Tests for pure discovery scoring functions."""

from serendipity_maximizer.discovery.scoring import rank_candidates, score_idea


def test_score_idea_basic():
    s = score_idea(impact=0.9, serendipity=0.8, effort=0.4)
    assert s > 1.0
    assert isinstance(s, float)


def test_score_idea_low_swap_penalty():
    normal = score_idea(0.9, 0.8, 0.4, low_swap_penalty=1.0)
    penalized = score_idea(0.9, 0.8, 0.4, low_swap_penalty=0.6)
    assert penalized < normal


def test_rank_candidates():
    cands = [
        {"idea": "a", "final_score": 0.3},
        {"idea": "b", "final_score": 0.9},
    ]
    ranked = rank_candidates(cands)
    assert ranked[0]["idea"] == "b"
