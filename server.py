import socket

s = socket.socket()
s.connect(('localhost', 8002))

while True:
    data = s.recv(1024).decode()

    if data == "END":
        print("\nAll frames received successfully!")
        break

    print("Received frames:", data)
    s.send("Acknowledgement received".encode())

s.close()