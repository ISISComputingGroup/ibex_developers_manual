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
```
* Arguments are introduced following "Args:"



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