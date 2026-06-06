import tkinter as tk
from tkinter import messagebox
import os
import shutil


class FileOrganizer:
    def abrir_explorador(self):
        os.startfile(os.path.expanduser("~")) #Abre el explorador de archivos
        

    def ordenar_archivos(self, seccion:str):
        carpetas = [
        "archivos excel",
        "archivos word",
        "archivos pdf",
        "archivos power point",
        "otros"
        ]

        for carpeta in carpetas:
            ruta_carpeta = os.path.join(seccion, carpeta)

            if not os.path.exists(ruta_carpeta):
               os.mkdir(ruta_carpeta)
        
        for name in os.listdir(seccion):
            ruta_name = os.path.join(seccion, name)
            if not os.path.isfile(ruta_name):
             continue
            else:
              if name.endswith(".pdf"):
                shutil.move(ruta_name, os.path.join(seccion, "archivos pdf"))
            
              elif name.endswith(".docx"):
                shutil.move(ruta_name, os.path.join(seccion, "archivos word"))
            
              elif name.endswith(".xlsx"):
                shutil.move(ruta_name, os.path.join(seccion, "archivos excel"))
            
              elif name.endswith(".pptx"):
                shutil.move(ruta_name, os.path.join(seccion, "archivos power point"))
            
              else:
                shutil.move(ruta_name, os.path.join(seccion, "otros"))


#Interfaz:

class Window:
    def __init__(self, root, organizador):
        self.root = root
        self.root.geometry("250x200+450+250")
        self.root.title("Organiza archivos")
        self.root.resizable(False, False)
        self.organizador = organizador

        #Menú
        self.barra_menu = tk.Menu(tearoff=0)
        self.root.config(menu=self.barra_menu)
        self.menu_principal = tk.Menu(tearoff=0)
        self.barra_menu.add_cascade(label="Buscar ruta", menu=self.menu_principal)

        self.menu_principal.add_command(label="Abirir Explorador de archivos", command=organizador.abrir_explorador)


        self.label = tk.Label(self.root, text="Buscar ruta", font=("Arial", 12))
        self.label.pack(side="top")

        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack()

        self.boton = tk.Button(self.root, text="ACEPTAR",width=20, command=self.ingresar_ruta, bg="green", fg="white")
        self.boton.pack(pady=10)

    def ingresar_ruta(self):
        seccion = self.entry.get()

        if not seccion:
            messagebox.showwarning("Advertencia", "Debe ingresar una ruta!!")
            return
        
        if not os.path.exists(seccion):
            messagebox.showerror("Error", "Ruta inexistente!! ✖")
            return
        
        else:
            try:
               self.organizador.ordenar_archivos(seccion)
               messagebox.showinfo("Info", "Los archivos fueron ordenados correctamente ✔")
               self.entry.delete(0,tk.END)
            except Exception as e:
               messagebox.showerror("Error", f'Ocurrio un problema:\n{e}')
        

if __name__ == "__main__":
    root = tk.Tk()
    organizador = FileOrganizer()
    app = Window(root, organizador)
    root.mainloop()