import sqlite3

f = open('/Users/akulgulrajani/Documents/latLongPed.txt', 'w')

connection = sqlite3.connect("/Users/akulgulrajani/Downloads/Hackathon/data/cuebiq_cbus_osu.db")
cursor = connection.cursor()

cursor.execute("SELECT latitude, longitude from cuebiq_ped")
result = cursor.fetchall()

counter = 0
for r in result:
	if counter < (len(r) -1):
		f.write("new google.maps.LatLng(%f,%f)," % (r[0],r[1]))
	else:
		f.write("new google.maps.LatLng(%f,%f)" % (r[0],r[1]))

connection.commit()

connection.close()
f.close()