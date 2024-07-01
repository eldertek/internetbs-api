SHELL=/bin/bash
PYTHON=python3
PKG_NAME=internetbs-api
VERSION=0.0.2
default: | clean check_tags bundle upload
	@echo "Full service complete"

clean:
	@echo "Removing the build/ dist/ and *.egg-info/ directories"
	@rm -rf build dist *.egg-info

check_tags:
	@echo "Making sure that a tag has been created with the correct version number (${VERSION})"; \
	TAGS=`git tag -l ${VERSION}`; \
	if echo $$TAGS | grep -q ${VERSION}; then echo "Found tag for version ${VERSION}"; \
	else echo "No git tag '${VERSION}' found. You can create it with the following command:"; \
	echo; echo "git tag ${VERSION} && git push --tags origin"; echo; exit 1; fi

bundle:
	@echo "Bundling the code"; echo
	@VERSION=${VERSION} ${PYTHON} setup.py sdist bdist_wheel

upload:
	@echo "Uploading built package to PyPI"
	@${PYTHON} `which twine` upload dist/*

upload_test:
	@echo; echo "Uploading built package to Test PyPI"
	@${PYTHON} `which twine` upload dist/* -r testpypi