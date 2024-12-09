import subprocess
import time


# 自动清理，1分钟一次
while True:
	# cmd阻塞运行,调用RAMMap
	subprocess.Popen("RAMMap-64bit -Ew", shell=True).wait()
	subprocess.Popen("RAMMap-64bit -Es", shell=True).wait()
	subprocess.Popen("RAMMap-64bit -Em", shell=True).wait()
	subprocess.Popen("RAMMap-64bit -Et", shell=True).wait()
	subprocess.Popen("RAMMap-64bit -E0", shell=True).wait()
	time.sleep(60)
