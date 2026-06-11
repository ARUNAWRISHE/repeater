import pyautogui
import time

# ==========================
# Configuration
# ==========================
start_num = 1   # Starting number
end_num = 25        # Ending number
wait_time = 45    # Wait time between iterations (seconds)
text_template = "Step {}"  # Custom text template, use {} for the number

# Time to switch to the target application
initial_delay = 5  # Seconds

# ==========================
# Script
# ==========================
print(f"You have {initial_delay} seconds to place the cursor...")
time.sleep(initial_delay)

for i in range(start_num, end_num + 1):
    text = text_template.format(i)

    pyautogui.write(text, interval=0.05)  # Types the text
    pyautogui.press('enter')              # Moves to next line

    print(f"Typed: {text}")

    if i != end_num:
        time.sleep(wait_time)

print("Completed!")