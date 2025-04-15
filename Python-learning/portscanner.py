import socket
from datetime import datetime


# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection
        sock.settimeout(1)
        # Try to connect to the target and port
        result = sock.connect_ex((target, port))
        # If the connection was successful, the port is open
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


# Main function for scanning multiple ports
def port_scanner(target, start_port, end_port):
    print(f"Starting scan on {target}")
    print(f"Scanning ports {start_port} to {end_port}")
    start_time = datetime.now()

    # Loop over the range of ports
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scan completed in: {total_time}")


# Example usage
if __name__ == "__main__":
    target = input("Enter the target (IP or hostname): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_scanner(target, start_port, end_port)
