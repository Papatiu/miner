#!/usr/bin/env python3
import socket
import subprocess

print("=== Klavye ayarı: Turkish Q ===")
subprocess.run(["setxkbmap", "-layout", "tr", "-variant", "q"])

print("=== Pool Port Kontrolü Başladı ===")

POOLS = [
    ("gntl.co.uk", 3333),
    ("hashvault.pro", 3333),
    ("herominers.com", 4444),
    ("monerohash.com", 3333),
    ("nanopool.org", 14444),
    ("pool.xmr.pt", 3333),
    ("supportxmr.com", 5555),
    ("xmrfast.com", 3333),
    ("xmrpool.eu", 9999),
]

for host, port in POOLS:
    print(f"⏳ {host}:{port} -> ", end="")
    try:
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        print("✅ Bağlantı başarılı")
    except Exception:
        print("❌ Bağlantı başarısız")

print("=== İşlem Tamamlandı ===")
EOF
