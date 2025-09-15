from smish.core import AutoRouter

if __name__ == "__main__":
    # Create a node called "alpha"
    node = AutoRouter(node_id="alpha")

    # Example: broadcast a test message
    node.broadcast({"msg": "hello future mesh"})

    # Uncomment this line to keep listening for peers
    # node.listen()
