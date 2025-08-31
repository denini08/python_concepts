# Types and More

## General 
* Python is dynamically typed language, obviously (thanks Copilot xD)
* type hintining vs type checking vs data validation
  * `type hinting` -> *what we expect something to be?* -> hints for developers and tools (linters, IDEs, type checkers)
  * `type checking` -> *static analysis* -> checking types at 'compile' time (mypy, pyright)
  * `data validation` -> *checking data at runtime* -> e.g. pydantic
* for lots of packages you need to install additional package for type checking, e.g. `pip install types-requests`
* general rule of thumb:
  * inputs -> generic
  * outputs -> specific
* flow: `untyped -> type hints -> dictionary with types keys/values -> dictionary with typed values -> dataclass with typed attributes`

## References
* [corey schafer avesome yt 1](https://youtu.be/fM4O9bModsE)
* [corey schafer avesome yt 2](https://youtu.be/RwH2UzC2rIo)
