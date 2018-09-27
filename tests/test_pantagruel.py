class TestWeb:
    def test_app_is_pantagruel(self, browser):
        browser.get('http://localhost:8000')
        assert 'Pantagruel' in browser.title