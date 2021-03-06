import socket
from TwitchBot.config import config


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = config["username"]
password = config["password"]  # http://twitchapps.com/tmi/
channel = config["channel"]

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
    print("Message : \"", msg, "\"Sent")



while True:
    msg = input("What To Send To Tobito?")
    send_message(msg)


