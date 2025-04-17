# Summary

We have re-enabled the pydev autocomplete, which is the autocomplete in the ibex GUI scripting window. This had been disabled for a while after we discovered a problem, but it is not an easy fix and the problem may actually have existed for a much longer time than we realised.

The problem only occurs with a "chained autocomplete". For example if you type `g.` or `b.` to autocomplete a command or block name then that works fine. The problem occurs if you try and autocomplete further on an already completed command. For example if you type `g.c` you will be able to complete a `g.cset` command with no problems. However if after having completed this as `g.cset("ablock", 1)` you then typed a further `.` (i.e. `g.cset("ablock", 1).`) you would end up running the `cset` command continuously. This is because the command line needs to run the function to find out what type of object it returns so as to be able to display the list of new options to complete on. So the bottom line is that simple single autocompletes will not give any problems, but be aware that autocompleting on the result of a command/function will cause the command/function to run continuously which may have undesirable side effects. This does not apply only to genie python functions, it applies to any python function. For a simple example if you type `print("hello")` in the scripting window and then press `.` rather than the enter key, it will print hello continuously as it needs to run the print function to get the autocomplete choice.         

# Further details and history

We found an issue in the `pydev` plugin, used for the embedded scripting console in the GUI, in https://github.com/ISISComputingGroup/IBEX/issues/7604 which basically ran a function on autocomplete continuously. An example of this is like so: 

```python 
def x():
    print("hello")
```

if you then used `x().` in a scripting console this would run in a never-ending loop and print "hello" continuously. 

This was alarming as we have several functions in our genie_python library which could be called this way by accident and this could have done bad things ie. move motors or set temperatures without the user realising. 

It was decided after investigation that we should [disable this for now](https://github.com/ISISComputingGroup/Pydev/pull/4), [triangulate](https://github.com/ISISComputingGroup/IBEX/issues/7850) when it started happening, then look into a solution. This led to [some investigation](https://github.com/ISISComputingGroup/IBEX/issues/7898) and we discovered that: 
a) this had been happening since the introduction of pydev in the GUI, though no one other than us had actually noticed - more on this later
b) this problem only happens in pydev's console view, which has no form of dynamic analysis of the code put into it

After talking to the maintainer and doing several days work into looking into the code, we decided that the best course of action was to re-enable for now on instruments and let instrument scientists know that it may cause issues. The fix isn't trivial due to the lack of dynamic analysis, but the continuously doing the action is a definite bug.

## How to enable or disable auto completion
Pydev on a built GUI client is stored as several jars in the `plugins\` directory. The one we care about is called `org.python.pydev.ast_XXX` where `XXX` is the version suffix. The jar contains lots of bytecode-compiled java classes which are not directly editable. 

In order to disable autocompletion on an instrument, you will need to (in `\instrument\apps\client_e4\plugins\org.python.pydev.ast_xxx`)

- rename `ast.jar` to `ast.jar.ACENABLED`
- copy `ast.jar` from `\\shadow<isis suffix>\ICP_P2$\Pydevup_042023\plugins\org.python.pydev.ast`

_Note: this will get reverted when we deploy a new GUI, so we may have to keep doing it until the underlying issue is solved._

