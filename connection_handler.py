def handle_client(client_socket, verbose):
    """Handle a client connection: echo received lines."""
    with client_socket:
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    # End connection
                    break
                if verbose:
                    print(f"Received: {data.decode(errors='ignore').rstrip()}")
                client_socket.sendall(data)
        except Exception as e:
            print(f"Connection error: {e}")