# DERIVED & Dependent on FILES...
# esv_verses.csv -> https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/
# esv_chapters.csv -> https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/
# esv_books.csv -> https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/

import pandas as pd
from bible_stats import BibleStats

verses = pd.read_csv('init_data/esv_verses.csv')
chapters = pd.read_csv('init_data/esv_chapters.csv')
books = pd.read_csv('init_data/esv_books.csv').drop('book_num', axis=1)

# ----------------------------------------------------------------------------------------------

verses.rename(columns={'word_count': 'Words'}, inplace=True)
verses['Reference'] = verses['book'].astype(str) + ' ' + verses['chapter'].astype(str) + ':' + verses['verse'].astype(str)
verses.set_index('Reference', inplace=True)
verses.drop(['book', 'chapter', 'verse'], axis=1, inplace=True)
verses.to_csv('CSV/ESV Verses.csv')
print('Successfully Created "CSV/ESV Verses.csv"')

# ----------------------------------------------------------------------------------------------

chapters.rename(columns={'book': 'Book', 'chapter': 'Chapter', 'num_verses': 'Verses', 'num_words': 'Words'}, inplace=True)
chapters['Reference'] = chapters['Book'].astype(str) + ' ' + chapters['Chapter'].astype(str)
chapters.set_index('Reference', inplace=True)
chapters.drop(['Book', 'Chapter'], axis=1, inplace=True)
if BibleStats.DEEPER_INFO:
    chapters['Wd/Vs'] = round(chapters['Words'] / chapters['Verses'], 1)
    for time in BibleStats.R_SPEEDS:
        chapters[f'Time ({time} WPM)'] = chapters['Words'].apply(lambda x: BibleStats.wpm(x, time))
chapters.to_csv('CSV/ESV Chapters.csv')
print('Successfully Created "CSV/ESV Chapters.csv"')

# ----------------------------------------------------------------------------------------------

books.rename(columns={'book': 'Book', 'num_chapters': 'Chapters', 'num_verses': 'Verses', 'num_words': 'Words'}, inplace=True)
books.set_index('Book', inplace=True)
if BibleStats.DEEPER_INFO:
    books['Vs/Ch'] = round(books['Verses'] / books['Chapters'], 1)
    books['Wd/Ch'] = round(books['Words'] / books['Chapters'], 1)
    books['Wd/Vs'] = round(books['Words'] / books['Verses'], 1)
    for time in BibleStats.R_SPEEDS:
        books[f'Time ({time} WPM)'] = books['Words'].apply(lambda x: BibleStats.wpm(x, time))
books.to_csv('CSV/ESV Books.csv')
print('Successfully Created "CSV/ESV Books.csv"')
