import ctypes
import sys
import wx
from wx import adv

# 用于创建托盘图标
import pystray
from PIL import Image
from pystray import MenuItem

# 用于调用cmd
import subprocess


automatic = False
empty_path = 6


'''
def RAMMap_run():
	cmd = 'RAMMap-64bit -Ew'
	res = subprocess.Popen(cmd)
	output_str = res.read()

	print(output_str)
'''


# 启动和关闭自动释放内存的文件
def Automatic():
	global automatic, i
	if automatic == True:
		automatic = False
		subprocess.Popen('taskkill /F /IM _Ea_.exe',shell=True) #强行终止进程
		#托盘气泡提示
		adv.NotificationMessage("RAMMap-64bit", message="已结束释放内存\n Automatic turn off").Show()
	elif automatic == False:
		automatic = True
		subprocess.Popen("start _Ea_.exe",shell=True)#启动（也可以用.py）
		# adv.NotificationMessage("").SetIcon(wx.Icon("ASNO.png")).Show()
		#托盘气泡提示
		adv.NotificationMessage("RAMMap-64bit", message="正在自动释放内存\n Automatic have already turn on").Show()


def Empty(path):
	# cmd调用RAMMap外部接口
	if path == 0:
		# 这里一定要阻塞运行，否则RAMMAP会报错
		subprocess.Popen("RAMMap-64bit -Ew",shell=True).wait()
		subprocess.Popen("RAMMap-64bit -Es",shell=True).wait()
		subprocess.Popen("RAMMap-64bit -Em",shell=True).wait()
		subprocess.Popen("RAMMap-64bit -Et",shell=True).wait()
		subprocess.Popen("RAMMap-64bit -E0",shell=True).wait()
	elif path == 1:
		subprocess.Popen("RAMMap-64bit -Ew",shell=True)
	elif path == 2:
		subprocess.Popen("RAMMap-64bit -Es",shell=True)
	elif path == 3:
		subprocess.Popen("RAMMap-64bit -Em",shell=True)
	elif path == 4:
		subprocess.Popen("RAMMap-64bit -Et",shell=True)
	elif path == 5:
		subprocess.Popen("RAMMap-64bit -E0",shell=True)


# 判断点击的选项
def click_menu(icon, item):
	global empty_path

	print("点击了", item)
	if str(item) == 'Empty automatic':
		Automatic()
	elif str(item) == 'Empty all':
		empty_path = 0
	elif str(item) == 'Empty Ew':
		empty_path = 1
	elif str(item) == 'Empty Es':
		empty_path = 2
	elif str(item) == 'Empty Em':
		empty_path = 3
	elif str(item) == 'Empty Et':
		empty_path = 4
	elif str(item) == 'Empty E0':
		empty_path = 5

	Empty(empty_path)
	empty_path = 6


# 关闭程序
def on_exit(icon, item):
	icon.stop()


def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False


app = wx.App(0)
# flag = adv.NotificationMessage.SetFlags("ASNO.png")

# 以管理员运行
if is_admin():
	# 创建托盘
	menu = (MenuItem(text='Empty all', action=click_menu),
	MenuItem(text='Empty Ew', action=click_menu),
	MenuItem(text='Empty Es', action=click_menu),
	MenuItem(text='Empty Em', action=click_menu),
	MenuItem(text='Empty Et', action=click_menu),
	MenuItem(text='Empty E0', action=click_menu),
	MenuItem(text='Empty automatic', action=click_menu),
	MenuItem(text='退出', action=on_exit),
	)
	image = Image.open("ASNO.png")# 托盘显示的图标
	icon = pystray.Icon("name", image, "RAMMap-64bit\nRUN", menu)# 鼠标放在托盘上显示的文字
	icon.run()
else:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
