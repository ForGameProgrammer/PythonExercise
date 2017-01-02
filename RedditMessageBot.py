import praw
import datetime
import time
import re

reddit = praw.Reddit('bot1') #praw.ini [bot1]
inbox = reddit.inbox

#Regex Search Term : Response
responses = {"Hello" : "Hello There! I am a bot written by ForGame (/u/for123game @ reddit)",
             "How are you":"Thank you for asking but I dont feel. :( . I am a bot written by ForGame (/u/for123game @ reddit)",
             "1+1" : "2"}

while 1:
    for message in inbox.unread():
        print("You have new message! ", datetime.datetime.now())
        print("Subject : ", message.subject)
        print("Message : ", message.body)
        for key,value in responses.items():
            if re.search(key, message.body, re.IGNORECASE):
                print("### Found", key, "in Message Repling With Hello Message ###")
                message.reply(value)
        print("----------------------------------\n")
        message.mark_read()

    time.sleep(3)


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