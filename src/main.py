import tkinter as tk

from chatgpt import chatgptmoedel

class chatGPT:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("ChatGPT Clone")
        self.winwidth = self.root.winfo_screenwidth()
        self.winheight = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (self.winwidth, self.winheight))
        self.root.resizable(False,False)
        self.root.config(bg="#36454F")
        self.logohead = tk.PhotoImage(file="../photos/newlogo122.png")  #download the logo from photos folder
        self.root.iconphoto(self.root,self.logohead)

        self.chatlabel = tk.Label(self.root,text="ChatGPT",font=("Bahnschrift",42),bg="#36454F",foreground="white")
        self.chatlabel.place(x=620,y=30,width=300,height=75)

        self.logo = tk.PhotoImage(file="../photos/newlogo122.png")   #download the logo from photos folder
        self.logoLabel = tk.Label(self.root, image=self.logo)
        self.logoLabel.place(x=710,y=120,width=120,height=89)

        self.answer_area = tk.Text(self.root,font=("Bahnschrift",15),bg="#36454F",foreground="white",highlightthickness=0, borderwidth=0)
        self.answer_area.place(x=160,y=240,width=1200,height=420)
        self.answer_area.configure(state="disabled")

        self.chatinput = tk.Text(self.root,font=("Arial",11),bg="white",foreground="black")
        self.chatinput.place(x=370,y=730,width=800,height=30)

        self.enterbtn = tk.Button(self.root, text="Submit", font=("Bahnschrift", 13), foreground="white", bg="#00A67E",
                                  command=self.getinfo)
        self.enterbtn.place(x=1200, y=730, width=100, height=40)


        self.clearbtn = tk.Button(self.root, text="Clear", font=("Bahnschrift", 13), foreground="white", bg="#00A67E",command=self.clear_area)
        self.clearbtn.place(x=1320, y=730, width=100, height=40)

        self.chatdesc = tk.Label(self.root,text="This a ChatGPT Clone. ChatGPT Clone may produce inaccurate information about people, places, or facts. ",font=("Bahnschrift",10),bg="#36454F",foreground="white")
        self.chatdesc.place(x=380,y=790,width=800,height=20)
        self.root.mainloop()


    def getinfo(self):
        self.input_value = self.chatinput.get(1.0, tk.END)
        self.answer = chatgptmoedel(self.input_value)
        self.chatinput.delete(1.0, tk.END)
        self.answer_area.configure(state="normal")
        self.final_answer = f"\n\n\n\n{self.input_value}Sure! Here's what I found for you. Hope it Helps you :\n" + self.answer
        self.answer_area.insert(tk.INSERT, self.final_answer)
        self.answer_area.configure(state="disabled")



    def clear_area(self):
        self.answer_area.configure(state="normal")
        self.answer_area.delete(1.0, tk.END)
        self.answer_area.configure(state="disabled")

chatGPT()
