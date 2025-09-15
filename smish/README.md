# Smish

> The Single-Action Microgateway Framework for the Post-API Era

Smish is a **polyglot mesh framework** that eliminates the overhead of traditional APIs.  
Instead of endpoints, you get **signals**, **intents**, and **fibers**.

---

## ✨ Why Smish?
- **Single-action gateways** that compress intent into execution  
- **Polyglot-first core** (Python, Rust, Go, TypeScript, C++, JS)  
- **Canary-driven self-healing mesh** for resilience  
- Designed for **AI-native systems**, not human-centric APIs  
- Ready for enterprise compliance with governance baked in  

---

## 🚀 Quickstart (Python)
```python
from smish_core.auto_router import AutoRouter

router = AutoRouter(node_id="alpha")
router.broadcast({"msg": "hello future mesh"})
