import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

pattern = re.compile(r'(.+:) ([A-Za-z]* [0-9]{2}, [0-9]{4})')
res = pattern.findall(text)
print(res)
number = 1
list_no = 0

for item in res:
    print(number)
    print(res[list_no][0])
    print(res[list_no][1])
    print("")
    number += 1
    list_no += 1