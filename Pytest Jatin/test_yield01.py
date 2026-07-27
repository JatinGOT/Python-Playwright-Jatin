import pytest


# Module fixture (runs once for this file)
@pytest.fixture(scope="module")
def preWork():
    print("\n[Module Setup]")

    # Return data to the test
    return "pass"


# Function fixture (runs before and after every test)
@pytest.fixture(scope="function")
def secondWork():
    print("[Function Setup]")

    yield

    print("[Function Teardown]")


def test_initialCheck(preWork, secondWork):
    print("Executing First Test")

    assert preWork == "pass"


def test_secondCheck(preWork, secondWork):
    print("Executing Second Test")

    assert preWork == "pass"