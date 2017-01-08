import socket
import re
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

def parse_message(data):

    return {
        'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data),
        'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data),
        'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)
    }



while True:
    data = sock.recv(1024)
    msg = parse_message(data.decode())
    if not msg["message"]:
        continue
    print(msg["username"][0], ":", msg["message"][0])

