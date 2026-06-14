from src.serendipity_maximizer.discovery.recombination import recombine


def test_recombine_produces_budget_items():
    signals = ["foo", "bar", "baz", "maritime", "sensor"]
    ideas = recombine(signals, budget=5, seed=123)
    assert len(ideas) <= 5
    assert all("recombination" in i for i in ideas)
