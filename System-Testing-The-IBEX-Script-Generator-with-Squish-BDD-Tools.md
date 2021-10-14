> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > [System Testing The IBEX Script Generator with Squish BDD Tools](System-Testing-The-IBEX-Script-Generator-with-Squish-BDD-Tools)

# BDD and Gherkin Overview

Behaviour-Driven Development (BDD) is a software development process that builds on the lessons learnt from Test-Driven Development (TDD). BDD focuses on developing a common understanding of the behaviour of an application. More details can be found at https://cucumber.io/docs/bdd/ and https://www.agilealliance.org/glossary/bdd/.

BDD works by taking requirements and user stories and describing them in a language that can be understood by developers and users, the Gherkin language https://cucumber.io/docs/gherkin/reference/. This language helps to accurately describe behaviour and provides a way to carefully consider what to build. Gherkin is most effective for designing software when combined with other techniques such as low-fidelity prototypes.

Gherkin also helps to automate testing. The steps in a `.feature` (gherkin) file can be linked to the code that runs the test step on the application. Squish supports this with its BDD tools https://www.froglogic.com/squish/features/bdd-behavior-driven-development-testing/. We have made use of this in the script generator for all its Squish testing. These tests can now act as documentation of the behaviour of the application and can be used to discuss the intricacies of the behaviour with scientists.

# Structure of our tests

Squish is split up into test suites, the script generator tests are all in the suite_script_gen_tests. The test cases in this suite are the `.feature` files that describe the behaviour in Gherkin. In general, we define a one or more features in each file with the `Feature:` tag and each feature has a collection of scenarios denoted by the `Scenario:` tag. The feature will have a title and a description and a scenario will have a title that acts as its description. 

# Implementing a new test

# Running the tests