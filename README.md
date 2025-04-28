# Server-Client Model using Triple DES (DES3)
This repository contains the implementation of **Triple DES (DES3)** encryption and decryption in a **client-server model**, enabling secure **dual communication** between the server and client.

## Overview

This repo demonstrates:
- Secure communication between a client and server using **Triple DES (3DES)** encryption.
- Encryption of outgoing messages and decryption of incoming messages on both sides.
- Practical usage of symmetric encryption algorithms in a networked environment.

**Triple DES (DES3)** enhances the security of standard DES by applying the encryption three times to each data block.

## Features

- Encrypt outgoing messages using Triple DES (DES3).
- Decrypt incoming messages using Triple DES (DES3).
- Full two-way (dual) encrypted communication between server and client.
- Secure and reliable message transfer using TCP sockets.

## Technologies Used

- Python 3
- `pycryptodome` library (`Crypto.Cipher.DES3`)
- Socket programming (TCP sockets)

## How to Run

1. Install dependencies:
   ```bash
   pip install pycryptodome
   ```

2. Start the server:
   ```bash
   python DES_server.py
   ```

3. In a new terminal, start the client:
   ```bash
   python DES_client.py
   ```

4. Start sending and receiving encrypted messages securely!

## Notes

- Triple DES, while more secure than DES, is considered slower and less secure than modern standards like AES.
- This repo is meant for educational purposes to demonstrate how Triple DES encryption can be used in real-world communication scenarios.
