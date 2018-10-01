from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from gargantua.views import home_page
# from gargantua.views import uploadcsv


class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page
    

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        assert response.content.decode() == expected_html

    def test_home_page_uploaded_file_is_csv(self):
        request = HttpRequest()
        request.method = 'POST'
        request.FILES

