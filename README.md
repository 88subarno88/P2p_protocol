# P2P Protocol — Message Forwarding via Bridge Peer

A simple peer-to-peer (P2P) socket communication project in Python that demonstrates **direct and indirect message passing** between peers. 
Peer 1 sends a message to Peer 3, but since they aren't directly connected, the message is routed through Peer 2 — the bridge.

---

## How It Works

```
Peer 1 (p1.py)  ──►  Peer 2 / Bridge (p2.py)  ──►  Peer 3 (p3.py)
   :5001                     :5002                        :5003
```

- **Peer 1** composes a message intended for Peer 3 and sends it to Peer 2.
- **Peer 2** acts as a bridge — it receives the message, sees it's not meant for itself, and forwards it to Peer 3.
- **Peer 3** listens on its port and prints the received message.

---

## Project Structure

```
p2p_protocol/
├── p1.py        # Sender — initiates the message
├── p2.py        # Bridge — forwards messages it doesn't own
└── p3.py        # Receiver — listens and displays incoming messages
```

---

## Getting Started

### Prerequisites

- Python 3.x
- No external libraries required (uses built-in `socket` module)

### Running the Project

You need **three separate terminals**, all in the `p2p_protocol/` directory.

> **Important:** Start the peers in reverse order (receiver first, bridge second, sender last) so that listeners are ready before any messages are sent.

---

**Terminal 1 — Start Peer 3 (Receiver)**
```bash
python p3.py
```
Expected output:
```
P3 is listening on port 5003
--- MESSAGE ---
From: Peer 5001
Message: msg is sending to p3 through p2.
```

---

**Terminal 2 — Start Peer 2 (Bridge)**
```bash
python p2.py
```
Expected output:
```
Peer 2 (The Bridge) is listening on port 5002
[Peer 2] got a message from 5001 which is for 5003.
[Peer 2] This isn't for p2. Forwarding to P3
[Peer 2] Forwarded.
```

---

**Terminal 3 — Run Peer 1 (Sender)**
```bash
python p1.py
```
Expected output:
```
[Peer 1] Sending message to Peer 3 via Peer 2 (5002)
[Peer 1] Message sent.
```

---

## Port Reference

| Peer   | Script  | Port  | Role          |
|--------|---------|-------|---------------|
| Peer 1 | p1.py   | 5001  | Sender        |
| Peer 2 | p2.py   | 5002  | Bridge / Relay|
| Peer 3 | p3.py   | 5003  | Receiver      |

---


---

## Notes
- All peers run on `localhost` (`127.0.0.1`).
