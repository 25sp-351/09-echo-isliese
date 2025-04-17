import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Multithreaded TCP Echo Server")
    parser.add_argument('-p', '--port', type=int, default=12345, help='Port to listen on (default: 12345)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print received messages')
    return parser.parse_args()