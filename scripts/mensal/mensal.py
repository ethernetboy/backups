import sys
import time
import paramiko 
import os
import cmd
import datetime
import glob
from git import Repo

now = datetime.datetime.now()
user = 'root'
password = 'root'
enable_password = '\n'
port=32768
f0 = open('cisco.txt')
for ip in f0.readlines():
       print('Realizando backup do switch:',ip)
       ip = ip.strip()
       filename_prefix = '/home/docker/backupsw/' + ip + '/Mensal/'
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(ip,port, user, password, look_for_keys=False)
       chan = ssh.invoke_shell()
       time.sleep(2)
       chan.send('enable\n')
       chan.send(enable_password +'\n')
       time.sleep(1)
       chan.send('term len 0\n')
       time.sleep(1)
       chan.send('sh run\n')
       time.sleep(20)
       output = chan.recv(999999)

       filename = "%s_%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,ip,now.day,now.month,now.year,now.hour,now.minute,now.second)
       f1 = open(filename, 'a')
       f1.write(output.decode("utf-8") )
       f1.close()
       ssh.close() 
       f0.close()

       files = glob.glob(filename_prefix + "*")
       files.sort(key=os.path.getmtime)
       os.remove(files[0]) 

      
time.sleep(20)
repo = Repo('/home/docker/backupsw/')
repo.git.add(A=True)
repo.index.commit('teste')
origin = repo.remote(name='origin')
origin.push() 
