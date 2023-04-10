import os
import sys
from tkinter import *



while True:
        #we need to add a input
        command = input('>> ')
        os.system(command)
        if command == 'exit':
                exit()
