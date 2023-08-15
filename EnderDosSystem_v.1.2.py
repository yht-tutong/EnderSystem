from __future__ import print_function
from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion.word_completer import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style as PTKStyle

from json import loads, dumps, load, dump
from hashlib import sha256
from colorama import Fore, Style, init
from time import sleep, localtime, strftime, time
from shutil import copy
from os import system, path, makedirs, listdir, remove
from re import match, compile
from requests import get
from webbrowser import open as webopen
from datetime import datetime

class EnderDos:
    def __init__(self): 
        self.command_status = {}
        self.command_completer = WordCompleter(['exit','help','register','login','download','calc','browser','clock','calendar','stopwatch','timer','notepad','settings','quit','cls','about'], ignore_case=True)
        self.enderdos_file_directory = ''
        self.urse = 'admin'

    def command_header(self,user,header):
        self.style_dict = PTKStyle.from_dict({'': '#FFFFFF','user': '#FF6347 bold','connectors_one': '#FF6347 bold','header': '#FF6347 bold','connectors_two': '#FFFFFF bold','input_header_one': '#00BFFF bold','input_header_two': '#FFFFFF',})
        self.message = [('class:user', user), ('class:connectors_one', '@'), ('class:header', header), ('class:connectors_two', ':'), ('class:input_header_one', '~'), ('class:input_header_two', '# '),]
        self.session = PromptSession(self.message, completer=self.command_completer, history=FileHistory('history.txt'), auto_suggest=AutoSuggestFromHistory(), style=self.style_dict)

    def clear_screen(self):
        system('cls')

    def enderdos_quit(self,message,time=3,mode=0):
        # 退出函数 message->信息 time->倒计时
        try:
            if mode == 0:
                for countdown in range(time,0,-1):
                    self.clear_screen()
                    print(Style.BRIGHT + Fore.RED + message)
                    print(Style.BRIGHT + Fore.CYAN + '请检查是否正确安装了环境!')
                    print(Style.BRIGHT + Fore.YELLOW + '欢迎您的下次使用!')
                    print(Style.BRIGHT + Fore.WHITE + '\n正在退出... ' + str(countdown))
                    sleep(1)
                sleep(0.5)
                quit()
            else:
                for countdown in range(time,0,-1):
                    self.clear_screen()
                    print(Style.BRIGHT + Fore.CYAN + message)
                    print(Style.BRIGHT + Fore.WHITE + '\n正在退出... ' + str(countdown))
                    sleep(1)
                sleep(0.5)
                quit()
        except Exception as e:
            print('退出失败,也许是环境不符合运行要求。。。')
            quit()

    def detect_config(self,cofing,cofing_file = 'c'):
        try:
            if cofing_file == 'c':
                cofing_file = 'C:/Users/Public/EnderDOS/' + cofing
            elif cofing_file == 'r':
                cofing_file = self.enderdos_file_directory + cofing
            with open(file=cofing_file,mode='r') as path:
                temp = path.read()
                return temp
        except Exception as e:
            self.enderdos_quit('配置文件{}损坏!!!'.format(cofing))

    def modify_urse(self,urse):
        self.urse = urse
        print(Style.BRIGHT + Fore.GREEN + '用户修改成功!')

    def create_folder(self,folder_path,name):
        try:
            if not path.exists(self.enderdos_file_directory + folder_path.replace('\\','/')):
                makedirs(self.enderdos_file_directory + folder_path.replace('\\','/'))
                print(Style.BRIGHT + Fore.GREEN + "{}文件夹创建成功!".format(name))
            else:
                print(Style.BRIGHT + Fore.YELLOW + "{}文件夹已经存在!".format(name))
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + "文件夹创建失败!")

    def flush_WordCompleter(self,mode,word): 
        # 刷新单词补全列表 mode = a -> 添加 r -> 删除 c -> 刷新
        try:
            if mode == 'a':
                self.command_completer.words.append(word)
            elif mode == 'r':
                self.command_completer.words.remove(word)
            elif mode == 'c':
                self.command_completer.words.clear()
        except Exception as e:
            self.enderdos_quit('自动补全修改失败!!!')

    def modify_config(self,cofing,content,modify_mode = 'w',cofing_file = 'c'):
        try:
            if cofing_file == 'c':
                cofing_file = 'C:/Users/Public/EnderDOS/' + cofing
            elif cofing_file == 'r':
                cofing_file = self.enderdos_file_directory + cofing
            if not path.exists(cofing_file):
                modify_mode = 'w'
                print('配置文件{}不存在,正在创建'.format(cofing))
            with open(file=cofing_file,mode=modify_mode) as file:
                file.write(content)
        except Exception as e:
            self.enderdos_quit(str(e)+'\n配置文件{}修改失败!!!'.format(cofing))

    def enderdos_input(self,urse,header,mode=0): # mode = 0 -> 输入命令模式 1 -> 计算器模式 2 -> 输入内容模式 3 -> 输入文件名模式
        while True:
            try:
                # 输入
                self.command_header(urse,header)
                input_command = self.session.prompt()

                if input_command == '':
                    print(Fore.RED + Style.BRIGHT + '请输入内容,如想换行请尝试输入\'空格\'')
                    continue
                
                elif mode == 4:
                    if not match(r'^[a-zA-Z0-9_.-/:]*$',input_command):
                        print(Fore.RED + Style.BRIGHT + '请勿输入特殊字符,输入范围在 a-z A-Z 0-9 _ . - / :')
                        continue
                    else:
                        return input_command
                    
                elif mode == 5:
                    if not match(r'^[0-9]*$',input_command):
                        print(Fore.RED + Style.BRIGHT + '请勿输入特殊字符,输入范围在0-9')
                        continue
                    else:
                        return input_command
                    
                else:   
                    if mode == 0:
                        # 设置检测
                        pattern = compile(r'^[A-Za-z0-9 ]+$')

                        # 检测特殊字符
                        if pattern.match(input_command):
                            temp = input_command.split(' ')
                            if mode == 0:
                                if len(temp) == 1:
                                    return temp[0]
                                else:
                                    return [temp[0],temp[1:]]
                        else:
                            print(Fore.YELLOW + Style.BRIGHT + '请勿输入特殊字符,输入范围在 a-z A-Z 0-9 空格')

                    elif mode == 1:
                        # 设置检测
                        pattern = compile(r'^[0-9/*-+.=!%()><exit]+$')
                        if pattern.match(input_command):
                            return input_command
                        else:
                            print(Fore.YELLOW + Style.BRIGHT + '请勿输入特殊字符,请输入表达式,或输入exit')

                    elif mode == 2:
                        pattern = compile(r'^[\u4e00-\u9fa5A-Za-z0-9_.-]+$')
                        if pattern.match(input_command):
                            return input_command
                        else:
                            print(Fore.YELLOW + Style.BRIGHT + '请勿输入特殊字符,输入范围在 a-z A-Z 0-9 汉字 空格 _ . -')

                    elif mode == 3:
                        pattern = compile(r'^[a-zA-Z0-9_.-]*$')
                        if pattern.match(input_command):
                            return input_command
                        else:
                            print(Fore.YELLOW + Style.BRIGHT + '请勿输入特殊字符,输入范围在 a-z A-Z 0-9 _ . -')

            except Exception as e:
                print(Fore.RED + Style.BRIGHT + '错误的输入！')

    def wirte_log(self,log,content,mode,e=''):
        if mode == 'i':
            mode = 'INFO'
        elif mode == 'e':
            mode = 'ERROR'
        elif mode == 'w':
            mode = 'WARNING'
        if e != '':
            e = '-> ' + str(e)
        self.modify_config(log + '/history.txt',strftime("%Y-%m-%d %H:%M:%S", localtime()) + ' ' + mode + ': ' + content + ' ' + e + '\n','a','r')
    
    def about(self):
        print(Fore.RED + Style.BRIGHT + '  _____               _                   ____                \n | ____|  _ __     __| |   ___   _ __    |  _ \\    ___    ___ \n |  _|   | \'_ \\   / _` |  / _ \\ | \'__|   | | | |  / _ \\  / __|\n | |___  | | | | | (_| | |  __/ | |      | |_| | | (_) | \\__ \\\n |_____| |_| |_|  \\__,_|  \\___| |_|      |____/   \\___/  |___/\n')
        print(Fore.CYAN + Style.BRIGHT + '末影dos(EnderDos)')
        print(Fore.WHITE + Style.BRIGHT + '作者:我叫小萌新QWQ\n版权:我叫小萌新QWQ 2023(C)')
        print(Fore.RED + Style.BRIGHT + '闲聊群群号:172225521(Q)')
    
    def help(self):
        print(Fore.GREEN + Style.BRIGHT + """欢迎使用 EnderDos 本产品由 我叫小萌新QWQ 一人单独制作
=====================
帮助列表：
help       打开本页面

register   注册
login      登录
download   下载文件
calc       计算器
browser    浏览器
clock      查看时间
calendar   查看日期
stopwatch  秒表
timer      计时器

notepad    记事本
settings   设置

about      关于
cls        清空屏幕
quit       退出
=====================""")

    def main(self):
        global ender_dos, note_pad, timeanddate, apply
        # 清屏
        self.clear_screen()
        
        # 欢迎语
        print(Fore.RED + Style.BRIGHT + '  _____               _                   ____                \n | ____|  _ __     __| |   ___   _ __    |  _ \\    ___    ___ \n |  _|   | \'_ \\   / _` |  / _ \\ | \'__|   | | | |  / _ \\  / __|\n | |___  | | | | | (_| | |  __/ | |      | |_| | | (_) | \\__ \\\n |_____| |_| |_|  \\__,_|  \\___| |_|      |____/   \\___/  |___/\n')
        print(Fore.CYAN + Style.BRIGHT + '欢迎使用末影dos(EnderDos)')
        print(Fore.WHITE + Style.BRIGHT + '作者:我叫小萌新QWQ\n版权:我叫小萌新QWQ 2023(C)')
        print(Fore.RED + Style.BRIGHT + '闲聊群群号:172225521(Q)')

        # 设置命令状态
        self.command_status = {}

        # 初始化colorama
        init(autoreset=True)

        # 检测注册信息
        user_manager = UserManager()
        user_manager.detect_users_config()

        # 读取安装路径
        self.enderdos_file_directory = self.detect_config('EnderDOS_path.txt').replace('\\','/') + '/'

        # 创建运行目录
        self.create_folder('enderdos','运行')
        
        # 更改运行目录
        self.enderdos_file_directory = self.enderdos_file_directory + self.urse + '/enderdos/'

        # 初始化Apply
        apply = Apply()
        apply.main()
        
        # 初始化时间
        timeanddate = TimeAndDate()
        
        # 初始化记事本
        note_pad = NotePad()
        note_pad.main()

        # 提示
        print(Style.BRIGHT + Fore.GREEN + '这个项目十分的不完善,接下来我会制作图形版本的EnerDos,尽请期待吧!!!')

        # 欢迎语
        print(Style.BRIGHT + Fore.CYAN + '\n键入\'help\'获取帮助')
        # 主循环
        while True:
            command = self.enderdos_input(self.urse, 'enderdos',3)
            if command == 'help':
                self.help()
            elif command == 'register':
                user_manager.register()
            elif command == 'login':
                user_manager.login()
            elif command == 'download':
                apply.download()
            elif command == 'browser':
                apply.browser()
            elif command == 'clock':
                timeanddate.clock()
            elif command == 'calendar':
                timeanddate.calendar()
            elif command == 'stopwatch':
                timeanddate.stopwatch()
            elif command == 'timer':
                timeanddate.timer()
            elif command == 'notepad':
                note_pad.pad()
            elif command == 'settings':
                apply.settings()
            elif command == 'about':
                self.about()
            elif command == 'cls':
                self.clear_screen()
            elif command == 'calc':
                apply.calculator()
            elif command == 'quit':
                self.enderdos_quit('欢迎您的下次使用!',3,1)
            else:
                print(Style.BRIGHT + Fore.YELLOW + '未知命令,请输入help查看帮助!')

class UserManager:
    def __init__(self):
        self.users = {}
        self.read_user_files()
    
    def read_user_files(self):
        if not path.exists('C:/Users/Public/EnderDOS/EnderDOS_user.txt'):
            with open('C:/Users/Public/EnderDOS/EnderDOS_user.txt, 'w') as f:
                pass
        temp = ender_dos.detect_config('EnderDOS_user.txt')
        try:
            if temp == '':
                self.users = {}
            else:
                self.users = loads(temp)
        except Exception as e:
            self.users = {}

    def detect_users_config(self):
        self.read_user_files()

        if self.users == '' or self.users == {}:
            print(Style.BRIGHT + Fore.YELLOW + '\n没有已注册用户!')
            self.register()
        else:
            print(Style.BRIGHT + Fore.GREEN + '\n注册信息存在!')
            self.login()

    def register(self):
        self.read_user_files()

        print(Style.BRIGHT + Fore.CYAN + '欢迎注册 enderdos')
        
        while True:
            print(Style.BRIGHT + Fore.WHITE + '请输入用户名')
            username = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos register',3)
            if username in self.users:
                print(Style.BRIGHT + Fore.RED + '用户名已被占用!!!')
            else:
                break
        
        while True:
            print(Style.BRIGHT + Fore.WHITE + '请输入密码:')
            password1 = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos register',3)
            print(Style.BRIGHT + Fore.WHITE + '请再次输入密码:')
            password2 = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos register',3)
            if password1 != password2:
                print(Style.BRIGHT + Fore.RED + '两次输入密码不一致!!!')
            else:
                break
            
        password_hash = self._hash_password(password1)
        self.users[username] = password_hash 

        print(Style.BRIGHT + Fore.CYAN + '注册成功!!!')
        
        users_json = dumps(self.users)
        
        ender_dos.modify_config('EnderDOS_user.txt',str(users_json))
        self.login()
        
    def login(self):
        self.read_user_files()
        
        while True:
            print(Style.BRIGHT + Fore.WHITE + '请选择模式 login 登录 register 注册 exit 退出程序')
            temp = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos login',3)
            if temp == 'login':
                print(Style.BRIGHT + Fore.CYAN + '欢迎登录 enderdos')
                while True:
                    print(Style.BRIGHT + Fore.WHITE + '请输入用户名')
                    username = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos login',3)
                    if username not in self.users:
                        print(Style.BRIGHT + Fore.RED + '用户名不存在!')
                    else:
                        break
                

                while True:
                    print(Style.BRIGHT + Fore.WHITE + '请输入密码')
                    password = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos login',3)
                    
                    if self._hash_password(password) != self.users[username]:
                        print(Style.BRIGHT + Fore.RED + '密码错误')
                    else:
                        print(Style.BRIGHT + Fore.GREEN + '登录成功!')
                        ender_dos.modify_urse(username)
                        break
                break
            
            if temp == 'register':
                self.register()
                break
            
            if temp == 'exit':
                ender_dos.enderdos_quit('欢迎您的下次使用!',mode=1)
                break
        
    def change_password(self):
        self.read_user_files()

        while True:
            print(Style.BRIGHT + Fore.WHITE + '请输入用户名:')
            username = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change password',3)
            print(Style.BRIGHT + Fore.WHITE + '请输入旧密码:')
            old_password = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change password',3)
            print(Style.BRIGHT + Fore.WHITE + '请输入新密码:')
            new_password = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change password',3)
            
            if username not in self.users:
                print(Style.BRIGHT + Fore.RED + '用户名不存在')
            else:
                if self._hash_password(old_password) != self.users[username]:
                    print(Style.BRIGHT + Fore.RED + '旧密码错误')
                else:
                    self.users[username] = self._hash_password(new_password)
                    users_json = dumps(self.users)
                    ender_dos.modify_config('EnderDOS_user.txt',str(users_json))
                    print(Style.BRIGHT + Fore.GREEN + '密码修改成功!')
                    break

        ender_dos.main()
        
    def change_username(self):
        self.read_user_files()

        while True:
            print(Style.BRIGHT + Fore.WHITE + '请输入要修改的用户名')
            username = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change username',3)
            print(Style.BRIGHT + Fore.WHITE + '请输入密码')
            password = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change username',3)
            print(Style.BRIGHT + Fore.WHITE + '请输入新用户名')
            new_username = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos change username',3)
        
            if username not in self.users:
                print(Style.BRIGHT + Fore.RED + '要修改的用户名不存在')
            else:
                if new_username in self.users:
                    print(Style.BRIGHT + Fore.RED + '新用户名已存在')
                else:
                    if self._hash_password(password) != self.users[username]:
                        print(Style.BRIGHT + Fore.RED + '密码错误')
                    else:
                        self.users.pop(username)
                        self.users[new_username] = password
                        print(Style.BRIGHT + Fore.RED + '用户名修改成功!')
                        users_json = dumps(self.users)
                        ender_dos.modify_config('EnderDOS_user.txt',str(users_json))
                        break
        
        ender_dos.main()

        
    def _hash_password(self, password):
        try:
            return sha256(password.encode('utf8')).hexdigest()  
        except Exception as e:
            ender_dos.enderdos_quit('加密失败！！！')

class Apply():
    def __init__(self): 
        pass

    def main(self):
        self.enderdos_file_directory = ender_dos.enderdos_file_directory      

    def download(self): 
        try:
            ender_dos.create_folder('download','下载')

            print(Style.BRIGHT + Fore.WHITE + '请输入要下载的文件URL')
            url = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos download',4)

            print(Style.BRIGHT + Fore.WHITE + '请输入保存的文件名(要加后缀，如 .html .txt .zip等)')
            filename = ender_dos.enderdos_input(ender_dos.urse, 'EnderDos download',3)

            response = get(url)
            with open(self.enderdos_file_directory + 'download/' + filename, 'wb') as f:
                f.write(response.content)

            print(Style.BRIGHT + Fore.GREEN + '文件下载成功' + Style.RESET_ALL)
            ender_dos.wirte_log('download','文件下载成功!','i')
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '文件下载失败')
            ender_dos.wirte_log('download','文件下载失败!'+ ' ' + str(url)  + ' ' + filename,'e',e)

    def calculator(self): 
        # 创建运行目录
        ender_dos.create_folder('calculator','计算器')

        print(Style.BRIGHT + Fore.WHITE + '请输入你要计算的表达式，输入"exit"来退出计算器')

        while True:
            expression = ender_dos.enderdos_input(ender_dos.urse,'Calculator',1)
            if expression.lower() == 'exit':
                print(Style.BRIGHT + Fore.WHITE + '已经退出计算器!')
                ender_dos.wirte_log('calculator','退出计算器','i')
                break
            try:
                log = eval(expression)
                print(Style.BRIGHT + Fore.WHITE + str(log))
                ender_dos.wirte_log('calculator','计算 ' + str(expression) + '=' + str(log),'i')
            except Exception as e:
                print(Style.BRIGHT + Fore.RED + '错误的表达式: ' + str(e) + Style.RESET_ALL)
                ender_dos.wirte_log('calculator','错误的表达式' + str(expression),'e',e)

    def settings(self): 
        while True: 
            print(Fore.WHITE + Style.BRIGHT + '1. 更改用户名 (测试,不会报错,别用)') 
            print(Fore.WHITE + Style.BRIGHT + '2. 更改密码') 
            print(Fore.WHITE + Style.BRIGHT + '3. 更改时间') 
            print(Fore.WHITE + Style.BRIGHT + '4. 更改日期') 
            print(Fore.WHITE + Style.BRIGHT + '0. 退出设置') 
            print(Fore.WHITE + Style.BRIGHT + '请选择操作') 
            choice = ender_dos.enderdos_input(ender_dos.urse,'settings',5)
            if choice == '1': 
                UserManager().change_username()
            elif choice == '2': 
                UserManager().change_password()
            elif choice == '3': 
                timeanddate.set_clock()
            elif choice == '4': 
                timeanddate.set_calendar()
            elif choice == '0': 
                break 
            else: 
                print(Fore.RED + '无效的选项' + Style.RESET_ALL) 

    def browser(self): 
        ender_dos.create_folder('browser','浏览器')
        print(Style.BRIGHT + Fore.WHITE + '请输入正确的网址')
        url = ender_dos.enderdos_input(ender_dos.urse,'browser',4)
        try:
            webopen(url)
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '打开浏览器失败' + str(e) + Style.RESET_ALL)
            ender_dos.wirte_log('calculator','打开浏览器失败' + str(url),'e',e)

class TimeAndDate: 
    def clock(self): 
        current_time = datetime.now().time() 
        print(Style.BRIGHT + Fore.GREEN + '当前时间是：' + str(current_time) + Style.RESET_ALL) 
 
    def set_clock(self): 
        print(Style.BRIGHT + Fore.WHITE + '请输入时')
        hour = int(ender_dos.enderdos_input(ender_dos.urse,'set clock',5))
        print(Style.BRIGHT + Fore.WHITE + '请输入分')
        minute = int(ender_dos.enderdos_input(ender_dos.urse,'set clock',5))
        print(Style.BRIGHT + Fore.WHITE + '请输入秒')
        second = int(ender_dos.enderdos_input(ender_dos.urse,'set clock',5))
        current_time = datetime.now() 
        new_time = current_time.replace(hour=hour, minute=minute, second=second) 
        print(Style.BRIGHT + Fore.YELLOW + '时间已更改为：' + str(new_time.time()) + Style.RESET_ALL) 
 
    def calendar(self): 
        current_date = datetime.now().date() 
        print(Style.BRIGHT + Fore.GREEN + '当前日期是：' + str(current_date) + Style.RESET_ALL) 
 
    def set_calendar(self): 
        print(Style.BRIGHT + Fore.WHITE + '请输入年')
        year = int(ender_dos.enderdos_input(ender_dos.urse,'set calendar',5))
        print(Style.BRIGHT + Fore.WHITE + '请输入月')
        month = int(ender_dos.enderdos_input(ender_dos.urse,'set calendar',5))
        print(Style.BRIGHT + Fore.WHITE + '请输入日')
        day = int(ender_dos.enderdos_input(ender_dos.urse,'set calendar',5))
        current_date = datetime.now() 
        new_date = current_date.replace(year=year, month=month, day=day) 
        print(Style.BRIGHT + Fore.YELLOW + '日期已更改为：' + str(new_date.date()) + Style.RESET_ALL) 
 
    def stopwatch(self): 
        input(Style.BRIGHT + Fore.CYAN + "按回车键开始秒表..." + Style.RESET_ALL) 
        start_time = time() 
        input(Style.BRIGHT + Fore.CYAN + "按回车键停止秒表..." + Style.RESET_ALL) 
        end_time = time() 
        elapsed_time = end_time - start_time 
        print(Style.BRIGHT + Fore.GREEN + '经过的时间：' + str(elapsed_time) + ' 秒' + Style.RESET_ALL) 
 
    def timer(self): 
        print(Style.BRIGHT + Fore.CYAN + '请输入倒计时时长(秒):' + Style.RESET_ALL)
        duration = int(ender_dos.enderdos_input(ender_dos.urse,'settings',5))
        print(Style.BRIGHT + Fore.CYAN + '计时器已开始，持续时间为 ' + str(duration) + ' 秒。' + Style.RESET_ALL) 
        sleep(duration) 
        print(Style.BRIGHT + Fore.GREEN + '计时器已完成。' + Style.RESET_ALL) 

class NotePad:
    def __init__(self):
        # 创建运行目录
        ender_dos.create_folder('notepad','记事本')

    def main(self):
        self.notes = {}
        self.load()

    def pad(self):
        while True:
            print(Fore.WHITE + Style.BRIGHT + '1. 新建笔记')
            print(Fore.WHITE + Style.BRIGHT + '2. 查看笔记') 
            print(Fore.WHITE + Style.BRIGHT + '3. 删除笔记')
            print(Fore.WHITE + Style.BRIGHT + '0. 返回上级菜单')
            print(Fore.WHITE + Style.BRIGHT + '请选择操作')
            choice = ender_dos.enderdos_input(ender_dos.urse,'notepad',5)
            if choice == '1':
                self.add_note()
            elif choice == '2':
                self.show_notes()
            elif choice == '3':
                self.delete_note()
            elif choice == '0':
                break
            else:
                print(Fore.RED + '无效的选项' + Style.RESET_ALL)

    def add_note(self):
        self.save()
        self.load()
        print(Style.BRIGHT + Fore.CYAN + "\n欢迎来到创建记事本向导!")

        while True:
            print(Style.BRIGHT + Fore.WHITE + "请输入文件名称")
            note_file_name = ender_dos.enderdos_input(ender_dos.urse,'Note input',3)

            if len(note_file_name) >= 19:
                print(Style.BRIGHT + Fore.YELLOW + "文件名太长,请控制在17个字符以内")
                continue
            elif note_file_name in self.notes:
                print(Style.BRIGHT + Fore.YELLOW + "文件名已存在,是否覆盖(y)或是再次输入(n)")
                overwrite = ender_dos.enderdos_input(ender_dos.urse,'Note input',3).lower()
                if overwrite == "y":
                    break
                elif overwrite == "n":
                    continue
                else:
                    print(Style.BRIGHT + Fore.RED + "请输入y或n")
                    continue
            else:
                break

        print(Style.BRIGHT + Fore.WHITE + "请输入记事内容,输入\'exit\'退出")

        contents = []

        try:
            while True:
                line = ender_dos.enderdos_input(ender_dos.urse,'Note input',2)

                if line.lower() == "exit":
                    print(Style.BRIGHT + Fore.WHITE + "正在保存记事本")
                    break
                    
                contents.append(line)
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '记事本写入失败')
        
        try:
            self.notes[note_file_name] = "\n".join(contents)
            self.notes[note_file_name + "_time"] = strftime("%Y-%m-%d %H:%M:%S", localtime())
            
            self.save()

            print(Style.BRIGHT + Fore.GREEN + "记事保存成功!")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '记事本保存失败')

    def show_notes(self):
        self.load()
        try:
            if len(self.notes.keys()) == 0:
                print(Style.BRIGHT + Fore.RED + '没有已经记录记事本')
                return
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '未知错误!')
        else:
            try:
                print(Style.BRIGHT + Fore.WHITE + "请输入要查看的记事名称 - {}".format(str(note_key))) 
                input = str(ender_dos.enderdos_input(ender_dos.urse,'Note show',3))
                if input not in note_key:
                    print(Style.BRIGHT + Fore.YELLOW + "记事本不存在")
                else:
                    print(Style.BRIGHT + Fore.CYAN + '\n' + '您的记事'.center(16," "))
                    print(Style.BRIGHT + Fore.WHITE + (' ' + input + ' ').center(20,"-"))
                    print(Style.BRIGHT + Fore.WHITE + self.notes[input + "_time"])
                    print(Style.BRIGHT + Fore.WHITE + self.notes[input])
                    print(Style.BRIGHT + Fore.WHITE + "-" * 20)
            except Exception as e:
                print(Style.BRIGHT + Fore.RED + '展示失败!')

    def load(self):
        global note_key
        try:
            # 加载文件
            with open("C:/Users/Public/EnderDOS/notes.json") as f:
                self.notes = load(f)
                print(Style.BRIGHT + Fore.GREEN + "记事本文件加载成功!")

            # 加载键
            temp = []
            for key in self.notes:
                temp.append(key)
            
            # 整理键
            num = 0
            note_key = []

            for key in temp:
                if num % 2 == 0:
                    note_key.append(key)
                num += 1
            
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '记事本加载失败')

    def save(self):
        try:
            with open("C:/Users/Public/EnderDOS/notes.json", "w") as f:
                dump(self.notes, f)
                print(Style.BRIGHT + Fore.GREEN + "记事本保存成功!")
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '记事本保存失败')

    def delete_note(self):
        try:
            if len(self.notes) == 0:
                print(Style.BRIGHT + Fore.RED + '没有已经记录记事本')
                return
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '未知错误!')
        else:
            try:
                print(Style.BRIGHT + Fore.WHITE + "请输入要删除的记事名称 - {}".format(str(note_key))) 
                input = str(ender_dos.enderdos_input(ender_dos.urse,'Note delete',3))
                if input not in note_key:
                    print(Style.BRIGHT + Fore.YELLOW + "记事本不存在")
                else:
                    self.notes.pop(input)
                    self.notes.pop(input + '_time')
                    print(Style.BRIGHT + Fore.BLUE + "删除成功!")
            except Exception as e:
                print(Style.BRIGHT + Fore.RED + '删除失败!')

class file_manager:
    def __init__(self):
        self.enderdos_file_directory = ender_dos.enderdos_file_directory
        self.file_manager_file = self.enderdos_file_directory + 'file_manager/'
        ender_dos.create_folder('file_manager','文件资源管理器')
    
    def main(self):
        while True:
            print(Style.BRIGHT + Fore.CYAN + '文件资源管理器' + Style.RESET_ALL)
            print(Fore.WHITE + Style.BRIGHT + '1. 浏览文件')
            print(Fore.WHITE + Style.BRIGHT + '2. 创建文件')
            print(Fore.WHITE + Style.BRIGHT + '3. 删除文件')
            print(Fore.WHITE + Style.BRIGHT + '4. 复制文件')
            print(Fore.WHITE + Style.BRIGHT + '5. 查看文件')
            print(Fore.WHITE + Style.BRIGHT + '0. 退出文件资源管理器')
            print(Fore.WHITE + Style.BRIGHT + '请选择操作!')
            choice = ender_dos.enderdos_input(ender_dos.urse,'file manager browse',5)
            if choice == '1':
                self.browse_files()
            elif choice == '2':
                self.create_file()
            elif choice == '3':
                self.delete_file()
            elif choice == '4':
                self.copy_file()
            elif choice == '5':
                self.view_file()
            elif choice == '0':
                break
            else:
                print(Fore.RED + '无效的选项' + Style.RESET_ALL)
        
    def browse_files(self):
        try:
            ender_dos.wirte_log('file_manager','打开浏览目录','i')
            print(Fore.WHITE + Style.BRIGHT + '请输入要浏览的目录路径')
            path = ender_dos.enderdos_input(ender_dos.urse,'file manager browse',4)
            path = self.file_manager_file + path
            if path.exists(path):
                print(listdir(path))
            else:
                print(Style.BRIGHT + Fore.RED + '路径不存在' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','路径不存在','w')
        except Exception as e:      
            print(Style.BRIGHT + Fore.RED + '浏览目录失败')
            ender_dos.wirte_log('file_manager','浏览目录失败','e',e)

    def create_file(self):
        try:
            ender_dos.wirte_log('file_manager','打开文件创建','i')
            print(Fore.WHITE + Style.BRIGHT + '请输入文件路径(如 test/test.txt)')
            path = ender_dos.enderdos_input(ender_dos.urse,'file manager create',4)
            path = self.file_manager_file + path
            if not path.exists(path):
                with open(path, 'w') as f:
                    print(Fore.GREEN + '文件创建成功' + Style.RESET_ALL)
                    ender_dos.wirte_log('file_manager','文件创建成功','i')
                if input('是否立即编辑文件?(y/n)').lower() == 'y':
                    print(Fore.WHITE + Style.BRIGHT + '请输入文件内容')
                    content = ender_dos.enderdos_input(ender_dos.urse,'file manager create',4)
                    with open(path, 'w') as f:
                        f.write(content)
                        ender_dos.wirte_log('file_manager','文件编辑成功','i')
            else:
                print(Style.BRIGHT + Fore.YELLOW + '文件已存在' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','文件已存在' + path,'w')
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '文件创建失败')
            ender_dos.wirte_log('file_manager','文件创建失败' + path,'w')

    def delete_file(self):
        try:
            ender_dos.wirte_log('file_manager','打开删除文件','i')
            print(Fore.WHITE + Style.BRIGHT + '请输入要删除的文件路径(如 test/test.txt)')
            path = ender_dos.enderdos_input(ender_dos.urse,'file manager delete',4)
            path = self.file_manager_file + path
            if path.exists(path):
                print('确定要删除该文件吗?删除后不可恢复!(y/n)')
                confirm = ender_dos.enderdos_input(ender_dos.urse,'file manager delete',4)
                if confirm == 'y':
                    remove(path)
                    print(Style.BRIGHT + Fore.GREEN + '文件删除成功' + Style.RESET_ALL)
                    ender_dos.wirte_log('file_manager','文件删除成功','i')
                else:
                    print(Style.BRIGHT + Fore.BLUE + '操作已取消' + Style.RESET_ALL)
                    ender_dos.wirte_log('file_manager','操作已取消','i')
            else:
                print(Style.BRIGHT + Fore.RED + '文件不存在' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','文件不存在','w')
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '发生错误' + Style.RESET_ALL)
            ender_dos.wirte_log('file_manager','删除文件发生错误','e',e)

    def copy_file(self):
        try:
            ender_dos.wirte_log('file_manager','打开复制文件','i')
            print(Fore.WHITE + Style.BRIGHT + '请输入源文件路径')
            src = ender_dos.enderdos_input(ender_dos.urse,'file manager copy',4)
            src = self.file_manager_file + src
            print(Fore.WHITE + Style.BRIGHT + '请输入目标文件路径')
            dst = ender_dos.enderdos_input(ender_dos.urse,'file manager copy',4)
            dst = self.file_manager_file + dst
            if path.exists(src):
                copy(src, dst)
                print(Fore.GREEN + '文件复制成功' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','文件复制成功','i')
            else:
                print(Fore.RED + '源文件不存在' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','源文件不存在','w')
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + '复制文件失败')
            ender_dos.wirte_log('file_manager','复制文件失败','e',e)

    def view_file(self):
        try:
            print(Fore.WHITE + Style.BRIGHT + '请输入文件路径')
            path = ender_dos.enderdos_input(ender_dos.urse,'file manager copy',4)
            path = self.file_manager_file + path
            if path.exists(path):
                with open(path, 'r') as f:
                    print(f.read())
                ender_dos.wirte_log('file_manager','查看' + path,'i')
            else:
                print(Style.BRIGHT + Fore.RED + '文件不存在' + Style.RESET_ALL)
                ender_dos.wirte_log('file_manager','查看' + path + '失败','w')
        except Exception as e:      
            print(Style.BRIGHT + Fore.RED + '查看文件失败')
            ender_dos.wirte_log('file_manager','查看文件失败','e',e)
    
if __name__ == '__main__': 
    ender_dos = EnderDos()
    ender_dos.main()
