from .base_page import BasePage
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):
    
    def should_be_empty(self):
       self. should_not_items()
       self.should_be_empty_text()
    
    def should_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
        "Items is presented, but should not be"
        
    def should_be_empty_text(self):
         assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Empty text is not presented"  


