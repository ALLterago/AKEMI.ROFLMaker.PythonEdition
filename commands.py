import time

from os import walk
from random import seed
from random import randint
from rich.progress import Progress,track

command_list = {
'0':'exit',
'1':'hacking rofl',
'2':'walk cool looking console util',
'3':'steam idler'}

def comExectutor(comid):

	if comid == 0:
		print("Bye...")
		return True

	elif comid == 1:
		hackingRofl()
		print("Hack compete")
		return False

	elif comid == 2:
		walkUtil()
		return False

	else:
		print("Command id unknown")
		return False


def hackingRofl():

	for i in track(range(50),"Initializing hacking utils..."):
		time.sleep(0.1)
		
	hackTarget = str(input("Hack target:"))
	
	for i in track(range(100),"identifying " + hackTarget):
		time.sleep(0.1)
		
	for i in track(range(125),"Configurating IP hack"):
		time.sleep(0.1)

	seed(hackTarget)
	with Progress(transient=True) as prog :
		iphack = prog.add_task("Hacking bank accounts",total=randint(500, 1500))
		jopahack = prog.add_task("Hacking jopa",total=randint(750,1750))
		vkhack = prog.add_task("Hacking Vkontakte",total=randint(250,1250))
		while not prog.finished:
			prog.update(iphack,advance=0.4)
			prog.update(jopahack,advance=0.6)
			prog.update(vkhack,advance=0.2)
			time.sleep(0.02)

	for i in track(range(50),"Searching for address"):
		time.sleep(0.1)

	for i in track(range(100),"Sending dagestan fighters"):
		time.sleep(0.1)


def walkUtil():

	for i in walk("/"):
		print(i)
		time.sleep(0.3)
