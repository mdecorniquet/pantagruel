class TestFunctionalWeb:
    def test_app_is_pantagruel(self, browser):
        browser.get('http://localhost:8000')
        assert 'Pantagruel' in browser.title
        header_text = browser.find_element_by_tag_name('h1').text
        assert 'Import CSV' in header_text
        inputbox = browser.find_element_by_id('id_new_item')
        assert inputbox.get_attribute('placeholder') == 'Select a file'