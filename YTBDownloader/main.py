#imports:
import customtkinter
import tkinter

#funcoes:

def funcaoSobre():
    #criacao do frame sobre:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    paginaSobre = customtkinter.CTk()
    paginaSobre.geometry("450x300")
    paginaSobre.title("Sobre YTBDownloader")

    #conteudo do frame sobre:
    autor = customtkinter.CTkLabel(paginaSobre, text = 'Autor:  Pedro Munhoz Rosin')
    autor.pack(padx = 10, pady = 10)
    
    bibliotecas = customtkinter.CTkLabel(paginaSobre, text = 'Bibliotecas utilizadas:   customtkinter, pytube')
    bibliotecas.pack(padx = 10, pady = 10)

    #fazer o frame paginaInicial nao fechar instantaneamente:
    paginaSobre.mainloop()

def funcaoBaixar():
    #criacao do frame baixar:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    paginaBaixar = customtkinter.CTk()
    paginaBaixar.geometry("450x300")
    paginaBaixar.title("Baixar vídeos e áudios")

    #conteudo do frame baixar:
    autor = customtkinter.CTkLabel(paginaBaixar, text = 'Autor:  Pedro Munhoz Rosin')
    autor.pack(padx = 10, pady = 10)
    

    #fazer o frame paginaInicial nao fechar instantaneamente:
    paginaBaixar.mainloop()

#criacao do frame paginaInicial:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
ytbdownloader = customtkinter.CTk()
ytbdownloader.geometry("450x300")
ytbdownloader.title("YTBDownloader")

#conteudo do frame paginaInicial:
title = customtkinter.CTkLabel(ytbdownloader, text = 'YTBDownloader')
title.pack(padx = 10, pady = 10)
subtitle = customtkinter.CTkLabel(ytbdownloader, text = 'O aplicativo para baixar vídeos e áudios do YouTube!')
subtitle.pack(padx = 10, pady = 10)
sobre = customtkinter.CTkButton(ytbdownloader, text = 'Sobre', command = funcaoSobre)
sobre.pack(padx = 10, pady = 10)
baixar = customtkinter.CTkButton(ytbdownloader, text = 'Baixar', command = funcaoBaixar)
baixar.pack(padx = 10, pady = 10)

#fazer o frame paginaInicial nao fechar instantaneamente:
ytbdownloader.mainloop()