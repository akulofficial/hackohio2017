import sqlite3

f = open("/Users/akulgulrajani/Documents/latLong1.json", "w")
connection = sqlite3.connect("/Users/akulgulrajani/Downloads/Hackathon/data/cuebiq_cbus_osu.db")
cursor = connection.cursor()

cursor.execute("SELECT latitude, longitude from cuebiq")
result = cursor.fetchall()

counter = 0;
f.write ("Coordinates: {")
f.write ('"latitude,longitude":"')
for r in result:
	if counter < (len(result) - 1):
		f.write('[' + str(r[0]) + ':' + str(r[1]) + '],')
		counter += 1
	else:
		strWriteFinal = '[' + str(r[0]) + ':' + str(r[1]) + ']"'
		f.write(strWriteFinal)

f.write ('}')
connection.commit()

connection.close()
f.close()