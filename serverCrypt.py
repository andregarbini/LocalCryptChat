from socket import socket, AF_INET, SOCK_STREAM
from Crypto.Cipher import AES
key = "OIESSAEHASENHAOK"
nkey = len(key)
aes = AES.new(key, AES.MODE_ECB)

server = '127.0.0.1'
port = int(input('Server port: '))

c = socket(AF_INET, SOCK_STREAM)
c.bind((server, port))
c.listen(2)
print("Waiting users...")
while True:
    conn, cli = c.accept()
    print("Connected with: ", cli)
    while True:
        r = conn.recv(1024)
        print("received: ", aes.decrypt(r).decode().replace('&',''))
        m = bytes(input("send a message: "), 'utf-8')
        while len(m) % nkey > 0:
            m += b"&"
        m_crypt = aes.encrypt(m)
        conn.send(m_crypt)
    conn.close()