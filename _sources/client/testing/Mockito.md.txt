# Mockito

:::{seealso}
- Read the [guide to testing in IBEX](An-Introduction-to-Unit-Testing) before reading this guide.
- For more detailed information on Mockito, see
[the Mockito homepage](https://site.mockito.org/) and the
[Mockito documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mockito.html).
:::

## Test Doubles

Test doubles are objects that stand in for a real object, for the purposes of unit testing. Terminology varies but
there are four usual types that are described:

* **Dummy** - an object that is passed around but not directly used by the method under test
* **Fake** - a working implementation of a class with a simplified internal implementation, for example an in memory
database where the production implementation uses a persistent database
* **Stub** - an object that provides a canned answer to a method call
* **Mock** - fake objects which know about which method calls they receive

See [this article](http://martinfowler.com/articles/mocksArentStubs.html) for more information. Mockito mostly helps
with Stub and Mock doubles.

## Verifying Interactions

To create a mock object using Mockito, in a way which is type-safe and works with generics, use the `@Mock` annotation:

```java
import org.mockito.Mock;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;
import static org.mockito.Mockito.verify;

import java.util.List;

@RunWith(MockitoJUnitRunner.StrictStubs.class)
public class SomeTest {
    @Mock private List<String> mockedList;
    
    @Test
    public void myUnitTest() {
        // using mock object - it does not throw any "unexpected interaction" exception
        mockedList.add("one");
        mockedList.clear();
    
        // selective, explicit, highly readable verification
        verify(mockedList).add("one");
        verify(mockedList).clear();
    }
}
```

:::{important}
The test class must be annotated with `@RunWith(MockitoJUnitRunner.StrictStubs.class)` - otherwise the `@Mock`
annotation will not be processed, and the mock object will be `null` during the test.
:::

In the above example, the generic `List<String>` interface is mocked, and has some method calls made on it. 
The verify calls replace the usual assert calls in this unit test, and check the method calls were made.

For non-generic classes, it is possible to use an older syntax to create the mock inline:

```java
SomeClass mockedList = mock(SomeClass.class);
```

:::{seealso}
The [Mockito Mock documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mock.html)
contains further details about how to construct mocks for more advanced use-cases.
:::

## Stubbing Method Calls

```java
@Mock private LinkedList<String> mockedList;

@Test
public void myUnitTest() {
    // stubbing appears before the actual execution
    when(mockedList.get(0)).thenReturn("first");

    // the following prints "first“
    System.out.println(mockedList.get(0));

    // the following prints "null" because get(999) was not stubbed
    System.out.println(mockedList.get(999));
}
```
    
This time the concrete class `LinkedList` is mocked instead of an interface. 
The mocked object returns what is asked of it when the method call is made with identical arguments.

:::{seealso}
The [Mockito documentation](https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mockito.html)
contains detailed documentation about how Mockito can be used to mock method calls for various cases.
:::

## Times Method is Called

Mockito has [several options](https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/verification/VerificationMode.html)
for checking how many times a particular method is called:
* `atLeast(int minNumber)` at least this many times
* `atLeastOnce()` at least once
* `atMost(int maxNumber)` at most this many times
* `never()` same as `times(0)`
* `times(int number)` exactly this number of times

The default is `times(1)`.
    
## Any Methods

When verifying method calls, if the value of an argument is not important, Mockito allows you to check that any object
of a specific type was used as an argument instead.

```java
// The initialisable observer has its update method called once
verify(mockObserver, times(1)).update(value, any(Exception.class), anyBoolean());
```
    
For common types methods such as `anyString()` are available, otherwise `any(Object.class)` can be used. A null
object will also be matched by using any.
See the [Mockito `ArgumentMatchers`](https://site.mockito.org/javadoc/current/org/mockito/ArgumentMatchers.html)
documentation for more details.

## Capturing Values on Method Calls

If you want to capture the object called in a method, perhaps to check some value, then a captor can be used.
See the code below for an example of how to do this.

```java
@Captor private ArgumentCaptor<Exception> exceptionCaptor;
@Mock private InitialisableObserver<String> mockObserver;
@Mock private Converter<Integer, String> mockConverter;

@Test
public void test_ConvertingObservable_with_conversion_exception() throws ConversionException {
    //Arrange        
    // initObservable is what our ConvertingObservable looks at, and testObservable we can call set methods on
    TestableObservable<Integer> testObservable = new TestableObservable<>();
    InitialiseOnSubscribeObservable<Integer> initObservable = new InitialiseOnSubscribeObservable<Integer>(testObservable);
    
    // converter with a stub conversion method
    when(mockConverter.convert(123)).thenThrow(new ConversionException("conversion exception!"));
    
    // Object we are really testing
    ConvertingObservable<Integer, String> convertObservable = new ConvertingObservable<>(initObservable, mockConverter);
    
    //Act
    convertObservable.addObserver(mockObserver);
    convertObservable.setSource(initObservable);
    testObservable.setValue(123);
    
    //Assert
    // The initialisable observer has its onError message called once, for the ConversionException
    verify(mockObserver, times(0)).onValue(anyString());
    verify(mockObserver, times(1)).onError(exceptionCaptor.capture());
    assertEquals("conversion exception!", exceptionCaptor.getValue().getMessage());
}
```

:::{important}
As with the `@Mock` annotation, the `@Captor` annotation will only be processed if the test class is annotated with
`@RunWith(MockitoJUnitRunner.StrictStubs.class)`.
:::

## Checking Order of Method Calls

Mockito can be used to check the order methods were called in.

```java
InOrder inOrder = inOrder(firstMock, secondMock);
 
inOrder.verify(firstMock).add("was called first");
inOrder.verify(secondMock).add("was called second");
```
    
## Spies

Spies can be used to stub a method or verify calls on a real class. Needing to use a partial mock like this might be
a symptom of problems with code though!

```java
// These are equivalent, but the first is the preferred approach
@Spy Foo spyOnFoo = new Foo("argument");
Foo spyOnFoo = Mockito.spy(new Foo("argument"));
```

## Examples

### IBEX Observable

Below is a full example, showing how the verification and stubbing can be used to check behaviour of an
observable.

In this example, `InitialiseOnSubscribeObservable` takes another observable as its argument, gets the current value of
that observable, and listens for changes. Here we stub the class that `InitialiseOnSubscribeObservable` is observing,
to simplify the test. The only method call we are testing is `getValue()`.

The `InitialisableObserver` is also mocked. As part of the test we want to check that it has its `update()` method
called with a specific set of arguments. We use `times(1)` to specify we want the method called exactly once.

```java
@Mock private InitialisableObserver<String> mockObserver;
@Mock private CachingObservable<String> mockObservable;

@Test
public void test_InitialiseOnSubscribeObservable_subscription() {
    //Arrange
    String value = "value";
    
    when(mockObservable.getValue()).thenReturn(value);
    
    // Object we are really testing
    InitialiseOnSubscribeObservable<String> initObservable = 
                           new InitialiseOnSubscribeObservable<>(mockObservable);
    
    //Act
    Object returned = initObservable.addObserver(mockObserver);
    
    //Assert: The initialisable observer has its update method called once
    verify(mockObserver, times(1)).update(value, null, false);
    
    // The InitialiseOnSubscribeObservable has the value returned from the mock observable
    assertEquals(value, initObservable.getValue());
    
    // A Unsubscriber is returned
    assertEquals(Unsubscriber.class, returned.getClass());
}
```

### DB Tests using `Answer`

In [`RdbWritterTests`](https://github.com/ISISComputingGroup/EPICS-IocLogServer/blob/master/LogServer/src/test/java/org/isis/logserver/rdb/RdbWritterTests.java),
there is an example of using an answer to perform a more complicated return. The answer works like this:

```java
when(mockPreparedStatement.executeQuery()).thenAnswer(resultAndStatement.new ResultsSetAnswer());
```

In this case the answer class is implemented as an inner class of another class, but this is not necessary.
The answer looks like:

```java
public class ResultsSetAnswer implements Answer<ResultSet> {
    @Override
    public ResultSet answer(InvocationOnMock invocation) throws Throwable {
        openedResultsSet++;
        return resultSet;
    }
}
```

In the above example, the `Answer` is used to keep track of the number of times a result set was opened; this `Answer`
implementation makes that information available in its parent class.

## Tips and Advice

* Use mocks to test interactions between a class and a particular interface
* Use mocks to avoid unit tests touching complex or buggy dependencies
* Do not mock type you don't own? Perhaps...
* Do not mock simple classes or value objects - may as well use the real thing
* Do not mock everything!
