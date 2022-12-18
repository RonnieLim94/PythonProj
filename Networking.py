
import socket

if __name__ == '__main__':
    network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    network.connect(("jbtalks.cc", 80))
    cmd = "GET https://www.jbtalks.cc/forum.php HTTP/1.0\n\n".encode()
    network.send(cmd)

    while True:
        data = network.recv(4096)
        if (len(data) < 1):
            break
        print(data.decode(encoding="ISO-8859-1"))
    network.close()

