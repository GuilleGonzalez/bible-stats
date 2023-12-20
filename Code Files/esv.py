# DERIVED & Dependent on FILES from https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/
from bible_stats import BibleStats # My Custom Class for the WPM Function & Constants
import pandas as pd

esv_books = pd.read_csv('ESV/esv_books.csv').drop('book_num', axis=1) # FILE FROM https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/
esv_chapters = pd.read_csv('ESV/esv_chapters.csv') # FILE FROM https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/
esv_verses = pd.read_csv('ESV/esv_verses.csv') # FILE FROM https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/

esv_books.rename(columns={'book': 'Book', 'num_chapters': 'Chapters', 'num_verses': 'Verses', 'num_words': 'Words'}, inplace=True)
esv_books.set_index('Book', inplace=True)
esv_books['Vs/Ch'] = round(esv_books['Verses'] / esv_books['Chapters'], 1)
esv_books['Wd/Ch'] = round(esv_books['Words'] / esv_books['Chapters'], 1)
esv_books['Wd/Vs'] = round(esv_books['Words'] / esv_books['Verses'], 1)
for time in range(BibleStats.MIN_WPM, BibleStats.MAX_WPM, BibleStats.INCREMENT):
    esv_books[f'Time ({time} WPM)'] = esv_books['Words'].apply(lambda x: BibleStats.wpm(x, time))
esv_books.to_csv('ESV/ESV Books.csv')

esv_chapters.rename(columns={'book': 'Book', 'chapter': 'Chapter', 'num_verses': 'Verses', 'num_words': 'Words'}, inplace=True)
esv_chapters['Reference'] = esv_chapters['Book'].astype(str) + ' ' + esv_chapters['Chapter'].astype(str)
esv_chapters.set_index('Reference', inplace=True)
esv_chapters.drop(['Book', 'Chapter'], axis=1, inplace=True)
esv_chapters['Wd/Vs'] = round(esv_chapters['Words'] / esv_chapters['Verses'], 1)
for time in range(BibleStats.MIN_WPM, BibleStats.MAX_WPM, BibleStats.INCREMENT):
    esv_chapters[f'Time ({time} WPM)'] = esv_chapters['Words'].apply(lambda x: BibleStats.wpm(x, time))
esv_chapters.to_csv('ESV/ESV Chapters.csv')

esv_verses.rename(columns={'word_count': 'Words'}, inplace=True)
esv_verses['Reference'] = esv_verses['book'].astype(str) + ' ' + esv_verses['chapter'].astype(str) + ':' + esv_verses['verse'].astype(str)
esv_verses.set_index('Reference', inplace=True)
esv_verses.drop(['book', 'chapter', 'verse'], axis=1, inplace=True)
esv_verses.to_csv('ESV/ESV Verses.csv')