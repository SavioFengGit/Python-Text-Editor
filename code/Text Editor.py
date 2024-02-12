# Python Text Editor

import os # Importo il modulo os per interagire con il sistema operativo.
from tkinter import * # Importo il modulo tkinter per creare e gestire l'interfaccia grafica, importando tutti i widget disponibili.
from tkinter import filedialog, colorchooser, font # Importo i moduli filedialog, colorchooser e font per creare delle finestre di dialogo per scegliere il file, il colore e il font.
from tkinter.messagebox import * # Importo il modulo messagebox per creare delle finestre di messaggio.
from tkinter.filedialog import * # Importo il modulo filedialog per creare delle finestre di dialogo per aprire e salvare i file.

def change_color(): # Definisco la funzione change_color, che non ha parametri.
    color = colorchooser.askcolor(title="pick a color...or else") # Creo una finestra di dialogo per scegliere un colore, e assegno il valore restituito alla variabile color. Il valore restituito è una tupla che contiene il codice RGB e il codice esadecimale del colore scelto.
    text_area.config(fg=color[1]) # Configuro l'area di testo, cambiando il colore del testo (fg) con il codice esadecimale del colore scelto (color[1]).

def change_font(*args): # Definisco la funzione change_font, che ha un parametro opzionale *args. Questo parametro serve per ricevere il valore del widget che ha chiamato la funzione, ma non viene usato nel codice.
    text_area.config(font=(font_name.get(), size_box.get())) # Configuro l'area di testo, cambiando il font e la dimensione del testo con i valori delle variabili font_name e size_box, che sono di tipo StringVar. Queste variabili memorizzano il nome e la dimensione del font scelti dall'utente tramite i widget OptionMenu e Spinbox.

def new_file(): # Definisco la funzione new_file, che non ha parametri.
    window.title("Untitled") # Cambio il titolo della finestra principale in "Untitled", indicando che il file è nuovo e non ha un nome.
    text_area.delete(1.0, END) # Cancello tutto il contenuto dell'area di testo, usando i parametri 1.0 e END. Questi parametri indicano l'inizio e la fine dell'area di testo, usando il formato riga.colonna.

def open_file(): # Definisco la funzione open_file, che non ha parametri.
    file = askopenfilename(defaultextension=".txt", # Creo una finestra di dialogo per aprire un file, e assegno il nome del file scelto alla variabile file. La finestra di dialogo ha un'opzione per impostare l'estensione di default a ".txt".
                           file=[("All Files", "*.*"), # Indico i tipi di file che si possono aprire, usando una lista di tuple. Ogni tupla contiene il nome e il filtro del tipo di file. Ad esempio, la prima tupla indica che si possono aprire tutti i file, usando il filtro "*.*".
                                 ("Text Documents", "*.txt")]) # Indico che si possono aprire i documenti di testo, usando il filtro "*.txt".

    if file is None: # Controllo se il file scelto è None, cioè se l'utente ha annullato l'operazione di apertura del file.
        return # Termino la funzione, senza fare nulla.

    else: # Indico che il file scelto non è None, cioè che l'utente ha selezionato un file da aprire.
        try: # Inizio un blocco try, che serve per gestire le possibili eccezioni che possono verificarsi durante l'apertura del file.
            window.title(os.path.basename(file)) # Cambio il titolo della finestra principale con il nome del file scelto, usando la funzione os.path.basename che restituisce solo il nome del file senza il percorso.
            text_area.delete(1.0, END) # Cancello tutto il contenuto dell'area di testo, per prepararsi a mostrare il contenuto del file scelto.

            file = open(file, "r") # Apro il file scelto in modalità di lettura ("r") e assegno l'oggetto file alla variabile file.

            text_area.insert(1.0, file.read()) # Inserisco il contenuto del file nell'area di testo, usando la funzione file.read che restituisce tutto il testo del file, e i parametri 1.0 che indicano l'inizio dell'area di testo.

        except Exception: # Inizio un blocco except, che serve per gestire le eccezioni che possono verificarsi durante l'apertura del file, ad esempio se il file non esiste o non è leggibile.
            print("couldn't read file") # Stampo un messaggio di errore nella console.

        finally: # Inizio un blocco finally, che serve per eseguire delle operazioni finali indipendentemente dal fatto che si sia verificata un'eccezione o meno.
            file.close() # Chiudo il file, liberando le risorse usate.


def save_file(): # Definisco la funzione save_file, che non ha parametri.
    file = filedialog.asksaveasfilename(initialfile='unititled.txt', # Creo una finestra di dialogo per salvare un file, e assegno il nome del file scelto alla variabile file. La finestra di dialogo ha un'opzione per impostare il nome iniziale del file a 'untitled.txt'.
                                        defaultextension=".txt", # Indico l'estensione di default del file a ".txt".
                                        filetypes=[("All Files", "*.*"), # Indico i tipi di file che si possono salvare, usando una lista di tuple. Ogni tupla contiene il nome e il filtro del tipo di file. Ad esempio, la prima tupla indica che si possono salvare tutti i file, usando il filtro "*.*".
                                                   ("Text Documents", "*.txt")]) # Indico che si possono salvare i documenti di testo, usando il filtro "*.txt".

    if file is None: # Controllo se il file scelto è None, cioè se l'utente ha annullato l'operazione di salvataggio del file.
        return # Termino la funzione, senza fare nulla.

    else: # Indico che il file scelto non è None, cioè che l'utente ha selezionato un file da salvare.
        try: # Inizio un blocco try, che serve per gestire le possibili eccezioni che possono verificarsi durante il salvataggio del file.
            window.title(os.path.basename(file)) # Cambio il titolo della finestra principale con il nome del file scelto, usando la funzione os.path.basename che restituisce solo il nome del file senza il percorso.
            file = open(file, "w") # Apro il file scelto in modalità di scrittura ("w") e assegno l'oggetto file alla variabile file.

            file.write(text_area.get(1.0, END)) # Scrivo il contenuto dell'area di testo nel file, usando la funzione text_area.get che restituisce tutto il testo dell'area di testo, e i parametri 1.0 e END che indicano l'inizio e la fine dell'area di testo.

        except Exception: # Inizio un blocco except, che serve per gestire le eccezioni che possono verificarsi durante il salvataggio del file, ad esempio se il file non è scrivibile o se c'è un problema di permessi.
            print("couldn't save file") # Stampo un messaggio di errore nella console.

        finally: # Inizio un blocco finally, che serve per eseguire delle operazioni finali indipendentemente dal fatto che si sia verificata un'eccezione
            file.close() # Chiudo il file, liberando le risorse usate.


def cut(): # Definisco la funzione cut, che non ha parametri.
    text_area.event_generate("<<Cut>>") # Genero un evento di tipo "Cut", che equivale a tagliare il testo selezionato e copiarlo negli appunti.


def copy(): # Definisco la funzione copy, che non ha parametri.
    text_area.event_generate("<<Copy>>") # Genero un evento di tipo "Copy", che equivale a copiare il testo selezionato negli appunti.


def paste(): # Definisco la funzione paste, che non ha parametri.
    text_area.event_generate("<<Paste>>") #

def about(): # Definisco la funzione about, che non ha parametri.
    showinfo("About this program", "Hello my friend!!!") # Creo una finestra di messaggio che mostra le informazioni sul programma, con il titolo "About this program" e il testo "This is a program written by YOUUUUU!!!".


def quit(): # Definisco la funzione quit, che non ha parametri.
    window.destroy() # Distruggo la finestra principale, terminando il programma.


window = Tk() # Creo un oggetto di tipo Tk, che rappresenta la finestra principale del programma.
window.title("Text editor program") # Imposto il titolo della finestra principale a "Text editor program".
file = None # Creo una variabile file e la inizializzo a None. Questa variabile servirà per memorizzare il nome del file aperto o salvato.

window_width = 500 # Creo una variabile window_width e la inizializzo a 500. Questa variabile indica la larghezza della finestra principale in pixel.
window_height = 500 # Creo una variabile window_height e la inizializzo a 500. Questa variabile indica l'altezza della finestra principale in pixel.
screen_width = window.winfo_screenwidth() # Creo una variabile screen_width e la inizializzo con il valore restituito dalla funzione window.winfo_screenwidth. Questa funzione restituisce la larghezza dello schermo in pixel.
screen_height = window.winfo_screenheight() # Creo una variabile screen_height e la inizializzo con il valore restituito dalla funzione window.winfo_screenheight. Questa funzione restituisce l'altezza dello schermo in pixel.

x = int((screen_width / 2) - (window_width / 2)) # Creo una variabile x e la inizializzo con il risultato di un'operazione matematica. Questa operazione calcola la coordinata x del punto in cui posizionare la finestra principale, in modo che sia centrata orizzontalmente sullo schermo.
y = int((screen_height / 2) - (window_height / 2)) # Creo una variabile y e la inizializzo con il risultato di un'operazione matematica. Questa operazione calcola la coordinata y del punto in cui posizionare la finestra principale, in modo che sia centrata verticalmente sullo schermo.

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y)) # Imposto la geometria della finestra principale, usando la funzione window.geometry e una stringa formattata. La stringa formattata ha il formato "larghezza x altezza + x + y", dove larghezza, altezza, x e y sono le variabili create in precedenza.

font_name = StringVar(window) # Creo un oggetto di tipo StringVar, che rappresenta una variabile di tipo stringa che può essere usata dai widget di tkinter, e lo assegno alla variabile font_name. Questa variabile memorizzerà il nome del font usato nell'area di testo. Il parametro window indica che la variabile appartiene alla finestra principale.
font_name.set("Arial") # Imposto il valore della variabile font_name a "Arial", usando la funzione set.

font_size = StringVar(window) # Creo un oggetto di tipo StringVar, che rappresenta una variabile di tipo stringa che può essere usata dai widget di tkinter, e lo assegno alla variabile font_size. Questa variabile memorizzerà la dimensione del font usato nell'area di testo. Il parametro window indica che la variabile appartiene alla finestra principale.
font_size.set("25") # Imposto il valore della variabile font_size a "25", usando la funzione set.

text_area = Text(window, font=(font_name.get(), font_size.get())) # Creo un oggetto di tipo Text, che rappresenta l'area di testo, e lo assegno alla variabile text_area. Il parametro window indica che il widget appartiene alla finestra principale. Il parametro font indica il font e la dimensione del testo, usando i valori delle variabili font_name e font_size, ottenuti con la funzione get.

scroll_bar = Scrollbar(text_area) # Creo un oggetto di tipo Scrollbar, che rappresenta la barra di scorrimento, e lo assegno alla variabile scroll_bar. Il parametro text_area indica che il widget appartiene all'area di testo.
window.grid_rowconfigure(0, weight=1) # Configuro la griglia della finestra principale, usando la funzione window.grid_rowconfigure. Questa funzione serve per impostare le proprietà delle righe della griglia. Il parametro 0 indica la prima riga. Il parametro weight indica il peso della riga, cioè quanto spazio occupa rispetto alle altre righe. Il valore 1 indica che la riga occupa tutto lo spazio disponibile.
window.grid_columnconfigure(0, weight=1) # Configuro la griglia della finestra principale, usando la funzione window.grid_columnconfigure. Questa funzione serve per impostare le proprietà delle colonne della griglia. Il parametro 0 indica la prima colonna. Il parametro weight indica il peso della colonna, cioè quanto spazio occupa rispetto alle altre colonne. Il valore 1 indica che la colonna occupa tutto lo spazio disponibile.
text_area.grid(sticky=N + E + S + W) # Posiziono l'area di testo nella griglia, usando la funzione text_area.grid. Questa funzione serve per inserire il widget nella griglia. Il parametro sticky indica come il widget si adatta allo spazio della cella. I valori N, E, S, W indicano i punti cardinali (nord, est, sud, ovest). La combinazione di questi valori indica che il widget si espande in tutte le direzioni, riempiendo la cella.
scroll_bar.pack(side=RIGHT, fill=Y) # Posiziono la barra di scorrimento nel widget padre, usando la funzione scroll_bar.pack. Questa funzione serve per inserire il widget in un contenitore. Il parametro side indica il lato del contenitore in cui posizionare il widget. Il valore RIGHT indica il lato destro. Il parametro fill indica come il widget si adatta allo spazio del contenitore. Il valore Y indica che il widget si espande verticalmente, riempiendo il contenitore.
text_area.config(yscrollcommand=scroll_bar.set) # Configuro l'area di testo, usando la funzione text_area.config. Questa funzione serve per impostare le opzioni del widget. Il parametro yscrollcommand indica la funzione da chiamare quando si scorre il testo verticalmente. Il valore scroll_bar.set indica la funzione set della barra di scorrimento, che serve per aggiornare la posizione e la dimensione della barra.

frame = Frame(window) # Creo un oggetto di tipo Frame, che rappresenta un contenitore per altri widget, e lo assegno alla variabile frame. Il parametro window indica che il widget appartiene alla finestra principale.
frame.grid() # Posiziono il frame nella griglia, usando la funzione frame.grid. Questa funzione serve per inserire il widget nella griglia. Non vengono specificati parametri, quindi il widget viene inserito nella prima cella libera della griglia.

color_button = Button(frame, text="color", command=change_color) # Creo un oggetto di tipo Button, che rappresenta un pulsante, e lo assegno alla variabile color_button. Il parametro frame indica che il widget appartiene al frame. Il parametro text indica il testo del pulsante. Il parametro command indica la funzione da chiamare quando si preme il pulsante. Il valore change_color indica la funzione change_color, che serve per cambiare il colore del testo.
color_button.grid(row=0, column=0) # Posiziono il pulsante nella griglia, usando la funzione color_button.grid. Questa funzione serve per inserire il widget nella griglia. Il parametro row indica la riga della griglia in cui posizionare il widget. Il valore 0 indica la prima riga. Il parametro column indica la colonna della griglia in cui posizionare il widget. Il valore 0 indica la prima colonna.

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font) # Creo un oggetto di tipo OptionMenu, che rappresenta un menu a tendina, e lo assegno alla variabile font_box. Il parametro frame indica che il widget appartiene al frame. Il parametro font_name indica la variabile di tipo StringVar che memorizza il nome del font scelto. Il parametro *font.families() indica la lista delle famiglie di font disponibili, ottenuta con la funzione font.families. Il



font_box = OptionMenu(frame, font_name, *font.families(), command=change_font) # Creo un oggetto di tipo OptionMenu, che rappresenta un menu a tendina, e lo assegno alla variabile font_box. Il parametro frame indica che il widget appartiene al frame. Il parametro font_name indica la variabile di tipo StringVar che memorizza il nome del font scelto. Il parametro *font.families() indica la lista delle famiglie di font disponibili, ottenuta con la funzione font.families. Il parametro command indica la funzione da chiamare quando si sceglie un'opzione dal menu. Il valore change_font indica la funzione change_font, che serve per cambiare il font del testo.
font_box.grid(row=0, column=1) # Posiziono il menu a tendina nella griglia, usando la funzione font_box.grid. Questa funzione serve per inserire il widget nella griglia. Il parametro row indica la riga della griglia in cui posizionare il widget. Il valore 0 indica la prima riga. Il parametro column indica la colonna della griglia in cui posizionare il widget. Il valore 1 indica la seconda colonna.

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font) # Creo un oggetto di tipo Spinbox, che rappresenta una casella di testo con dei pulsanti per aumentare o diminuire il valore, e lo assegno alla variabile size_box. Il parametro frame indica che il widget appartiene al frame. Il parametro from_ indica il valore minimo che si può inserire nella casella. Il valore 1 indica il minimo. Il parametro to indica il valore massimo che si può inserire nella casella. Il valore 100 indica il massimo. Il parametro textvariable indica la variabile di tipo StringVar che memorizza il valore della casella. Il valore font_size indica la variabile font_size, che memorizza la dimensione del font scelta. Il parametro command indica la funzione da chiamare quando si cambia il valore della casella. Il valore change_font indica la funzione change_font, che serve per cambiare la dimensione del testo.
size_box.grid(row=0, column=2) # Posiziono la casella nella griglia, usando la funzione size_box.grid. Questa funzione serve per inserire il widget nella griglia. Il parametro row indica la riga della griglia in cui posizionare il widget. Il valore 0 indica la prima riga. Il parametro column indica la colonna della griglia in cui posizionare il widget. Il valore 2 indica la terza colonna.

menu_bar = Menu(window) # Creo un oggetto di tipo Menu, che rappresenta la barra dei menu, e lo assegno alla variabile menu_bar. Il parametro window indica che il widget appartiene alla finestra principale.
window.config(menu=menu_bar) # Configuro la finestra principale, usando la funzione window.config. Questa funzione serve per impostare le opzioni della finestra. Il parametro menu indica il widget da usare come barra dei menu. Il valore menu_bar indica la variabile menu_bar, che contiene il widget Menu.

file_menu = Menu(menu_bar, tearoff=0) # Creo un oggetto di tipo Menu, che rappresenta il sottomenu File, e lo assegno alla variabile file_menu. Il parametro menu_bar indica che il widget appartiene alla barra dei menu. Il parametro tearoff indica se il sottomenu può essere staccato dalla barra dei menu. Il valore 0 indica che non può essere staccato.
menu_bar.add_cascade(label="File", menu=file_menu) # Aggiungo il sottomenu File alla barra dei menu, usando la funzione menu_bar.add_cascade. Questa funzione serve per inserire un widget Menu nella barra dei menu. Il parametro label indica il nome del sottomenu. Il valore "File" indica il nome del sottomenu. Il parametro menu indica il widget da usare come sottomenu. Il valore file_menu indica la variabile file_menu, che contiene il widget Menu.
file_menu.add_command(label="New", command=new_file) # Aggiungo il comando New al sottomenu File, usando la funzione file_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "New" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore new_file indica la funzione new_file, che serve per creare un nuovo file.
file_menu.add_command(label="Open", command=open_file) # Aggiungo il comando Open al sottomenu File, usando la funzione file_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Open" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore open_file indica la funzione open_file, che serve per aprire un file esistente.
file_menu.add_command(label="Save", command=save_file) # Aggiungo il comando Save al sottomenu File, usando la funzione file_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Save" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore save_file indica la funzione save_file, che serve per salvare il file corrente.
file_menu.add_separator() # Aggiungo un separatore al sottomenu File, usando la funzione file_menu.add_separator. Questa funzione serve per inserire una linea orizzontale nel menu, per dividere i comandi in gruppi.
file_menu.add_command(label="Exit", command=quit) # Aggiungo il comando Exit al sottomenu File, usando la funzione file_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Exit" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore quit indica la funzione quit, che serve per chiudere il programma.

edit_menu = Menu(menu_bar, tearoff=0) # Creo un oggetto di tipo Menu, che rappresenta il sottomenu Edit, e lo assegno alla variabile edit_menu. Il parametro menu_bar indica che il widget appartiene alla barra dei menu. Il parametro tearoff indica se il sottomenu può essere staccato dalla barra dei menu. Il valore 0 indica che non può essere staccato.
menu_bar.add_cascade(label="Edit", menu=edit_menu) # Aggiungo il sottomenu Edit alla barra dei menu, usando la funzione menu_bar.add_cascade. Questa funzione serve per inserire un widget Menu nella barra dei menu. Il parametro label indica il nome del sottomenu. Il valore "Edit" indica il nome del sottomenu. Il parametro menu indica il widget da usare come sottomenu. Il valore edit_menu indica la variabile edit_menu, che contiene il widget Menu.
edit_menu.add_command(label="Cut", command=cut) # Aggiungo il comando Cut al sottomenu Edit, usando la funzione edit_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Cut" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore cut indica la funzione cut, che serve per tagliare il testo selezionato e copiarlo negli appunti.
edit_menu.add_command(label="Copy", command=copy) # Aggiungo il comando Copy al sottomenu Edit, usando la funzione edit_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Copy" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore copy indica la funzione copy, che serve per copiare il testo selezionato negli appunti.
edit_menu.add_command(label="Paste", command=paste) # Aggiungo il comando Paste al sottomenu Edit, usando la funzione edit_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "Paste" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore paste indica la funzione paste, che serve per incollare il testo dagli appunti nell'area di testo.

help_menu = Menu(menu_bar, tearoff=0) # Creo un oggetto di tipo Menu, che rappresenta il sottomenu Help, e lo assegno alla variabile help_menu. Il parametro menu_bar indica che il widget appartiene alla barra dei menu. Il parametro tearoff indica se il

help_menu = Menu(menu_bar, tearoff=0) # Creo un oggetto di tipo Menu, che rappresenta il sottomenu Help, e lo assegno alla variabile help_menu. Il parametro menu_bar indica che il widget appartiene alla barra dei menu. Il parametro tearoff indica se il sottomenu può essere staccato dalla barra dei menu. Il valore 0 indica che non può essere staccato.
menu_bar.add_cascade(label="Help", menu=help_menu) # Aggiungo il sottomenu Help alla barra dei menu, usando la funzione menu_bar.add_cascade. Questa funzione serve per inserire un widget Menu nella barra dei menu. Il parametro label indica il nome del sottomenu. Il valore "Help" indica il nome del sottomenu. Il parametro menu indica il widget da usare come sottomenu. Il valore help_menu indica la variabile help_menu, che contiene il widget Menu.
help_menu.add_command(label="About", command=about) # Aggiungo il comando About al sottomenu Help, usando la funzione help_menu.add_command. Questa funzione serve per inserire un comando nel menu. Il parametro label indica il nome del comando. Il valore "About" indica il nome del comando. Il parametro command indica la funzione da chiamare quando si seleziona il comando. Il valore about indica la funzione about, che serve per mostrare le informazioni sul programma.

window.mainloop() # Avvio il mainloop di tkinter, che gestisce gli eventi dell'interfaccia grafica. Questa funzione deve essere l'ultima riga del codice, perché blocca l'esecuzione del programma finché la finestra principale non viene chiusa.


#Author Xiao Li Savio Feng