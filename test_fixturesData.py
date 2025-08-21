# tests/test_fixtures.py
import pytest

# ---------------- Fixture Example ----------------
@pytest.fixture
def sample_list():
    print("\nSetup: Creating a sample list")
    data = [1, 2, 3, 4, 5]
    yield data   # Test runs here
    print("\nTeardown: Clearing the list")

# ---------------- Tests Using Fixture ----------------
def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_max(sample_list):
    assert max(sample_list) == 5

def test_min(sample_list):
    assert min(sample_list) == 1
