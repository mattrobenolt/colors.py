clean:
	rm -rf *.egg-info
	rm -rf dist

publish:
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

.PHONY: clean publish
