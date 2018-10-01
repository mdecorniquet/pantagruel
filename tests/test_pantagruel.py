import os
from selenium.webdriver.common.keys import Keys

TESTCSV_FILENAME = os.path.join(os.path.dirname(__file__), 'sample.csv')

class TestFunctionalWeb:
    def test_app_is_pantagruel(self, browser):
        assert os.path.isfile(TESTCSV_FILENAME)
        browser.get('http://localhost:8000')
        assert 'Pantagruel' in browser.title
        header_text = browser.find_element_by_tag_name('h1').text
        assert 'Import CSV' in header_text
        inputbox = browser.find_element_by_id('id_new_item')
        assert inputbox.get_attribute('name') == 'inputcsv'
        inputbox.send_keys(r'C:\Users\mdecorniquet\Documents\perso\pantagruel\tests\sample.csv')
        body = browser.find_elements_by_tag_name('body')
        assert 'Import OK' in body
        # table = browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # assert any(row.text == 'HOST' for row in rows)