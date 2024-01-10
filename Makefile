install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

int:
	poetry run flake8 brain_games

reinstall:
	python3 -m pip install dist/*.whl --force-reinstall
