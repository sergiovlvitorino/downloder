from subprocess import call
import os

class Downloader:
	def __init__(self):
		pass

	def run(self):
		for link in self.read_file():
			command = "wget " + link
			self.command_line(command)

	def read_file(self):
		links = []
		with open("links.txt", "r+") as fp:
			for line in fp:
				links.append(line)
		return links

	def command_line(self, command):
		os.system(command)

if __name__ == "__main__":
	Downloader().run()
