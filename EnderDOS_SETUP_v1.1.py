# 导入所需的库
from __future__ import print_function
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from colorama import init,Fore
import os
import requests
import zipfile
from time import sleep,time

# 初始化colorama，用于在命令行中显示颜色
init(autoreset=True)

# 定义版本号
ver = 1.1

# 定义用户输入提示词
Word_1 = WordCompleter(['exit', 'start'], ignore_case=True)
Word_2 = WordCompleter(['1', '2', '3'], ignore_case=True)

# 定义一些提示语句
say_1 = ["Installer for EnderDOS version 1.1","Setup prepares EnderDOS to run on your computer.","""To run the installer, you need to know the following:
 * You have good internet or mobile data (which allows you to connect to the internet)
 * You have the environment Python that the installer runs
 * You have an indicator device
 * You have a keyboard device for typing""","To set up EnderDOS correctly, you should complete the installer.","""\nWhen you are ready, press Enter or enter "start"\n\nExit without completing the setup enter "exit"\n"""]

say_2 = ["You can install EnderDOS on your hard disk, indicating the path to install.","""Recommended Path:
   Install on desktop [1]
   Installed on C drive [2]
Can also be installed on a specified path [3]""","""If you have not completed setting up exit, please enter "Exit"\n\nEnter the serial number of the path you want to install
"""]

# 检查是否已经安装了EnderDOS
def EnderDOSDetect():
    # 如果没有'EnderDOS'目录，就创建一个
    if not os.path.exists('C:/Users/Public/EnderDOS'):
        os.makedirs('C:/Users/Public/EnderDOS')
        return True
    
    # 读取安装信息
    try:
        detect_ver = float(open(file='C:/Users/Public/EnderDOS/EnderDOS_ver.txt',mode='r').read())
        detect_path = open(file='C:/Users/Public/EnderDOS/EnderDOS_path.txt',mode='r').read()
        detect_open_Installation_status = open(file='C:/Users/Public/EnderDOS/EnderDOS_Installation_status.txt',mode='r').read()
        
    except Exception as f:
        if f == 'FileNotFoundError':
            print(Fore.YELLOW + 'Detect Error: FileNotFoundError')
            print(Fore.YELLOW + 'Reinstall for you......')
            return True
        else:
            print(f)
            print(Fore.RED + 'Unknown error[2], contact bilibili_我叫小萌新QWQ')
            print(Fore.RED + 'The configuration file is corrupted')
            print(Fore.CYAN + '* Run the hotfix, and then start Setup again')
            sleep(5)
            return False

    # 判断安装信息
    if detect_open_Installation_status == 'True' and detect_ver < ver:
        print(Fore.GREEN + 'Meets installation conditions !!!')
        return True
    elif detect_open_Installation_status == 'True' and detect_ver >= ver:
        print(Fore.YELLOW + 'You have EnderDOS installed and are up to date !!!')
        print(Fore.CYAN + 'Installation path:' + detect_path)
        return False
    elif detect_open_Installation_status == 'False':
        print(Fore.GREEN + 'Meets installation conditions !!!')
        return True     
    else:
        print(Fore.RED + 'Unknown error[1], contact bilibili_我叫小萌新QWQ')
        print(Fore.RED + 'The configuration file is corrupted')
        print(Fore.CYAN + '* Run the hotfix, and then start Setup again')
        sleep(5)
        return False

# 定义安装程序类
class EnderDOSInstaller:
    # 初始化安装程序
    def __init__(self):
        self.installation_directory = ""  # 设置安装目录

    # 运行安装程序
    def run(self):
        os.system('cls')
        # 打印欢迎信息
        self.print_message(say_1[0]+'\n')
        self.print_message(Fore.CYAN + say_1[1])
        self.print_message(say_1[2])
        self.print_message(Fore.GREEN + say_1[3])
        self.print_message(Fore.CYAN + say_1[4])

        # 等待用户输入
        while True:
            user_input = prompt('Eender Dos SetUp >', history=FileHistory('history.txt'), 
                            auto_suggest=AutoSuggestFromHistory(), 
                            completer=Word_1)
            # 如果用户输入'exit'，则退出程序
            if user_input.strip().lower() == 'exit':
                for i in range(3,0,-1):
                    os.system('cls')
                    self.print_message('The installer has exited safely !')
                    self.print_message('Next......'+str(i))
                    sleep(1)
                quit()
            # 如果用户输入'start'，则开始安装
            elif user_input.strip().lower() == 'start' or user_input.strip().lower() == '':
                break
            else:
                # 如果用户输入的既不是'exit'也不是'start'，则提示用户重新输入
                self.print_message(Fore.RED + 'Spelling error, please check the spelling and try again!')
                sleep(3)
                os.system('cls')
                self.print_message(say_1[0]+'\n')
                self.print_message(Fore.CYAN + say_1[1])
                self.print_message(say_1[2])
                self.print_message(Fore.GREEN + say_1[3])
                self.print_message(Fore.CYAN + say_1[4])

        # 设置安装路径
        self.setpath()

    def dir_size(self,start_path):
        try:
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(start_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp)
            return total_size
        except Exception as e:
            print(Fore.RED + '(dir_size) Unknown error, contact bilibili_我叫小萌新QWQ' + str(e))
            return 0

    # 设置安装路径
    def setpath(self):
        global path
        sleep(0.35)
        os.system('cls')
        self.print_message(Fore.GREEN + say_2[0]+'\n')
        self.print_message(say_2[1]+'\n')
        self.print_message(Fore.CYAN + say_2[2])

        # 等待用户输入
        while True:
            user_input = prompt('Eender Dos SetUp >', history=FileHistory('history.txt'), 
                            auto_suggest=AutoSuggestFromHistory(), 
                            completer=Word_2)
            # 如果用户输入'exit'，则退出程序
            if user_input.strip().lower() == 'exit':
                for i in range(3,0,-1):
                    os.system('cls')
                    self.print_message('The installer has exited safely !')
                    self.print_message('Next......'+str(i))
                    sleep(1)
                quit()
            # 如果用户输入'1'，则将桌面设为安装路径
            elif user_input.strip().lower() == '1':
                path = os.path.join(os.path.expanduser("~"), 'Desktop') + '/'
                os.system('cls')
                break
            # 如果用户输入'2'，则将C盘设为安装路径
            elif user_input.strip().lower() == '2':
                path = "C:/Program Files/"
                os.system('cls')
                break
            # 如果用户输入'3'，则弹出文件选择框让用户选择安装路径 
            elif user_input.strip().lower() == '3':
                self.print_message(Fore.YELLOW + 'This feature is under maintenance!!!')
                sleep(3)
                os.system('cls')
                self.print_message(Fore.GREEN + say_2[0])
                self.print_message(say_2[1]+'\n')
                self.print_message(Fore.CYAN + say_2[2])
            elif user_input.strip().lower() == '':
                self.print_message(Fore.RED + 'Please enter the serial number you want to select')
                sleep(3)
                os.system('cls')
                self.print_message(Fore.GREEN + say_2[0])
                self.print_message(say_2[1]+'\n')
                self.print_message(Fore.CYAN + say_2[2])
            else:
                self.print_message(Fore.RED + 'Spelling error, please check the spelling and try again!')
                sleep(3)
                os.system('cls')
                self.print_message(Fore.GREEN + say_2[0]+'\n')
                self.print_message(say_2[1]+'\n')
                self.print_message(Fore.CYAN + say_2[2])
        
        # 设置安装目录
        self.installation_directory = path

        # 创建安装目录
        self.create_installation_directory()

        # 下载并解压文件
        self.install()

        sleep(1)

        os.system('cls')

        # 安装完成后，打印出安装目录的大小
        self.print_directory_size()

        # 安装完成
        self.print_message(Fore.CYAN + 'Installation path: ' + path.replace('\\','/')+'EnderDOS/')
        self.print_message(Fore.GREEN + "EnderDOS installation complete!")

    # 创建安装目录
    def create_installation_directory(self):
        print(self.installation_directory.replace('\\','/')+'EnderDOS/')
        if not os.path.exists(self.installation_directory.replace('\\','/')+'EnderDOS/'):
            os.makedirs(self.installation_directory.replace('\\','/')+'EnderDOS/')
            self.print_message(Fore.GREEN + "The installation directory was created successfully!")
            sleep(0.5)
        else:
            self.print_message(Fore.YELLOW + "The installation directory already exists")
            sleep(0.5)
    # 进度条模块
    def progressbar(url,path):
        if not os.path.exists(path):   # 看是否有该文件夹，没有则创建文件夹
            os.mkdir(path)
        start = time() #下载开始时间
        response = requests.get(url, stream=True)
        size = 0    #初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(response.headers['content-length'])  # 下载文件总大小
        try:
            if response.status_code == 200:   #判断是否响应成功
                print('Start download,[File size]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
                filepath = path+'\Pikachu.jpg'  #设置图片name，注：必须加上扩展名
                with open(filepath,'wb') as file:   #显示进度条
                    for data in response.iter_content(chunk_size = chunk_size):
                        file.write(data)
                        size +=len(data)
                        print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
            end = time()   #下载结束时间
            print('Download completed!,times: %.2f秒' % (end - start))  #输出下载用时时间
        except:
            print('Error!')

    def Create_configuration_file(self):
        if not os.path.exists('C:/Users/Public/EnderDOS'):
            os.makedirs('C:/Users/Public/EnderDOS')
        with open(file='C:/Users/Public/EnderDOS/EnderDOS_Installation_status.txt',mode='w') as s:
            s.write('True')
        with open(file='C:/Users/Public/EnderDOS/EnderDOS_ver.txt',mode='w') as s:
            s.write(str(ver))
        with open(file='C:/Users/Public/EnderDOS/EnderDOS_path.txt',mode='w') as s:
            s.write(str(path+'EnderDOS\\').replace('/','\\'))

    # 下载并解压文件
    def install(self):
        try:
            self.progressbar('https://github.com/yht-tutong/EnderSystem/releases/download/EnderDos/EnderDosSystem_v.1.2.exe',path.replace('\\','/')+'EnderDOS/EnderDosSystem_v.1.2.exe')
        except:
            print(Fore.GREEN + '也许是github拦截了,正在重试!!!\n手动下载->https://github.com/yht-tutong/EnderSystem/releases/download/EnderDos/EnderDosSystem_v.1.2.exe')
            while True:
                if str(input('您是否已经下载完成并已经移到{}目录中,这不是闹着玩的!(y/n)'.format(str(self.installation_directory)))).lower() == 'y':
                    self.Create_configuration_file()
                    break
                
        

    # 下载文件
    def install_file(self,url,file):
        r = requests.get(url,allow_redirects=True)
        with open(file,'wb') as f:
            f.write(r.content)
            for i in range(3,0,-1):
                os.system('cls')
                self.print_message('Downloading......')
                self.waiting()
                sleep(1)
            os.system('cls')
            self.print_message(Fore.GREEN + "Download file successful!")

    # 解压文件
    def unpack(self,file,outdir):
        try:
            zip = zipfile.ZipFile(file)
            zip.extractall(outdir)
            zip.close()
            os.remove(self.installation_directory + 'EnderDOS/install.zip')
        except Exception as e:
            print(e)
            try:
                os.remove(path.replace('\\','/')+'EnderDOS/file.zip')
            except Exception as a:
                self.print_message(Fore.RED + "Unpack removeError:" + str(a) + '\nUnknown error, contact bilibili_我叫小萌新QWQ')

    # 打印消息
    def print_message(self, message):
        print(message)

    # 打印目录大小
    def print_directory_size(self):
        try:
            total = 0
            with os.scandir(self.installation_directory) as it:
                for entry in it:
                    if entry.is_file():
                        total += entry.stat().st_size
                    elif entry.is_dir():
                        total += self.dir_size(str(str(self.installation_directory).replace('\\','/')+'EnderDOS/'))
            self.print_message(Fore.MAGENTA + "The installation directory size is: " + str(total) + " bytes")
        except Exception as l:
            self.print_message(Fore.RED + "print_directory_size Error:" + str(l) + '\nUnknown error, contact bilibili_我叫小萌新QWQ')

# 主程序
if __name__ == '__main__':
    if EnderDOSDetect():
        sleep(2)
        installer = EnderDOSInstaller()
        installer.run()
    else:
        sleep(30)