import re

file = open('site_list_2019.html', 'r')
html_text = file.read()
pattern = re.compile(r'[\w]+\.[\w]*')
websites = pattern.findall(html_text)
for item in websites:
    print(item)