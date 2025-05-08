import hashlib
import os

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None

def load_reference_hashes(file="hashes.txt"):
    if not os.path.exists(file):
        return {}
    with open(file, 'r') as f:
        lines = f.readlines()
    return dict(line.strip().split() for line in lines)

def save_reference_hashes(hashes, file="hashes.txt"):
    with open(file, 'w') as f:
        for path, h in hashes.items():
            f.write(f"{path} {h}\n")

def check_files(file_paths):
    current_hashes = {path: get_file_hash(path) for path in file_paths}
    reference_hashes = load_reference_hashes()

    for path, new_hash in current_hashes.items():
        if path in reference_hashes:
            if new_hash != reference_hashes[path]:
                print(f"🚨 ALERT: Integrity check failed for: {path}")
            else:
                print(f"✅ OK: {path}")
        else:
            print(f"⚠️ New file detected: {path}")

    save_reference_hashes(current_hashes)

if __name__ == "__main__":
    files = input("Enter comma-separated file paths to check: ").split(",")
    files = [f.strip() for f in files]
    check_files(files)
