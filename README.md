# 2b IMPLEMENTATION OF SLIDING WINDOW PROTOCOL
## AIM
## ALGORITHM:
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
DEVELOPED BY T.GOSHANRAJAN(212225040098)
## CLIENT
```
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
```
## SERVER
```
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
```

## OUPUT

<img width="1328" height="372" alt="Screenshot 2026-11-02 090242" src="https://github.com/user-attachments/assets/35612955-a5e1-4658-af81-6c73c8778193" />
<img width="1325" height="222" alt="Screenshot 2026-11-02 090327" src="https://github.com/user-attachments/assets/dbd75add-ddb7-422d-b694-b3c51326efb2" />

## RESULT
Thus, python program to perform stop and wait protocol was successfully executed
