ROBOT = "go2"  # 机器人型号，目前只有 "go2"
ROBOT_SCENE = "../robot_description/" + ROBOT + "/scene.xml"  # 机器人场景文件路径
DOMAIN_ID = 1  # 域 ID
INTERFACE = "lo"  # 网络接口

USE_JOYSTICK = 1  # 使是否用手柄模拟 Unitree 无线控制器
JOYSTICK_TYPE = "xbox"  # 支持的手柄布局："xbox" 或 "switch"
JOYSTICK_DEVICE = 0  # 手柄设备编号

PRINT_SCENE_INFORMATION = True  # 打印机器人连杆、关节和传感器信息
ENABLE_ELASTIC_BAND = False  # 虚拟弹性带，h1 抬升时使用

SIMULATE_DT = 0.005  # 模拟步长，需大于 viewer.sync() 的运行时间
VIEWER_DT = 0.02  # 可视化步长（50 FPS）
