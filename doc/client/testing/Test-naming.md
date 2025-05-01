# Test naming

When writing tests, it is important that the purpose and expected outcome of the test is clear from the name. This has several advantages:

- It helps other developers debug failing tests
- It helps clarify your own thoughts as to the purpose of the test
- It defines the code itself by explicitly stating the expected interface. Ideally you should be able to reconstruct a functional class entirely from its tests
- And more

It isn't expected that all tests will follow this guide, many tests pre-date this guide. Sometimes as well, these guidelines may prove overly restrictive or add unnecessary bulk to the test name. As ever, discretion is advised, but be clear why you're not following the guidelines if you choose not to. For example "'Initializes_ok' is fine as a test name because I'm just checking that I can initialize the class" would be a bad reason.

There are many test naming formats out there, each with pros and cons, and each with people who get far too passionate about their personal favourite. We have opted to go with the GIVEN_WHEN_THEN format.

Test names should take the following form:

```
GIVEN_[pre-conditions]_WHEN_[action]_THEN_[result]
```

GIVEN, WHEN, and THEN are in capitals with the rest of the test name in lower case, words are separated by underscores.

In some cases, there are no preconditions, or the preconditions are truly trivial (be wary of jumping to that conclusion though). In those cases given may be omitted.

Where possible don't include the method being tested name in the test name as that could change over time.

Given that java methods usually use CamelCase, it is useful to tell CheckStyle to ignore the name format add a warning suppression to the top of the class:

```
    @SuppressWarnings({ "checkstyle:magicnumber", "checkstyle:methodname" })
    public class GIVEN_my_test_isnt_written_in_camel_case_WHEN_test_is_viewed_in_eclipse_THEN_checkstyle_does_not_issue_warning {
```
    
It may be worth adding the magic-number suppression too depending on the type of tests.