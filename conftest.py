# tests/test_class_fixtures.py
import pytest

@pytest.fixture(scope="class")
def setup_class_fixture():
    print("\n[Setup] Creating shared resource for test class")
    resource = {"user": "Anup", "role": "QA Automation"}
    yield resource
    print("\n[Teardown] Cleaning up shared resource")

class TestClassFixtures:
    def test_user_in_resource(self, setup_class_fixture):
        assert setup_class_fixture["user"] == "Anup"

    def test_role_in_resource(self, setup_class_fixture):
        assert setup_class_fixture["role"] == "QA Automation"

    def test_add_key(self, setup_class_fixture):
        setup_class_fixture["level"] = "Intermediate"
        assert "level" in setup_class_fixture
