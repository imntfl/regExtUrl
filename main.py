import re

r = re.findall(r'\b[li]\w+.\w+', 'http://server.com/downloads/life_changing_plans.pdf')
r2 = re.findall(r'\b[li]\w+.\w+', 'http://server.com/downl/life_changing_plans.doc')
r3 = re.findall(r'\b[r]\w+.\w+', 'https://server-dot.com/root.pdf')

print(r)
print(r2) 
print(r3)
