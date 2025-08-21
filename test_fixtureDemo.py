
import pytest

@pytest.fixture()# because already commenly declared in conftest.py
def setup():
    print("i am setting up")

# we will delare a class no need to write setup for 100 test case

@pytest.mark.usefixtures("setup")# this is for all cases no no need to write setup agin again
class Testexample:
    def test_fixture_demo(self):
        print("i will execute steps of fixtureDemo")

    def test_fixture_demo1(self):
        print("i will execute steps of fixtureDemo1")

    def test_fixture_demo2(self):
        print("i will execute steps of fixtureDemo2")

    def test_fixture_demo3(self):
        print("i will execute steps of fixtureDemo3")


import pytest

class TestFixtureDemo:

    def test_fixture_demo(self):
        print("This is a test using fixture demo")
