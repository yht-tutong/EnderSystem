from os import path,makedirs
from time import sleep

if not path.exists('C:/Users/Public/EnderDOS'):
    makedirs('C:/Users/Public/EnderDOS')

while True:
    temp = input('请确认是否将本文件移到enderdos_system同级目录下(y/n)')
    if temp == 'y':
        temp = (path.abspath('')+'/').replace('\\','/')
        print(temp + 'EnderDosSystem_v.1.2.exe')
        if path.lexists(temp + 'EnderDosSystem_v.1.2.exe'):
            break
        else:
            print('骗人~~~\n请将本文件移到enderdos_system同级目录下')
            sleep(10)
            quit()
    elif temp == 'n':
        print('请将本文件移到enderdos_system同级目录下')
        sleep(10)
        quit()
    else:
        print('输入正确选项!')

with open(file='C:/Users/Public/EnderDOS/EnderDOS_Installation_status.txt',mode='w') as s:
    s.write('True')

with open(file='C:/Users/Public/EnderDOS/EnderDOS_ver.txt',mode='w') as s:
    s.write('1.2')

with open(file='C:/Users/Public/EnderDOS/EnderDOS_path.txt',mode='w') as s:
    s.write(str(temp+'EnderDOS\\').replace('/','\\'))

print('修改成功')