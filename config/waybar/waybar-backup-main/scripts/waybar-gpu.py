#!/usr/bin/env python3
import json
import os

def get_intel_gpu_data():
    data = {"temp": 0, "freq": 0, "max_freq": 0}
    try:
        # Temperatura (poate varia folderul, de obicei e in coretemp sau i915)
        temp_path = "/sys/class/thermal/thermal_zone0/temp" 
        if os.path.exists(temp_path):
            with open(temp_path, "r") as f:
                data["temp"] = int(int(f.read().strip()) / 1000)

        # Frecventa curenta (MHz)
        freq_path = "/sys/class/drm/card0/gt_cur_freq_mhz"
        if os.path.exists(freq_path):
            with open(freq_path, "r") as f:
                data["freq"] = int(f.read().strip())

        # Frecventa maxima
        max_freq_path = "/sys/class/drm/card0/gt_max_freq_mhz"
        if os.path.exists(max_freq_path):
            with open(max_freq_path, "r") as f:
                data["max_freq"] = int(f.read().strip())
    except:
        pass
    return data

gpu = get_intel_gpu_data()
usage_pct = int((gpu["freq"] / gpu["max_freq"] * 100)) if gpu["max_freq"] > 0 else 0

# Culori in functie de temperatura
color = "#81c8be" # Verde/Cyan default
if gpu["temp"] > 60: color = "#e5c890" # Galben
if gpu["temp"] > 75: color = "#e78284" # Rosu

output = {
    "text": f"󰢮 <span foreground='{color}'>{gpu['temp']}°C</span>",
    "tooltip": f"Intel HD Graphics\nFrecvență: {gpu['freq']} / {gpu['max_freq']} MHz\nUtilizare: {usage_pct}%",
    "class": "gpu"
}

print(json.dumps(output))
