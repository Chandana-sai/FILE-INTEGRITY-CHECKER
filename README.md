# FILE-INTEGRITY-CHECKER

COMPANY : CODTECH IT SOLUTIONS

NAME : PURLLA CHANDANA SAI PRIYANKA

INTERN ID :CT06DM729

DOMAIN :CYBER SECURITY AND ETHICAL HACKING

DURATION :6 WEEKS

MENTOR : NEELA SANTOSH

DESCRIPTION :
🛡️ File Integrity Checker
A simple Python script to monitor file integrity using SHA-256 hash comparisons. It allows users to create a secure hash baseline of files in a directory and later verify if any files have been modified, deleted, or added.

🔧 Features
Create Baseline: Generate and save SHA-256 hashes for all files in a specified directory.

Check Integrity: Detect changes by comparing the current state of files to the previously saved baseline.

Change Detection:

Modified files

New files

Deleted files

📂 How It Works

The script scans the ./monitor directory (can be customized).

It creates a JSON file (baseline_hashes.json) that stores the relative file paths and their SHA-256 hashes.

On running an integrity check, it re-computes hashes and compares them to the baseline.

🚀 Usage
Run the script from the command line:

bash
Copy
Edit
python file_integrity_checker.py
You'll be prompted to:

1: Create a baseline

2: Check file integrity

⚠️ Make sure the ./monitor directory exists before running the script.

🧩 Dependencies
Python 3.x (standard libraries only: os, hashlib, json)

📄 License
This project is licensed under the MIT License.

Let me know if you'd like a README.md version with Markdown formatting or any additional features like email notifications or logging support.




You said:
AT LEAST 500 WORDS

ChatGPT said:
Sure! Here's a detailed GitHub repository description (over 500 words) you can use as your README.md file:

🛡️ File Integrity Checker
The File Integrity Checker is a simple yet powerful Python tool designed to monitor the integrity of files within a specified directory. By leveraging SHA-256 cryptographic hashes, this script allows you to track changes to your files over time, helping you detect tampering, corruption, or unauthorized modifications.

This tool is especially useful for administrators, developers, researchers, or anyone who wants to ensure that important files remain unchanged and secure.

📌 Overview
The tool works in two main phases:

Baseline Creation: In this phase, the tool walks through a target directory and calculates the SHA-256 hash of every file it finds. These hashes are saved in a file called baseline_hashes.json. This serves as the trusted state of your files at a specific point in time.

Integrity Check: Later, when you run the tool again, it recalculates the hashes of all the current files and compares them against the saved baseline. If there are discrepancies, the tool reports which files were modified, deleted, or newly added since the baseline was created.

🔧 Features
✅ SHA-256 Based Hashing: Utilizes secure hashing to ensure high confidence in integrity verification.

✅ Baseline Generation: Saves hash values in a structured JSON file for reference.

✅ Change Detection:

Modified files – files whose contents have changed.

New files – files that were added after the baseline.

Deleted files – files that existed during baseline creation but no longer exist.

✅ User-friendly CLI interface: Simple menu to create baselines or run integrity checks.

✅ Lightweight and Dependency-Free: Uses only built-in Python libraries.

🚀 Getting Started
Prerequisites
Python 3.6 or later

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/file-integrity-checker.git
cd file-integrity-checker
Create the directory to be monitored (if it doesn’t exist):

bash
Copy
Edit
mkdir monitor
Run the script:

bash
Copy
Edit
python file_integrity_checker.py
📂 How It Works
Step 1: Creating the Baseline
Select option 1 from the menu to generate a baseline. The script will:

Traverse all files under the ./monitor directory.

Compute SHA-256 hashes for each file.

Save these hashes in baseline_hashes.json.

Step 2: Checking File Integrity
Select option 2 to perform an integrity check. The script will:

Recalculate the current hashes of the files in the ./monitor directory.

Compare them to the hashes stored in the baseline.

Report any:

Modified files (same name but different hash)

Deleted files (present in baseline but missing now)

New files (present now but not in baseline)

💻 Example Output
sql
Copy
Edit
FILE INTEGRITY CHECKER
1. Create baseline
2. Check file integrity
Select an option (1 or 2): 2

🛡️ Integrity Check Report:
----------------------------
Modified Files: ['example.txt']
New Files: ['new_script.py']
Deleted Files: ['old_config.ini']
----------------------------
📁 Directory Structure
bash
Copy
Edit
file-integrity-checker/
│
├── file_integrity_checker.py
├── baseline_hashes.json        # Created after baseline generation
└── monitor/                    # Directory to monitor for changes
🧩 Modules Used
os – For directory and file path operations.

hashlib – For computing SHA-256 hashes.

json – For storing and reading the baseline hash data.

input() – For basic menu interaction.

🔒 Use Cases
Monitoring configuration files in servers.

Verifying the integrity of research data.

Detecting tampering in scripts or codebases.

Ensuring no unauthorized files are added to sensitive directories.

📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

🤝 Contributions
Contributions are welcome! If you have suggestions, bug reports, or improvements, feel free to open an issue or submit a pull request.

OUTPUT :

![Image](https://github.com/user-attachments/assets/11a86613-b3bb-4cc2-97c2-02c17c9e6f40)







