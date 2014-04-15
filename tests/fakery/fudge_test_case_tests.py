import fudge
from unittest import TestCase
from fakery import FudgeTestCase

class FudgeTestCaseTest(TestCase):

    class MyTest(FudgeTestCase):
        def test_foo(self):
            pass
        def tearDown(self):
            pass

    def tearDown(self):
        fudge.clear_expectations()

    @fudge.with_fakes
    def test_patches_test_method_to_clear_calls(self):
        self.setup_fudge_mocks()

        self.clear_calls_mock.expects_call()

        test_case = FudgeTestCaseTest.MyTest('test_foo')
        test_case.test_foo()
        self.restore_fudge_patches()

    @fudge.with_fakes
    def test_patches_test_method_to_verify(self):
        self.setup_fudge_mocks()

        self.verify_mock.expects_call()

        test_case = FudgeTestCaseTest.MyTest('test_foo')
        test_case.test_foo()
        self.restore_fudge_patches()

    @fudge.with_fakes
    def test_clears_expectations_in_tear_down(self):
        self.setup_fudge_mocks()

        self.clear_expectations_mock.expects_call()

        test_case = FudgeTestCaseTest.MyTest('test_foo')
        test_case.tearDown()
        self.restore_fudge_patches()

    @fudge.with_fakes
    def test_clears_expectations_in_class_without_tear_down(self):
        self.setup_fudge_mocks()
        class TestWithoutTearDown(FudgeTestCase):
            def test_foo(self):
                pass

        self.clear_expectations_mock.expects_call()

        test_case = TestWithoutTearDown('test_foo')
        test_case.tearDown()
        self.restore_fudge_patches()

    @fudge.with_fakes
    def test_patches_test_method_to_clear_calls_only_once(self):
        self.setup_fudge_mocks()

        self.verify_mock.expects_call().times_called(1)
        self.clear_calls_mock.expects_call().times_called(1)

        test_case = FudgeTestCaseTest.MyTest('test_foo')
        test_case = FudgeTestCaseTest.MyTest('test_foo')
        test_case.test_foo()
        self.restore_fudge_patches()

    def setup_fudge_mocks(self):
        self.clear_expectations_mock = fudge.Fake('clear_expectations').is_callable()
        self.clear_expectations_patch = fudge.patch_object('fudge', 'clear_expectations', self.clear_expectations_mock)
        self.clear_calls_mock = fudge.Fake('clear_calls').is_callable()
        self.clear_calls_patch = fudge.patch_object('fudge', 'clear_calls', self.clear_calls_mock)
        self.verify_mock = fudge.Fake('verify').is_callable()
        self.verify_patch = fudge.patch_object('fudge', 'verify', self.verify_mock)

    def restore_fudge_patches(self):
        self.clear_expectations_patch.restore()
        self.clear_calls_patch.restore()
        self.verify_patch.restore()
