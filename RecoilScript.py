import keyboard
import mouse
import time

running = False

def toggle_running():
    global running
    running = not running
    print(f"Recoil control {'ON' if running else 'OFF'}")

keyboard.add_hotkey('f6', toggle_running)

print("Press F6 to toggle recoil control ON/OFF.")

while True:
    if running and mouse.is_pressed(button='left'):
        print("Recoil control...")
        
        time.sleep(0.01)
