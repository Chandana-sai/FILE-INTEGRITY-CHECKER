import os
import hashlib
import json
# Define the directory to monitor
MONITOR_DIR = "./monitor"

# File to store baseline hash values
BASELINE_FILE = "baseline_hashes.json"

def calculate_hash(file_path):
    """
    Calculate SHA-256 hash of a given file.
    """
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline():
    """
    Create a baseline of file hashes in the MONITOR_DIR.
    """
    hashes = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            relative_path = os.path.relpath(path, MONITOR_DIR)
            file_hash = calculate_hash(path)
            if file_hash:
                hashes[relative_path] = file_hash

    with open(BASELINE_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    print("✅ Baseline hash values saved successfully.")

def check_integrity():
    """
    Compare current file hashes to baseline to detect changes.
    """
    if not os.path.exists(BASELINE_FILE):
        print("❌ Baseline file not found. Please run 'create_baseline()' first.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_hashes = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            relative_path = os.path.relpath(path, MONITOR_DIR)
            file_hash = calculate_hash(path)
            if file_hash:
                current_hashes[relative_path] = file_hash

    modified = []
    new_files = []
    deleted = []

    # Check for modifications and deletions
    for file in baseline:
        if file not in current_hashes:
            deleted.append(file)
        elif baseline[file] != current_hashes[file]:
            modified.append(file)

    # Check for new files
    for file in current_hashes:
        if file not in baseline:
            new_files.append(file)

    print("\n🛡️ Integrity Check Report:")
    print("----------------------------")
    print("Modified Files:", modified if modified else "None")
    print("New Files:", new_files if new_files else "None")
    print("Deleted Files:", deleted if deleted else "None")
    print("----------------------------")

def main():
    print("FILE INTEGRITY CHECKER")
    print("1. Create baseline")
    print("2. Check file integrity")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
