import socket
import json

def start_peer3():
    host='127.0.0.1'
    port=5003  # P3's address
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"P3 is listening on port {port}")

    conn,addr = s.accept()
    data =conn.recv(1024).decode('utf-8')
    
    if data:
        # Decode the JSON message
        msg = json.loads(data)
        print("\n---MESSAGE ---")
        print(f"From: Peer {msg['src']}")
        print(f"Message: {msg['data']}")
    conn.close()

if __name__ == "__main__":
    start_peer3()