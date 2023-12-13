import tkinter as tk
from create_album import insert_creater
from read_albums import insert_reader

def home():
    """
    Go to home screen.
    """
    global frame

    #Create GUI elements:
    frame = tk.Frame(window)
    buttonCreate = tk.Button(frame, text = "Criar Álbum", command = create)
    ButtonRead = tk.Button(frame, text = "Listar Álbuns", command = read)
    
    #Insert GUI elements:
    buttonCreate.pack()
    ButtonRead.pack()
    frame.pack()

def create():
    """
    Go to the album creation screen.
    """
    frame.destroy()
    global frameMain
    frameMain = insert_creater(window)
    insert_back()

    
def read():
    """
    Go to the screen that lists albums.
    """
    frame.destroy()
    global frameMain
    frameMain= insert_reader(window)
    insert_back()


def insert_back():
    """
    Insert the back button in the window.
    """
    global buttonHome
    buttonHome = tk.Button(window, text="Voltar", command=back)
    buttonHome.pack()


def back():
    """
    Return to Home Screen
    """
    frameMain.destroy()
    buttonHome.destroy()
    home()


if __name__ == "__main__":
    #Create the Window:
    window = tk.Tk()

    #Create and insert GUI elements:
    home()

    #Open the window:
    window.mainloop()