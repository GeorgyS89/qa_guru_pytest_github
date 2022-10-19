import pytest
from selene import have, be
from selene.support.shared import browser


@pytest.fixture(params=[(800, 600), (1920, 1080)])
def browser_size(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


mobile = pytest.mark.parametrize("browser_size", [(800, 600)], indirect=True)


@mobile
def test_parametrized_for_mobile(browser_size):
    browser.open('/')
    browser.element(".Button-label").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))


desktop = pytest.mark.parametrize("browser_size", [(1920, 1080)], indirect=True)


@desktop
def test_parametrized_for_desktop(browser_size):
    browser.open('/')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))
