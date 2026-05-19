"""
没有触觉感知，仅大拇指夹取
张开手掌-->移动到抓取的固定位置-->大拇指移动到固定位置，夹取物体
"""

import sys
sys.path.append('/home/chark/linkerhand-python-sdk')
# print(sys.path)
from LinkerHand.linker_hand_api import LinkerHandApi

import time
import jkrc  


# 封装沿z轴向上移动的函数
def jaka_linear_move_z(distance):
    robot.login()#登录  
    robot.power_on() #上电  
    robot.enable_robot()  
    print("沿Z轴向上移动") 

    tcp_pos=[0,0,distance,0,0,0]  
    robot.linear_move(tcp_pos,1,True,15)  

    time.sleep(3)  
    robot.logout()




# 注意修改成绝对运动
joint_shakeHand = [1.7788700470813605, 1.5160035649775419, 1.7058096395683742, 3.6527536195264347, 1.447604617737367, 0.8140719507856603]
joint_transfer = [1.8685457970871147, 1.0379887926373477, 0.9810034260405898, 3.6153792610972757, 1.507176579738873, 0.8142748802177897]
joint_object = [1.7812167469804219, 2.0933435938787466, 2.052321218060239, 2.102622532127219, 1.6272105867538167, 0.8141790092819777]


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


# 每次移动机械臂之前，首先确保手处于张开位置，防止碰到其他物体
linker_hand.finger_move(pose=pose_open)
time.sleep(3)


# 机械臂移动到抓取位置
# 运动模式，绝对运动是0，相对运动是1;阻塞True,非阻塞False
robot.login()#登录  
robot.power_on() #上电  
robot.enable_robot()  
move_mode = 0  
is_block = True

print("move1")  
robot.joint_move(joint_object,move_mode,True,0.3)  


# 延时10s,获取关节位置
time.sleep(10)
ret = robot.get_joint_position()  
if ret[0] == 0:  
    print("成功获取到关节位置，关节位置：",ret[1])  
else:  
    print("some things happend,the errcode is: ",ret[0])  
robot.logout()  


# 判断关节位置是不是抓取位置，如果是，进行抓取
if(ret[1]==joint_object):
    
    linker_hand.finger_move(pose=pose_grasp0)
    time.sleep(3)

    linker_hand.finger_move(pose=pose_grasp2)
    
    # while(1):
    #     normal_force = linker_hand._get_normal_force()
    #     print(normal_force)
    #     time.sleep(0.5)

    jaka_linear_move_z(200)
	
else:
    print('没有成功移动到握手位置')





   
