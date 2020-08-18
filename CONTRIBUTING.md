# Contributing to SE_Team03

Thank you and congratulations on your decision to contribute to this open source project.

This project follows certain guidelines (not rules) to maintain uniformity and standardize the code across the repository. New developers are open to suggest changes to the current guidelines by submitting a new pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [JavaScript Styleguide](#javascript-styleguide)
  * [Python Styleguide](#python-styleguide)

## Code of Conduct

All developers contributing to this project abide by the [Code of Conduct](CODE_OF_CONDUCT.md) defined for this project. Violations should be reported at  [pushkarsdravid@gmail.com](mailto:pushkarsdravid@gmail.com).
Please follow these steps to have your contribution considered by the maintainers:


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Attach issue id in the commit message for easier tracking

### JavaScript Styleguide

All JavaScript must adhere to [JavaScript Standard Style](https://standardjs.com/).

* Prefer the object spread operator (`{...anotherObj}`) to `Object.assign()`
* Inline `export`s with expressions whenever possible
  ```js
  // Use this:
  export default class ClassName {

  }

  // Instead of:
  class ClassName {

  }
  export default ClassName
  ```
* Place requires in the following order:
    * Built in Node Modules (such as `path`)
    * Built in Atom and Electron Modules (such as `atom`, `remote`)
    * Local Modules (using relative paths)
* Place class properties in the following order:
    * Class methods and properties (methods starting with `static`)
    * Instance methods and properties
* [Avoid platform-dependent code](https://flight-manual.atom.io/hacking-atom/sections/cross-platform-compatibility/)
* All files must end in a new line

### Python Styleguide

All Python code must adhere to [Python Standard Style](https://www.python.org/dev/peps/pep-0008/)

* Prefer lambda wherever possible
* User 4 spaces over tabs
* Criteria for creating unit tests:
    * The function acts as a wrapper to a module function - NO
    * The function doesnt have any changing parameters - NO
* All files must end in a new line