from setuptools import setup


setup(
    name = "schema_linter",
    description = "Script to lint the schemas",
    url = "https://github.com/HumanCellAtlas/metadata-schema/",
    python_requires = ">=3.6",
    entry_points = {'console_scripts': [
        "schema_linter = src.schema_linter:main"
        ]
    }
)