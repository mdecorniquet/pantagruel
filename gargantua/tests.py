from django.urls import resolve
from django.http import HttpRequest

from gargantua.views import home_page


class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page
    

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        assert response.content.startswith(b'<html>')
        assert b'<title>Pantagruel</title>' in response.content
        assert response.content.endswith(b'</html>')