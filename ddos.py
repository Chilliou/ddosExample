import threading
import socket
import time

def send_socket(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    try:
        sock.connect(server_address)
    except Exception as e:
        print(f"Erreur de connexion : {e}")
        return

    while True:
        try:
            message = b'This is the message. It will be repeated.'
            sock.sendall(message)
            data = sock.recv(1024)
            print(repr(data))
            #time.sleep(1)  # Ajout d'un délai
        except Exception as e:
            print(f"Erreur durant l'envoi ou la réception : {e}")
            sock.close()
            break

server_address = ('176.181.225.177', 5173)

for i in range(4096):
    t = threading.Thread(target=send_socket, args=(server_address,))
    t.start()
