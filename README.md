# Simple Honeypot

## What is it?
A Python script that listens on a port and logs any connection attempts, helping you detect scanning or attack activity on your system.

## Why use it?
Honeypots help you catch and analyze unauthorized access attempts, giving you insight into possible threats and attack patterns.

## Features
- Listens on a specified TCP port
- Logs IP and port of every connection to `honeypot.log`
- Optionally sends a fake SSH banner

## Installation
No external requirements — works with Python 3 standard library.

## Usage
1. Change `PORT` in `honeypot.py` if needed.
2. Run the script:
    ```bash
    python honeypot.py
    ```
3. Check `honeypot.log` for connection attempts.

## License

MIT License
