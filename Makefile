clean:
	rm -f *.egg-info
	rm -rf dist

publish:
	python setup.py sdist upload

.PHONY: publish
