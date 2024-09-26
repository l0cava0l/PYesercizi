import socket

# Dati del server
server_address = ("", 6980)  # Accetta qualsiasi indirizzo IP sulla porta 6980
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creazione socket UDP del server
udp_server_socket.bind(server_address)  # Associazione socket a indirizzo IP e porta
print("Server UDP in ascolto...")

# Imposta un contatore per ricevere 10 messaggi
message_count = 0
MAX_MESSAGES = 10

# Ciclo per ricevere 10 messaggi
while message_count < MAX_MESSAGES:
    # Ricezione del messaggio dal client
    data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)
    print(f"Messaggio {message_count + 1} ricevuto: {data.decode()} da {client_address}")
    
    # Invia risposta al client
    response = "ricevuto"
    udp_server_socket.sendto(response.encode(), client_address)
    
    # Incrementa il contatore dei messaggi ricevuti
    message_count += 1

# Chiusura del socket del server dopo aver ricevuto 10 messaggi
print("Server ha ricevuto 10 messaggi. Chiusura del server.")
udp_server_socket.close()
