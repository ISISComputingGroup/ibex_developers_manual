> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > [System Testing The IBEX Script Generator with Squish BDD Tools](System-Testing-The-IBEX-Script-Generator-with-Squish-BDD-Tools)

# BDD and Gherkin Overview

Behaviour-Driven Development (BDD) is a software development process that builds on the lessons learnt from Test-Driven Development (TDD). BDD focuses on developing a common understanding of the behaviour of an application. More details can be found at https://cucumber.io/docs/bdd/ and https://www.agilealliance.org/glossary/bdd/.

BDD works by taking requirements and user stories and describing them in a language that can be understood by developers and users, the Gherkin language https://cucumber.io/docs/gherkin/reference/. This language helps to accurately describe behaviour and provides a way to carefully consider what to build. Gherkin is most effective for designing software when combined with other techniques such as low-fidelity prototypes.

Gherkin also helps to automate testing. The steps in a `.feature` (gherkin) file can be linked to the code that runs the test step on the application. Squish supports this with its BDD tools https://www.froglogic.com/squish/features/bdd-behavior-driven-development-testing/. We have made use of this in the script generator for all its Squish testing. These tests can now act as documentation of the behaviour of the application and can be used to discuss the intricacies of the behaviour with scientists.

# Structure of our tests

Squish is split up into test suites, the script generator tests are all in the suite_script_gen_tests. The test cases in this suite are the `.feature` files that describe the behaviour in Gherkin. In general, we define a one or more features in each file with the `Feature:` tag and each feature has a collection of scenarios denoted by the `Scenario:` tag. The feature will have a title and a description and a scenario will have a title that acts as its description. 

Each scenario is made up of a set of `Given`, `When`, `Then` steps. These steps can take parameters including whole tables and can be ordered in lots of different ways. `Given` generally describes the state the application should be in before a user action, `When` describes a user action and `Then` describes verification of the state of the application after a user action. More details can be found at https://cucumber.io/docs/gherkin/ and in the Squish tutorials on https://www.froglogic.com/squish/features/bdd-behavior-driven-development-testing/.

The `Given`, `When` and `Then` steps are linked to code which is stored in the test suite resources steps area. For example, the `then_tooltip.py` file contains `Then` steps related to tooltip behaviour. Steps are defined like this:

```python
@Then("the following actions have a tooltip |word|")
def step(context, status):
    actions_that_we_expect_have_a_tooltip = context.table
    do_test_code()
```

This step takes a table as a parameter (accessed through `context.table`) and a word parameter (described by the decorator with `|word|` and passed to the step function as `status`). A step can have multiple decorators of `@Given`, `@When` and `@Then`. There are also more abilities such as using `From` sections and passing data between tests through the context variable - details at https://doc.froglogic.com/squish/latest/api.bdt.functions.html.

# Scenario and Feature hooks

In the script section of the test suite resources, there is a file named `bdd_hooks.py`. This file contains a number of functions hooked into the tests to run at the beginning and end of features. For example:

```python
@OnFeatureStart
def hook(context):
    do_hook_code()
```

Before the scenarios of a feature are run this hook is called by Squish. We utilise `@OnFeatureStart`, `@OnScenarioStart`, `@OnScenarioEnd` and `@OnFeatureEnd` to carry out the test setup and cleanup activities. More details at `6.19.10. Performing Actions During Test Execution Via Hooks` of https://doc.froglogic.com/squish/latest/api.bdt.functions.html.

# Implementing a new test

# Running the tests