from django.urls import resolve
from gargantua.views import home_page

class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page