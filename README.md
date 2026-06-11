# Repeater

A simple Python automation script using `pyautogui` to type out a sequence of steps with configurable intervals.

## Prerequisites

- Python 3.x
- `pyautogui` library

You can install the required dependency using pip:

```bash
pip install pyautogui
```

## Usage

1. Open the file `script.py` in your text editor.
2. Modify the `Configuration` variables to suit your needs:
   - `start_num`: The starting number for the step sequence.
   - `end_num`: The ending number for the step sequence.
   - `wait_time`: The wait time between each step iteration (in seconds).
   - `text_template`: The template for the text to type. Use `{}` as a placeholder for the number (e.g., `"Item #{}"` will output `"Item #1"`).
   - `initial_delay`: The initial delay before the script starts typing (in seconds), giving you time to switch to the target application.
3. Run the script from your terminal:

```bash
python script.py
```

4. Quickly switch to the application where you want the text to be typed and place your cursor there. You will have `initial_delay` seconds to do this.

## How it Works

The script will type out "Step X" where X is a number between `start_num` and `end_num`. It simulates typing with a slight interval between keystrokes and presses the 'enter' key after each step. It waits for `wait_time` seconds between each step, and stops after reaching the `end_num`.
