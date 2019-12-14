# -*- coding:utf-8 -*- 
import time 
import os 
import sched 

schedule = sched.scheduler(time.time, time.sleep) 

def execute_command(cmd, inc):
	os.system(cmd) 
	schedule.enter(inc, 0, execute_command, (cmd, inc)) 

def main(cmd, inc=600): 
	schedule.enter(0, 0, execute_command, (cmd, inc)) 
	schedule.run() 

if __name__ == '__main__': 
	print ("ctrl + C to stop")
	main("python batch_publish.py", 600) 