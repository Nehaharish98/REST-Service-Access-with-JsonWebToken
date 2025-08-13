PYTHON=python3.13.5

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest tests/test_script.py

lint:
	flake8 .

format:
	black .

precommit:
	pre-commit run --all-files

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
