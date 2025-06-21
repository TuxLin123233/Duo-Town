import os
import threading
import subprocess

print("Duo小镇项目启动器: 请输入以下命令执行操作\n")

data = {
    "run": "运行Django和Vue服务器",
    "migrate": "数据库数据迁移"
}

def run_django():
    subprocess.run(['python', 'app/manage.py', 'runserver'])

def run_vue():
    os.chdir("vue")
    subprocess.run(['npm', 'run', 'dev'])

for i in data:
    print(f'<{i}>\t\t', data[i])

user = input("> ")

if user == "run":
    django_thread = threading.Thread(target=run_django)
    vue_thread = threading.Thread(target=run_vue)

    django_thread.start()
    vue_thread.start()

    django_thread.join()
    vue_thread.join()

elif user == "migrate":
    os.system("python app/manage.py makemigrations")
    os.system("python app/manage.py migrate")