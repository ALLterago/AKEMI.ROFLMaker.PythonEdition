#written and directed by Nyancotine "ALLterago" Labooten

import pyfiglet

import commands

from rich.console import Console


def showBanner(banner_text):

	banner = pyfiglet.figlet_format(banner_text,font="banner3-D")
	print(banner)


def showCommandList():

	print("Available commands:")
	for i in range(len(commands.command_list)):
		print(str(i) + ":" + commands.command_list[str(i)] + "\n")


def main():

	isOver = False
	
	showBanner("akemi rofl maker")
	showCommandList()

	while isOver != True:
		
		try:
			isOver = commands.comExectutor(int(input("Enter command id:")))
		except ValueError:
			print("Invalid id input type")
			
		if isOver == True:	
			pass
		else:
			showCommandList()


if __name__ == "__main__":
	main()
