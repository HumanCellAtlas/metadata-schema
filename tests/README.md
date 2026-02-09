# Running the schema tests

You will need node.js to run the tests

- Get Node.js: https://nodejs.org/en/ (v18 LTS)

- If you use [Homebrew](https://brew.sh/) you can install node by doing:
```
brew install node@18
```

After installation check that everything is correctly installed and which versions you are running:

```bash
node -v
npm -v
```

## Run the test suite

```bash
cd tests
npm install
npm test
```

### Running in vs code

The tests are visible in the "Testing" sidebar after installing [Mocha Test Explorer](https://marketplace.cursorapi.com/items/?itemName=hbenl.vscode-mocha-test-adapter)
