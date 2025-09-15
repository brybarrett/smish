import socket
import json

class AutoRouter:
    def __init__(self, node_id: str, port: int = 5000):
        self.node_id = node_id
        self.port = port

    def broadcast(self, payload: dict):
        """Send a JSON payload over UDP broadcast"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message = json.dumps({"node": self.node_id, "payload": payload})
        sock.sendto(message.encode(), ("255.255.255.255", self.port))
        print(f"[{self.node_id}] broadcasted: {payload}")

    def listen(self):
        """Listen for broadcast messages"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.port))
        print(f"[{self.node_id}] listening on port {self.port}...")
        while True:
            data, addr = sock.recvfrom(1024)
            msg = json.loads(data.decode())
            print(f"[{self.node_id}] received from {msg['node']}: {msg['payload']}")
