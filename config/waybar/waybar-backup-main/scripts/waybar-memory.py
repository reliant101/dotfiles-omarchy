#!/usr/bin/env python3
import json
import psutil

def main():
    mem = psutil.virtual_memory()
    pct = mem.percent
    used = mem.used / (1024**3)
    total = mem.total / (1024**3)

    lines = [
        "<span foreground='#a6d189'> Memory Info</span>",
        "─" * 30,
        f"Used:  {used:.2f} GB",
        f"Total: {total:.2f} GB",
        f"Usage: {pct}%"
    ]

    print(json.dumps({
        "text": f" <span foreground='#a6d189'>{pct}%</span>",
        "tooltip": "\n".join(lines),
        "markup": "pango",
        "class": "memory"
    }))

if __name__ == "__main__":
    main()
