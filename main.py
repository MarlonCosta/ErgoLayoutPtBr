import json
import os

from pynput.keyboard import Key, Listener

key_log = {}


def load_log(path: str):
    """Loads the logging file, if it doesnt exists, creates it"""

    if not os.path.exists(path):
        with open(path, "a+") as file:
            file.write("{}")

    with open(path, "r") as existing_file:
        data = json.load(existing_file)

    return data


def save_log(data: dict, path: str):
    """Saves data to logfile"""

    with open(path, "w") as file:
        json.dump(data, file)


def update_json(key: Key):
    """Resolves the key press event, adding to the number of presses for the key"""
    global key_log

    try:
        if key.char is not None:
            key = key.char.lower()
    except AttributeError:
        pass

    try:
        if key.name is not None:
            key = key.name.lower()
    except AttributeError:
        pass

    if key in key_log:
        key_log[key] = key_log[key] + 1
    else:
        key_log[key] = 1

    save_log(key_log, log_file)


if __name__ == '__main__':
    log_file = os.path.dirname(os.path.abspath(__file__)) + "/log_file.json"
    key_log = load_log(log_file)

    with Listener(on_release=update_json) as listener:
        listener.join()
