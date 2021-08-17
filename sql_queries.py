'''
Author: Jay Sorathiya
The main purpose of this module is to let us create/drop all tables for
Sparkify database.
'''

# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists Users ;"
song_table_drop = "DROP table if exists Songs ;"
artist_table_drop = "DROP table if exists Artists ;"
time_table_drop = "DROP table if exists Time ;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY, 
    start_time BIGINT NOT NULL, 
    user_id INT NOT NULL, 
    level VARCHAR, 
    song_id VARCHAR,
    artist_id VARCHAR, 
    session_id INT, 
    location VARCHAR, 
    user_agent VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY, 
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    gender VARCHAR, 
    level VARCHAR
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY, 
    title VARCHAR NOT NULL, 
    artist_id VARCHAR NOT NULL, 
    year INT NOT NULL, 
    duration FLOAT NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY, 
    name VARCHAR NOT NULL, 
    location VARCHAR, 
    latitude NUMERIC, 
    longitude NUMERIC
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time BIGINT PRIMARY KEY, 
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week INT NOT NULL, 
    month INT NOT NULL, 
    year INT NOT NULL, 
    weekday INT NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING ;
""")

user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING ;
""")

song_table_insert =("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING ;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING ;

""")


time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING ;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, s.artist_id
FROM artists AS a
JOIN songs AS s
ON a.artist_id = s.artist_id
WHERE s.title = (%s) AND a.name = (%s) AND s.duration = (%s);
""")
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
