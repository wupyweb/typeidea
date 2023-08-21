import socket

EOL1 = b"\n\n"
EOL2 = b"\n\r\n"

def handle_connection(conn, addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    conn.send(b"HTTP/1.1 200 OK\n\n")
    conn.send(b"Hello, world!\n")
    conn.close()


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(("127.0.0.1", 8080))
    serversocket.listen(5)
    print("Listening on port 8080")

    try:
        while True:
            conn, addr = serversocket.accept()
            ab = "12"
            import pdb; pdb.set_trace()
            handle_connection(conn, addr)
    finally:
        serversocket.close()


if __name__ == "__main__":
    main()