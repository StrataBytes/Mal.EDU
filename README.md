# Malware Removal Exercise Tool
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) | **Author:** Stratabytes

## Introduction

This project is designed as an educational exercise for understanding and practicing malware removal techniques. It simulates behaviors commonly associated with malware, such as disabling certain keyboard shortcuts and implementing persistence mechanisms. It's intended strictly for educational purposes within controlled environments.

## Features

- **'Windows Driver Foundation - User-mode Driver Framework Host Process.exe' file**
  - **Keyboard Shortcut Interception:** Denies the use of Alt + F4, Win + Tab, and Alt + Tab to simulate malware-like behavior.
  - **Self-Termination Prevention:** The script will terminate itself if unfocused, simulating malware's evasion techniques, making it hard to track in programs like task manager.
  - **Misleading Name:** In attempts to trick the technician, the EXE is named to deceive.

- **'Client Server Runtime Process.bat'**
  - **Persistence Simulation:** Includes instructions to schedule the script to restart and to set up the executable to run on boot, mimicking malware persistence.

## Setup

**Pre-requisites:**

- Ensure Python is installed on your system with pyinstaller (`pip install pyinstaller`) to not trigger Windows antivirus.
  - Adding an exception to the antivirus will point the technician to the script, making it easier to find - not recommended.

**Steps:**

1. **'Client Server Runtime Process.bat'**
   - Run as admin and verify it has fully setup.

2. **Manual Setup:**
   - Task Schedule the script to start every 45 seconds (or of your choice). This simulates the persistence technique used by malware to ensure it remains active.
   - Set the executable to start on boot. This helps in understanding how malware ensures its activation with each system start.

## Usage

- Download both .bat file and .exe - you may also download the raw python script to build yourself.
- Follow the setup instructions to simulate malware persistence.
- Use this as an educational tool to practice malware removal techniques. **Do not use for malicious intent!**

> **Note:** This tool is meant for educational purposes in a controlled environment. Do not use it on unconsented systems.

## Future Plans

- **Self-Heal Function:** To further mimic malware behaviors, a future update will include a self-heal function. This function will create backups of the script in different locations. If one instance is deleted, the other will replicate itself, necessitating the use of safe mode or Hirens for complete removal.

## Contributing

Contributions to improve the tool or extend its functionalities for educational purposes are welcome. Please ensure any contributions do not include actual malicious code or support harmful activities.

## License

This project is licensed under the GPL 2.0. See the LICENSE file for more details.
