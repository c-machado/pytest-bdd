import json
import pytest
import selenium.webdriver

from selenium.webdriver import Chrome


CONFIG_PATH = 'tests/step_defs/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'Headless Chrome', 'firefox']


# print a message with the step in case of error
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dictionary
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    assert isinstance(config['wait_time'], int)
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture()
def browser(config_browser, config_wait_time):
    # Initialize Chrome WebDriver Instance
    driver = selenium.webdriver.Remote(command_executor='http://192.168.0.24:4444/wd/hub',
            desired_capabilities={"browserName": "firefox"})
    # if config_browser == 'chrome':
    #     driver = selenium.webdriver.Chrome()
    # elif config_browser == 'firefox':
    #     driver = selenium.webdriver.Firefox()
    # elif config_browser == 'Headless Chrome':
    #     opts = selenium.webdriver.ChromeOptions()
    #     opts.add_argument('headless')
    #     driver = selenium.webdriver.Chrome(options=opts)
    # else:
    #     raise Exception(f'"{config_browser}" is not supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
