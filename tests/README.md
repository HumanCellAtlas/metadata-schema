# Running the schema tests

You will need node.js to run the tests

- Get Node.js: https://nodejs.org/en/ (v8.11.1 LTS)

- If you use [Homebrew](https://brew.sh/) you can install node by doing:
```
brew install node
```

After installation check that everything is correctly installed and which versions you are running:
```
node -v
npm -v
```

## Run the test suite
```
cd tests
npm install
npm test
```