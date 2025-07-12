import socket
from datetime import datetime

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222       # Change to any unused port

def log_attempt(addr):
    with open("honeypot.log", "a") as f:
        log_entry = f"{datetime.now()} - Connection from {addr[0]}:{addr[1]}\n"
        f.write(log_entry)
    print(f"Connection logged: {addr[0]}:{addr[1]}")

def main():
    print(f"[*] Honeypot listening on port {PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            log_attempt(addr)
            # Optionally, send a fake banner
            conn.sendall(b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n")
            conn.close()

if __name__ == "__main__":
    main()
