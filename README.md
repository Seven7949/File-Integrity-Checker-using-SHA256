# File-Integrity-Checker-using-SHA256
Because if someone even thinks about tampering with your files… you’ll catch 'em red-handed. 
# 🔐 File Integrity Checker (SHA256)

A simple Python script to monitor and verify file integrity using SHA256 hash comparisons.  
Perfect for detecting file tampering, corruption, or unauthorized changes.

---

## ✅ Features

- Generates and stores reference hashes of important files
- Compares current hash to detect changes
- Flags newly added or modified files
- Lightweight and beginner-friendly

---

## ⚙️ Requirements

- Python 3

---

## 🚀 How to Use

### 1. First Run – Set Baseline

```bash
python3 filEnter your files like this:

Enter comma-separated file paths to check: /etc/passwd, /home/user/config.json
This will create a hashes.txt storing SHA256 hashes for those files.

2. Subsequent Runs
Run the script again with same paths to check for changes.
You’ll see alerts like:

✅ OK: /etc/passwd  
🚨 ALERT: Integrity check failed for: /home/user/config.json
📎 Example

hashes.txt:
 /etc/passwd  a83d0d42c7160f8c0340f8b1e05d4e0babc23...
💡 Use Cases

Monitoring sensitive system files
Verifying code or config changes
Detecting backdoors or unauthorized modifications
⚠️ Warning

Keep the hashes.txt file safe — if an attacker modifies that too, you’re blind.

👩‍💻 Author

You already know who 😏 — YourGitHub

🧾 License

MIT. Use it. Fork it. Just don’t abuse it.e_integrity_checker.py
