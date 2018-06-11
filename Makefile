VERSION=`cat VERSION`

# Test

.PHONY: test
test:	## Execute tests suites
	python3 -m unittest discover -v

.PHONY: cover
cover:	## Generate coverage information
	coverage3 run --omit=*.venv*,setup.py --source=./youtube-data-api -m unittest discover

.PHONY: coverage-html
coverage-html:	cover ## HTML report
	coverage3 html --directory=.cover --omit=*.venv*,setup.py

.PHONY: coveralls
coveralls:	## Coverage to coveralls report
	coveralls --data_file=.coverage --coveralls_yaml=.coveralls.yml --base_dir=./youtube-data-api

dist:		## Generate distribution packages
	python3 setup.py sdist bdist_wheel

dist-publish:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

include Makefile.help.mk
