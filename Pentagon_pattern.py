import tkinter as tk
import turtle

def show_animation():
    
    t = turtle.Turtle()
    t.speed(int(e1.get()))
    s = turtle.Screen()
    s.bgcolor("black")
    t.pencolor("green")
    angle = 0
    size = 1
    while 1:
        for i in range(int(e2.get())):
            t.forward(150)
            t.left(int(e4.get()))
        t.right(int(e3.get()))
        angle += size
        if angle >= int(e5.get())/size:
            break
    turtle.done()





master = tk.Tk()
master.geometry('600x600')
tk.Label(master, 
         text="enter animation speed 0-fastest, 10-fast, 6-normal, 3-slow, 1-slowest").grid(row=0)
tk.Label(master, 
         text="enter the number of sides").grid(row=1)

tk.Label(master, 
         text="enter the distance that for shifting towards the right").grid(row=2)

tk.Label(master, 
         text="enter the distance for left shift").grid(row=3)

tk.Label(master, 
         text="enter the angle till which the animation has to proceed").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e3 = tk.Entry(master)
e4 = tk.Entry(master)

e5 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


tk.Button(master, 
          text='Show', command=show_animation).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=8)

tk.mainloop()