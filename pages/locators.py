from selenium.webdriver.common.by import By


class BasePageLocators:
    ELEMENTS = (By.CSS_SELECTOR, 'div.card:nth-child(1)')


class ElementsPageLocators:
    CHECK_BOX = (By.ID, 'item-1')
    DIR_EXPAND = (By.CSS_SELECTOR, '.rct-collapse')
    SUBDIR_EXPAND = (By.CSS_SELECTOR, 'li.rct-node:nth-child(3) > span:nth-child(1) > button:nth-child(1)')
    FILE_IN_SUBDIR = (By.CSS_SELECTOR, 'li.rct-node-leaf:nth-child(1) > span:nth-child(1)')
    RESULT_MESSAGE = (By.ID, 'result')
    FILE_NAME = (By.CSS_SELECTOR,
                 'li.rct-node-leaf:nth-child(1) > span:nth-child(1) > label:nth-child(2) > span:nth-child(4)')
