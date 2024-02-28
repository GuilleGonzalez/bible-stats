# Fully Dependent on: 'CSV/{version} Books.csv' and 'CSV/{version} Sections.csv' (i.e. "KJV Books.csv" and "KJV Sections.csv")
import pandas as pd
from bible_stats import BibleStats

VERSION = 'KJV'

sections = pd.read_csv(f'CSV/{VERSION} Sections.CSV').set_index('Section').to_dict(orient='index')
books = pd.read_csv(f'CSV/{VERSION} Books.CSV').set_index('Book').to_dict(orient='index')
print()

for section, data in sections.items():
    print(f'{section}: ({data['Books']} Books | {data['Chapters']:,} Chapters | {data['Verses']:,} Verses | {data['Words']:,} Words)')
print()
for book, data in books.items():
    print(f'{book} ({data['Chapters']} Chapters | {data['Verses']:,} Verses | {data['Words']:,} Words)')

for key, value in sections.items():
    sections[key] = list(value.values())
sections_list = sections.keys()

# -------------------------------------------------------------------------------------

def print_section(section: str):
    print(f'\n<h3>{section}:</h3>')
    print(f'<p class="sub-p">({sections[section][0]} Books | {sections[section][1]:,} Chapters | {sections[section][2]:,} Verses | <nobr>{sections[section][3]:,} Words)</nobr></p>\n')

print('\n\n\n<h1>Bible Statistics</h1>\n<hr>')
s = sections['Bible']
print(f'<p class="mid-p">{s[0]} Books | {s[1]:,} Chapters | {s[2]:,} Verses | <nobr>{s[3]:,} Words</nobr></p>\n<br>\n')

s = sections['Old Testament']
print('<h2>Old Testament:</h2>')
print(f'<p class="sub-p">({s[0]} Books | {s[1]:,} Chapters | {s[2]:,} Verses | <nobr>{s[3]:,} Words)</nobr></p>')

print_section('Pentateuch')

i = 0
for book, data in books.items():
    if i == 5: print_section('History')
    elif i == 17: print_section('Poetry')
    elif i == 22: print_section('Major Prophets')
    elif i == 27: print_section('Minor Prophets')
    elif i == 39:
        s = sections['New Testament']
        print('<br>\n<h2>New Testament:</h2>')
        print(f'<p class="sub-p">({s[0]} Books | {s[1]:,} Chapters | {s[2]:,} Verses | <nobr>{s[3]:,} Words)</nobr></p>')
        print_section('Gospels')
    elif i == 43: print('\n<h3>History:</h3>')
    elif i == 44: print_section('Pauline Epistles')
    elif i == 57: print_section('General Epistles')
    elif i == 65: print('\n<h3>Apocrypha:</h3>')
        
    print(f'<p>{book}</p>')
    print(f'<p class="sub-p">({data['Chapters']} Chapters | {data['Verses']:,} Verses | {data['Words']:,} Words)</p>')
    i += 1
print('<br>\n<br>\n\n\n')

'''
for section, data in sections.items():
    print(f'<h3>{section}:</h3>')
    print(f'<p class="sub-p">({data['Books']} Books | {data['Chapters']:,} Chapters | {data['Verses']:,} Verses | <nobr>{data['Words']:,} Words)</nobr></p>')
    print()
'''
