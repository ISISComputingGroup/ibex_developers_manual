**New conventions should not be added to this document without first being discussed at a 'Code Chat'.**

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

        It doesn't say you should not use it though.
        Python does not really have the concept of private.
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
We have decided to follow Google on this; however, some older docstrings may not match this, so please adjust them as you come across them.

PyCharm can be set to auto-generate Google style dostrings via `File --> Settings --> Tools --> Python Integrated Tools`

#### Examples

```python
class ExampleClass:
    """
    This is a class docstring.

    There should be a newline between this docstring and the following method.
    """

    def an_example_method(self, param1, param2=None, *args, **kwargs):
        """
        This is an example of a method.

        Here is where more details are written. It can take up multiple lines 
        and so on. blah blah blah.It can take up multiple lines and so on.
        blah blah blah.It can take up multiple lines and so on.
        blah blah blah.

        Note:
            self is not included in the 'Args' section.

        Args:
            param1 (int): The first parameter.
            param2 (string, optional): The second parameter. Defaults to None.
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
def waitfor_runstate(state, maxwaitsecs=3600, onexit=False):
    """
    Wait for a particular instrument run state.

    Args:
        state (string): The state to wait for (e.g. "paused").
        maxwaitsecs (int, optional): The maximum time to wait before carrying on.
        onexit (bool, optional): Wait for runstate to change from the specified state.

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
