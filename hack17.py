import sqlite3


def FloatOrNegOne(value):
    try:
        return float(value)
    except:
        return -1.0

def IntOrNegOne(value):
    try:
        return int(value)
    except:
        return -1
    
f = open('/Users/akulgulrajani/Documents/cuebiq_cbus_osu.txt', 'r')

connection = sqlite3.connect("/Users/akulgulrajani/Downloads/Hackathon/data/cuebiq_cbus_osu.db")
cursor = connection.cursor()
sql_command= """
CREATE TABLE cuebiq (
count INTEGER PRIMARY KEY,
ts CHAR(19),
ts_date CHAR(10),
ts_hour TINYINT,
time_lag_seconds MEDIUMINT(6),
id_num CHAR(64),
os_code INT(1),
latitude FLOAT(1,9),
longitude FLOAT(1,9),
distance_from_last FLOAT(5,5),
total_distance FLOAT(6,5),
point_seq INT(3),
acc INT(5),
tz_offset INT(5),
ipadd VARCHAR(15),
source_id CHAR(32),
manuf VARCHAR(10),
model VARCHAR(10),
car_code INT(6),
last_seen CHAR(10),
usr_agent VARCHAR(180),
zip_code CHAR(5),
speed_mps FLOAT(2,4),
cum_avg_spd FLOAT(2,4),
linger_flag VARCHAR(1));
"""
cursor.execute(sql_command)
count = 1
store = f.readline()
while store != "":
    ts, ts_date, ts_hour, time_lag_seconds, id_num, os_code, latitude, longitude, distance_from_last, total_distance, point_seq, acc, tz_offset, ipadd, source_id, manuf, model, car_code, last_seen, usr_agent, zip_code, speed_mps, cum_avg_spd, linger_flag=store.split("|")
    ts_hour = int(ts_hour)
    time_lag_seconds = IntOrNegOne(time_lag_seconds)
    os_code = int(os_code)
    latitude = FloatOrNegOne(latitude)
    longitude = FloatOrNegOne(longitude)
    distance_from_last = FloatOrNegOne(distance_from_last)
    total_distance = FloatOrNegOne(total_distance)
    point_seq = int(point_seq)
    acc = int(acc)
    tz_offset = int(tz_offset)
    speed_mps = FloatOrNegOne(speed_mps)
    cum_avg_spd = FloatOrNegOne(speed_mps)
    
    sql_command = "INSERT INTO cuebiq  VALUES (%d,'%s', '%s', %d, %d, '%s', %d, %f, %f, %f, %f, %d, %d, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %f, %f, '%s');" % (count,
    ts,
    ts_date,
    ts_hour,
    time_lag_seconds,
    id_num,
    os_code,
    latitude,
    longitude,
    distance_from_last,
    total_distance,
    point_seq,
    acc,
    tz_offset,
    ipadd,
    source_id,
    manuf,
    model,
    car_code,
    last_seen,
    usr_agent,
    zip_code,
    speed_mps,
    cum_avg_spd,
    linger_flag)
    
    cursor.execute(sql_command)
    count += 1
    store = f.readline()


#cursor.execute("SELECT * FROM cuebiq;")
#print("fetchall:")
#result = cursor.fetchall()
#for r in result:
    #print(r)

connection.commit()

connection.close()
f.close()

    

