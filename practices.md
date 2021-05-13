# Good practices

## `assert` keyword
This is meant to be used as a debugging tool for internal checks of where the program should never possibly go. As stated in *Python Tricks*, while exceptions can signal errors where the user can take corrective action to fix the issue, assertions are signals for developers that something that was supposed to be impossible has happened.

### Example
We want to ensure that the amount of items available for a given product is always greater than or equal to 0 (can't have negative stock)

```py
def decrease_stock(item):
    stock_item = self.items.get(item.id) - 1
    assert stock_item.inventory - 1 >= 0
    stock_item.inventory -= 1
```

## `pprint`
This is a built-in module to allow Pretty Printing of objects such as dictionaries, in order to make debugging easier. Examples can be found in the [pprint docs](https://docs.python.org/3/library/pprint.html).

## Naming conventions
The conventions are as follows:
- Regular variables are named using underscores to separate words like `the_item` (as opposed to camelCase) and should be descriptive of what the variable stores.
- Single leading underscore `_var` variables are used when an attribute in a class is meant for internal use and shouldn't be used outside of the class
- A trailing underscore `var_` is used when the identifier conflicts with a keyword that already exists in the python language, such as `int` or `class`. One should never redefine these keywords, so an underscore is used to distinguish them.
- double leading underscores `__var` triggers "name mangling" in classes, i.e the Python interpreter will rename these variables so that subclasses can't access/override the values.
- `__var__` should not be used for attributes, this is the naming convention for so-called "dunders" or magic methods, as described in [magic methods](magicmethods.md)
- Single underscores (just `_`) are used as "ignored" variables, as described in [assignment](assignment.md)

## Using virtualenvs
`virtualenvs` are used to isolate projects from one another. Of course, there is a global Python installation on systems and one can install any dependencies using `pip`. However when working with different projects all of which may use different versions of Python or dependencies, it isn't desirable to use the same global Python installation for everything. This is where `virtualenvs` come in (virtual environment). With this, dependencies and even Python versions can be isolated from one another. Please see [venv](https://docs.python.org/3/library/venv.html#module-venv) and [pyenv](https://github.com/pyenv/pyenv) as examples of programs that can do this. Dependency managers such as [Pipenv](https://pypi.org/project/pipenv/) and [poetry](https://github.com/python-poetry/poetry) are also well-known and widely used, and often integrate with the above mentioned tools.

---

### References
[1] [Python docs -- assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)  
[2] [Python docs -- pprint](https://docs.python.org/3/library/pprint.html)  
[3] [PEP 8 -- Style Guide for Python Code (naming conventions)](https://www.python.org/dev/peps/pep-0008/#naming-conventions)  
[4] [Python docs -- venv](https://docs.python.org/3/library/venv.html#module-venv)

#### Books that mention this topic:
[5] *Python Tricks: A Buffet of Awesome Python Features* by Dan Bader  
[6] *Effective Python: 90 Specific Ways to Write Better Python* by Brett Slatkin  
[7] *Python Cookbook, Third Edition* by David Beazley and Brian K. Jones  
[8] *Writing Idiomatic Python 3* by Jeff Knupp  
[9] *The Little Book of Python Anti-Patterns* by QuantifiedCode  