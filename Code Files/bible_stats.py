'''
SUGGESTED RUNNING ORDER
1) general.ipynb -> Converts the Raw General Bible Books & Sections to the Official Ones
2) esv.py -> Converts Files From ESV Source to More Proper Format  (Source -> https://versenotes.org/a-list-of-books-in-the-bible-by-number-of-chapters/)
3) esv_view.ipynb (Dependent on #2) -> Views These More Properly Formatted ESV Files
4) esv_section.ipynb (Also Dependent on #2) -> From the Properly Formatted ESV Files Generates the Raw & Non-raw ESV Section CSVs
5) esv_custom.ipynb (Dependent on #2 & #4) -> Shows Expected Reading Time Based on a Custom WPM Reading Speed
6) diff.ipynb (Dependent on #1, #2, and #4) -> Compares My General File Data to the ESV Version Data
* #1, #2, #4, and #5: Are All Depend on "bible_stats.py" (This File) which include 'My Custom Class for the WPM Function & Constants'
This is just my suggested order. As long as dependents scripts are run first all should be fine. 
    So #1 & #2 Could Swap Order, #3 & #4 Could Also Swap, So Also #5 & #6
'''

class BibleStats():
    MIN_WPM = 150
    MAX_WPM = 251
    INCREMENT = 50
    def wpm(word_count: int, speed):
        time = word_count / speed
        hrs, mins, secs = int(time // 60), int(time % 60), int(float(time * 60) % 60)
        return f'{hrs}hr {mins}m' if hrs > 0 else f'{mins}m {secs}s'
    