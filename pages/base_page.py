class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def click_on(self, find_method, element):
        element_to_click = self.browser.find_element(find_method, element)
        element_to_click.click()
