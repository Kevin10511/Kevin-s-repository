pizzeria_menu = {
        "MARGHERITA": "Senza condimento,salsa e formaggio",
        "PROSCIUTTO": "Prosciutto,salsa e formaggio",
        "ROSSA": "Solo salsa",
        "VIENNA": "Vienna,salsa e formaggio",
        "SALSICCIA": "Salsiccia,salsa e formaggio",
        "PATATINE": "Patatine fritte,salsa e formaggio",
        "PROSCITTO E FUNGHI": "Prosciutto,funghi,salsa e formaggio",
        "BUFALA": "Formaggio di bufala,salsa e formaggio"
        }

ordine = input("Scegli la tua pizza(usa lettere maiuscole): ")
if ordine in pizzeria_menu.keys():
    print(pizzeria_menu[ordine])
else:
    print("Non facciamo quella pizza. Controlla se hai scritto il nome senza errori!")
