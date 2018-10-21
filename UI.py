# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 00:22:37 2018

@author: sheeplib
"""

try:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
except Importerror:
    import Tkinter as tk
    from Tkinter import filedialog
    from Tkinter import messagebox
import tkinterhtml as tkhtml
import markdown as mk

def loadfile(filename):
    try:
        tmpfile = open(filename,'r')
        text.delete('1.0', tk.END)
        text.insert('1.0', tmpfile.read())
        tmpfile.close()
    except IOError:
        messagebox.showerror(title='Error', message='''There's no such file''')
def savefile(filename):
    try:
        tmpfile = open(filename,'w+')
        tmpfile.write(text.get('1.0', tk.END))
        tmpfile.close()
    except IOError:
        messagebox.showerror(title='Error', message='''File save error''')
def markdownencoding():
    htmlframe.set_content(mk.markdown(text.get('1.0', tk.END)))
    #text2.insert(tk.INSERT, text.get('1.0', tk.END))
def encodingbuttoncallback():
    savefile('tmp.md')
    markdownencoding()
def loadtmpbuttoncallback():
    loadfile('tmp.md')
    markdownencoding()
def openfilebuttoncallback():
    filename = filedialog.askopenfilename()
    loadfile(filename)
    markdownencoding()
def saveasfilebuttoncallback():
    filename = filedialog.asksaveasfilename()
    if filename!='':
        savefile(filename)

# 控件定义
root = tk.Tk()
lframe = tk.Frame(root)
buttonpanel = tk.Frame(lframe)
s1 = tk.Scrollbar(lframe)
s2 = tk.Scrollbar(lframe, orient=tk.HORIZONTAL)# HORIZONTAL 设置水平方向的滚动条，默认是竖直
text = tk.Text(lframe, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
buttonencoding = tk.Button(buttonpanel,text='Encoding', command=encodingbuttoncallback)
htmlframe = tkhtml.HtmlFrame(root)
buttonloadtmp = tk.Button(buttonpanel, text='Load Tmp', command=loadtmpbuttoncallback)
buttonopenfile = tk.Button(buttonpanel, text='Open File', command=openfilebuttoncallback)
buttonsaveasfile = tk.Button(buttonpanel, text='Save As', command=saveasfilebuttoncallback)

# 初始界面
text.insert(tk.INSERT, '''
# Markdown 编辑
## 2018年9月12日
''')
markdownencoding()
#text2 =tk.Text(root)
s1.pack(side=tk.RIGHT, fill=tk.Y)
s2.pack(side=tk.BOTTOM, fill=tk.X)
text.pack(expand=tk.YES, fill=tk.BOTH)
buttonencoding.pack(side=tk.RIGHT, fill=tk.X)
buttonloadtmp.pack(side=tk.LEFT, fill=tk.X)
buttonopenfile.pack(side=tk.LEFT, fill=tk.X)
buttonsaveasfile.pack(side=tk.LEFT, fill=tk.X)
buttonpanel.pack(side=tk.BOTTOM, fill=tk.X)
lframe.pack(side=tk.LEFT, fill=tk.Y)
htmlframe.pack(side=tk.RIGHT)
#text2.pack(side=tk.RIGHT)

# 开启主循环
root.mainloop()
