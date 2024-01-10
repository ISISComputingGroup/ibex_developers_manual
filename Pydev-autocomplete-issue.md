# Pydev autocomplete issue

We found an issue in the `pydev` plugin, used for the embedded scripting console in the GUI, in https://github.com/ISISComputingGroup/IBEX/issues/7604 which basically ran a function on autocomplete continuously. An example of this is like so: 

```python 
def x():
    print("hello")
```

if you then used `x().` in a scripting console this would run in a never-ending loop and print "hello" continuously. 

This was alarming as we have several functions in our genie_python library which could be called this way by accident and this could have done bad things ie. move motors or set temperatures without the user realising. 

It was decided after investigation that we should disable this for now, [triangulate](https://github.com/ISISComputingGroup/IBEX/issues/7850) when it started happening, then look into a solution. 


## How to enable or disable auto completion
Pydev on a built GUI client is stored as several jars in the `plugins\` directory. The one we care about is called `org.python.pydev.ast_XXX` where `XXX` is the version suffix. The jar contains lots of bytecode-compiled java classes which are not directly editable. 

In order to disable autocompletion on an instrument, you will need to (in `\instrument\apps\client_e4\plugins\org.python.pydev.ast_xxx`)

- rename `ast.jar` to `ast.jar.ACENABLED`
- copy `ast.jar` from `\\shadow<isis suffix>\ICP_P2$\Pydevup_042023\plugins\org.python.pydev.ast`


