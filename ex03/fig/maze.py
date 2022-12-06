import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key=""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    cx,cy=300,400
    tori = image=tk.PhotoImage(file="ex03/fig/8.png")
    canvas.create_image(cx,cy,image=tori,tag="kokaton")
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyPress>",key_up)
    root.mainloop()