import pytest
from pages.elements_page import ElementsPage
from pages.locators import BasePageLocators, ElementsPageLocators


@pytest.mark.select_file_in_subdir
class TestElementsCheckBox:
    def test_check_box_in_subdir(self, browser):
        link = "https://demoqa.com"
        page = ElementsPage(browser, link)
        page.open()
        page.click_on(*BasePageLocators.ELEMENTS)
        page.click_on(*ElementsPageLocators.CHECK_BOX)
        page.click_on(*ElementsPageLocators.DIR_EXPAND)
        page.click_on(*ElementsPageLocators.SUBDIR_EXPAND)
        page.click_on(*ElementsPageLocators.FILE_IN_SUBDIR)
        page.should_be_result_message()
