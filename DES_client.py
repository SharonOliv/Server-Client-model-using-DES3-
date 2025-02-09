import socket
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Key(24 bytes)
key = DES3.adjust_key_parity(b'!@#$%^&*TOP SECRET KEY98')

def des3_encrypt(plaintext):
    iv = get_random_bytes(8)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), DES3.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv.hex() + ciphertext.hex()

def des3_decrypt(ciphertext_hex):
    iv = bytes.fromhex(ciphertext_hex[:16])
    ciphertext = bytes.fromhex(ciphertext_hex[16:])
    decipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_padded_text = decipher.decrypt(ciphertext)
    return unpad(decrypted_padded_text, DES3.block_size).decode()

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_ip = '192.168.0.141'  #server's IP address
        server_port = 21312
        client_socket.connect((server_ip, server_port))
        print(f"Connected to the server at {server_ip}:{server_port}")

        while True:
            client_message = input("CLIENT (plaintext): ")
            encrypted_message = des3_encrypt(client_message)
            print(f"CLIENT SENDING (plaintext): {client_message}")
            print(f"CLIENT SENDING (encrypted, HEX): {encrypted_message}")
            client_socket.send(encrypted_message.encode())

            if client_message.lower() == "bye":
                print("Closing connection...")
                break

            encrypted_response = client_socket.recv(1024).decode()
            print(f"SERVER SENT (encrypted, HEX): {encrypted_response}")
            decrypted_response = des3_decrypt(encrypted_response)
            print(f"SERVER SENT (decrypted): {decrypted_response}")
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
