import socket
import hmac
import hashlib
import os

key = b'secret_key'  # Secret key used for HMAC

# Create socket and connect to server
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

# Send message to server with nonce
message = b'sabarish'
nonce = os.urandom(16)  # Generate random nonce
data = message + nonce
h = hmac.new(key, data, hashlib.sha256)  # Create HMAC object using SHA256 hash algorithm
mac = h.digest()  # Generate MAC for message and nonce
s.sendall(data + mac)  # Send message, nonce, and MAC to server

# Receive response from server with nonce
data = s.recv(1024)
s.close()

# Verify response, nonce, and MAC
response = data[:-32]  # Extract response from received data
nonce = data[-48:-32]  # Extract nonce from received data
mac = data[-32:]  # Extract MAC from received data
data = response + nonce
h = hmac.new(key, data, hashlib.sha256)  # Create HMAC object using SHA256 hash algorithm
if hmac.compare_digest(mac, h.digest()):  # Compare generated MAC with received MAC
    print('Response:', response)
    print('Nonce:', nonce)
else:
    print('Invalid MAC')
