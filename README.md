fakery
======
[![Build Status](https://travis-ci.org/garyjohnson/fakery.svg?branch=master)](https://travis-ci.org/garyjohnson/fakery)

Trying to make fudge mocks in Python easier.

# Installing
To install using pip, you can include ```fakery``` in your requirements.txt file, and then install using ```pip install -r requirements.txt```

# Usage
To use, import ```fakery.fudge_test_case.FudgeTestCase``` and use it as the base class instead of the usual ```unittest.TestCase```:

```python
from fakery.fudge_test_case import FudgeTestCase

class MyTest(FudgeTestCase):

  def test_foo(self):
    pass
```

Here's what fakery does for you:

#### Automatically adds @fudge.with_fakes

With just fudge: @fudge.with_fakes must be added to each test to acutally verify expectations on mocks. Very easy to forget and have tests that pass even when they shouldn't.

```python
class MyTest(TestCase):

    @fudge.with_fakes
    def test_foo(self):
        my_mock.expects_call()
```

With fakery: @fudge.with_fakes is added automatically to each test

```python
class MyTest(FudgeTestCase):

    def test_foo(self):
        my_mock.expects_call()
```

#### Automatically clears expectations
With just fudge: You have to call fudge.clear_expectations() after each test

```python
class MyTest(TestCase):

    def tearDown(self):
        fudge.clear_expectations()
```

With fakery: fudge.clear_expectations() is automatically called after each test

```python
class MyTest(FudgeTestCase):

    # no tearDown needed!
```

#### Makes mocking constructors easier
With just fudge: You have to mock the constructor, patch it, then verify against the mock that it returns

```python
class MyTest(TestCase):

    def setUp(self):
        foo_type_mock = fudge.Fake('Foo').is_callable()
        self.foo_type_patch = fudge.patch_object('my_module', 'Foo', foo_type_mock)
        self.foo_instance_mock = foo_type_mock.returns_fake().is_a_stub()

    def tearDown(self):
        fudge.clear_expectations()
        self.foo_type_patch.restore()

    def test_foo(self):
      self.foo_instance_mock.expects_call('bar')
```

With fakery: Convenience methods are provided for mocking constructors, and when used, patches are automatically restored

```python
class MyTest(FudgeTestCase):

    def setUp(self):
        self.foo_instance_mock = self.patch_constructor('my_module', 'Foo')

    def test_foo(self):
        self.foo_instance_mock.expects_call('bar')
```

####TODO: document patch_attribute and patch_method, notes about how you import (import x.y vs from x import y), better usage scenarios
