import socket
import argparse

# Start the TCP echo server
def start_echo_server(host='0.0.0.0', port=12345, verbose=False):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        with client_socket:
            try:
                # Keep communicating with the client until it disconnects
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break  # Client closed the connection
                    if verbose:
                        print(f"Received: {data.decode().rstrip()}")
                    # Echo the received data back to the client
                    client_socket.sendall(data)
            except Exception as e:
                print(f"Error: {e}")
        print(f"Connection with {client_address} closed.")

# Parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple TCP Echo Server")
    parser.add_argument('-p', '--port', type=int, default=12345, help='Port to listen on (default 12345)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    start_echo_server(port=args.port, verbose=args.verbose)
