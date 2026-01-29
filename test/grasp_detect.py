import sys
sys.path.append('/home/chark/linkerhand-python-sdk')
# print(sys.path)
from LinkerHand.linker_hand_api import LinkerHandApi

import time
import jkrc  


def jaka_linear_move_z(distance):
    robot.login()#登录  
    robot.power_on() #上电  
    robot.enable_robot()  
    print("沿Z轴向上移动") 

    tcp_pos=[0,0,distance,0,0,0]  
    robot.linear_move(tcp_pos,1,True,5)  

    time.sleep(3)  
    robot.logout()

# 获取法向压力
def get_normal_force():
    force = linker_hand.get_force()
    print(f"force:{force}")
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

    


# 手掌姿势预定义
pose_fist=[40, 0, 0, 0, 0, 131, 10, 100, 180, 240, 19, 255, 255, 255, 255, 135, 0, 0, 0, 0]
pose_open=[255, 255, 255, 255, 255, 255, 10, 100, 180, 240, 245, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_OK=[191, 95, 255, 255, 255, 136, 107, 100, 180, 240, 72, 255, 255, 255, 255, 116, 99, 255, 255, 255]
pose_like=[255, 0, 0, 0, 0, 127, 10, 100, 180, 240, 255, 255, 255, 255, 255, 255, 0, 0, 0, 0]

pose_grasp0=[255, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_grasp1=[168, 138, 137, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 63, 64, 66, 255, 255]
pose_grasp2=[202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 1, 255, 255, 255, 255]



# 机械臂初始化
robot = jkrc.RC("192.168.2.64")#返回机器人对象  

# 灵巧手初始化API hand_type:left or right   hand_joint:L7 or L10 or L20 or L25
linker_hand = LinkerHandApi(hand_type="right", hand_joint="L20")
linker_hand.set_speed(speed=[120,200,200,200,200])


linker_hand.finger_move(pose=pose_open)

while(1):
    
    normal_force = get_normal_force()
    print(f"normal_force:{normal_force}")
    time.sleep(0.5)