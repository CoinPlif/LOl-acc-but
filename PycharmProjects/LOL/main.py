import pyautogui as pg
import time
import os
from model import AcceptModel


def gather_data():
    file_path = os.path.abspath(__file__)
    parent_path = "/".join(file_path.split("\\")[:-1])
    pictures_path = parent_path + "/Pictures"
    if not os.path.exists(pictures_path):
        os.mkdir("Pictures")

    for timestamp in range(300):
        time.sleep(1)
        pg.screenshot(pictures_path + f'PIC{timestamp}.jpg')
        print(f"Screenshot {timestamp} saved")


def inference(model):
    screenshot_path = model.parent_path + '/inference.jpg'
    pg.screenshot(screenshot_path)
    ans = model.predict(screenshot_path)
    if isinstance(ans, str):
        print(f"\n{time.time()}: " + ans)
        return False
    else:
        print(f"\n{time.time()}: ", ans[0], ans[1], ans[2], ans[3])
        box_coord = ans
        pg.click((box_coord[0] + box_coord[2]) / 2, (box_coord[1] + box_coord[3]) / 2)
        return True


def start():
    file_path = os.path.abspath(__file__)
    accept_model = AcceptModel(file_path)

    while True:
        time.sleep(0.5)
        if inference(accept_model):
            break


start()
