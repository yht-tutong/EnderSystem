from os import path,makedirs

if not path.exists('C:/Users/Public/EnderDOS'):
    makedirs('C:/Users/Public/EnderDOS')
with open(file='C:/Users/Public/EnderDOS/EnderDOS_Installation_status.txt',mode='w') as s:
    s.write('True')
with open(file='C:/Users/Public/EnderDOS/EnderDOS_ver.txt',mode='w') as s:
    s.write('1.2')
while True:
    temp = input('请选择你的程序安装位置(C盘[1]桌面[2])')
    if temp == '1':
        temp = "C:/Program Files/"
        break
    elif temp == '2':
        temp = path.join(path.expanduser("~"), 'Desktop') + '/'
        break
    else:
        print('输入正确选项!')
with open(file='C:/Users/Public/EnderDOS/EnderDOS_path.txt',mode='w') as s:
    s.write(str(temp+'EnderDOS\\').replace('/','\\'))