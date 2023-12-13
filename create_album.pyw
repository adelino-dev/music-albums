import tkinter as tk
from datetime import datetime

def insert_creater(window):
    """
    Insert an album registration menu in the window.
    """

    #Global variables:
    global entryName
    global album_year
    global check_launch
    global entryArtist

    #DATA:
    CURRENT_YEAR = datetime.now().year
    album_year = tk.IntVar()
    check_launch = tk.IntVar()
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()

    #Create the GUI elements:
    frame = tk.Frame(window)
    frameName = tk.Frame(frame)
    frameYear = tk.Frame(frame)
    frameArtist = tk.Frame(frame)
    frameLaunch = tk.Frame(frame)
    frameCreate = tk.Frame(frame)

    labelName = tk.Label(frameName, text= "Nome do Álbum:")
    labelYear = tk.Label(frameYear, text = "Ano de lançamento:")
    labelArtist = tk.Label(frameArtist, text = "Banda/Artista:")
    
    entryName = tk.Entry(frameName)
    spinboxYear = tk.Spinbox(frameYear, 
                                from_ = 1940, to= CURRENT_YEAR, 
                                textvariable= album_year)
    entryArtist= tk.Entry(frameArtist)
    checkLaunch = tk.Checkbutton(frameLaunch, 
                                    text="Álbum lançamento do Artista", 
                                    variable= check_launch,
                                    onvalue=1, offvalue=0)
    buttonCreate = tk.Button(frameCreate, text ="Criar Álbum", 
                            command = set_album)

    #Insert the GUI elements:

    labelName.grid(row=0, column=0)
    labelYear.grid(row=0, column=0)
    labelArtist.grid(row=0, column=0)

    entryName.grid(row=0, column=1)
    spinboxYear.grid(row=0, column=1)
    entryArtist.grid(row=0, column=1)
    checkLaunch.grid(row=0, column=0)
    buttonCreate.pack(anchor="center")

    frameName.pack(anchor="w")
    frameYear.pack(anchor="w")
    frameArtist.pack(anchor="w")
    frameLaunch.pack(anchor="w")
    frameCreate.pack(anchor="center")

    x = (window_width - frame.winfo_reqwidth())//2
    y = (window_height - frame.winfo_reqheight())//2
    frame.pack(padx=x, pady=y)
    window.mainloop()

def set_album():
    """
    Get the information entered in the album registration menu 
    and record it in the album_list.txt file.
    """
    name = entryName.get()
    year = album_year.get()
    artist = entryArtist.get()
    launch = check_launch.get()

    album_info = "{} {} {} {}\n".format(name, year, artist, launch)
    album_list = open("album_list.txt", 'a', encoding="utf-8")
    album_list.write(album_info)
    print(album_info)

if __name__ == "__main__":
    #Create the Window:
    window = tk.Tk()

    #Create GUI elements:
    insert_creater(window)

    #Open the window:
    window.mainloop