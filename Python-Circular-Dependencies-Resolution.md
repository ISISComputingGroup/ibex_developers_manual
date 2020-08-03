> [Wiki](Home) > [genie_python](genie_python) > [Python Circular Dependencies Resolution](Python-Circular-Dependencies-Resolution)

It is possible to get circular dependencies in python the normal way to resolve this is to take the circular dependent items into another file. However now with typing it is possible to get circular references only through typing it is possible to resolve this by:

1. Instead of the type use the text version of the type
1. Import the type using: 
   ```
   if TYPE_CHECKING:
       from XXX import XXXX
   ```

For example:

```
from x import ArgType
def myfun(arg: ArgType):
```

replace with:
```
if TYPE_CHECKING:
    from x import ArgType

def myfun(arg: 'ArgType'):
```


