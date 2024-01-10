# Pydev autocomplete issue

We found an issue in the `pydev` plugin, used for the embedded scripting console in the GUI, in https://github.com/ISISComputingGroup/IBEX/issues/7604 which basically ran a function on autocomplete continuously. An example of this is like so: 

```python 
def x():
    print("hello")
```

if you then used `x().` in a scripting console this would run in a never-ending loop and print "hello" continuously. 

This was alarming as we have several functions in our genie_python library which could be called this way by accident and this could have done bad things ie. move motors or set temperatures without the user realising. 

It was decided after investigation that we should disable this for now, [triangulate](https://github.com/ISISComputingGroup/IBEX/issues/7850) when it started happening, then look into a solution. This led to some investigation and we discovered that: 
a) this had been happening since the introduction of pydev in the GUI, though no one other than us had actually noticed - more on this later
b) this problem only happens in pydev's console view, which has no form of dynamic analysis of the code put into it

After talking to the maintainer and doing several days work into looking into the code, we decided that the best course of action was to re-enable for now on instruments and let ISs know that it may cause issues. The fix isn't trivial due to the lack of dynamic analysis, but the continuously doing the action is a definite bug.

## How to enable or disable auto completion
Pydev on a built GUI client is stored as several jars in the `plugins\` directory. The one we care about is called `org.python.pydev.ast_XXX` where `XXX` is the version suffix. The jar contains lots of bytecode-compiled java classes which are not directly editable. 

In order to disable autocompletion on an instrument, you will need to (in `\instrument\apps\client_e4\plugins\org.python.pydev.ast_xxx`)

- rename `ast.jar` to `ast.jar.ACENABLED`
- copy `ast.jar` from `\\shadow<isis suffix>\ICP_P2$\Pydevup_042023\plugins\org.python.pydev.ast`


