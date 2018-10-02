from boddle import boddle


class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page
        with boddle(path='/'):
            assert home_page
    

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        assert response.content.decode() == expected_html

    def test_home_page_uploaded_file_is_csv(self):
        request = HttpRequest()
        request.method = 'POST'
        request.FILES

