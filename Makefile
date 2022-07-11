
PYTHON=.venv/bin/python
SRC=src
TESTS=tests

test: test-python test-node

.PHONE: test-python
test-python: $(TESTS)/python/*.py $(SRC)/*.py
	PYTHONPATH=$(SRC) $(PYTHON) -munittest discover --start $(TESTS)/python

$(TESTS)/package.json:

$(TESTS)/node_modules/: $(TESTS)/package.json
	cd $(TESTS) ; npm install ; touch node_modules/

.PHONE: test-node
test-node: $(TESTS)/schema.test.js $(TESTS)/node_modules
	cd $(TESTS) ; npm test