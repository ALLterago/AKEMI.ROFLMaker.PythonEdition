import pyfiglet

import commands

from rich.console import Console

command_list = {
'0':'exit',
'1':'hacking rofl',
'2':'steam idler'}

def showBanner(banner_text):
	banner = pyfiglet.figlet_format(banner_text,font="banner3-D")
	print(banner)


def showCommandList():
	print("Available commands:")
	for i in range(len(command_list)):
		print(str(i) + ":" + command_list[str(i)] + "\n")


def main():
	showBanner("akemi rofl maker")
	showCommandList()

	while commands.comExectutor(int(input("Enter command id:"))) != 1:
		pass


if __name__ == "__main__":
	main()
