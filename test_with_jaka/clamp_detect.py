"""
目标:感知到滑移，拇指继续弯曲，增大夹紧力
正常流程：手掌张开-->机械臂移动到抓取位置-->大拇指就位，开启触觉线程-->拇指末端弯曲，触觉力大于阈值，停止弯曲-->z轴向上移动
该程序实现的功能：1线程拇指末端弯曲，2线程监控法向力和切向力，并实时打印出来，拉动瓶子，可以观察法向力和切向力的变化趋势
总结：
"""

import sys
sys.path.append('/home/chark/linkerhand-python-sdk')
# print(sys.path)
from LinkerHand.linker_hand_api import LinkerHandApi

import time
import jkrc  

import threading


# 封装jaka的函数
def jaka_joint_move(joint_pose):
    
    robot.login()#登录  
    robot.power_on() #上电  
    robot.enable_robot()  

    robot.joint_move(joint_pose,0,True,0.3) 

    time.sleep(3)
    robot.logout()


def jaka_linear_move_z(distance):
    robot.login()#登录  
    robot.power_on() #上电  
    robot.enable_robot()  
    # print("沿Z轴向上移动") 

    tcp_pos=[0,0,distance,0,0,0]  
    robot.linear_move(tcp_pos,1,True,10)  

    time.sleep(3)  
    robot.logout()

# 获取法向压力
def get_normal_force():
    force = linker_hand.get_force()
    # print(f"force:{force}")
    return force[0]

# 获取切向压力
def get_tangential_force():
    force = linker_hand.get_force()
    # print(f"force:{force}")
    return force[1]

# 获取切向压力方向
def get_tangential_force_dir():
    force = linker_hand.get_force()
    # print(f"force:{force}")
    return force[2]

# 获取接近感觉
def get_approach_inc():
    force = linker_hand.get_force()
    # print(f"force:{force}")
    return force[3]




value_mcp = 255
# 大拇指尖端步进弯曲，超过阈值停止
def finger_move_thumb_mcp(step):
        global value_mcp
        
        if(stop_thumb):
            return

        value_mcp -= step
        
        # 大拇指就位时对应的拇指根部是0，保证拇指根部值不会小于0
        if(value_mcp > 0):
            linker_hand.finger_move([202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, value_mcp, 255, 255, 255, 255])
        else:
            value_mcp = 0


stop_thumb = False
force_threshold = 20

thumb_normal_force = []
thumb_tangential_force = []
thumb_tangential_force_dir = []
# 感知拇指法向压力、切向压力
def tactile_monitor():
    global stop_thumb,force_threshold,value_mcp
    

    while(1):
        normal_force = get_normal_force()
        tangential_force = get_tangential_force()
        tangential_force_dir = get_tangential_force_dir()

        # thumb_normal_force = normal_force[0]
        # thumb_tangential_force = tangential_force[0]
        # thumb_tangential_force_dir = tangential_force_dir[0]
        # thumb_normal_force = normal_force[1]
        # thumb_tangential_force = tangential_force[1]
        # thumb_tangential_force_dir = tangential_force_dir[1]
        # # thumb_normal_force = normal_force[2]
        # thumb_tangential_force = tangential_force[2]
        # thumb_tangential_force_dir = tangential_force_dir[2]
        # thumb_normal_force = normal_force[3]
        # thumb_tangential_force = tangential_force[3]
        # thumb_tangential_force_dir = tangential_force_dir[3]
        thumb_normal_force = normal_force[4]
        thumb_tangential_force = tangential_force[4]
        thumb_tangential_force_dir = tangential_force_dir[4]
        print(f"法向压力：{thumb_normal_force};切向压力：{thumb_tangential_force};切向压力方向：{thumb_tangential_force_dir}")
        
        
        if not stop_thumb and thumb_normal_force > force_threshold:
            print("force_threshold:", force_threshold)
            print("thumb_normal_force:", thumb_normal_force)
            print("value_mcp:",value_mcp)
            print("触觉检测到接触，发出停止信号")
            stop_thumb = True
            
        
        # 10ms,别太快
        time.sleep(0.01)




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
pose_grasp1=[202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255]
pose_grasp2=[202, 255, 255, 255, 255, 150, 10, 100, 180, 240, 0, 255, 255, 255, 255, 1, 255, 255, 255, 255]


# 机械臂初始化
robot = jkrc.RC("192.168.2.64")#返回机器人对象 


# 灵巧手初始化API hand_type:left or right   hand_joint:L7 or L10 or L20 or L25
linker_hand = LinkerHandApi(hand_type="right", hand_joint="L20")
linker_hand.set_speed(speed=[120,200,200,200,200])

# 手掌先张开，避免移动过程中与其他物体接触
linker_hand.finger_move(pose=pose_open)
time.sleep(2)


# # 大拇指就位，先横摆，再拇指根部弯曲到位
# linker_hand.finger_move(pose=pose_grasp0)
# time.sleep(2)

# linker_hand.finger_move(pose=pose_grasp1)
# time.sleep(2)



# 启动触觉监听线程
tactile_thread = threading.Thread(target=tactile_monitor)
tactile_thread.start()



# while 1:

#     finger_move_thumb_mcp(2)
#     time.sleep(0.02)

    # if(stop_thumb):
    #     break

# print("拇指力达到阈值，运动停止")