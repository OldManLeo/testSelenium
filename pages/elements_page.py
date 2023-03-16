from pages.base_page import BasePage
from pages.locators import ElementsPageLocators


class ElementsPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ElementsPage, self).__init__(*args, **kwargs)

    def should_be_result_message(self):
        file_name = self.browser.find_element(*ElementsPageLocators.FILE_NAME).text
        file_name = file_name.strip('.doc').replace(' ', '')
        file_name = file_name[0].lower() + file_name[1:]
        right_message_text = f'You have selected :\n{file_name}'
        result_message = self.browser.find_element(*ElementsPageLocators.RESULT_MESSAGE).text
        assert right_message_text == result_message
