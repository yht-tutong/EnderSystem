try:
    # 加载rmtree\sleep模块
    from shutil import rmtree
    from os import path
    from time import sleep

    c_path = 'C:/Users/Public/EnderDOS'

    # 删除配置文件夹
    if path.exists(c_path):
        rmtree(c_path)
        
    # 提示信息
    print('删除成功!')
except Exception as e:
    print(e)
    print('没救了!')

try:
    sleep(10)
except Exception as e:
    print(e)