import socket
if __name__ == '__main__':
    hostname = 'hust.edu.vn'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))
