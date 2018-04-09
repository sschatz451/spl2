# bus-und-haltestelle.py

personen = 0
anzahl_haltestellen = input("Bitte geben Sie die Anzahl der Haltestellen ein: ")
x = True
counter_while = 1
c = True
while(x):
	if(counter_while == int(anzahl_haltestellen)):
		x = False
	eingabe = input("Bitte geben Sie ein wieviele Personen einsteigen: ")
	personen = personen + int(eingabe)
	while(c):
		eingabea = input("Bitte geben Sie ein wieviele Personen aussteigen: ")
		if(personen<int(eingabea)):
			c = True
			print("Es befinden sich nur ", personen, " Personen im Bus.")
		else:
			c = False
			personen = personen - int(eingabea)
	counter_while = counter_while + 1
	if(personen<60):
		print("Es befinden sich ", personen, " Personen im Bus.")
		c = True
	else:
		personen = personen - 60
		print("Es können ", personen, " Personen leider nicht mitfahren.")
		c = True
