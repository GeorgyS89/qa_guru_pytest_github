import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def mobile():
    browser.config.window_width = 800
    browser.config.window_height = 600



def test_github_signin_desktop(desktop):
    browser.open('/')
    browser.element(".HeaderMenu-link--sign-in").click()


def test_github_signin_mobile(mobile):
    browser.open('/')
    browser.element(".Button-label").click()
    browser.element(".HeaderMenu-link--sign-in").click()

