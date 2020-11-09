from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print( "Launching Chrome browser" )
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print( "Launching FireFox browser" )
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver


# This method will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption( "--browser" )


# This is method will pass the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption( "--browser" )


##################### Pytest HTML Report ################################

# It is hook for adding environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'DBankDemo'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Tanjot'


# It is hook to delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop( "Java_Home", None )
    metadata.pop( "Plugins", None )
