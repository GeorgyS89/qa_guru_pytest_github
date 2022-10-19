import pytest
from selene.support.shared import browser
from selene.support import by


@pytest.mark.parametrize(["browser_height", "browser_width"],
                         [(1920, 1080), (800, 600)],
                         ids=["Desktop", "Mobile"],
                         )
def test_parametrized_for_desktop(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser.config.window_width != 1920:
        pytest.skip("This is a test for desktop use!")
    browser.open("https://github.com")
    browser.element(by.link_text("Sign in")).click()


@pytest.mark.parametrize(["browser_height", "browser_width"],
                         [(1920, 1080), (800, 600)],
                         ids=["Desktop", "Mobile"],
                         )
def test_parametrized_for_mobile(browser_height, browser_width):
    browser.config.window_height = browser_height
    browser.config.window_width = browser_width
    if browser.config.window_width > 600:
        pytest.skip("This is a test for mobile use!")
    browser.open("https://github.com")
    browser.element(".Button-label").click()
    browser.element(by.link_text("Sign in")).click()

