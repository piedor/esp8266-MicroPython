"""
    Classe per semplificare l'utilizzo della libreria ampy
"""
import os


class ConnectMicroPython:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def runCode(self, filename):
        self._runLine("run", filename)

    def putCode(self, pcFolder, microFolder):
        self._runLine("put", pcFolder, microFolder)

    def getCode(self, microFolder):
        self._runLine("get", microFolder)

    def ls(self, microFolder):
        self._runLine("ls", microFolder)

    def rm(self, filename):
        self._runLine("rm", filename)

    def rmdir(self, microFolder):
        self._runLine("rmdir", microFolder)

    def _runLine(self, command, arg1, arg2=""):
        print("ampy -p %s -b %d %s %s %s" %
              (self.port, self.baudrate, command, arg1, arg2))
        os.system("ampy -p %s -b %d %s %s %s" %
                  (self.port, self.baudrate, command, arg1, arg2))
