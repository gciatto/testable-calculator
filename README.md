# Calculator

A simple calculator toolkit written in Python, with several UIs, tests, and quality assurance facilities.

## Remarks

UI code is clearly separated from the business logic. 
Actually, two sorts of UIs are provided: a command-line interface (CLI) and a graphical user interface (GUI), 
based on [Kivy](https://kivy.org/).

Tests are provided for the business logic, for the CLI, and for the GUI.
All test cases are written using the [`unittest`](https://docs.python.org/3/library/unittest.html) framework.
Test code is clearly separated from the main code: it is placed in a `tests` directory.

Quality assurance facilities include:
- test coverage
- static code analysis

## Requirements

- Python 3.11
- Kivy 2.3

### Development requirements

- [Coverage.py](https://coverage.readthedocs.io/en/7.4.3/) 7.4.0
- [Mypy](https://mypy.readthedocs.io/en/stable/) 1.9.0
- [Pytest](https://docs.pytest.org/en/8.0.x/) 8.1.0


## How to run the calculator

The software can be run as either a __desktop app__ or a __command-line__ tool.

> Recall restoring the dependencies before running the app for the first time.

### Running the calculator as a desktop app

Open a shell in this directory, and run the following command:

```bash
python -m calculator.ui.gui
```

### Running the calculator as a command-line tool

Open a shell in this directory, and run the following command:

```bash
python -m calculator.ui.cli EXPRESSION
```

where `EXPRESSION` is a mathematical expression to be evaluated.


## How to restore dependencies

Open a shell in this directory, and run the following command:

```bash
pip install -r requirements-dev.txt
```

This shall restore also the dependencies from the `requirements.txt` file.

## How to run tests from the command line

> Assumption: you have restored the dependencies.

You may exploit the following commands to run __all__ the tests:

```bash
python -m unittest discover -v -s tests
```

> While running the tests, the calculator GUI may quickly appear and disappear, multiple times. 
> This is normal, as the tests are exercising the GUI.

You may exploit the following commands to run __only__ the tests for the business logic:

```bash
python -m unittest discover -v -s tests -p 'test_model.py'
```

A similar command may be exploited to test just the CLI (`test_cli.py`) or the GUI (`test_gui.py`).

## How to run tests from the VS Code GUI

> Assumption: you have restored the dependencies, and you are using Visual Studio Code.

Lunch configurations are already provided in the `.vscode` directory.

You may switch to the "Run and Debug" view, and select the desired configuration from the dropdown menu.

Instructions here: <https://code.visualstudio.com/docs/editor/debugging>

## How to perform quality assurance checks

### Test coverage

> Assumption: you have restored the dependencies.

Open a shell in this directory, and run the following commands (2 commands in a row):

```bash
python -m coverage run -m unittest discover -v -s tests
python -m coverage report -m
```

The output should be similar to the following:

```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
calculator\__init__.py      38      3    92%   13, 39, 48
calculator\ui\cli.py        21      3    86%   16-17, 27
calculator\ui\gui.py        57      8    86%   57-59, 63, 65, 67, 71, 78
tests\test_cli.py           15      0   100%
tests\test_gui.py           30      0   100%
tests\test_model.py         38      0   100%
------------------------------------------------------
TOTAL                      199     14    93%
```

You may make the output more pleasant, by generating a HTML report:

```bash
python -m coverage html
```

Then, open the generated file `htmlcov/index.html` in your web browser.

### Compile the code to check for syntax / import errors

> Assumption: you have restored the dependencies.

Open a shell in this directory, and run the following command:

```bash
python -m compileall calculator tests
```

If no error is printed, the code is free from syntax / import errors.

### Static code analysis

> Assumption: you have restored the dependencies.

Open a shell in this directory, and run the following command:

```bash
python -m mypy calculator tests
```

The output should be similar to the following:

```text
calculator\__init__.py:13: error: Unsupported operand types for + ("str" and "int")  [operator]
calculator\__init__.py:44: error: Parameterized generics cannot be used with class or instance checks  [misc]
calculator\__init__.py:44: error: Argument 2 to "isinstance" has incompatible type "<typing special form>"; expected "_ClassInfo"  [arg-type]
calculator\__init__.py:46: error: Returning Any from function declared to return "int | float"  [no-any-return]
Found 4 errors in 1 file (checked 6 source files)
```
