# Testing Commands Cheat Sheet

Quick reference for common test-related commands in this repository.

## Quick checks

```bash
python3 -m unittest
python3 -m unittest discover -s tests
```

Tips:
- Use `python3 -m unittest` for the simplest default run.
- Use explicit discovery when you want to make the test root obvious.

## Run the full test suite

```bash
python3 -m unittest discover -s tests
poetry run python3 -m unittest discover -s tests
```

Tips:
- Prefer `poetry run ...` when the project depends on a Poetry-managed virtual
  environment.
- Prefer the plain `python3` form when you only need the standard library test
  runner.

## Run one test module

```bash
python3 -m unittest tests.test_domain_structure
poetry run python3 -m unittest tests.test_domain_structure
```

Tips:
- Use the dotted module path, not the file system path.
- This is the fastest way to re-run one focused test file while iterating.

## Run one test case or one test method

```bash
python3 -m unittest tests.test_domain_structure.DomainStructureTestCase
python3 -m unittest tests.test_domain_structure.DomainStructureTestCase.test_domain_packages_import
```

Tips:
- Run a test case when you are iterating on one behavior area.
- Run a single method when isolating a failure.

## Verbose output

```bash
python3 -m unittest -v
python3 -m unittest discover -s tests -v
```

Tips:
- Use `-v` to show each test name as it runs.
- Verbose output is useful when reviewing discovery behavior or failures.

## Fail fast

```bash
python3 -m unittest -f
python3 -m unittest discover -s tests -f
```

Tips:
- `-f` stops on the first failure.
- This is useful when fixing a broken suite in small steps.

## Buffer output

```bash
python3 -m unittest -b
python3 -m unittest discover -s tests -b
```

Tips:
- `-b` hides `print()` output for passing tests.
- Buffered mode keeps logs shorter when debugging a noisy suite.

## Combine useful flags

```bash
python3 -m unittest discover -s tests -v -f
python3 -m unittest discover -s tests -v -b
```

Tips:
- `-v -f` is a good combination for quick feedback.
- `-v -b` is useful when you want names without excessive passing output.

## Run tests through Poetry

```bash
poetry run python3 -m unittest
poetry run python3 -m unittest discover -s tests -v
```

Tips:
- Use this when you want consistent execution inside the project environment.
- `poetry run` avoids relying on shell activation state.

## Common workflow

```bash
poetry install
poetry run python3 -m unittest discover -s tests -v
python3 -m unittest tests.test_domain_structure
```

## Common issues

- If `python` is not available, use `python3`.
- If a test module is not found, check whether you used the dotted module path.
- If discovery returns zero tests, confirm the file name starts with
  `test_` and that it lives under `tests/`.
- If imports fail, confirm the code under test is reachable from the current
  environment or virtual environment.
