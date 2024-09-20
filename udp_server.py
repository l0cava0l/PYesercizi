import socket

# Dati del server
server_address = ("", 6980)  # Accetta qualsiasi indirizzo IP sulla porta 6980
BUFFER_SIZE = 4096  # Dimensione massima del buffer per la ricezione dei dati
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# creo socket UDP del server
udp_server_socket.bind(server_address)# Associazione socket a indirizzo IP e porta
print("ti ascpecto")


data, client_address = udp_server_socket.recvfrom(BUFFER_SIZE)# server riceve messaggio
print(f"Messaggio ricevuto: {data.decode()} da {client_address}")#ricevo dato dal cliente


response = "ricevuto"#risposta
udp_server_socket.sendto(response.encode(), client_address)#mando riposta

udp_server_socket.close()#chiusura socket
