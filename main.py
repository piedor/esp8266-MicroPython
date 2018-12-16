from ConnectMicroPython import ConnectMicroPython

# ConnectMicroPython(port, baudrate)
m = ConnectMicroPython('COM5', 115200)

# run a local python script remotely on Micro Python ---> runCode(filename.py)
m.runCode("./code/sensore_distanza.py")

# put a file or a folder on Micro Python
# m.putCode("main.py",".")

# print file text
# m.getCode("main.py")

# remove a file or a folder on Micro Python
# m.rm("main.py")

# list of files in dir
# m.ls("./code")

# remove a dir
# m.rmdir("./code")
