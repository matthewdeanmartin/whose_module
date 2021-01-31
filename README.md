# whose_module
Find what package on pypi has a module you want to import

Related
- [Pypi](http://pypi.com/) They could implement this sort of search and API...someday
- [Nullage](http://nullege.com/) Python code/package search engine
- [Libraries.io](https://libraries.io/) Has API
- [Snyk Advisor](https://snyk.io/advisor/python/)
- [Pypi Stats](https://pypistats.org/) Has API

# Problem
Say you have main.py
```lang=python
import foobar
```

You have this code and you don't know where `foobar` is from, e.g. what pypi package do you need to install to get it.
This is obviously a problem of getting code form somewhere else without the corresponding requirements.txt or Pipfile.
This problem is largely unsolved up to now.

I will attempt to solve it by:
- safely parsing source code to get the list of top level modules
- getting a list of candidates where the package name = module name. This is not always the case that a match is meaningful.
    - *requests* the module is *requests* the package
    - *bs4* the module is *beautifulsoup4* the package
- Download the most popular packages & create a datafile with the modules that these packages export.
    - There are 7TB of pypi packages, and they keep changing.
    - So it pays to just pay attention to popular packages

As a side effect I will try to also export
- Which modules are exported by currently installed packaged
- Which modules are loaded in a live program.

But those are less import problems to solve.


Docs
-----
* [Prior Art](https://github.com/matthewdeanmartin/whose_module/blob/main/docs/prior_art.md) Similar and overlapping tools.
* [Security Considerations](https://github.com/matthewdeanmartin/whose_module/blob/main/docs/security.md)
* [Contributing to whose_module](https://github.com/matthewdeanmartin/whose_module/blob/main/CONTRIBUTING.md)
* [Code of Conduct for whose_module](https://github.com/matthewdeanmartin/whose_module/blob/main/CODE_OF_CONDUCT.md)
