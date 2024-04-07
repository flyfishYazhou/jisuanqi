import tkinter as my

'''tkinter界面设计'''

'''键盘事件'''
def keypressbtn(event):
    btx=event.widget
    l1.setvar(btx.txt)

'''界面设计'''
win = my.Tk()
win.geometry('310x600')
win.resizable(width = "false", height = "false")
win.title("计算器")

'''显示区'''
f1=my.Frame(win,borderwidth=5,background="red")
f1.pack(expand=1,fill='both')
l1=my.Label(f1,font=("雅黑",25),text="0.00",anchor="e")
l1.pack(expand=1,fill="both",pady=2,padx=2)
l2=my.Label(f1,font=("雅黑",25),anchor="e")
l2.pack(expand=1,fill="both",pady=2,padx=2)

'''按钮区'''
aniuNiub=[['%','CE','C','←'],
          [7,8,9,'＋'],
          [4,5,6,'－'],
          [1,2,4,'×'],
          [0,'·','÷','＝']]
f2 = my.Frame(win,borderwidth=5, background="green")
f2.pack(expand=1, fill="both", ipadx=3, ipady=3)
listx = []
for i, aniuNiubRoW in enumerate(aniuNiub):
    for j, aniuNiubCol in enumerate(aniuNiubRoW):
        #print("{},{}".format(i,aniuNiubCol))
        btntemp=my.Button(f2, text=aniuNiubCol, font=("华文中宋", 25), width=2, command="keypressbtn")
        btntemp.grid(row=i,column=j,padx=10,pady=10,ipadx=2,ipady=2)
        btntemp.bind('<Button-1>',keypressbtn)
        listx.append(btntemp)
    #print("\n")

'''功能区'''
f4 = my.Frame(win,borderwidth=5,background="red",width=500,height=300)
f4.pack(fill="both", ipadx=50,ipady=50)
b1 = my.Button(f4, text="退出", command=win.quit)
b1.pack(expand=1, fill="both")

win.mainloop()
