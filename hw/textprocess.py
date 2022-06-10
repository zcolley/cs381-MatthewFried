import re
text = '''
"555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
'''
# extract numbers
numbers = re.findall(r'\d+', text)
# print(numbers)

# extract names
names = re.findall('[A-Za-z.,]+(?: [A-Za-z.,]+)*', text)
# print(names)
# arrange order
re_arrange = re.findall(
    "/^[A-Z][a-z]{0,19}[\s,][A-Z][a-z]{0,19}$/", text)
# print(re_arrange)

# 4 dr/dev
dr = re.findall(r'(Dr\.\s\w+\s\w+)', text)
rev = re.findall(r'(Rev\.\s\w+\s\w+)', text)
dr_rev = dr + rev
# print(dr_rev)

# 5  extract names
# mid_name_and_last_name = re.findall(
#     '/\w+([[:space:]])\w+([[:space:]])\w+$/gm', text)
# print(mid_name_and_last_name)

# 6 html <title>+++BREAKING NEWS+++<title>
html_str = '<title>+++BREAKING NEWS+++<title>'
html = re.findall('^<$>', html_str)
# print(html)

# equation
equation_str = '(5-3)^2=5^2-2*5*3+3^2'
str_equation = re.findall(
    '((-?(?:\d+(?:\.\d+)?))|([-+\/*()])|(-?\.\d+))', equation_str)
print(str_equation)
