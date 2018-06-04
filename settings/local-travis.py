from .defaults import *
import os

os_env = os.environ

DRIVER = 'Remote'

caps = {
    'chrome': {'browser': 'Chrome', 'browser_version': '61.0', 'os': 'Windows', 'os_version': '10', 'resolution': '2048x1536'},
    'edge': {'browser': 'Edge', 'os': 'Windows', 'os_version': '10', 'resolution': '2048x1536'},
    'firefox': {'os' : 'OS X', 'os_version' : 'Sierra', 'browser' : 'Firefox', 'browser_version' : '59.0', 'browserstack.geckodriver' : '0.18.0'},
    'msie': {'browser': 'IE', 'browser_version': '11', 'os': 'Windows', 'os_version': '10', 'resolution': '2048x1536'},
    'android': {'device': 'Samsung Galaxy S8', 'realMobile': 'true', 'os_version': '7.0'},
    'ios': {'device': 'iPhone 7', 'realMobile': 'true', 'os_version': '10.0'},
    'safari': {'browser': 'Safari', 'browser_version': '10.1', 'os': 'OS X', 'os_version': 'Sierra', 'safari.options': {'technologyPreview': 'true'}}
}

BUILD = os_env.get('TEST_BUILD', 'firefox')
DESIRED_CAP = caps[BUILD]

upper_build = BUILD.upper()
password = os_env.get('{}_USER_PASSWORD'.format(upper_build))

USER_ONE = os_env.get('{}_USER'.format(upper_build))
USER_ONE_PASSWORD = password if password else os_env.get('USER_ONE_PASSWORD')


#TODO: Fix settings. Possibly turn into envars. Let the consistent pattern be utilized.
OSF_HOME = 'https://test.osf.io'
API_DOMAIN = 'https://test-api.osf.io'
FILE_DOMAIN = 'https://test-files.osf.io'

BSTACK_USER = os.environ.get('BSTACK_USER')
BSTACK_KEY = os.environ.get('BSTACK_KEY')