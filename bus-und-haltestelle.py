# bus-und-haltestelle.py

personen = 0
anzahl_haltestellen = input("Bitte geben Sie die Anzahl der Haltestellen ein: ")
x = True
counter_while = 1
while(x):
	if(counter_while == int(anzahl_haltestellen)):
		x = False
	eingabe = input("Bitte geben Sie ein wieviele Personen einsteigen: ")
	personen = personen + int(eingabe)
	eingabea = input("Bitte geben Sie ein wieviele Personen aussteigen: ")
	personen = personen - int(eingabea)
	counter_while = counter_while + 1
	print("Es befinden sich ", personen, " Personen im Bus.")