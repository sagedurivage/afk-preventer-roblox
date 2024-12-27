
import pyautogui
import time
from AppKit import NSWorkspace
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent, kCGEventKeyDown, kCGEventKeyUp, kCGEventSourceStateHIDSystemState, CGEventPost, CGEventSourceCreate, kCGEventSourceStateHIDSystemState, kCGEventSourceStateHIDSystemState
import Quartz.CoreGraphics as CG
import time

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

