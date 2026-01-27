from LinkerHand.linker_hand_api import LinkerHandApi


def main():
    # 初始化API hand_type:left or right   hand_joint:L7 or L10 or L20 or L25
    linker_hand = LinkerHandApi(hand_type="left", hand_joint="L10")
    # 设置手指速度
    linker_hand.set_speed(speed=[120,200,200,200,200])
    # 设置手扭矩
    linker_hand.set_torque(torque=[200,200,200,200,200])
    # 获取手当前状态
    hand_state = linker_hand.get_state()
    # 打印状态值
    print(hand_state)

if __name__ == "__main__":
    main()