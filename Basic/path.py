import os.path
import time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目的绝对路径

log_path = os.path.join(base_dir, r"Log/{}.log".format(time.strftime("%Y-%m-%d", time.localtime())))  # log存放路径
