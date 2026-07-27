import pytest

@pytest.fixture(scope="module")
def setup():
    print("I am fixture")
def test_initial(setup):
    print("First test case !")

# @pytest.mark.skip
@pytest.mark.smoke

def test_second(setup):
    print("Second test case !")