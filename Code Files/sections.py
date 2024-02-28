# Fully Dependent on: 'CSV/{version} Books.csv' (i.e. "ESV Books.csv" or "KJV Books.csv")
import pandas as pd
from bible_stats import BibleStats

VERSION = 'KJV'

book = pd.read_csv(f'CSV/{VERSION} Books.csv').set_index('Book')
reading_times = [f'Time ({word_count} WPM)' for word_count in BibleStats.R_SPEEDS]
book.drop(reading_times, axis=1, inplace=True)
book.drop(['Vs/Ch', 'Wd/Ch', 'Wd/Vs'], axis=1, inplace=True)
bk = book.rename(columns={'Chapters': 'c', 'Verses': 'v', 'Words': 'w'})

sections = [
    {'S': 'Bible', 'B': 66, 'C': bk.sum()['c'], 'V': bk.sum()['v'], 'W': bk.sum()['w']},
    {'S': 'Old Testament', 'B': 39, 'C': bk.iloc[:39].sum()['c'], 'V': bk.iloc[:39].sum()['v'], 'W': bk.iloc[:39].sum()['w']},
    {'S': 'New Testament', 'B': 27, 'C': bk.iloc[39:].sum()['c'], 'V': bk.iloc[39:].sum()['v'], 'W': bk.iloc[39:].sum()['w']},
    {'S': 'Pentateuch', 'B': 5, 'C': bk.iloc[0:5].sum()['c'], 'V': bk.iloc[0:5].sum()['v'], 'W': bk.iloc[0:5].sum()['w']},
    {'S': 'History', 'B': 12, 'C': bk.iloc[5:17].sum()['c'], 'V': bk.iloc[5:17].sum()['v'], 'W': bk.iloc[5:17].sum()['w']},
    {'S': 'Poetry', 'B': 5, 'C': bk.iloc[17:22].sum()['c'], 'V': bk.iloc[17:22].sum()['v'], 'W': bk.iloc[17:22].sum()['w']},
    {'S': 'Major Prophets', 'B': 5, 'C': bk.iloc[22:27].sum()['c'], 'V': bk.iloc[22:27].sum()['v'], 'W': bk.iloc[22:27].sum()['w']},
    {'S': 'Minor Prophets', 'B': 12, 'C': bk.iloc[27:39].sum()['c'], 'V': bk.iloc[27:39].sum()['v'], 'W': bk.iloc[27:39].sum()['w']},
    {'S': 'Gospels', 'B': 4, 'C': bk.iloc[39:43].sum()['c'], 'V': bk.iloc[39:43].sum()['v'], 'W': bk.iloc[39:43].sum()['w']},
    {'S': 'History (Acts)', 'B': 1, 'C': bk.iloc[43:44].sum()['c'], 'V': bk.iloc[43:44].sum()['v'], 'W': bk.iloc[43:44].sum()['w']},
    {'S': 'Pauline Epistles', 'B': 13, 'C': bk.iloc[44:57].sum()['c'], 'V': bk.iloc[44:57].sum()['v'], 'W': bk.iloc[44:57].sum()['w']},
    {'S': 'General Epistles', 'B': 8, 'C': bk.iloc[57:65].sum()['c'], 'V': bk.iloc[57:65].sum()['v'], 'W': bk.iloc[57:65].sum()['w']},
    {'S': 'Apocalypse (Revelation)', 'B': 1, 'C': bk.iloc[65:].sum()['c'], 'V': bk.iloc[65:].sum()['v'], 'W': bk.iloc[65:].sum()['w']},
]

sections_df = pd.DataFrame(sections)
sections_df.rename(columns={'S': 'Section', 'B': 'Books', 'C': 'Chapters', 'V': 'Verses', 'W': 'Words'}, inplace=True)
sections_df.set_index('Section', inplace=True)

if BibleStats.DEEPER_INFO:
    sections_df['Ch/Book'] = round(sections_df['Chapters'] / sections_df['Books'], 1)
    sections_df['Vs/Book'] = round(sections_df['Verses'] / sections_df['Books'], 1)
    sections_df['Wd/Book'] = round(sections_df['Words'] / sections_df['Books']).astype('int')

    sections_df['Vs/Ch'] = round(sections_df['Verses'] / sections_df['Chapters'], 1)
    sections_df['Wd/Ch'] = round(sections_df['Words'] / sections_df['Chapters'], 1)
    sections_df['Wd/Vs'] = round(sections_df['Words'] / sections_df['Verses'], 1)

    for time in BibleStats.R_SPEEDS:
        sections_df[f'Time ({time} WPM)'] = sections_df['Words'].apply(lambda x: BibleStats.wpm(x, time))

sections_df.to_csv(f'CSV/{VERSION} Sections.csv')
print(f'Successfully Created "CSV/{VERSION} Sections.csv"')
