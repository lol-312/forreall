import os
import pyautogui
import time
import keyboard

def find_and_click(image_paths):
    for image_path in image_paths:
        while True:
            try:

                absolute_image_path = os.path.join(os.path.dirname(__file__), image_path)


                button_image = pyautogui.locateOnScreen(absolute_image_path)

                if button_image is not None:

                    button_center = pyautogui.center(button_image)
                    pyautogui.click(button_center)


                    # time.sleep(0.1)

                    pyautogui.press('esc')
                    break
                else:
                    print(f"Button image not found for {image_path}. Retrying in 0.1 seconds.")
                    # time.sleep(0.1)
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Retrying.")
               # time.sleep(0.1)


script_path = os.path.dirname(os.path.abspath(__file__))
image_paths = [
    os.path.join(script_path, 'photos', 'image1.png'),
    os.path.join(script_path, 'photos', 'image2.png')
]

while True:
    find_and_click(image_paths)
    # time.sleep(0.1)
