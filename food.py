from struct import pack
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random

food = {
    'OREZ CU CIUPERCI': 'orez, morcovi, ciuperci',
    'MAMALIGA CU CIUPERCI': 'mamaliga, ciuperci, faina, lapte',
    'SARMALE': 'ceapa, orez, carne tocata',
    'CIORBA RADAUTEANA': 'pui, smantana,galbenusuri, otet, pastarnac, ceapa,ardei, morcovi,telina, patranjel, usturoi',
    'NOODLE SOUP': 'supa la plic',
    'BURGER': 'carne tocata, chifla, faina',
    'SARMALE': 'ceapa, carne tocata, orez, sare, piper, vegeta, ardei piscator, boia, ardei rosu, pasta de rosii',
    'CIORBA DE CARTOFI': 'cartofi, legume, boia',
    'CIORBA DE FASOLE BOABE': 'fasole, legume',
    'CIORBA DE BURTA': 'burta, usturoi, smantana',
    'CIORBA DE PERISOARE': 'carne tocata, legume',
    'CIORBA DE SALATA VERDE': 'salata, usturoi,smantana',
    'SALATA CU PUI': 'pui, salata,legume, crutoane, dresing',
    'SUPA DE PUI': 'pui, morcov, telina, cartofi, ceapa, patrunjel, sare, piper, boia,ulei',
    'PASTE CU TON': 'paste, ton, pasta de rosii, legume',
    'OMLETA': 'ceapa, salam, oua, mozzarella, ciuperci',
    'SPANAC': 'lapte, oua, usturoi, faina, unt',
    'VINETE': 'vinete, oua, ulei, ceapa',
    'OREZ CU PUI': 'orez, pui, sfecla',
    'MAMALIGA CU TOCANITA': 'faina, pui, mamaliga, condimente',
    'FRIPURA': 'carne, condimente',
    'ZACUSCA': 'a la borcan',
    'CEREALE CU LAPTE': 'simplu si usor',
    'FASOLE CU CARNATI': 'ro',
    'CARTOFI PRAJITI CU *': 'cu oua, cu carnati, cu cascaval',
    'CARTOFI RANTALITI': 'ceapa, cartofi',
    'SUPA DE GALUSTE': 'gris, pui, condimente, morcovi',
    'IAGNIE DE FASOLE': 'ro',
    'GUIAS': 'cartofi,ceapa',
    'CIORBA DE FASOLE VERDE': 'ro',
    'CIORBA DE VARZA': 'ro',
    'CARTOFI NATUR CU SNITEL DE PUI': 'ro',
    'SALATA DE CARTOFI ORIENTALA': 'ro',
    'FICAT DE PUI': 'ro',
    'DOVLECEL': 'pane sau la cuptor',
    'CARTOFI CU PUI LA CUPTOR': 'cu usturoi',
    'CLATITE': 'yummy',
    'GOMBOTI CU PRUNE': 'ro',
    'CHIFTELE CU PIREU': 'ro',
    'PIREU CU PUI': 'ro',
    'MICI': 'dinaia buni'
}


def callback():
        mancare_aleatoriu = random.choice(list(food.items()))
        print(mancare_aleatoriu)
        tkinter.messagebox.showinfo(mancare_aleatoriu)
        return mancare_aleatoriu

    

# root window
root = tk.Tk()
root.geometry('600x600')
root.resizable(True, True)
root.title('CE SA GATESC?')

# button ce sa gatesc?
po = ttk.Button(root, text="Ce sa gatesc?", compound=tk.LEFT,
                command=callback)
po.pack(ipadx=5, ipady=5, expand=True)


download_icon = tk.PhotoImage(file='E:/food/gatit.png')
do = ttk.Button(
    root,
    image=download_icon,
    command=callback
)

do.pack(ipadx=1, ipady=1, expand=True)


# Exit button
ex = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit())

ex.pack(ipadx=1, ipady=1, expand=True)


root.mainloop()
