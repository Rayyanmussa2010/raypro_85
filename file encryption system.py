# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:43:46 2022

@author: DELL
"""

import hashlib
from simplecrypt import encrypt, decrypt
from tkinter import filedialog as fd
from tkinter import*
root=Tk()
root.geometry("300x300")
root.title("file encryption system")

def MD5():
    

applymd5=Button(root, text="Apply MD5", command=city_name)
applymd5.place(relx=0.5, rely=0.5, anchor=CENTER)
applysha256=Button(root, text="Apply SHA256", command=city_name)
applysha256.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()