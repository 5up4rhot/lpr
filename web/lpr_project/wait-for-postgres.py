#!/usr/bin/env python
import psycopg2
import os
import time

database_url = os.environ["DATABASE_URL"]
connection_down = True

while connection_down:
    try:
        conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
        connection_down = False
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        time.sleep(1)
