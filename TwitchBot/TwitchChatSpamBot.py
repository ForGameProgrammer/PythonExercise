import socket
import time
from TwitchBot.config import config

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = config["username"]
password = config["password"]  # http://twitchapps.com/tmi/
channel = input("Which Channel To Spam? : ")

server = config["server"]
port = config["port"]

sock.connect((server, port))

sock.settimeout(None)
sock.send(('USER %s\r\n' % username).encode('utf-8'))
sock.send(('PASS %s\r\n' % password).encode('utf-8'))
sock.send(('NICK %s\r\n' % username).encode('utf-8'))

sock.send(('JOIN #%s\r\n' % channel).encode('utf-8'))


def send_message(msg):
    toSend = ('PRIVMSG #%s :%s\n' % (channel, msg)).encode('utf-8')
    sock.send(toSend)
    print("Message : \"", msg, "\" Sent")


count = int(input("How Many Different Massages to Send? : "))
msg = []

for i in range(count):
    msg.append(input("What Message To Spam?(%s) : " % i))
delay = int(input("How often Send? (Seconds) : "))

lastSend = 0
which = 0
sock.settimeout(None)

while True:
    if time.time() - lastSend >= delay:
        message = msg[which]
        send_message(message)
        which += 1
        if which >= count:
            which = 0
        lastSend = time.time()
