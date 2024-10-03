from pynput import keyboard

# Funzione che viene chiamata ogni volta che un tasto viene premuto
def on_press(key):
    try:
        if key.char.isalpha():#solo lettere della tasiera
            print(f"Tasto premuto: {key.char}")
    except AttributeError:
        pass#ignora altri pulsanti tasiera
with keyboard.Listener(on_press=on_press) as listener:#si avvia prima x chiamare on_press
    listener.join()

"""
on_press: Questa funzione viene chiamata ogni volta che viene premuto un tasto.
Verifica se il tasto premuto è una lettera (key.char.isalpha()).
Stampa il tasto se è una lettera.
keyboard.Listener: Questo oggetto monitora i tasti premuti e chiama la funzione on_press per ogni pressione di tasto.
"""