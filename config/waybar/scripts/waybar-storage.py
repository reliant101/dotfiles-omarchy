#!/usr/bin/env python3
import json
import subprocess
import os
import psutil
import time

SSD_ICON = "󰋊"
TOOLTIP_WIDTH = 45

def get_color(value, metric_type):
    if value < 40: return "#a6d189" # Verde
    if value < 70: return "#e5c890" # Galben
    return "#e78284" # Rosu

def main():
    try:
        usage = psutil.disk_usage('/')
        used_pct = int(usage.percent)
        total_gb = usage.total / (1024**3)
        used_gb = usage.used / (1024**3)
        free_gb = usage.free / (1024**3)

        lines = []
        lines.append(f"<span foreground='#8caaee'>󰋊 Storage Dashboard</span>")
        lines.append("─" * TOOLTIP_WIDTH)
        lines.append(f"<b>Root (/)</b>")
        lines.append(f"Total: {total_gb:.1f} GB")
        lines.append(f"Used:  {used_gb:.1f} GB ({used_pct}%)")
        lines.append(f"Free:  {free_gb:.1f} GB")
        
        # Bară vizuală
        bar_w = 20
        filled = int((used_pct / 100) * bar_w)
        bar = f"<span foreground='{get_color(used_pct, '')}'>{'█'*filled}</span><span foreground='#414559'>{'░'*(bar_w-filled)}</span>"
        lines.append(f"\n{bar} {used_pct}%")

        output = {
            "text": f"{SSD_ICON} <span foreground='{get_color(used_pct,'')}'>{used_pct}%</span>",
            "tooltip": "\n".join(lines),
            "markup": "pango",
            "class": "storage"
        }
        print(json.dumps(output))
    except Exception as e:
        print(json.dumps({"text": "Err", "tooltip": str(e)}))

if __name__ == "__main__":
    main()
