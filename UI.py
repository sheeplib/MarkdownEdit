# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 00:22:37 2018

@author: sheeplib
"""

try:
    import tkinter as tk
except Importerror:
    import Tkinter as tk
import tkinterhtml as tkhtml
import markdown as mk

def markdownencoding():
    htmlframe.set_content(mk.markdown(text.get('1.0', tk.END)))
    #text2.insert(tk.INSERT, text.get('1.0', tk.END))
    
# 控件定义
root = tk.Tk()
lframe = tk.Frame(root)
s1 = tk.Scrollbar(lframe)
s2 = tk.Scrollbar(lframe, orient=tk.HORIZONTAL)# HORIZONTAL 设置水平方向的滚动条，默认是竖直
text = tk.Text(lframe, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none')
button = tk.Button(lframe,text='Encoding', command=markdownencoding)
htmlframe = tkhtml.HtmlFrame(root)

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
button.pack(side=tk.BOTTOM, fill=tk.X)
lframe.pack(side=tk.LEFT, fill=tk.Y)
htmlframe.pack(side=tk.RIGHT)
#text2.pack(side=tk.RIGHT)

# 开启主循环
root.mainloop()
