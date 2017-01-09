import praw
import time
import winsound
import sqlite3

connection = sqlite3.connect("freegamesonsteam.db")
cursor = connection.cursor()

createTable = """CREATE TABLE IF NOT EXISTS Submissions
      (ID TEXT PRIMARY KEY NOT NULL,
       TITLE TEXT,
       CONTENT TEXT,
       URL TEXT);"""
insertToTable = "INSERT INTO Submissions VALUES (?,?,?,?)"
getFromTable = "SELECT * FROM Submissions WHERE (ID = ?)"

cursor.execute(createTable)

Freq = 5000 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second

reddit = praw.Reddit('bot1') #praw.ini [bot1]
subreddit = reddit.subreddit("FreeGamesOnSteam")


while True:
    for submission in subreddit.new(limit=10):
        searchValue = (submission.id,)
        cursor.execute(getFromTable, searchValue)
        if len(cursor.fetchall()):
            continue

        print("Title : ", submission.title)
        print("Content : ", submission.selftext)
        print("URL : ", submission.url)
        print("-------------------------------")
        #Values To Add, Execute
        insertValues = (submission.id, submission.title, submission.selftext, submission.url)
        cursor.execute(insertToTable, insertValues) #SQL Execute
        connection.commit() #Save
        winsound.Beep(Freq, Dur) #Beep :)
    time.sleep(10)

connection.close()

"""
dir(submission)
'_comments_by_id',
'_fetch',
'_fetched',
'_flair',
'_info_path',
'_mod',
'_reddit',
'_reset_attributes',
'_safely_add_arguments',
'_vote',
'approved_by',
'archived',
'author',
'author_flair_css_class',
'author_flair_text',
'banned_by',
'clear_vote',
'clicked',
'comment_limit',
'comment_sort',
'comments',
'contest_mode',
'created',
'created_utc',
'delete',
'distinguished',
'domain',
'downs',
'downvote',
'duplicates',
'edit',
'edited',
'flair',
'fullname',
'gild',
'gilded',
'hidden',
'hide',
'hide_score',
'id',
'id_from_url',
'is_self',
'likes',
'link_flair_css_class',
'link_flair_text',
'locked',
'media',
'media_embed',
'mod',
'mod_reports',
'name',
'num_comments',
'num_reports',
'over_18',
'parse',
'permalink',
'quarantine',
'removal_reason',
'reply',
'report',
'report_reasons',
'save',
'saved',
'score',
'secure_media',
'secure_media_embed',
'selftext',
'selftext_html',
'shortlink',
'spoiler',
'stickied',
'subreddit',
'subreddit_id',
'suggested_sort',
'thumbnail',
'title',
'unhide',
'unsave',
'ups',
'upvote',
'url',
'user_reports',
'visited'
"""
