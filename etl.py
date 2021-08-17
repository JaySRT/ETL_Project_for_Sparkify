'''
Author : Jay Sorathiya

Running this file connects to Sparkify database and process the ETL pipeline for users
activity data and songs metadata.
'''

import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This function reads song data from a JSON `filepath` file and inserts it into
    song and artist tables based on different columns.

    Parameters:
    -----------
    cur : psycopg2.cursor
        cursor obtained from active session to execute PostgreSQL commands.

    filepath : str or path object
        path string to the song file.
    """
    
    # open song file
    df = pd.read_json(filepath, lines = True)

    # insert song record
    song_data = df.loc[0, ["song_id", "title", "artist_id", "year", "duration"]].values.tolist()
    
    #Changing the data type from np.int64 to int
    song_data[-2] = int(song_data[-2])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df.loc[0, ["artist_id", "artist_name", "artist_location", "artist_latitude",
                             "artist_longitude"]].values.tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    This function reads log data from a JSON `filepath` file, filter the logs to include
    useractivity that has level == 'NextSong', and insert the data into
    users, time, and songplay tables.

    Parameters:
    -----------
    cur : psycopg2.cursor
        cursor obtained from active session to execute PostgreSQL commands.

    filepath : str or path object
        path  string to the song file.
    '''
    
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[(df.page == "NextSong")]

    # convert timestamp column to datetime
    time_data = pd.to_datetime(df.ts, unit='ms')
    
    # insert time data records
    time_df = pd.DataFrame({'Start_time': df['ts'], 'hour': time_data.dt.hour, 
                        'day': time_data.dt.day, 'week_of_year': time_data.dt.week, 
                        'month': time_data.dt.month, 'year': time_data.dt.year, 
                        'weekday':time_data.dt.weekday})
    #column_labels = ('Start_time', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday')
    #time_df = pd.DataFrame(data = time_data, columns = column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, 
                         row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    This is ETL function that extracts files from the `filepath` and executes the function 
    provided in its parameter. This function will iterate over all the files present in the 
    filepath and process the data according to the function called in its parameter.

    Parameters:
    -----------
    cur : psycopg2.cursor
        cursor obtained from active session to execute PostgreSQL commands.
        
    conn : psycopg2.connect
        Making a connection with the database
    
    filepath : str or path object
        path  string to the song file.
    
    func : Function to perform
        Functions that are defined for processing the type of data.
    '''
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    '''
    This is the main function that will run the Data pipeline to do the Job.
    
    '''
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
