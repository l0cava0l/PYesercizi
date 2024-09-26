import socket

# Dati del server
server_address = ("", 6980)  # Accetta qualsiasi indirizzo IP sulla porta 6980
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati

# Creazione socket UDP del server
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associazione del socket all'indirizzo IP e porta specificati
udp_server_socket.bind(server_address)

print("Server UDP in ascolto...")

while True:
    # Server riceve il messaggio dal client
    data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
    message = data.decode()  # Decodifica del messaggio

    # Stampa il messaggio ricevuto
    print(f"Messaggio ricevuto: {message} da {client_address}")

    # Se il messaggio è "exit", chiudi la connessione
    if message.lower() == "exit":
        print("Chiusura del server...")
        udp_server_socket.close()
        break

    # Invio di una risposta al client
    response = input("Rispondi al client: ")
    udp_server_socket.sendto(response.encode(), client_address)
