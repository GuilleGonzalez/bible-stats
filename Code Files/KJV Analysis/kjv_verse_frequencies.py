abbrev_dict = {
    'Ge': 'Genesis', 'Ex': 'Exodus', 'Le': 'Leviticus', 'Nu': 'Numbers', 'De': 'Deuteronomy',
    'Jos': 'Joshua', 'Jg': 'Judges', 'Ru': 'Ruth', '1Sa': '1 Samuel', '2Sa': '2 Samuel',
    '1Ki': '1 Kings', '2Ki': '2 Kings', '1Ch': '1 Chronicles', '2Ch': '2 Chronicles',
    'Ezr': 'Ezra', 'Ne': 'Nehemiah', 'Es': 'Esther', 'Job': 'Job', 'Ps': 'Psalms',
    'Pr': 'Proverbs', 'Ec': 'Ecclesiastes', 'Song': 'Song of Solomon', 'Isa': 'Isaiah',
    'Jer': 'Jeremiah', 'La': 'Lamentations', 'Eze': 'Ezekiel', 'Da': 'Daniel', 'Ho': 'Hosea',
    'Joe': 'Joel', 'Am': 'Amos', 'Ob': 'Obadiah', 'Jon': 'Jonah', 'Mic': 'Micah', 'Na': 'Nahum',
    'Hab': 'Habakkuk', 'Zep': 'Zephaniah', 'Hag': 'Haggai', 'Zec': 'Zechariah', 'Mal': 'Malachi',
    'Mt': 'Matthew', 'Mr': 'Mark', 'Lu': 'Luke', 'Joh': 'John', 'Ac': 'Acts', 'Ro': 'Romans',
    '1Co': '1 Corinthians', '2Co': '2 Corinthians', 'Ga': 'Galatians', 'Eph': 'Ephesians',
    'Php': 'Philippians', 'Col': 'Colossians', '1Th': '1 Thessalonians', '2Th': '2 Thessalonians',
    '1Ti': '1 Timothy', '2Ti': '2 Timothy', 'Tit': 'Titus', 'Phm': 'Philemon', 'Heb': 'Hebrews',
    'Jas': 'James', '1Pe': '1 Peter', '2Pe': '2 Peter', '1Jo': '1 John', '2Jo': '2 John',
    '3Jo': '3 John', 'Jude': 'Jude', 'Re': 'Revelation'
}

with open('../init_data/kjv_raw.txt') as src:
    lines = src.readlines()
    
verses = {}
for line in lines:
    ref = abbrev_dict.get(line.split()[0], line.split()[0]) + ' ' + line.split()[1]
    verse = ' '.join(line.split()[2:])
    if verse in verses:
        verses[verse].append(ref)
    else: verses[verse] = [ref]
    
filtered_verses = {k: v for k, v in verses.items() if len(v) > 1}
sorted_verses = dict(sorted(filtered_verses.items(), key=lambda item: len(item[1]), reverse=True))

with open('kjv_verse_frequencies.txt', 'w') as txt:
    for verse, refs in sorted_verses.items():
        txt.write(f'{", ".join(refs)} -> {verse}\n')

