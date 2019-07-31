import subprocess
import platform
import uuid
import sys
import os

dir = "./tmpcode/"

def deleteFiles(filename):
	# Deleting the files which were created
	try:
		os.unlink(dir+filename)
	except:
		pass

def compile(code, inputVars, fn, timeout=5):
	#Writing code to a temporary file
	stringLength = 8
	baseFilename = uuid.uuid4().hex[0:stringLength]
	filename = baseFilename + '.py'
	file = open(dir+filename,"w+")
	file.write(code)
	file.close()
	
	# Running the code
	command = []
	inputVars = inputVars.encode('utf-8')
	if platform.system() == 'Linux:':
		command = ["python3", filename]
	else:
		command = ["python", filename]
	try:
		if(inputVars == ""):
			try:
				run = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, timeout=timeout)
			except subprocess.TimeoutExpired as e:
				result = {"stdout": "", "stderr": "Code timedout (possibly went into a never-ending loop)"}
				fn(result)
				deleteFiles(filename)
				return
		else:
			try:
				run = subprocess.run(command, input=inputVars ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, timeout=timeout)
			except subprocess.TimeoutExpired:
				result = {"stdout": "", "stderr": "Code timedout (possibly went into a never-ending loop)"}
				fn(result)
				deleteFiles(filename)
				return
		result = {"stdout": run.stdout.decode('utf-8'), "stderr": run.stderr.decode('utf-8')}
		fn(result)
		deleteFiles(filename)
	except Exception as e:
		result = {"stdout": "", "stderr": str(e)}
		try:
			fn(result)
		except Exception as e:
			result = {"stdout": "", "stderr": str(e)}
			print(result)
			deleteFiles(filename)
			return
		deleteFiles(filename)
		return