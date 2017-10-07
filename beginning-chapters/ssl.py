import argparse, socket, ssl, sys, textwrap
import ctypes
hostname = "www.google.com.vn"

context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations("/etc/ssl/certs/ca-certificates.crt")
sock = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=hostname)
sock.connect((hostname,443))

cert = sock.getpeercert()

print(cert)