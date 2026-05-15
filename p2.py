import socket
import json

def start_peer2():
    host='127.0.0.1'
    port=5002  # P2's address
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Peer 2 (The Bridge) is listening on port {port}")

    # receive the message from P1
    conn,addr=s.accept()
    data= conn.recv(1024).decode('utf-8')
    if data:
        msg = json.loads(data)
        print(f"\n[Peer 2] got a message from {msg['src']} which is  for {msg['dest']}.")

        # is it needs to be forwarded?
        if msg['dest'] =='5003':
            print(f"[Peer 2] This isn't for p2. Forwarding to P3 ")
            
            #create a new socket act as a client for p3
            forward_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            forward_socket.connect(('127.0.0.1', 5003))
            forward_socket.sendall(data.encode('utf-8'))
            forward_socket.close()
            print("[Peer 2] Forwarded.")
    conn.close()

if __name__ == "__main__":
    start_peer2()