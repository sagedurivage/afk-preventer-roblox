
import pyautogui
import time
from AppKit import NSWorkspace

# Configuration
target_app = "Roblox"
interval = 300  # 300 seconds = 5 minutes between keystrokes

def focus_window(title):
    """Find and activate a window with the specified title."""
    # Get the list of currently running applications
    workspace = NSWorkspace.sharedWorkspace()
    apps = workspace.runningApplications()
    for app in apps:
        if title.lower() in app.localizedName().lower():
            app.activateWithOptions_(4)  # Bring the app to the front
            print(f"Focused window: {app.localizedName()}")
            return True
    print(f"No window found with title containing: {title}")
    return False

print("AFK script running. Press Ctrl+C to stop.")
try:
    while True:
        # Focus the target application
        if focus_window(target_app):
            time.sleep(0.5) # Allow time for target app to focus
            pyautogui.press('space')  # Simulate a space bar press
            print("Space bar pressed.")
        time.sleep(interval)  # Wait for the specified interval
except KeyboardInterrupt:
    print("Script stopped.")


# ---------- Bonus Implementation of an alternate Auto-Clicking Function ---------- #
# # Focus the target application once
# if focus_window(target_app):
#     print(f"Application {target_app} focused. Starting loop.")
# else:
#     print(f"Failed to find or focus {target_app}. Exiting.")
#     exit(1)

# print("Mouse click script running. Press Ctrl+C to stop.")
# try:
#     while True:
#         # Perform a mouse click
#         pyautogui.click()
#         print("Mouse clicked.")
#         time.sleep(interval)  # Wait for the specified interval
# except KeyboardInterrupt:
#     print("Script stopped.")

