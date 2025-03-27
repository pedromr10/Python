#imports:
import customtkinter
import tkinter
from pytube import YouTube

#variaveis: 
linkStr = tkinter.StringVar()

#funcoes:
def funcaoSobre():
    #criacao do frame sobre:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    paginaSobre = customtkinter.CTk()
    paginaSobre.geometry("300x200")
    paginaSobre.configure(fg_color = '#a34957')
    paginaSobre.title("Sobre YTBDownloader")

    #conteudo do frame sobre:
    autor = customtkinter.CTkLabel(paginaSobre, text = 'Autor:  Pedro Munhoz Rosin', text_color='white')
    autor.pack(padx = 10, pady = 10)
    
    bibliotecas = customtkinter.CTkLabel(paginaSobre, text = 'Bibliotecas utilizadas:   customtkinter, pytube', text_color='white')
    bibliotecas.pack(padx = 10, pady = 10)

    funcionalidades = customtkinter.CTkLabel(paginaSobre, text = 'Funcionalidades:\n   - É possível baixar vídeos com a \nmaior qualidade disponível;\n- É possível baixar faixas de áudio.', text_color='white')
    funcionalidades.pack(padx = 10, pady = 10)

    #fazer o frame paginaInicial nao fechar instantaneamente:
    paginaSobre.mainloop()

def funcaoBaixar():

    #criacao do frame baixar:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    paginaBaixar = customtkinter.CTk()
    paginaBaixar.geometry("450x300")
    paginaBaixar.configure(fg_color = '#a34957')
    paginaBaixar.title("Baixar vídeos e áudios")

    #conteudo do frame baixar:
    title = customtkinter.CTkLabel(paginaBaixar, text = 'Cole o link do vídeo aqui:', text_color='white')
    title.pack(padx = 10, pady = 10)
    linkEntry = customtkinter.CTkEntry(paginaBaixar, text_color= 'white', fg_color='#4d0511', border_color='white', border_width = 1, width=300, textvariable=linkStr)
    linkEntry.pack(padx = 10, pady = (1, 10))
    download = customtkinter.CTkButton(paginaBaixar, text = 'Fazer Download', command =funcaoDownload(), text_color='white', fg_color='#6e0818', hover_color='#4d0511')
    download.pack(padx = 10, pady = 10)

    

    #fazer o frame paginaInicial nao fechar instantaneamente:
    paginaBaixar.mainloop()

def funcaoDownload():
    link = linkStr.get()
    print(link)

#criacao do frame paginaInicial:
#customtkinter.set_appearance_mode("System")
#customtkinter.set_default_color_theme("blue")
ytbdownloader = customtkinter.CTk()
ytbdownloader.geometry("350x200")
ytbdownloader.configure(fg_color = '#a34957')
ytbdownloader.title("YTBDownloader")


#conteudo do frame paginaInicial:
title = customtkinter.CTkLabel(ytbdownloader, text = 'YTBDownloader', text_color='white')
title.pack(padx = 10, pady = 10)
subtitle = customtkinter.CTkLabel(ytbdownloader, text = 'O aplicativo para baixar vídeos e áudios do YouTube!', text_color='white')
subtitle.pack(padx = 10, pady = 10)
baixar = customtkinter.CTkButton(ytbdownloader, text = 'Baixar', command = funcaoBaixar, text_color='white', fg_color='#6e0818', hover_color='#4d0511')
baixar.pack(padx = 10, pady = 10)
sobre = customtkinter.CTkButton(ytbdownloader, text = 'Sobre', command = funcaoSobre, text_color='white', fg_color='#6e0818', hover_color='#4d0511')
sobre.pack(padx = 10, pady = 10)

#fazer o frame paginaInicial nao fechar instantaneamente:
ytbdownloader.mainloop()