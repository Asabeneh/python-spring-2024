import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',

]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)