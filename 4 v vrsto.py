from tkinter import*

class stiri_v_vrsto:
    #najprej sem naredil okno v katerem se bo igrala igrica
    def __init__(self, master):
        
        self.platno = Canvas(master, width=1050, height=900)
        self.platno.grid(row=2, column=1)
        self.platno.bind('<Button-1>', self.klik)
        
        menu=Menu(master)
        master.config(menu=menu)
        menu.add_command(label='Zapri', command=master.destroy)
        menu.add_command(label='Nova igra', command=self.novaigra)

        naslov=Label(master, text='4 v vrsto')
        naslov.grid(row=1, column=1)

        

        

    def novaigra(self):
        self.novaigra = self.platno.delete(ALL)

    def klik(self, event):
        self.x=event.x
        self.y=event.y

        

    
        

root=Tk()
app=stiri_v_vrsto(root)
root.mainloop()
