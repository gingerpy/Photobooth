import os, os.path
import glob
import subprocess

# Path to the shared folder
dir = "PUT YOUR PATH HERE"

# Inital number of files in folder
num_files_old = len([name for name in os.listdir(dir)])
print(num_files_old)


# The while-loop ensures that the program keeps running
while True:
	# Constantly check the number of files in folder
	num_files_new = len([name for name in os.listdir(dir)])

	# If the number of files in folder is larger than num_files_old
	if (num_files_new > num_files_old):

		# Get the latest file of the folder = the newest pic
		files = glob.glob("PUT YOUR PATH HERE/*")
		new_pic = max(files, key = os.path.getctime)
		
		print ("A new picture has been added")
		print (new_pic)

		# Modify the string for the command line call, i.e. change the slashes to backslashes
		change_string = r"PUT YOUR PATH HERE WITH BACKSLASHES"
		change_string = new_pic.replace("PUT YOUR PATH HERE WITH SLASHES", change_string)

		# Modify the string (for printer) for the command line call
		prt_string = 'rundll32.exe ' + r'C:\WINDOWS\System32\shimgvw.dll,ImageView_PrintTo /pt ' + '"' + change_string + '" ' + '"' + "PUT YOUR PRINTER NAME HERE" + '"'

		# Print the picture
		subprocess.call(prt_string, shell=True)
		
		# Modify the string (for file moving) for the command line call
		trf_string = r'move ' + '"' + change_string + '"' + ' ' + '"' + r'C:\xampp\htdocs\PUT PATH TO YOUR SUBFOLDER HERE' +'"'

		# Move the newest pic into the directory of the xampp webserver
		subprocess.call(trf_string, shell=True)


		# Update Number of files in folder
		num_files_old = len([name for name in os.listdir(dir)])
	
		


		
