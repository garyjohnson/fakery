import fudge
from unittest import TestCase
from fakery.fudge_test_case import FudgeTestCase

class FudgeTestCaseTest(TestCase):

    def tearDown(self):
        fudge.clear_expectations()

    @fudge.with_fakes
    def test_patches_test_method_to_clear_calls(self):
        clear_calls_mock = fudge.Fake('clear_calls').is_callable()
        clear_calls_patch = fudge.patch_object('fudge', 'clear_calls', clear_calls_mock)
        verify_patch = fudge.patch_object('fudge', 'verify', fudge.Fake('verify').is_callable())
        class MyTest(FudgeTestCase):
            def test_foo(self):
                pass

        clear_calls_mock.expects_call()

        test_case = MyTest('test_foo')
        test_case.test_foo()

        clear_calls_patch.restore()
        verify_patch.restore()

    @fudge.with_fakes
    def test_patches_test_method_to_verify(self):
        clear_calls_patch = fudge.patch_object('fudge', 'clear_calls', fudge.Fake('clear_calls').is_callable())
        verify_mock = fudge.Fake('verify').is_callable()
        verify_patch = fudge.patch_object('fudge', 'verify', verify_mock)
        class MyTest(FudgeTestCase):
            def test_foo(self):
                pass

        verify_mock.expects_call()

        test_case = MyTest('test_foo')
        test_case.test_foo()

        clear_calls_patch.restore()
        verify_patch.restore()

    @fudge.with_fakes
    def test_patches_test_method_to_clear_calls_only_once(self):
        clear_calls_mock = fudge.Fake('clear_calls').is_callable()
        clear_calls_patch = fudge.patch_object('fudge', 'clear_calls', clear_calls_mock)
        verify_mock = fudge.Fake('verify').is_callable()
        verify_patch = fudge.patch_object('fudge', 'verify', verify_mock)
        class MyTest(FudgeTestCase):
            def test_foo(self):
                pass

        verify_mock.expects_call().times_called(1)
        clear_calls_mock.expects_call().times_called(1)

        test_case = MyTest('test_foo')
        test_case = MyTest('test_foo')
        test_case.test_foo()

        clear_calls_patch.restore()
        verify_patch.restore()
