# Test naming

When writing tests, it is important that the purpose and expected outcome of the test is clear from the name.
This has several advantages, for example:

- It helps other developers debug failing tests
- It helps clarify your own thoughts as to the purpose of the test
- It defines the code itself by explicitly stating the expected interface. Ideally you should be able to reconstruct a
functional class entirely from its tests

While new tests should aim to follow the conventions documented here, it is allowable to deviate in cases such as:
- Older tests which predate this naming convention; although if you are doing significant refactoring, consider updating
the old test names to match this convention.
- Adding tests to existing/external code which uses a different convention; prefer to adopt the convention in the
surrounding code for consistency.
- The convention is too restrictive for a particular test. Use discretion here; only deviate from the guidelines if you
have a strong reason to do so.

There are many test naming formats out there, each with pros and cons. We have opted to go with the
[Given When Then format](https://martinfowler.com/bliki/GivenWhenThen.html). The given-when-then scheme is broadly
comparable with other common test naming & structuring schemes such as arrange-act-assert, but with different names.

**Test names should take the following form:**

```
GIVEN_[pre-conditions]_WHEN_[action]_THEN_[result]
```

GIVEN, WHEN, and THEN are in capitals with the rest of the test name in lower case, words are separated by underscores.

In cases where there are no preconditions, or where the preconditions are very simple, the "given" section may be
omitted.

Where possible, don't include the method being tested name in the test name, as that could change over time.

Given that java methods usually use CamelCase, it is useful to tell Checkstyle to ignore the name format add a warning
suppression to the top of the class:

```java
@SuppressWarnings({ "checkstyle:magicnumber", "checkstyle:methodname" })
public class SomethingTest {
    @Test
    public void GIVEN_my_test_isnt_written_in_camel_case_WHEN_test_is_viewed_in_eclipse_THEN_checkstyle_does_not_issue_warning() {}
}
```

In some cases, the `checkstyle:magicnumber` suppression may also be helpful, depending on the type of tests.
