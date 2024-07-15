> [Wiki](Home) > [genie_python](genie_python) > [Python Conventions](Python-conventions)

For dependency conventions see [Python dependencies](Python-dependencies).

### Coding style
We try to follow [PEP8](https://www.python.org/dev/peps/pep-0008/) for coding style where possible or suitable.
 
A clear exception is when it comes to line length; PEP8 suggests a line length limit of 79 characters but defaults to 100, but PyCharm defaults to 120. I recommend following PEP8 and modifying PyCharm default to 100 on this (See: `File -> Settings -> Editor -> Code Style -> Python -> Wrapping and Braces -> Hard wrap at: `).

**We have a [Ruff config](https://github.com/ISISComputingGroup/reusable-workflows/blob/main/ruff.toml), you can setup ruff to work with most `IDE's` and then use our config to lint your code, or run ruff from command line before making a pull request, standards compliance will be enforced by this config at pull request. So before making a pull request you should ensure any files you have changed have been formatted by ruff, and pass its checks. Ruff can also automatically fix many violations.**

For new repos containing python you should add the following [workflow](https://github.com/ISISComputingGroup/reusable-workflows/blob/main/.github/workflows/linters.yml) to ensure standards compliance.

Key points relating to general code formatting:

* Use 4 spaces per indentation level
* Spaces are the preferred indentation method not tabs
* Surround top-level function and class definitions with two blank lines
* Method definitions inside a class are surrounded by a single blank line
* Class names should normally use the CapWords convention
* Function/method names should be lowercase, with words separated by underscores as necessary to improve readability
* Comments should have a space after the # and start with a capital letter (unless it is a variable name)
* Files should have one blank line at the end
* Methods and function definitions should contain type hints.

```python
import os


class CapsWordName(object):
    def method_that_has_underscores(self, x: any, y=None: any):
        """
        See docstring guide below.
        """
        if y is not None:
            x += y
        return x

    def one_blank_line_before_next_method(self, max: int) -> int:
        """
        See docstring guide below.
        """
        # This comment starts with a capital letter
        total = 0        

        for i in range(max):
            if i % 2 == 0:
                # i is even. 
                # Previous line starts with lowercase because i is a variable name.
                total += i

        return total

    def _this_method_is_non_public(self) -> int:
        """
        The single underscore warns people using this class that this method 
        is not part of the API, so may change and should be used with care.

        It doesn't say you should not use it though.
        Python does not really have the concept of private.
        """
        return 123456       

```

### Docstring format

Here we also deviate from PEP8 in that our format is based mostly on the [Google style](https://google.github.io/styleguide/pyguide.html). It is not identical however.
See below for usage examples, but some key points to follow are:

* Docstrings start and end with triple double-quotes
* Newline after opening `"""`
* First line of text should be a one sentence description followed by a full-stop and then an empty line. More details can then follow

Google style suggests that argument descriptions start with a capital and end with a full-stop.
```python
    Args:
        state: The state to wait for (e.g. "paused").
```
We have decided to follow Google on this; however, some older docstrings may not match this, so please adjust them as you come across them.

PyCharm can be set to auto-generate Google style dostrings via `File --> Settings --> Tools --> Python Integrated Tools`

PyCharm also supports the ability to specify types in the docstring. This includes being able to write objects class names, for example: 

This is useful because it will syntax highlight potential type errors before you even debug, as well as allow you to quickly perform introspection on objects of that type in you code (Ctrl-Left Click).

#### Examples

```python
class ExampleClass:
    """
    This is a class docstring.

    There should be a newline between this docstring and the following method.
    """

    def an_example_method(self, param1: int, param2=None: string, *args, **kwargs):
        """
        This is an example of a method.

        Here is where more details are written. It can take up multiple lines 
        and so on. blah blah blah.It can take up multiple lines and so on.
        blah blah blah.It can take up multiple lines and so on.
        blah blah blah.

        Note:
            self is not included in the 'Args' section.

        Args:
            param1: The first parameter.
            param2 (optional): The second parameter. Defaults to None.
                Subsequent line(s) of description should be indented.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: True if successful, False otherwise.

        Raises:
            ValueError: If param2 is equal to param1.
        """
```

```python
def a_function_that_returns_none(param1):
    """
    This function does not return anything.

    Python returns None for functions that don't explicitly return anything. 
    As PyCharm automatically creates a return tag in the docstring we leave 
    it in and put None.
    
    Args:
        param1: Some input value.

    Returns: 
        None.
    """
```

```python
def waitfor_runstate(state: string, maxwaitsecs=3600: int, onexit=False: bool):
    """
    Wait for a particular instrument run state.

    Args:
        state: The state to wait for (e.g. "paused").
        maxwaitsecs (optional): The maximum time to wait before carrying on.
        onexit (optional): Wait for runstate to change from the specified state.

    Examples:
        Wait for a run to enter the paused state:
        >>> waitfor_runstate("paused")

        Wait for a run to exit the paused state:
        >>> waitfor_runstate("paused", onexit=True)
    """
```

```python
def get_number_periods():
    """
    Get the number of software periods.

    Returns:
        int: The number of periods.
    """
```

```python
def get_blocknames(self):
    """ 
    Get all the blocknames including those in the components.

    Returns:
        list : The names of all the blocks.
    """
```

### Code conventions

#### Use f-strings to construct strings from values, or .format() when this is not possible (e.g. when you wish to use the same template multiple times with different variables).
```python
# Single value
name = 'eric'
print(f'Name: {name}')

# Multiple values
name = 'eric'
age = 11
print(f'Name: {name}, Age: {age}')

# With a class
print(f'Name: {user.name}, Age: {user.age}, Sex: {user.sex}')

# Limit to two decimal points
name = 'eric'
age =  12.3456789
print('Name: {name}, Age: {age:.2f}')

# if you want to re-use a template then prefer .format(), as fstrings are evaluated immediatley.
template = 'Name: {}, Age: {}'
print(template.format('Eric', 11)
...
print(template.format('Alice', 13)
```
AVOID using the older `%` formatter or concatenating strings with `+`.

#### Use os.path.join to create file paths from strings
```python
os.path.join('directory', 'subdirectory1', 'subdirectory2')
```
AVOID combining strings with '\\', '\\\\' or '/'


### GitHub Workflows:
You can add a GitHub workflow to perform lint checking on your repository to enforce PEP8 standards here:
[Pylint GitHub Workflow](https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/Shared-utility-scripts#github-workflows)

