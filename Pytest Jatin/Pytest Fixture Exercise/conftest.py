import  pytest


# Runs only ONCE for the entire test execution
@pytest.fixture(scope="session")
def setup_session():
    print("\n========== SESSION START ==========")

# Runs ONCE for each test file (module)
@pytest.fixture(scope="module")
def setup_module():
    print("\n========== MODULE START ==========")


# Runs BEFORE and AFTER every test function
@pytest.fixture(scope="function")
def setup_function():
    print("\n========== FUNCTION START ==========")

