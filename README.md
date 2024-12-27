# AFK Preventer for Roblox Games

This project is a simple script to prevent automatic logout in Roblox games by simulating periodic keystrokes, specifically pressing the space bar, to keep the game active. It ensures that the game server doesn’t kick you out due to inactivity while you're away from the keyboard (AFK).

## Features

- **Focused Window Navigation**: Ensures that a player’s Roblox Client is currently the main window or focused.
- **Prevents AFK Timeout**: Periodically simulates a spacebar press to keep the game session active.
- **Customizable**: Modify the time intervals between keystrokes or adapt the script for other games or applications.

## Prerequisites

To run this project, you'll need the following:

- **macOS** (the script was developed and tested on macOS)
- **Python 3.x**

### Dependencies
This project uses the following Python libraries:
- **pyautogui**: For simulating keyboard presses.
- **pyobjc-framework-Quartz**: For macOS-specific window management.

You can install these dependencies using the provided `requirements.txt`.

## Installation

Follow these steps to get the script running on your machine:

### 1. Clone the repository
```bash
git clone https://github.com/sagedurivage/afk-preventer-roblox.git
```
```bash
cd afk-preventer-roblox
```

### 2. Set up the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.command` file (optional)
To easily run the script, create a `.command` file by following these steps:
1. Create a new file called `run_automation.command` in the root of the project.
2. Add the following content:
```bash
#!/bin/bash

# Navigate to the Project/ directory
cd </path/to/your/Project/>

# Activate the virtual environment
source venv/bin/activate

# Run the Python script
python3 afk-preventer-roblox.py
```
3. Make it executable:
```bash
chmod +x run_automation.command
```

### 5. Run the script
You can now run the script by double-clicking the `.command` file.

## Usage

- Simply run the script, and it will periodically simulate a spacebar key press to prevent AFK timeouts in Roblox games.
- The script will continue running until you manually stop it (e.g., using `Ctrl + C` in the terminal).

## Customization

- **Time Interval**: You can customize the interval between keystrokes in the script by adjusting the sleep time between simulated key presses.
- **Target Application**: If you want to adapt the script to work with another application, you can modify the logic for identifying the target window.

## Troubleshooting

### Common Errors:
1. **`ModuleNotFoundError` for pyautogui or pyobjc**:
   - Ensure you have activated the virtual environment (`source venv/bin/activate`)
   - And installed the dependencies (`pip install -r requirements.txt`)

2. **Window detection issues**:
   - Make sure that your target application is open and correctly identified by the script.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to [pyautogui](https://pyautogui.readthedocs.io/en/latest/) for automating GUI interactions.
- Thanks to [pyobjc-framework-Quartz](https://pypi.org/project/pyobjc-framework-Quartz/) for macOS window management.
- Roblox ToS Consideration: [devforum.roblox.com](https://devforum.roblox.com/t/is-an-afk-system-agaisnt-roblox-tos/3026316)
