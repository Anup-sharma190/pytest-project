# PYTEST METHOD NAME SHOULD START WITH TEST_
#any code should be wrapped in method only
#method name should have sence ,2 method name should not be same otherwise pytest will override previous one
#-k stands for keyword selection to execute method by its key word
#you can run specific file with py.test -k <filename> -v -s
# smoke test is basic test if it fail reject the build dont move further

# you can mark (tag) tests with @pytest.mark.smoke and than run with -m
#def test_firstProgram():# 1 test method treated by pytest it alwasys treat one method one test case
#@pytest.mark.smoke
# you can skip by custommakr @pytest.mark.skip
#@pytest.mark.skip
#@pytest.mark.xfail
#fixture are used as setup and tear down methods for test cases
#make conftest file coomen for all files link to fixture


# tests/test_assertions.py

def test_equal():
    assert 5 == 5


def test_not_equal():
    assert 5 != 3


def test_in_list():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits


def test_greater_than():
    assert 10 > 5


def test_string_contains():
    message = "pytest makes testing easy"
    assert "pytest" in message






