from selenium.webdriver.common.by import By

import settings
from base.locators import (
    ComponentLocator,
    GroupLocator,
    Locator,
)
from components.navbars import InstitutionsNavbar
from pages.base import OSFBasePage


class InstitutionsLandingPage(OSFBasePage):
    url = settings.OSF_HOME + '/institutions/'

    # TODO fix insitution typo
    identity = Locator(
        By.CSS_SELECTOR, 'div[data-test-insitutions-header]', settings.VERY_LONG_TIMEOUT
    )

    search_bar = Locator(By.CSS_SELECTOR, '.ember-text-field')

    # Group Locators
    institution_list = GroupLocator(By.CSS_SELECTOR, 'span[data-test-institution-name]')

    navbar = ComponentLocator(InstitutionsNavbar)


class BaseInstitutionPage(OSFBasePage):

    base_url = settings.OSF_HOME + '/institutions/'
    url_addition = ''

    def __init__(self, driver, verify=False, institution_id=''):
        self.institution_id = institution_id
        super().__init__(driver, verify)

    @property
    def url(self):
        return self.base_url + self.institution_id + self.url_addition


class InstitutionBrandedPage(BaseInstitutionPage):

    identity = Locator(
        By.CSS_SELECTOR,
        '#fileBrowser > div.db-header.row > div.db-buttonRow.col-xs-12.col-sm-4.col-lg-3 > div > input',
    )

    empty_collection_indicator = Locator(By.CLASS_NAME, 'db-non-load-template')

    # Group Locators
    project_list = GroupLocator(By.CSS_SELECTOR, '#tb-tbody > div > div > div.tb-row')


class InstitutionAdminDashboardPage(BaseInstitutionPage):

    url_addition = '/dashboard'

    identity = Locator(By.CSS_SELECTOR, 'div[data-analytics-scope="Dashboard"]')
    loading_indicator = Locator(By.CSS_SELECTOR, '.ball-scale', settings.LONG_TIMEOUT)
    departments_listbox_trigger = Locator(
        By.CSS_SELECTOR,
        'div.ember-basic-dropdown-trigger.ember-power-select-trigger._select_tdvp4z',
    )
    total_user_count = Locator(
        By.CSS_SELECTOR,
        'div.ember-view._panel_1dj7yu._sso-users-connected_1w5vdt > div > div.panel-body',
    )
    total_project_count = Locator(
        By.CSS_SELECTOR,
        'div.ember-view._panel_1dj7yu._projects_1w5vdt > div > div.panel-body > div > h3',
    )
    public_project_count = Locator(
        By.CSS_SELECTOR, 'div._projects-count_1ky9tx > span:nth-child(1) > strong'
    )
    private_project_count = Locator(
        By.CSS_SELECTOR, 'div._projects-count_1ky9tx > span:nth-child(2) > strong'
    )

    department_options = GroupLocator(
        By.CSS_SELECTOR, 'ul.ember-power-select-options > li.ember-power-select-option'
    )
    user_table_rows = GroupLocator(
        By.CSS_SELECTOR,
        'div._table-wrapper_1w5vdt > div > div.ember-view > div > div > table > tbody > tr',
    )

    def select_department_from_listbox(self, department):
        for option in self.department_options:
            if option.text == department:
                option.click()
                break
