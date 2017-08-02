# Python Conventions
```
>>> import this
```
### Coding style
We try to follow [PEP8](https://www.python.org/dev/peps/pep-0008/) for coding style where possible or suitable.
 
A clear exception is when it comes to line length; PEP8 suggests a line length limit of 79 characters, but PyCharm defaults to 120. We follow PyCharm on this.

**PyCharm warns on many deviations from PEP8, please don't ignore it.**

Key points relating to general code formatting:

* Use 4 spaces per indentation level
* Spaces are the preferred indentation method not tabs
* Surround top-level function and class definitions with two blank lines
* Method definitions inside a class are surrounded by a single blank line
* Class names should normally use the CapWords convention
* Function/method names should be lowercase, with words separated by underscores as necessary to improve readability
* Comments should have a space after the # and start with a capital letter (unless it is a variable name)
* Files should have one blank line at the end

```python
import os


class CapsWordName(object):
    def method_that_has_underscores(self, x, y=None):
        """
        See docstring guide below.
        """
        if y is not None:
            x += y
        return x

    def one_blank_line_before_next_method(self, max):
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

    def _this_method_is_non_public(self):
        """
        The single underscore warns people using this class that this method 
        is not part of the API, so may change and should be used with care.

        Python doesn't really have private variables or methods:
            'We are all consenting adults here'
        """
        return 123456       

```

### Docstring format

Here we also deviate from PEP8 in that our format is based mostly on the [Google style](https://google.github.io/styleguide/pyguide.html).
See below for usage examples, but some key points to follow are:

* Docstrings start and end with triple double-quotes
* Newline after opening `"""`
* First line of text should be a one sentence description followed by a full-stop and a new line. More details can then follow
* Args can have their suggested type declared in brackets. This is optional, but preferred in code a user may encounter, for example: in genie_python

Google style suggests that argument descriptions start with a capital and end with a full-stop.
```python
    Args:
        state (string): The state to wait for (e.g. "paused").
```
We don't currently follow this, but if someone wants to go through all the code and change this then feel free. Please remember to update the examples below too.

#### Examples

```python
def an_example_function(param1, param2=None, *args, **kwargs):
    """
    This is an example of a function.

    Here is where more details are written. It can take up multiple lines and so on.
    blah blah blah.It can take up multiple lines and so on.
    blah blah blah.It can take up multiple lines and so on.
    blah blah blah.

    Args:
        param1 (int): the first parameter.
        param2 (string, optional): the second parameter. Defaults to None.
            Subsequent line(s) of description should be indented
        *args: variable length argument list
        **kwargs: arbitrary keyword arguments

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: if param2 is equal to param1
    """
```

```python
def waitfor_runstate(state, maxwaitsecs=3600, onexit=False):
    """
    Wait for a particular instrument run state.

    Args:
        state (string): the state to wait for (e.g. "paused")
        maxwaitsecs (int, optional): the maximum time to wait for the state before carrying on
        onexit (bool, optional): wait for runstate to change from the specified state

    Examples:
        Wait for a run to enter the paused state:
        >>> waitfor_runstate("pause")

        Wait for a run to exit the paused state:
        >>> waitfor_runstate("pause", onexit=True)
    """
```

```python
def get_number_periods():
    """
    Get the number of software periods.

    Returns:
        int: the number of periods
    """
```

```python
def get_blocknames(self):
    """ 
    Get all the blocknames including those in the components.

    Returns:
        list : the names of all the blocks
    """
```
