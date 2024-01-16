# from fabric import Connection
# from invoke import task

# @task
# def test(c):
#     conn = Connection(host='34.82.228.195', user='bondar1983ovdoc1', connect_kwargs={"key_filename": "C:/.ssh/id_rsa"})
#     conn.run('date')
#     conn.local('date')



# import os
from fabric.api import env, settings, run, local, cd, sudo

from config import mIP, mNAME, mADRESSVM


vm_ip = "35.197.36.43"


env.hosts = [vm_ip]
env.user = "bondar1983ovdoc1"

# env.hosts = [mIP]
# env.user = mNAME

# current_directory = os.path.dirname(os.path.abspath(__file__))
# adress_filename = os.path.join(current_directory, '.ssh/id_rsa')
# adress_filename = str(adress_filename.replace("\\", "/"))
# print(adress_filename)
# env.key_filename = adress_filename

# env.key_filename = "C:/.ssh/id_rsa"

env.reject_unknown_hosts = False
env.disable_known_hosts = True

def test():
    with settings(connect_kwargs={"key_filename": "C:/Users/Alex01/.ssh/id_rsa"}, warn_only=True):
        run("date")
        local("date")

def update():
	# with cd(mADRESSVM):	
	with cd("/home/bondar1983ovdoc1/newswebsite"):		
		run("git stash")
		run("git pull")
		sudo("supervisorctl restart flask")
