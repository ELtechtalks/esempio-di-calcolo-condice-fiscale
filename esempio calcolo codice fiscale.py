import tkinter as tk

# Dizionario che mappa il nome del comune al suo codice catastale
codici_catastali = {
    'Milano': 'F205',
    'Roma': 'H501',
    # ...
}

def calcola_cf():
    # Raccogli i dati dall'interfaccia grafica
    nome = entry_nome.get()
    cognome = entry_cognome.get()
    data_di_nascita = entry_data_di_nascita.get()
    sesso = var_sesso.get()
    luogo_di_nascita = entry_luogo_di_nascita.get()

    # Utilizza le regole per il calcolo del codice fiscale per generare il codice
    # Genera le prime tre lettere dal cognome
    consonanti_cognome = ''.join(c for c in cognome if c not in 'AEIOU')
    vocali_cognome = ''.join(c for c in cognome if c in 'AEIOU')
    codice_cognome = (consonanti_cognome + vocali_cognome + 'XXX')[:3]

    # Genera le prime tre lettere dal nome
    consonanti_nome = ''.join(c for c in nome if c not in 'AEIOU')
    vocali_nome = ''.join(c for c in nome if c in 'AEIOU')
    if len(consonanti_nome) >= 4:
        codice_nome = consonanti_nome[0] + consonanti_nome[2] + consonanti_nome[3]
    else:
        codice_nome = (consonanti_nome + vocali_nome + 'XXX')[:3]

    # Genera i due numeri dall'anno di nascita
    anno_di_nascita = data_di_nascita.split('/')[-1]
    codice_anno = anno_di_nascita[2:]

    # Genera la lettera dal mese di nascita
    mese_di_nascita = data_di_nascita.split('/')[1]
    mesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'H', '07': 'L', '08': 'M', '09': 'P', '10': 'R', '11': 'S', '12': 'T'}
    codice_mese = mesi[mese_di_nascita]

    # Genera i due numeri dal giorno di nascita (aggiungendo 40 se il sesso è femminile)
    giorno_di_nascita = int(data_di_nascita.split('/')[0])
    if sesso == 'F':
        giorno_di_nascita += 40
    codice_giorno = str(giorno_di_nascita).zfill(2)

    # Genera le quattro lettere dal luogo di nascita
    codice_luogo = codici_catastali[luogo_di_nascita]
def calcola_cf():
       # ...
   # Genera il carattere di controllo
   pari = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   dispari = 'ABCDEFGHIJABCDEFGHIJKLMNOPQRSTUVWXYZ'
   resto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   somma = 0
   for i in range(15):
       c = codice_fiscale[i]
       if i % 2 == 0:
           somma += dispari.find(c)
       else:
           somma += pari.find(c)
   codice_controllo = resto[somma % 26]

   codice_fiscale = codice_cognome + codice_nome + codice_anno + codice_mese + codice_giorno
   # Crea l'interfaccia grafica
root = tk.Tk()
root.title('Calcolo Codice Fiscale')

label_nome = tk.Label(root, text='Nome')
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_cognome = tk.Label(root, text='Cognome')
label_cognome.pack()
entry_cognome = tk.Entry(root)
entry_cognome.pack()

label_data_di_nascita = tk.Label(root, text='Data di nascita (GG/MM/AAAA)')
label_data_di_nascita.pack()
entry_data_di_nascita = tk.Entry(root)
entry_data_di_nascita.pack()

label_sesso = tk.Label(root, text='Sesso')
label_sesso.pack()
var_sesso = tk.StringVar(value='M')
radiobutton_maschio = tk.Radiobutton(root, text='Maschio', variable=var_sesso, value='M')
radiobutton_maschio.pack()
radiobutton_femmina = tk.Radiobutton(root, text='Femmina', variable=var_sesso, value='F')
radiobutton_femmina.pack()

label_luogo_di_nascita = tk.Label(root, text='Luogo di nascita')
label_luogo_di_nascita.pack()
entry_luogo_di_nascita = tk.Entry(root)
entry_luogo_di_nascita.pack()

button_calcola = tk.Button(root, text='Calcola', command=calcola_cf)
button_calcola.pack()

label_risultato = tk.Label(root, text='')
label_risultato.pack()

root.mainloop()