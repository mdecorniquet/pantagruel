from selenium import webdriver

# def test_django():
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title