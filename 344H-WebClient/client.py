import sys
import socket


def get(url):
    scheme, _, host, path = url.split('/', 3)

    if scheme != "http:":
        raise Exception(f'Unsupported scheme "{scheme}" used.')

    path = ''.join(['/', path])
    try:
        host, port = host.split(':')
    except ValueError:
        port = 80

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((host, port))

    crlf = "\r\n"
    s = f"GET {path} HTTP/1.1{crlf}Host: {host}{crlf}{crlf}"
    sock.sendall(s.encode('utf-8'))

    data = []
    while True:
        tmp = sock.recv(512)
        if not tmp:
            sock.close()
            break

        data.append(tmp.decode('utf-8'))

    return ''.join(data)


print(get("http://httpbin.org/get"))
