# Mal.EDU - Educational Malware Removal Exercise Tool
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) <br>
**Author:** StrataBytes

## Introduction

This project is designed as an educational exercise for understanding and practicing malware removal techniques. It simulates behaviors commonly associated with malware, such as disabling certain keyboard shortcuts and implementing persistence mechanisms. It's intended strictly for educational purposes within controlled environments.

## Features

- **'csrss.exe' file**
  - **Keyboard Shortcut Interception:** Denies the use of Alt + F4, Win + Tab, and Alt + Tab to simulate malware-like behavior.
  - **Self-Termination Prevention:** The script will terminate itself if unfocused, simulating malware's evasion techniques, making it hard to track in programs like task manager.
  - **Misleading Name:** In attempts to trick the technician, the EXE is named to deceive.

- **'setup.bat'**
  - **Persistence Simulation:** Includes instructions to schedule the script to restart and to set up the executable to run on boot, mimicking malware persistence.

## Setup

**Pre-requisites, for better result, but not required:**

- Ensure Python is installed on your system with pyinstaller (`pip install pyinstaller`) to help reduce triggering Windows antivirus.
  - Adding an exception to the antivirus will point the technician to the script, making it easier to find - not recommended, however it may be needed.

**Steps:**

1. **'setup.bat'**
   - Run as admin and walk through the initialization prompts. (Location, Time, Conditions, ect.)
   - verify it has fully setup.
   - Delete the setup batch file.

2. **Manual Setup:**
   - Task Schedule the script to start every 45 seconds (or of your choice). This simulates the persistence technique used by malware to ensure it remains active.
   - Set the executable to start on boot. This helps in understanding how malware ensures its activation with each system start.
   - Remember to hide the EXE file! Copy two if need be, one to be seen on startup programs and one for the task scheduler so it cannot be taken out with one stone.

3. **Removing**
   - Simply run as admin on the remove.bat file included.

## Usage

- Download both .bat file and .exe - you may also download the raw python script to build yourself.
- Follow the setup instructions to simulate malware persistence.
- Use this as an educational tool to practice malware removal techniques. **Do not use for malicious intent!**

> **Note:** This tool is meant for educational purposes in a controlled environment. Do not use it on unconsented systems.


## Limitations

- Somewhat easy to find if the user knows to look for it in startup or task scheduler.
- Cannot recover from deletion.
- Every once in a while, it can trip Windows Defender due to the nature of an EXE built in pyinstaller, causing WD to delete it instantly. It will also sometimes get flagged due to evasion behavior.
  - To somewhat fix, build the raw script (with pyinstaller) on the exercise computer making it no longer a forign application. This only helps a really small amount.

## Manual Building
- Be sure python is installed and add to PATH is selected during setup.
  - Download required libraries: Open CMD prompt as admin, run the following commands `pip install pyinstaller`, `pip install pygame`, `pip install keyboard` (if needed).
- Download the python script PLUS the image and put it in a folder.
- In CMD prompt, navigate to the folder.
- Now, run the build command, `pyinstaller --onefile --add-data "img.jpg;." csrss.py`
- Done! Now go back up to the steps section.

> **Note:** You can also change the image before running the build command.

## Future Plans

- **Self-Heal Function:** To further mimic malware behaviors, a future update will include a self-heal function. This function will create backups of the script in different locations. If one instance is deleted, the other will replicate itself, necessitating the use of safe mode or Hirens for complete removal.

## Contributing

Contributions to improve the tool or extend its functionalities for educational purposes are welcome. Please ensure any contributions do not include actual malicious code or support harmful activities.

## License

This project is licensed under the GPLv3. See the LICENSE file for more details.
