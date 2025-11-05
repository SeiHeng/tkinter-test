import tkinter as tk

sh = tk.Tk()

#標題
sh.title('tkiner test shh')

#大小 寬x高
sh.geometry('400x300')
sh.minsize(width=400 , height=200)#視窗最小化
sh.maxsize(width=800 , height=600)#視窗最大化
#sh.resizable(0,0)#1 = True(可以縮放) 0 = False（禁止縮放）

#icon 標題圖案
sh.iconbitmap(r'D:\vs\123.ico')

#配置（顔色）
sh.config(background='grey') #background可以縮寫bg

#透明度
sh.attributes('-alpha' , 0.3) # 0~1 1 = 100%  0 = 0%

#置頂
#sh.attributes('-topmost', True) #開啓置頂 True  關閉置頂 Flase





sh.mainloop()