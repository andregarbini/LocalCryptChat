import sys

from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import AES

key = "OIESSAEHASENHAOK"
nkey = len(key)
aes = AES.new(key, AES.MODE_ECB)

server = input('Server ID: ')
port = int(input('Server port: '))

while True:
    c = socket(AF_INET, SOCK_STREAM)
    try:
        c.connect((server, port))
    except ConnectionRefusedError as e:
        print('\nThis server does not exist.\nEnding connection...')
        sys.exit()
    try:
        while True:
            m = bytes(input("send a message: "), 'utf-8')
            while len(m) % nkey > 0:     
                m += b"&"
            m_crypt = aes.encrypt(m)
            c.send(m_crypt)
            r = c.recv(1024)
            print("received: ", aes.decrypt(r).decode().replace('&',''))
    except (ConnectionAbortedError, ConnectionResetError) as e:
        print('\nIt looks like the server is no longer working\nEnding connection...')
        sys.exit()
    c.close()