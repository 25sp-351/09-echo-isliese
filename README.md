# Multithreaded TCP Echo Server

This project implements a multithreaded TCP echo server in Python.

The server:
- Echoes every line of input it receives back to the client.
- Supports multiple simultaneous client connections using threading.
- Handles connection closures gracefully without crashing.
- Supports command-line arguments for custom port selection and verbose mode.

---

## Project Structure
09-ECHO-ISLIESE/
├── server.py              # Main server file (accept connections and spawn threads)
├── connection_handler.py  # Handle individual client connections
├── utils.py                # Parse command-line arguments

---

## How to Run

#### 1. Start the server:
Run `server.py`

#### 2. Test echo: 
Open terminal and enter `telnet localhost 12345`

