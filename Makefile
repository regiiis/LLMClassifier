.PHONY: lint

# Code quality
lint:
	pre-commit run --all-files
