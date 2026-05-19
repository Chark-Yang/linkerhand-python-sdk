"""
特点: 感知到触觉,停止夹紧,2个线程,only pinky; pinky will stop bending when sensing the tactile force
运动流程:pinky ready pose -> step bending & sensing force 
"""

import sys
sys.path.append('/home/chark/linkerhand-python-sdk')
# print(sys.path)
from LinkerHand.linker_hand_api import LinkerHandApi

import time
import threading


# 获取法向压力
def get_normal_force():
    force = linker_hand.get_force()
    # print(f"force:{force}")
    return force[0]

# 获取切向压力
def get_tangential_force():
    force = linker_hand.get_force()
    print(f"force:{force}")
    return force[1]

# 获取切向压力方向
def get_tangential_force_dir():
    force = linker_hand.get_force()
    print(f"force:{force}")
    return force[2]

# 获取接近感觉
def get_approach_inc():
    force = linker_hand.get_force()
    print(f"force:{force}")
    return force[3]


value_mcp = 255
# 大拇指尖端步进弯曲
def finger_move_thumb_mcp(step):
        global value_mcp, stop_thumb
        
        if(stop_thumb):
            return

        value_mcp -= step
        
        # 大拇指就位时对应的拇指根部是0，保证拇指根部值不会小于0
        if(value_mcp > 0):
            linker_hand.finger_move([202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, value_mcp, 255, 255, 255, 255])
        else:
            value_mcp = 0



# 小指步进弯曲
def finger_move_pinky_mcp_pip(mcp_step = 5, pip_step = 5):
        global value_pinky_mcp, value_pinky_pip, stop_pinky
        
        if(stop_pinky):
            return

        value_pinky_mcp -= mcp_step
        value_pinky_pip -= pip_step

        if value_pinky_mcp < 0:
            value_pinky_mcp = 0
        if value_pinky_pip < 0:
            value_pinky_pip = 0

        if(value_pinky_mcp != 0 or value_pinky_pip != 0):
            linker_hand.finger_move([255, 255, 255, 255, value_pinky_mcp, 255, 37, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, value_pinky_pip])

        


# stop_thumb = False
# force_threshold = 20
# normal_force = []
# thumb_normal_force = []
# 触觉监听线程，只干一件事：设标志位
# def tactile_monitor():
#     global stop_thumb,normal_force,thumb_normal_force,value_mcp

#     while not stop_thumb:
#         normal_force = get_normal_force()   
#         thumb_normal_force = normal_force[0]
        
#         if thumb_normal_force > force_threshold:
#             print("force_threshold:", force_threshold)
#             print("thumb_normal_force:", thumb_normal_force)
#             print("value_mcp:",value_mcp)
#             print("触觉检测到接触，发出停止信号")
#             stop_thumb = True
#             break

#         time.sleep(0.01)  # 10ms，别太快

stop_pinky = False
force_threshold = 20
normal_force = []
pinky_normal_force = []

def tactile_pinky_monitor():
    global stop_pinky,normal_force,pinky_normal_force

    while not stop_pinky:
        normal_force = get_normal_force()   
        pinky_normal_force = normal_force[4]
        
        if pinky_normal_force > force_threshold:
            print("force_threshold:", force_threshold)
            print("pinky_normal_force:", pinky_normal_force)
            # print("value_pinky_mcp:", value_pinky_mcp)
            # print("value_pinky_pip:", value_pinky_pip)
            print("触觉检测到接触，发出停止信号")
            stop_pinky = True
            break

        time.sleep(0.01)  # 10ms，别太快


# 手掌姿势预定义
pose_fist=[40, 0, 0, 0, 0, 131, 10, 100, 180, 240, 19, 255, 255, 255, 255, 135, 0, 0, 0, 0]
pose_open=[255, 255, 255, 255, 255, 255, 10, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_OK=[191, 95, 255, 255, 255, 136, 107, 100, 180, 240, 72, 255, 255, 255, 255, 116, 99, 255, 255, 255]
pose_like=[255, 0, 0, 0, 0, 127, 10, 100, 180, 240, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0]

# pose_grasp0是拇指侧摆到位,pose_grasp1拇指根部弯曲到位,pose_grasp2拇指末端弯曲到位
pose_grasp0=[255, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_grasp1=[202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_grasp2=[202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 1, 255, 255, 255, 255]

# pinky_grasp2是小指根部微微弯曲，PIP微微弯曲，呈现预备抓握状态
pose_pinky_grasp2=[255, 255, 255, 255, 199, 255, 37, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 148]

# 灵巧手初始化API hand_type:left or right   hand_joint:L7 or L10 or L20 or L25
linker_hand = LinkerHandApi(hand_type="right", hand_joint="L20")
linker_hand.set_speed(speed=[120,200,200,200,200])


# 手掌先张开，避免移动过程中与其他物体接触
linker_hand.finger_move(pose=pose_open)
time.sleep(2)


# 大拇指就位，先横摆
# linker_hand.finger_move(pose=pose_grasp0)
# print("pose_grasp0")
# time.sleep(4)

# 拇指根部弯曲到位，稍微弯曲
# linker_hand.finger_move(pose=pose_grasp1)
# print("pose_grasp1")
# time.sleep(4)

# # 启动触觉监听线程
tactile_thread = threading.Thread(target=tactile_pinky_monitor)
tactile_thread.start()

# 拇指末端弯曲，直到触觉检测到接触
# while not stop_thumb:
#     finger_move_thumb_mcp(5)
#     time.sleep(0.05)


# len = len(pose_pinky_grasp2)
# pinky_mcp_value = pose_pinky_grasp2[4]
# pinky_pip_value = pose_pinky_grasp2[19]
# print("len:", len)
# print("pinky_mcp_value:", pinky_mcp_value)
# print("pinky_pip_value:", pinky_pip_value)

value_pinky_mcp = pose_pinky_grasp2[4]
value_pinky_pip = pose_pinky_grasp2[19]

# 小指就位，预备抓取
linker_hand.finger_move(pose=pose_pinky_grasp2)
time.sleep(2)

while not stop_pinky:
    finger_move_pinky_mcp_pip(4, 2)
    time.sleep(0.05)

