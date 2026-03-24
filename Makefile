TEST_DIR := test-initial-commit

.PHONY: dev clean run build publish

dev:
	pip install -e .

init:
	mkdir -p $(TEST_DIR)

clean:
	rm -rf $(TEST_DIR)/*

run:
	cd $(TEST_DIR) && initial-commit

build:
	rm -rf dist
	python -m build

check: build
	twine check dist/*

publish: build
	twine upload dist/*