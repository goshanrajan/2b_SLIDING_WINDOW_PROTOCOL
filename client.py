import socket

s = socket.socket()
s.bind(('localhost', 8002))
s.listen(1)

print("Waiting for server...")
c, addr = s.accept()

n = int(input("Enter number of frames: "))
w = int(input("Enter window size: "))

frames = list(range(1, n + 1))

for i in range(0, n, w):
    window = frames[i:i+w]

    print("\nSending frames:", window)
    c.send(str(window).encode())

    ack = c.recv(1024).decode()
    print(ack)

c.send("END".encode())

c.close()
s.close()