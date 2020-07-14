#!/usr/bin/env python3
import socket


def scan_port_range(host: str, port_start: int, port_end: int) -> []:
    ip = socket.gethostbyname(host)
    ports = []
    for i in range(port_start, port_end):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, i))
        if result == 0:
            ports.append(i)
        s.close()
    return ports


if __name__ == "__main__":
    host: str = str(input("Hostname to scan: "))
    port_start: int = int(input("Port range start: "))
    port_end: int = int(input("Port range end: "))
    print("Ports open: {}".format(scan_port_range(host, port_start, port_end)))
