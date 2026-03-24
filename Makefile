TEST_DIR := test-initial-commit

.PHONY: dev clean run build publish

dev:
	pip install -e .

clean:
	rm -rf $(TEST_DIR)/*

run:
	cd $(TEST_DIR) && initial-commit

build:
	pip install build --quiet
	python -m build

publish: build
	pip install twine --quiet
	twine upload dist/*