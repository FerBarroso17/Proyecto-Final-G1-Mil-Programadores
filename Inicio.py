import tkinter as tk

class AppInicio():

    def __init__(self, master):
        self.master = master
        self.master.title('Tour Musical')
        self.master.geometry('300x300')
        self.master.config(bg='black')
        self.master.resizable(True, False)
        self.frame = tk.Frame(self.master, bg='black')
        self.frame.pack(expand=True, fill='both')
        self.label = tk.Label(self.frame, text='Tour Musical', bg='black', fg='white', font=('Arial', 20))
        self.label.pack(expand=True, fill='both')
        self.boton = tk.Button(self.frame, text='Iniciar', bg='black', fg='white', font=('Arial', 20))
        self.boton.pack(expand=True, fill='both')
        self.boton = tk.Button(self.frame, text='Salir', bg='black', fg='white', font=('Arial', 20))
        self.boton.pack(expand=True, fill='both')

if __name__ == '__main__':
    root = tk.Tk()
    tourmusical = AppInicio(root)
    root.mainloop(0)