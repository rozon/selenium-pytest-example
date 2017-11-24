import pytest


@pytest.fixture
def browser():
    return pytest.config.getoption("-B")


@pytest.fixture
def browserstack_flag():
    return pytest.config.getoption("-M")


@pytest.fixture
def browser_version():
    return pytest.config.getoption("-V")


@pytest.fixture
def platform():
    return pytest.config.getoption("-P")


@pytest.fixture
def os_version():
    return pytest.config.getoption("-O")


@pytest.fixture
def resolution():
    return pytest.config.getoption("-R")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Default option is chrome")
    parser.addoption("-M", "--browserstack_flag",
                     dest="browserstack_flag",
                     default="N",
                     help="Run the test in Browserstack: Y or N")
    parser.addoption("-V", "--ver",
                     dest="browser_version",
                     default="62",
                     help="Browser version")
    parser.addoption("-P", "--platform",
                     dest="platform",
                     default="Windows",
                     help="OS Platform: Windows, Linux, OS X")
    parser.addoption("-O", "--os_version",
                     dest="os_version",
                     default="10",
                     help="OS Version: XP, 7, 10, High Sierra")
    parser.addoption("-R", "--resolution",
                     dest="resolution",
                     default="1366x768",
                     help="OS Resolution: 1024x768, 1280x800, 1280x1024, 1366x768")
