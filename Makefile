env:
	echo making virtual env in ~/venv-grAIde
	python3 -m venv ~/venv-grAIde
	echo "run . ~/venv-grAIde/bin/activate"
init: env
	pip install -r requirements.txt
	pip install pyinstaller

test:
	py.test tests

exe:
	pyinstaller grade.py grade.spec

.PHONY: env exe init test
