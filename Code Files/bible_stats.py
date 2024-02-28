'''
SUGGESTED RUNNING ORDER
1) Have Needed Data in the "init_data" Folder (esv_books.csv, esv_chapters.csv, esv_verses.csv, and kjv_raw_txt): Look at "esv.py" and "kjv.py" respectively to find appropriate free downloadable URLs.
2) Run "esv.py" & "kjv.py" (Making Sure the Defaults in "bible_stats.py" {this file} are as you want it)
3) Run "sections.py" for both the newly created "ESV Books.csv" and "KJV Books.csv" (from step 2)
4) Run "to_html.py" to Copy/Paste into the HTML for the Webpages
5) Optionally Lookat/Run "analysis.ipynb", "custom_time.ipynb", and "diff.ipynb"
'''

class BibleStats():
    DEEPER_INFO = True
    MIN_WPM = 150
    MAX_WPM = 251
    INCREMENT = 50
    R_SPEEDS = range(MIN_WPM, MAX_WPM, INCREMENT)
    def wpm(word_count: int, speed):
        time = word_count / speed
        hrs, mins, secs = int(time // 60), int(time % 60), int(float(time * 60) % 60)
        return f'{hrs}hr {mins}m' if hrs > 0 else f'{mins}m {secs}s'
    