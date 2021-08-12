# DROP TABLES

songplay_table_drop = ("DROP table if exists songplays")
user_table_drop = ("DROP table if exists Users ;")
song_table_drop = ("DROP table if exists Songs ;")
artist_table_drop = ("DROP table if exists Artists ;")
time_table_drop = ("DROP table if exists Time ;")

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (Songplay_id int, Start_time date, User_id int, Level int, Song_id int, artist_id int, session_id int, Location varchar, User_agent varchar) ;")

user_table_create = ("CREATE TABLE IF NOT EXISTS Users (User_id int, First_name varchar, Last_name varchar, Gender varchar, Level int) ;")

song_table_create = ("CREATE TABLE IF NOT EXISTS Songs (Song_id int, Title varchar, Artist_id int, Year int, Duration int) ;")

artist_table_create = ("CREATE TABLE IF NOT EXISTS Artists (Artist_id int, Name varchar, Location varchar, Latitude int, Longitude int) ;")

time_table_create = ("CREATE TABLE IF NOT EXISTS Time (Start_time int, Hour int, Day varchar, Week varchar, Month varchar, Year int, Weekday varchar) ;")

# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplays (Songplay_id, Start_time, User_id, Level, Song_id, artist_id, session_id, Location, User_agent) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

user_table_insert = "INSERT INTO Users (User_id, First_name, Last_name, Gender, Level) \
                 VALUES (%s, %s, %s, %s, %s)"

song_table_insert = "INSERT INTO Songs (Song_id, Title, Artist_id, Year, Duration) \
                 VALUES (%s, %s, %s, %s, %s)"

artist_table_insert = "INSERT INTO Artists (Artist_id, Name, Location, Latitude, Longitude) \
                 VALUES (%s, %s, %s, %s, %s)"


time_table_insert = "INSERT INTO Time (Start_time, Hour, Day, Week, Month, Year, Weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]