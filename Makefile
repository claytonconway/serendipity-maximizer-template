.PHONY: setup install dev-install run-serendipity demo test lint format clean

# --- Setup ---
setup: install

install:
	pip install -e .

dev-install:
	pip install -e ".[dev,llm,notebooks]"
	pre-commit install || true

# --- Run ---
run-serendipity:
	python -m serendipity_maximizer.orchestrators.supervisor_graph

demo: run-serendipity

# Quick smoke without installing (uses python path)
demo-direct:
	PYTHONPATH=src python -m serendipity_maximizer.orchestrators.supervisor_graph

# --- Quality ---
test:
	pytest -q --tb=short

lint:
	ruff check src tests
	ruff format --check src tests || true

format:
	ruff format src tests
	ruff check --fix src tests

# --- Maintenance ---
clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

# Future CCDS-style targets (adapt for agents)
data:
	@echo "TODO: implement data download / generation pipeline (see references/ and agents/packs/)"

train:  # "train" in this context = fine-tune or register new specialists / embeddings
	@echo "TODO: specialist training / embedding index build step"

reports:
	@echo "TODO: generate reports/figures from latest register + scores"