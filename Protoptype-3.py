import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.ensemble import IsolationForest
from plyer import notification  # Desktop notifications
from cryptography.fernet import Fernet  # Secure logging
from fpdf import FPDF  # PDF report generation
import os
import webbrowser  # To open the report
from datetime import datetime

# File Paths
KEY_FILE = "encryption_key.key"
LOG_FILE = "hacking_attempts.log"
REPORT_FILE = "hacking_report.pdf"
BLOCKED_FILE = "blocked_sources.log"

# Generate or Load Encryption Key
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

cipher_suite = Fernet(key)

# Simulate Brainwave Data
np.random.seed(42)
normal_brainwaves = np.random.normal(0, 1, 1000)  # 1000 normal data points
hacked_brainwaves = normal_brainwaves.copy()
hacked_brainwaves[500:520] += 6  # Mild Attack
hacked_brainwaves[750:760] += 8  # Severe Attack

# Create DataFrame
timestamps = pd.date_range(start=datetime.now(), periods=1000, freq="S")  # Simulated timestamps
df = pd.DataFrame({"Timestamp": timestamps, "Signal": hacked_brainwaves})

# AI-Based Anomaly Detection
X = df["Signal"].values.reshape(-1, 1)
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)
df["Anomaly"] = model.predict(X)

# Classify Attack Severity
df["Severity"] = "Normal"
df.loc[(df["Signal"] >= 5) & (df["Signal"] < 8) & (df["Anomaly"] == -1), "Severity"] = "Mild Attack"
df.loc[(df["Signal"] >= 8) & (df["Anomaly"] == -1), "Severity"] = "Severe Attack"

# Identify hacking attempts
anomalies = df[df["Anomaly"] == -1]

# Secure Logging & Blocking
if not anomalies.empty:
    log_entry = f"Hacking Detected at: {list(anomalies['Timestamp'])}\nSeverity: {anomalies['Severity'].value_counts().to_dict()}\n"
    encrypted_log = cipher_suite.encrypt(log_entry.encode())

    with open(LOG_FILE, "ab") as log_file:
        log_file.write(encrypted_log + b"\n")

    with open(BLOCKED_FILE, "a") as block_file:#blocking
        block_file.write(f"Blocked sources at: {list(anomalies['Timestamp'])}\n")

    # Generate Report
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Hacking Attempt Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Timestamps of Attacks: {list(anomalies['Timestamp'])}\n")
    pdf.multi_cell(0, 10, f"Severity Levels: {anomalies['Severity'].value_counts().to_dict()}\n")
    pdf.multi_cell(0, 10, f"Blocked sources recorded in '{BLOCKED_FILE}'.\n")
    pdf.multi_cell(0, 10, f"Encrypted logs saved in '{LOG_FILE}'.\n")
    pdf.output(REPORT_FILE)

    # Open Report
    webbrowser.open(REPORT_FILE)

    # Desktop Notification
    notification.notify(
        title="Hacking Detected!",
        message=f"{len(anomalies)} hacking attempts detected. Report saved.",
        app_name="Brainwave Security",
    )

# 🎥 **Animated Visualization**
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, len(df))
ax.set_ylim(min(df["Signal"]) - 1, max(df["Signal"]) + 1)
line, = ax.plot([], [], label="Brainwave Signal", color="blue")
scatter = ax.scatter([], [], color="red", label="Hacking Attempt", marker="x")
ax.set_xlabel("Time")
ax.set_ylabel("Brainwave Signal")
ax.set_title("Real-Time AI-Detected Hacking Attempts")
ax.legend()

# Update function for animation
def update(frame):
    line.set_data(df.index[:frame], df["Signal"][:frame])
    detected_anomalies = df.iloc[:frame][df["Anomaly"] == -1]
    scatter.set_offsets(np.c_[detected_anomalies.index, detected_anomalies["Signal"]])
    return line, scatter

ani = animation.FuncAnimation(fig, update, frames=len(df), interval=50, blit=False)
plt.show()
