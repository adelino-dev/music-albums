import tkinter as tk
from tkinter import ttk

def insert_reader(window):
    """
    Insert the list of registered albums into the window
    and return the main frame widget.
    """

    #Get album information:
    album_list = open("album_list.txt", "r")
    albums = album_list.readlines()

    #Create frame:
    frame = tk.Frame(window)

    #Inform that there are no albums registered:
    if len(albums) == 0:
        label = tk.Label(frame, text = "Não há álbuns cadastrados.")
        label.pack()
    
    #List the albums:
    else:
        #Create Treeview:
        treeAlbums = ttk.Treeview(frame,
                                show="headings",
                                columns=("name", 
                                        "year", 
                                        "artist",
                                        "launch"),)
        
        #Configure column names:
        treeAlbums.heading("name", text="Nome do Álbum")
        treeAlbums.heading("year", text="Ano de Lançamento")
        treeAlbums.heading("artist", text="Banda/Artista")
        treeAlbums.heading("launch", text="Lançamento do Artista")    

        for album in albums:
            album = album[0:-1].split("|")
            album[-1] = "Sim" if (album[-1] == "1") else "Não"
            treeAlbums.insert("", tk.END, values=album)

        treeAlbums.pack()
    frame.pack()

    return frame

if __name__ == "__main__":
    #Create the Window:
    window = tk.Tk()

    #Create GUI elements:
    insert_reader(window)

    #Open the window:
    window.mainloop()