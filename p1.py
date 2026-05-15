import socket
import json

def start_peer1():
    # p1 connecting to p2
    target_host = '127.0.0.1'
    target_port = 5002 

    # creating a data packet
    message = {
        "src": "5001",
        "dest": "5003",
        "data": "msg is sending to p3 through p2."
    }

    print(f"[Peer 1] Sending message to Peer 3 via Peer 2 ({target_port})")
    
    # Connect and send
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_host, target_port))
    s.sendall(json.dumps(message).encode('utf-8'))
    s.close()
    print("[Peer 1] Message sent.")

if __name__ == "__main__":
    start_peer1()