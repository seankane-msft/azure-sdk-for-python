import os

import pytest
import vcr

class InheritedTestClass(object):
    def setup_class(self,
        enable_recording=True
    ):
        print("setting up InheritedTestClass\n")
        self.abc = 123
        self.vcr = vcr.VCR(
            cassette_library_dir="abc",
            # before_record_request=self._process_request_recording,
        )

    def teardown_class(self):
        print("tearing down InheritedTestClass\n")

    def setup_method(self, method):
        self.method_name = method.__name__
        self.diagnose = os.environ.get("AZURE_TEST_DIAGNOSE", None) == 'True'
        self.clean_up_functions = []
        print("setup_method {} \n".format(self.method_name))

    def teardown_method(self, method):
        print("tearing down: {}\n".format(self.method_name))
        for f in self.clean_up_functions:
            f()

    def create_random_name(self, prefix, length):
        if len(prefix) > length:
            raise ValueError('The length of the prefix must not be longer than random name length')

        padding_size = length - len(prefix)
        if padding_size < 4:
            raise ValueError('The randomized part of the name is shorter than 4, which may not be able to offer enough '
                            'randomness')

        random_bytes = os.urandom(int(math.ceil(float(padding_size) / 8) * 5))
        random_padding = base64.b32encode(random_bytes)[:padding_size]

        return str(prefix + random_padding.decode().lower())

class TestTables(InheritedTestClass):

    def setup_class(self):
        super(TestTables, self).setup_class(self)
        self.vcr = "ABC"
        print("setting up TestTables\n")

    def teardown_class(self):
        super(TestTables, self).teardown_class(self)
        self.vcr = 123
        print("tearing down TestTables\n")

    def test_something(self):
        assert self.diagnose is not None
        assert self.vcr is not None
        assert 1

    def test_something_else(self):
        assert self.diagnose is not None
        assert self.abc is 123
        assert 3