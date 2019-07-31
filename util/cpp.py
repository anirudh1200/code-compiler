import subprocess
import uuid
import sys
import os

dir = "./tmpcode/"

def deleteFiles(filename, baseFilename):
	# Deleting the files which were created
	try:
		os.unlink(dir+filename)
	except:
		pass
	try:
		os.unlink(dir+baseFilename+'.exe')
	except:
		pass

def compile(code, inputVars, fn, timeout=5):
	#Writing code to a temporary file
	stringLength = 8
	baseFilename = uuid.uuid4().hex[0:stringLength]
	filename = baseFilename + '.cpp'
	file = open(dir+filename,"w+")
	file.write(code)
	file.close()

	#Compiling the code
	try:
		command = ["g++", filename, "-o", baseFilename+'.exe']
		run = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, timeout=timeout)
		if(run.stderr):
			result = {"stdout": None, "stderr": run.stderr.decode('utf-8')}
			fn(result)
			deleteFiles(filename, baseFilename)
			return
	except Exception as e:
		result = {"stdout": None, "stderr": str(e)}
		os.unlink(dir+filename)
		fn(result)
		deleteFiles(filename, baseFilename)
		return
	
	# Running the code
	command = ["./{}.exe".format(baseFilename)]
	inputVars = inputVars.encode('utf-8')
	try:
		if(inputVars == ""):
			try:
				run = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, timeout=timeout)
			except subprocess.TimeoutExpired as e:
				result = {"stdout": "", "stderr": "Code timedout (possibly went into a never-ending loop)"}
				fn(result)
				deleteFiles(filename, baseFilename)
				return
		else:
			try:
				run = subprocess.run(command, input=inputVars ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, timeout=timeout)
			except subprocess.TimeoutExpired:
				result = {"stdout": "", "stderr": "Code timedout (possibly went into a never-ending loop)"}
				fn(result)
				deleteFiles(filename, baseFilename)
				return
		result = {"stdout": run.stdout.decode('utf-8'), "stderr": run.stderr.decode('utf-8')}
		fn(result)
		deleteFiles(filename, baseFilename)
	except Exception as e:
		result = {"stdout": "", "stderr": str(e)}
		try:
			fn(result)
		except Exception as e:
			result = {"stdout": "", "stderr": str(e)}
			print(result)
			deleteFiles(filename)
			return
		deleteFiles(filename, baseFilename)
		return