import pytest


@pytest.fixture()
def test():
    print("Normal Scope !")
    yield
    print("Second Scope")


def test1(test):
    print("Execute it ")