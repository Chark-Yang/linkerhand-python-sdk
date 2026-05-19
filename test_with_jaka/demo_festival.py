"""
演示视频：2025 nonono，2026，yoyoyo!
"""

import sys
sys.path.append('/home/chark/linkerhand-python-sdk')
# print(sys.path)
from LinkerHand.linker_hand_api import LinkerHandApi

import time

# 手掌姿势预定义
#修改pose_fist，防止干涉
pose_fist=[40, 0, 0, 0, 0, 81, 10, 100, 180, 240, 19, 255, 255, 255, 255, 135, 0, 0, 0, 0]
pose_open=[255, 255, 255, 255, 255, 255, 10, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_OK=[191, 95, 255, 255, 255, 136, 107, 100, 180, 240, 72, 255, 255, 255, 255, 116, 99, 255, 255, 255]
pose_like=[255, 0, 0, 0, 0, 127, 10, 100, 180, 240, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0]

pose_ye=[99, 255, 255, 0, 0, 119, 0, 255, 180, 240, 62, 255, 255, 255, 255, 99, 255, 255, 0, 0]
pose_one=[40, 255, 0, 0, 0, 81, 125, 100, 180, 240, 19, 255, 255, 255, 255, 135, 255, 0, 0, 0]
pose_one_right=[40, 255, 0, 0, 0, 131, 0, 100, 180, 240, 19, 255, 255, 255, 255, 135, 255, 0, 0, 0]
pose_one_left=[40, 255, 0, 0, 0, 131, 255, 100, 180, 240, 19, 255, 255, 255, 255, 135, 255, 0, 0, 0]
pose_two=[40, 255, 255, 0, 0, 81, 35, 177, 180, 240, 19, 255, 255, 255, 255, 135, 255, 255, 0, 0]
pose_three=[40, 255, 255, 255, 0, 161, 62, 123, 180, 240, 13, 255, 255, 255, 255, 0, 255, 255, 255, 0]
pose_four=[40, 255, 255, 255, 255, 161, 62, 123, 180, 242, 13, 255, 255, 255, 255, 0, 255, 255, 255, 255]
pose_five=[255, 255, 255, 255, 255, 255, 10, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_six=[255, 0, 0, 0, 255, 128, 10, 100, 180, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 255]
pose_seven=[0, 0, 0, 0, 0, 161, 10, 127, 180, 219, 18, 255, 255, 255, 255, 255, 195, 205, 0, 0]
pose_eight=[255, 255, 0, 0, 0, 202, 104, 100, 180, 240, 233, 255, 255, 255, 255, 255, 255, 0, 0, 0]
pose_nine=[40, 255, 0, 0, 0, 131, 103, 100, 180, 240, 19, 255, 255, 255, 255, 135, 47, 0, 0, 0]

pose_spider=[255, 255, 0, 0, 255, 128, 10, 100, 180, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255]
pose_spider_flex=[255, 255, 0, 0, 255, 128, 10, 100, 180, 255, 255, 255, 255, 255, 255, 151, 78, 0, 0, 78]
# "比耶":[99, 255, 255, 0, 0, 119, 0, 255, 180, 240, 62, 255, 255, 255, 255, 99, 255, 255, 0, 0],
# "壹": [40, 255, 0, 0, 0, 131, 125, 100, 180, 240, 19, 255, 255, 255, 255, 135, 255, 0, 0, 0],
# "贰": [40, 255, 255, 0, 0, 81, 35, 177, 180, 240, 19, 255, 255, 255, 255, 135, 255, 255, 0, 0],
# "叁": [40, 255, 255, 255, 0, 161, 62, 123, 180, 240, 13, 255, 255, 255, 255, 0, 255, 255, 255, 0],
# "肆": [40, 255, 255, 255, 255, 161, 62, 123, 180, 242, 13, 255, 255, 255, 255, 0, 255, 255, 255, 255],
# "伍": [255, 255, 255, 255, 255, 255, 10, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255],
# "陆": [255, 0, 0, 0, 255, 128, 10, 100, 180, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 255],
# "漆": [0, 0, 0, 0, 0, 161, 10, 127, 180, 219, 18, 255, 255, 255, 255, 255, 195, 205, 0, 0],
# "捌": [255, 255, 0, 0, 0, 202, 104, 100, 180, 240, 233, 255, 255, 255, 255, 255, 255, 0, 0, 0],
# "玖": [40, 255, 0, 0, 0, 131, 103, 100, 180, 240, 19, 255, 255, 255, 255, 135, 47, 0, 0, 0],


# 灵巧手初始化API hand_type:left or right   hand_joint:L7 or L10 or L20 or L25
linker_hand = LinkerHandApi(hand_type="right", hand_joint="L20")
linker_hand.set_speed(speed=[200,200,200,200,200])


# 2025
linker_hand.finger_move(pose=pose_open)
time.sleep(2)
linker_hand.finger_move(pose=pose_open)
time.sleep(2)

linker_hand.finger_move(pose=pose_two)
time.sleep(2)

linker_hand.finger_move(pose=pose_fist)
time.sleep(2)

linker_hand.finger_move(pose=pose_two)
time.sleep(2)

linker_hand.finger_move(pose=pose_five)
time.sleep(2)


# no姿势
linker_hand.finger_move(pose=pose_one)
time.sleep(1)
linker_hand.finger_move(pose=pose_one_right)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_left)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_right)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_left)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_right)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_left)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_right)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one_left)
time.sleep(0.3)
linker_hand.finger_move(pose=pose_one)
time.sleep(2)

# 2026
linker_hand.finger_move(pose=pose_two)
time.sleep(2)

linker_hand.finger_move(pose=pose_fist)
time.sleep(2)

linker_hand.finger_move(pose=pose_two)
time.sleep(2)

linker_hand.finger_move(pose=pose_six)
time.sleep(3)

# 蜘蛛侠
linker_hand.finger_move(pose=pose_spider)
time.sleep(2)
linker_hand.finger_move(pose=pose_spider_flex)
time.sleep(0.5)
linker_hand.finger_move(pose=pose_spider)
time.sleep(0.5)
linker_hand.finger_move(pose=pose_spider_flex)
time.sleep(0.5)
linker_hand.finger_move(pose=pose_spider)
time.sleep(0.5)
linker_hand.finger_move(pose=pose_spider)