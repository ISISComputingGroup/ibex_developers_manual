> [Wiki](Home) > [The GUI](The-GUI) > [Testing](GUI-Testing) > Mockito

You should read the guide to testing in IBEX before reading this guide.

This guide gives some basic advice on using Mockito for unit testing in IBEX. For more information on Mockito see http://mockito.org/.

Please update this guide with tips or anything you find useful in Mockito.

## Test Doubles

Test doubles are objects that stand in for a real object, for the purposes of unit testing. Terminology varies but there are four usual types that are described:

* Dummy - an object that is passed around but never used

* Fake - a working implementation of a class with a cheat, for example an in memory database

* Stub - an object that provides a canned answer to a method call

* Mock - fake objects which know about which method calls they receive

See [this article](http://martinfowler.com/articles/mocksArentStubs.html) for more information. Mockito mostly helps with Stub and Mock doubles.

## Verifying Interactions

```
    import static org.mockito.Mockito.*;

    // mock creation
    List mockedList = mock(List.class);

    // using mock object - it does not throw any "unexpected interaction" exception
    mockedList.add("one");
    mockedList.clear();

    // selective, explicit, highly readable verification
    verify(mockedList).add("one");
    verify(mockedList).clear();
```

Here the List interface is mocked, and has some method calls made on it. The verify calls replace the usual assert calls in this unit test, and check the method calls were made. In this example it is trivial to see they are called.

## Stubbing Method Calls

```
    // you can mock concrete classes, not only interfaces
    LinkedList mockedList = mock(LinkedList.class);

    // stubbing appears before the actual execution
    when(mockedList.get(0)).thenReturn("first");

    // the following prints "first“
    System.out.println(mockedList.get(0));

    // the following prints "null" because get(999) was not stubbed
    System.out.println(mockedList.get(999));
```
    
This time the concrete class LinkedList is mocked instead of an interface. The mocked object returns what is asked of it when the method call is made with identical arguments.

## IBEX Example

Below is a less trivial example, showing how the verification and stubbing can be used to check behaviour of an observable.

In this example InitialiseOnSubscribeObservable takes another observable as its argument, gets the current value of that observable, and listens for changes. Here we stub the class that InitialiseOnSubscribeObservable is observing, to simplify the test. The only method call we care about is `getValue()`.

The InitialisableObserver is also mocked. As part of the test we want to check that it has its `update()` method called with a specific set of arguments. We use `times(1)` to specify we want the method called exactly once.

```
    @Test
    public void test_InitialiseOnSubscribeObservable_subscription() {
      //Arrange
      String value = "value";

      // Mock observer, templated objects need cast
      InitialisableObserver<String> mockObserver = 
                               (InitialisableObserver<String>) mock(InitialisableObserver.class);

      // Mock observable with stub method
      CachingObservable<String> mockObservable = 
                               (CachingObservable<String>) mock(CachingObservable.class);
      when(mockObservable.getValue()).thenReturn(value);

      // Object we are really testing
      InitialiseOnSubscribeObservable<String> initObservable = 
                               new InitialiseOnSubscribeObservable<>(mockObservable);

      //Act
      Object returned = initObservable.addObserver(mockObserver);

      //Assert
      // The initialisable observer has its update method called once
      verify(mockObserver, times(1)).update(value, null, false);

      // The InitialiseOnSubscribeObservable has the value returned from the mock observable
      assertEquals(value, initObservable.getValue());

      // A Unsubscriber is returned
      assertEquals(Unsubscriber.class, returned.getClass());
    }
```

## Times Method is Called

Options for checking how many times a particular method is called:

* `atLeast(int minNumber)` at least this many times

* `atLeastOnce()` at least once

* `atMost(int maxNumber)` at most this many times

* `never()` same as `times(0)`

* `times(int number)` exactly this number of times
    
## Any Methods

When verifying method calls if the value of an argument is not important Mockito allows you to check that any object of a specific type was used as an argument instead.

```
    // The initialisable observer has its update method called once
    verify(mockObserver, times(1)).update(value, any(Exception.class), anyBoolean());
```
    
For common types methods such as `anyString()` are available, otherwise `any(Object.class)` can be used. A null object will also be matched by using any.

## Capturing Values on Method Calls

If you want to capture the object called in a method, perhaps to check some value, then a captor can be used. See the code below for an example of how to do this. It is important to call `MockitoAnnotations.initMocks(this);` in the test set up method, otherwise the captor is never initialised.

```
    @Captor ArgumentCaptor<Exception> exceptionCaptor;
    
    @Before
	public void setUp() {
		// This is to initialise the exceptionCaptor
		MockitoAnnotations.initMocks(this);
    }

    @Test
    public void test_ConvertingObservable_with_conversion_exception() throws ConversionException {
		//Arrange
		InitialisableObserver<String> mockObserver = mock(InitialisableObserver.class);
		
		// initObservable is what our ConvertingObservable looks at, and testObservable we can call set methods on
		TestableObservable<Integer> testObservable = new TestableObservable<>();
		InitialiseOnSubscribeObservable<Integer> initObservable = new InitialiseOnSubscribeObservable<Integer>(testObservable);
		
		// Mock converter, with a stub conversion method
		Converter<Integer, String> mockConverter = mock(Converter.class);
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

## Checking Order of Method Calls

Mockito can be used to check the order methods were called in.

```
    InOrder inOrder = inOrder(firstMock, secondMock);
     
    inOrder.verify(firstMock).add("was called first");
    inOrder.verify(secondMock).add("was called second");
```
    
## Spies

Spies can be used to stub a method or verify calls on a real class. Needing to use a partial mock like this might be a symptom of problems with code though!

```
    // These are equivalent    
    @Spy Foo spyOnFoo = new Foo("argument");
    Foo spyOnFoo = Mockito.spy(new Foo("argument"));
```

## DB Tests using Answer Example

In RdbWritterTests (C:\Instrument\Apps\EPICS\ISIS\IocLogServer\master\LogServer\src\test\java\org\isis\logserver\rdb) there is an example of using an answer to perform a more complicated return. The answer works like this:

```
when(mockPreparedStatement.executeQuery()).thenAnswer(resultAndStatement.new ResultsSetAnswer());
```
I have chosen to implement the answer class as an inner class of another class but you don't have to. The answer looks like:

```
public class ResultsSetAnswer implements Answer<ResultSet> {
        @Override
        public ResultSet answer(InvocationOnMock invocation) throws Throwable {
            openedResultsSet++;
            return resultSet;
        }
    }
```
The reason I am using answer here is to keep the number of times I opened a results set up to date so this answer stores that info in its parent class.

## Tips and Advice

* Use mocks to test interactions between a class and a particular interface

* Use mocks to avoid unit tests touching complex or buggy dependencies

* Do not mock type you don't own? Perhaps...

* Do not mock simple classes or value objects - may as well use the real thing

* Do not mock everything!
