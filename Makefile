.PHONY: setup run-serendipity test

setup:
	pip install -e .

run-serendipity:
	python -m serendipity_maximizer.orchestrators.supervisor_graph

test:
	pytest