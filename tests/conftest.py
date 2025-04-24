import pytest
from stellar_harvest_ie_producers.logging_config import setup_logging


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """
    This fixture runs once per test session, before any tests execute,
    and configures the root logger according to our logging_config.
    """
    setup_logging()


# def pytest_configure(config):
#     """
#     This hook is called as soon as pytest is initialized (before collecting tests).
#     """
#     setup_logging()
