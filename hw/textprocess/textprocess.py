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

new_names = []
# arrange order
for char in names:
    # print(char.split(' '))
    name = char.split(' ')
    if name[0][-1] == ',':
        name[0] = name[0][:len(name[0]) - 1]

        name[0], name[1] = name[1], name[0]
        new_names.append(' '.join(name))
    else:
        new_names.append(char)

# print(new_names)

# 4 dr/dev
#
res = []
for char in names:
    name = char.split(' ')
    if name[0] == 'Dr.' or name[0] == 'Rev.':
        res.append(True)
    else:
        res.append(False)

# print(res)

# dr_rev = re.findall(r'(?:Dr|Rev)\.\s\w+\s\w+', text)
# print(dr_rev)


# 5  extract names
# mid_name_and_last_name = re.findall(
#     '/\w+([[:space:]])\w+([[:space:]])\w+$/gm', text)
# print(mid_name_and_last_name)

# 6 html <title>+++BREAKING NEWS+++<title>
'''
<.+> this will fail because . means any characters so it takes space and + etc
so it will print whole string. correct regex is <\w+>  \w means character from a-z, 0 - 9 and under score. so this regex 
will extract first html tag.
'''
html_str = '<title>+++BREAKING NEWS+++<title>'
html = re.findall('<\w+>', html_str)
# print(html)

# equation
equation_str = '(5-3)^2=5^2-2*5*3+3^2'
res = re.findall(r'^\([0-9-^=*+)]+', equation_str)
print(res)
