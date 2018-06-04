import pytest

from pages.login import login
from pages.cos import COSDonatePage
from pages.search import SearchPage
from pages.landing import LandingPage
from pages.support import SupportPage
from pages.meetings import MeetingsPage
from pages.project import MyProjectsPage
from pages.dashboard import DashboardPage
from pages.registries import RegistriesPage
from pages.user import UserProfilePage, UserSettingsPage
from pages.preprints import PreprintLandingPage, PreprintSubmitPage


#TODO: Test Navbar from all services including reviews and such - they might not have the same navbar always


# Class used to inject generic tests
class NavbarTestLoggedOut:

    def test_osf_home_dropdown_link(self, page, driver):
        page.navbar.service_dropdown.click()
        page.navbar.home_link.click()
        LandingPage(driver, verify=True)

    def test_preprints_dropdown_link(self, page, driver):
        page.navbar.service_dropdown.click()
        page.navbar.preprints_link.click()
        PreprintLandingPage(driver, verify=True)

    def test_registries_dropdown_link(self, driver, page):
        page.navbar.service_dropdown.click()
        page.navbar.registries_link.click()
        RegistriesPage(driver, verify=True)

    def test_meetings_dropdown_link(self, page, driver):
        page.navbar.service_dropdown.click()
        page.navbar.meetings_link.click()
        MeetingsPage(driver, verify=True)

    def test_sign_up_button(self, driver, page):
        page.navbar.sign_up_button.click()
        assert 'register' in driver.current_url

    def test_user_dropdown_not_present(self, page):
        assert page.navbar.user_dropdown.absent()

# Class used to inject generic tests
class NavbarTestLoggedIn:

    def test_user_profile_menu_profile_link(self, driver, page):
        page.navbar.user_dropdown.click()
        page.navbar.user_dropdown_profile.click()
        assert UserProfilePage(driver, verify=True)

    def test_user_profile_menu_support_link(self, driver, page):
        page.navbar.user_dropdown.click()
        page.navbar.user_dropdown_support.click()
        assert SupportPage(driver, verify=True)

    def test_user_profile_menu_settings_link(self, driver, page):
        page.navbar.user_dropdown.click()
        page.navbar.user_dropdown_settings.click()
        assert UserSettingsPage(driver, verify=True)

    def test_sign_in_button_not_present(self, page):
        assert page.navbar.sign_in_button.absent()

    def test_sign_up_button_not_present(self, page):
        assert page.navbar.sign_up_button.absent()

    def test_logout_link(self, driver, page):
        page.navbar.user_dropdown.click()
        page.navbar.logout_link.click()
        assert 'goodbye' in driver.current_url
        login(driver)


class TestOSFHomeNavbar(NavbarTestLoggedOut):

    @pytest.fixture()
    def page(self, driver):
        page = LandingPage(driver)
        page.goto()
        return page

    def test_my_projects_link_not_present(self, page):
        assert page.navbar.my_projects_link.absent()

    def test_search_link(self, driver, page):
        page.navbar.search_link.click()
        assert SearchPage(driver, verify=True)

    def test_support_link(self, page, driver):
        page.navbar.support_link.click()
        assert SupportPage(driver, verify=True)

    def test_donate_link(self, page, driver):
        page.navbar.donate_link.click()
        COSDonatePage(driver, verify=True)

    def test_sign_in_button(self, page, driver):
        page.navbar.sign_in_button.click()
        assert 'login' in driver.current_url


class TestOSFHomeNavbarLoggedIn(NavbarTestLoggedIn):

    @pytest.fixture()
    def page(self, driver, must_be_logged_in):
        page = DashboardPage(driver)
        page.goto()
        return page

    def test_my_projects_link(self, page, driver):
        page.navbar.my_projects_link.click()
        assert MyProjectsPage(driver, verify=True)


class TestPreprintsNavbar(NavbarTestLoggedOut):

    @pytest.fixture()
    def page(self, driver):
        page = PreprintLandingPage(driver)
        page.goto()
        return page

    # todo: add id to those html tags in ember osf to make the find_element possible
    # def test_search_link(self):
    #     page.navbar.search_link.click()
    #     search_url = settings.OSF_HOME + '/search/'
    #     assert driver.current_url == search_url
    #
    # def test_support_link(self):
    #     page.navbar.support_link.click()
    #     support_url = settings.OSF_HOME + '/support/'
    #     assert driver.current_url == support_url
    #
    # def test_donate_link(self):
    #     page.navbar.donate_link.click()
    #     assert 'cos.io/donate-to-cos' in driver.current_url
    #
    # def test_sign_in_button(self):
    #     page.navbar.sign_in_button.click()
    #     assert 'login' in driver.current_url

@pytest.mark.usefixtures('must_be_logged_in')
class TestPreprintsNavbarLoggedIn(NavbarTestLoggedIn):

    @pytest.fixture()
    def page(self, driver):
        page = PreprintLandingPage(driver)
        page.goto()
        return page

    def test_add_a_preprint_link(self, page, driver):
        page.navbar.add_a_preprint_link.click()
        PreprintSubmitPage(driver, verify=True)


class TestMeetingsNavbar(NavbarTestLoggedOut):

    @pytest.fixture()
    def page(self, driver):
        page = MeetingsPage(driver)
        page.goto()
        return page

    def test_search_link_not_present(self, page):
        assert page.navbar.search_link.absent()

    def test_support_link(self, page, driver):
        page.navbar.support_link.click()
        support_url = 'http://help.osf.io/m/meetings/'
        assert driver.current_url == support_url

    def test_donate_link(self, page, driver):
        page.navbar.donate_link.click()
        COSDonatePage(driver, verify=True)

    def test_sign_in_button(self, page, driver):
        page.navbar.sign_in_button.click()
        assert 'login' in driver.current_url


@pytest.mark.usefixtures('must_be_logged_in')
class TestMeetingsNavbarLoggedIn(NavbarTestLoggedIn):

    @pytest.fixture()
    def page(self, driver):
        page = MeetingsPage(driver)
        page.goto()
        return page


class TestRegistriesNavbar(NavbarTestLoggedOut):

    @pytest.fixture()
    def page(self, driver):
        page = RegistriesPage(driver)
        page.goto()
        return page

    # todo: add id to those html tags in ember osf to make the find_element possible
    # def test_search_link(self):
    #     page.navbar.search_link.click()
    #     search_url = settings.OSF_HOME + '/search/'
    #     assert driver.current_url == search_url
    #
    # def test_support_link(self):
    #     page.navbar.support_link.click()
    #     support_url = settings.OSF_HOME + '/support/'
    #     assert driver.current_url == support_url
    #
    # def test_donate_link(self):
    #     page.navbar.donate_link.click()
    #     assert 'cos.io/donate-to-cos' in driver.current_url
    #
    # def test_sign_in_button(self):
    #     page.navbar.sign_in_button.click()
    #     assert 'login' in driver.current_url


@pytest.mark.usefixtures('must_be_logged_in')
class TestRegistriesNavbarLoggedIn(NavbarTestLoggedIn):

    @pytest.fixture()
    def page(self, driver):
        page = RegistriesPage(driver)
        page.goto()
        return page