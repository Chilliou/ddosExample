import threading
import socket

def send_socket(server_address):
    # Création d'un socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    sock.connect(server_address)

    while True:
        try:
            # Envoi de données au serveur
            message = b'This is the message.  It will be repeated.'
            sock.sendall(message)

            # Réception de la réponse du serveur
            data = sock.recv(1024)
        except:
            # Fermeture du socket en cas d'erreur
            sock.close()
            break

        print(repr(data))

# Création de plusieurs threads pour envoyer des sockets simultanément
server_address = ('IP_ADDRESS', PORT)
for i in range(5):
    t = threading.Thread(target=send_socket, args=(server_address,))
    t.start()