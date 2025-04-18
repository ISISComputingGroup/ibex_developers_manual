# System Testing with Squish BDD Tools

## BDD and Gherkin Overview

Behaviour-Driven Development (BDD) is a software development process that builds on the lessons learnt from Test-Driven Development (TDD). BDD focuses on developing a common understanding of the behaviour of an application. More details can be found at https://cucumber.io/docs/bdd/ and https://www.agilealliance.org/glossary/bdd/.

BDD works by describing the behaviours of an application in a language that can be understood by developers and users, the Gherkin language https://cucumber.io/docs/gherkin/reference/, enabling a conversation on detailed application behaviour. This language helps to accurately describe behaviour and provides a way to carefully consider what to build. Gherkin is most effective for designing software when combined with other techniques such as low-fidelity prototypes.

Gherkin also helps to automate testing. The steps in a `.feature` (gherkin) file can be linked to the code that runs the test step on the application. Squish supports this with its BDD tools https://www.froglogic.com/squish/features/bdd-behavior-driven-development-testing/. We have made use of this in the script generator for all its Squish testing. These tests can now act as documentation of the behaviour of the application and can be used to discuss the intricacies of the behaviour with scientists.

## Structure of our tests

Squish is split up into test suites, the script generator tests are all in the `suite_script_gen_tests`. The test cases in this suite are the `.feature` files that describe the behaviour in Gherkin. In general, we define one or more features in each file with the `Feature:` tag and each feature has a collection of scenarios denoted by the `Scenario:` tag. The feature will have a title and a description and a scenario will have a title that acts as its description. 

Each scenario is made up of a set of `Given`, `When`, `Then` steps. These steps can take parameters including whole tables and can be ordered in lots of different ways. `Given` generally describes the state the application should be in before a user action, `When` describes a user action and `Then` describes verification of the state of the application after a user action. More details can be found at https://cucumber.io/docs/gherkin/ and in the Squish tutorials on https://www.froglogic.com/squish/features/bdd-behavior-driven-development-testing/.

The `Given`, `When` and `Then` steps are linked to code which is stored in the test suite resources steps area. For example, the `then_tooltip.py` file contains `Then` steps related to tooltip behaviour. Steps are defined like this:

```python
@Then("the following actions have a tooltip |word|")
def step(context, status):
    actions_that_we_expect_have_a_tooltip = context.table
    do_test_code()
```

This step takes a table as a parameter (accessed through `context.table`) and a word parameter (described by the decorator with `|word|` and passed to the step function as `status`). A step can have multiple decorators of `@Given`, `@When` and `@Then`. There are also more abilities such as using `From` sections and passing data between tests through the context variable - details at https://doc.froglogic.com/squish/latest/api.bdt.functions.html.

We do not generally edit the test.py file in the test case resources scripts. This script is created by squish and handles starting up tests and setting up the hooks. This could be used to start up the client instead of using `@OnFeatureStart` to speed up tests and enable us to better structure our features without concern for lengthening our tests.

## Scenario and Feature hooks

In the script section of the test suite resources, there is a file named `bdd_hooks.py`. This file contains a number of functions hooked into the tests to run at the beginning and end of features. For example:

```python
@OnFeatureStart
def hook(context):
    do_hook_code()
```

Before the scenarios of a feature are run this hook is called by Squish. We utilise `@OnFeatureStart`, `@OnScenarioStart`, `@OnScenarioEnd` and `@OnFeatureEnd` to carry out the test setup and cleanup activities. More details at `6.19.10. Performing Actions During Test Execution Via Hooks` of https://doc.froglogic.com/squish/latest/api.bdt.functions.html.

## Implementing a new test

Have you already agreed to a gherkin description of the behaviour required? If so then add it to the test cases either as a new feature (there's a little button labelled BDD in the test cases section of the Squish GUI) or if your feature fits well into a feature already in the test suite then include the scenarios in there - this avoids running feature start and end code which restarts the client and lengthens the tests, though don't be afraid to add a new feature if it doesn't fit.

If you haven't already agreed on the behaviour, consider creating a design for the feature with gherkin and a low-fidelity prototype and reviewing it with other developers and script generator users - this depends on how major and well defined the feature is. If you're not sure, ask the team!

Now that you have your feature, scenario and steps laid out it's time to write the test code. Are any of the steps already defined in the test suite resources? They may not have the same name but they may have the same functionality - you can add a new `@Given`, `@When` or `@Then` decorator to the step or rename the step in the test case. Any steps that don't have an already defined test function for you will need to implement, these steps will be annotated by Squish in the test case.

To add the steps you want you can either code them directly by writing a test step function or you can record it. If you right-click on a feature or scenario in the test case and click `Record Missing Steps in Feature/Scenario` then the test will execute the steps it knows and then pauses on the steps it doesn't know to record any button clicks and do any verification steps as according to the squish recording tools - see the tutorial on https://www.froglogic.com/squish/features/recording-and-playback/. After recording, this will insert the step function into a file in the steps section of the test suite resources - often this is in a file that doesn't make sense so please move it to somewhere it does make sense. 

Although the recording is useful, it often produces brittle step functions, please make use of the utilities in the global scripts area to improve the robustness of the test and see https://github.com/ISISComputingGroup/ibex_developers_manual/wiki/System-Testing-with-Squish#writing-tests for some hints, tips and gotchas.

## Running the tests

You can run the whole test suite with the play button located above the test cases next to the new BDD test case button. You can also run test cases with the run button next to the case in the case list. You can run features and scenarios by right-clicking and pressing run.