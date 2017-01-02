import praw

reddit = praw.Reddit('bot1') #praw.ini [bot1]
subreddit = reddit.subreddit("learnpython") #reddit.com/r/learnpython
inbox = reddit.inbox

#Subreddit Track
for submission in subreddit.hot(limit=5): #Get Top 5
    print("Title : ", submission.title)
    print("Text : ", submission.selftext)
    print("Score : ", submission.score)
    print("---------------------------\n")

for message in inbox.all():
    print("Subject : ", message.subject)
    print("Message : ", message.body)
    #if message.body == "sup":
        #message.reply("Supp")
    print("----------------------------------\n")
# print(dir(submission))  # Get what it can do

"""
print(dir(inbox))
'all'
'comment_replies'
'mark_read'
'mark_unread'
'mentions'
'message'
'messages'
'parse'
'sent'
'submission_replies'
'unread'
"""

"""
print(dir(message))
'author',
'block',
'body',
'body_html',
'context',
'created',
'created_utc',
'dest',
'distinguished',
'first_message',
'first_message_name',
'fullname',
'id',
'mark_read',
'mark_unread',
'name',
'new',
'parent_id',
'parse',
'replies',
'reply',
'subject',
'subreddit',
'was_comment'
"""