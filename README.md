### BCI Theft Detection System:

An **AI-powered Brain-Computer Interface (BCI) security system** that detects **brainwave data theft** in real time using **Isolation Forest anomaly detection**.  
This system provides **attack classification, secure logging, PDF reporting, desktop notifications**, and an **animated live visualization** of hacking attempts.

---

##  Features

✅ **AI-Based Anomaly Detection** – Detects unusual patterns in brainwave signals  
✅ **Severity Classification** – Differentiates between *Mild* and *Severe* attacks  
✅ **Secure Logging** – Uses AES-based encryption (via `cryptography.fernet`)  
✅ **Attack Blocking Simulation** – Logs and blocks malicious sources  
✅ **Automated PDF Reports** – Generates professional attack summaries  
✅ **Desktop Notifications** – Instant alerts for detected threats  
✅ **Real-Time Visualization** – Animated graph of hacking attempts  

---

## Screenshots

### 🔹 Real-Time Hacking Detection
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e2a1f023-c3a7-4ff4-93a5-9534a0926ea0" />


### 🔹 PDF Hacking Report

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d149bcad-e22f-428a-a2f6-9322eabc056c" />

---

## Tech Stack

- **Programming Language:** Python 3.x
- **AI & ML:** Scikit-learn (Isolation Forest)
- **Data Handling:** NumPy, Pandas
- **Visualization:** Matplotlib (with animation)
- **Security:** Cryptography (Fernet encryption)
- **Reporting:** FPDF (PDF generation)
- **Alerts:** Plyer (Desktop notifications)

---

## 📂 Project Structure

BCI_Theft_Detection/
│── static/screenshots/ # Images for README
│── encryption_key.key # Generated encryption key (auto-created)
│── hacking_attempts.log # Encrypted attack logs
│── blocked_sources.log # Blocked malicious sources
│── hacking_report.pdf # Generated attack report
│── bci_theft_detection.py # Main application script
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## ⚙️ Installation & Setup
1. clone the Repositary
   
2️⃣ Create Virtual Environment
bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Run the Program
bash

python bci_theft_detection.py
##How It Works
Simulated Brainwave Data – Generates normal and attack signals

AI Detection – Isolation Forest flags anomalies

Severity Classification – Categorizes attacks as Mild or Severe

Secure Logging – Encrypts attack logs with AES-256 equivalent security

Blocking Mechanism – Records and blocks malicious sources

Reporting – Creates PDF with attack details

Visualization – Animated graph showing hacking events



👤 Author
Biswajit Rout
📧 Email: work.bjr07@gmail.com
🌐 GitHub:BJR07


