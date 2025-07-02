.PHONY: lint

# Code quality
lint:
	pre-commit run --all-files

runapp:
	# Run the application
	cd app && \
	python main.py
