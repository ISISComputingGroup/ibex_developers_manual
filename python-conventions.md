# Python Conventions

* Use [PEP8](https://www.python.org/dev/peps/pep-0008/) for coding styles

### Docstring format

Based on the [Google style](https://google.github.io/styleguide/pyguide.html).
See below for usage examples, but some key points to adhere to:

* Docstrings start and end with triple double-quotes
* Newline after opening `"""`
* First line of text should be a one sentence description followed by a full-stop and a new line. More details can then follow, for example:
```python
def my_function():
    """
    This does something mysterious.

    Here is where more details are written. It can take up multiple lines and so on.
    blah blah blah.
```

#### Examples

With usage examples:

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

With return values:

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
        list : The names of all the blocks
    """
```

With exceptions:

```python
def an_example_function(param1, param2=None, *args, **kwargs):
    """
    This is an example of a function.

    Args:
        param1 (int): the first parameter
        param2 (string, optional): the second parameter. Defaults to None.
            Subsequent line(s) of description should be indented
        *args: variable length argument list
        **kwargs: arbitrary keyword arguments

    Returns:
        bool: True if successful, False otherwise.

    Raises:
        ValueError: if param2 is equal to param1
```