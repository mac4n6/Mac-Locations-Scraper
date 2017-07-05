#!/usr/bin/python
'''
Copyright (c) 2017, Station X Labs, LLC
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
	* Redistributions of source code must retain the above copyright
	  notice, this list of conditions and the following disclaimer.
	* Redistributions in binary form must reproduce the above copyright
	  notice, this list of conditions and the following disclaimer in the
	  documentation and/or other materials provided with the distribution.
	* Neither the name of the Station X Labs, LLC nor the
	  names of its contributors may be used to endorse or promote products
	  derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL STATION X LABS, LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import simplekml
import sqlite3
from time import gmtime, localtime, strftime
import csv
import sys
import argparse
from argparse import RawTextHelpFormatter
import os

def getTablesNColumns():
	global tables
	global columns

	tables = []

	tables = cur.execute('SELECT name FROM sqlite_master').fetchall()

	for table in tables:
		columns = []
		cur.execute('PRAGMA TABLE_INFO({})'.format(table[0]))
		columns = [tup[1] for tup in cur.fetchall()]

		for item in columns:
			if "latitude" in item.lower():

				extractLocations(table[0])


def extractLocations(table):
 
	global folder_name
	folder_name = ""
	if output_type == 'k' or output_type == 'e':
		dir_name = f + " - " + table
		folder_name = kml.newfolder(name=dir_name)

	try:
		sql = "select * from " + table
		cur.execute(sql)

		rows = cur.fetchall()

		for row in rows:

			col_row = dict(zip(columns,row))

			global data_stuff
			data_stuff = ""

			for k,v in col_row.iteritems():
				data = str(k) + ": " + str(v) + " "
				data_stuff = data_stuff + str(data).encode("utf8")

			data_stuff = data_stuff.replace("\n"," ")
			data_stuff = data_stuff.replace(",", "_") 

			try: 
				if row["Timestamp"]:
					timestamp = row["Timestamp"] + 978307200
				timestamp_formatted = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(timestamp))

				if output_type == 'c' or output_type == 'e':
					loccsv.writerow([f,table,timestamp_formatted, str(row["Latitude"]), str(row["Longitude"]), data_stuff])

				if output_type == 'k' or output_type == 'e':
					point = folder_name.newpoint(name=timestamp_formatted)
					point.description = ("Original Database Tuple Data: " + data_stuff)
					point.coords = [(row["Longitude"],row["Latitude"])]
					point.style.iconstyle.color = simplekml.Color.red
					point.style.labelstyle.scale = 0.5
					point.timestamp.when = timestamp_formatted	
			except:
				pass
			
			try:
				if row["ZTIMESTAMP"]:
					timestamp = row["ZTIMESTAMP"] + 978307200
				timestamp_formatted = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(timestamp))

				if output_type == 'c' or output_type == 'e':
					loccsv.writerow([f,table,timestamp_formatted, str(row["ZLATITUDE"]), str(row["ZLONGITUDE"]), data_stuff])

				if output_type == 'k' or output_type == 'e':
					point = folder_name.newpoint(name=timestamp_formatted)
					point.description = ("Original Database Tuple Data: " + data_stuff)
					point.coords = [(row["ZLONGITUDE"],row["ZLATITUDE"])]
					point.style.iconstyle.color = simplekml.Color.red
					point.style.labelstyle.scale = 0.5
					point.timestamp.when = timestamp_formatted	
			except:
				pass
			
			try:
				if row["ZDATE"]:
					timestamp = row["ZDATE"] + 978307200
				timestamp_formatted = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(timestamp))

				if output_type == 'c' or output_type == 'e':
					loccsv.writerow([f,table,timestamp_formatted, str(row["ZLATITUDE"]), str(row["ZLONGITUDE"]), data_stuff])

				if output_type == 'k' or output_type == 'e':
					point = folder_name.newpoint(name=timestamp_formatted)
					point.description = ("Original Database Tuple Data: " + data_stuff)
					point.coords = [(row["ZLONGITUDE"],row["ZLATITUDE"])]
					point.style.iconstyle.color = simplekml.Color.red
					point.style.labelstyle.scale = 0.5
					point.timestamp.when = timestamp_formatted	
			except:
				pass			
			
			try:
				if row["ZDATE"]:
					timestamp = row["ZDATE"] + 978307200
				timestamp_formatted = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime(timestamp))

				if output_type == 'c' or output_type == 'e':
					loccsv.writerow([f,table,timestamp_formatted, str(row["ZLOCLATITUDE"]), str(row["ZLOCLONGITUDE"]), data_stuff])

				if output_type == 'k' or output_type == 'e':
					point = folder_name.newpoint(name=timestamp_formatted)
					point.description = ("Original Database Tuple Data: " + data_stuff)
					point.coords = [(row["ZLOCLONGITUDE"],row["ZLOCLATITUDE"])]
					point.style.iconstyle.color = simplekml.Color.red
					point.style.labelstyle.scale = 0.5
					point.timestamp.when = timestamp_formatted	
			except:
				pass	
	except:
		pass
			
if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="\
	Extract locations from iOS and macOS databases into CSV and KML formats.\
	\n\n\tiOS Location Databases: \
	\n\t/private/var/root/Library/Caches/locationd/\
	\n\t\t- cache_encryptedA.db\
	\n\t\t- lockCache_encryptedA.db\
	\n\t\t- cache_encryptedB.db\
	\n\t/private/var/mobile/Library/Caches/com.apple.routined/\
	\n\t\t- cache_encryptedB.db\
	\n\t\t- CoreRoutine.sqlite (iOS 10)\
	\n\n\tmacOS Location Databases: \
	\n\t/var/folders/zz/zyxvpxvq6csfxvn_n00000sm00006d/C/\
	\n\t\t- cache_encryptedA.db\
	\n\t\t- lockCache_encryptedA.db\
	\n\n\tVersion: 1.1\
	\n\tUpdated: 07/04/2017\
	\n\tAuthor: Sarah Edwards | @iamevltwin | mac4n6.com | oompa@csh.rit.edu"
		, prog='mac_locations_scraper.py'
		, formatter_class=RawTextHelpFormatter)
	parser.add_argument('-output', choices=['k','c','e'], action="store", help="k=KML, c=CSV, e=EVERTHING")
	parser.add_argument('directory_of_dbs')

	args = parser.parse_args()

	global output_type
	output_type = None

	global csvfile
	global loccsv
	global kml

	locdir = args.directory_of_dbs
	
	if args.output == 'c' or args.output == 'e':
		output_type = 'c'

		with open('mac_locations_scraped.csv', 'wb') as csvfile:
			loccsv = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			loccsv.writerow(['Database','Table','Timestamp (GMT)', 'Latitude', 'Longitude', 'Original Database Tuple Data'])

			for root, dirs, filenames in os.walk(locdir):
				for f in filenames: 
					if f.endswith(".db") or f.endswith(".sqlite"):
						print "Scraping locations for CSV from: " + f  
						db = os.path.join(root,f)
						conn = sqlite3.connect(db)
						with conn:
							conn.row_factory = sqlite3.Row
							cur = conn.cursor()
							getTablesNColumns()
			print "...Locations are being saved in the CSV file ios_locations_scraped.csv"

	if args.output == 'k' or args.output =='e':
		output_type = 'k'
		kml = simplekml.Kml()
		
		for root, dirs, filenames in os.walk(locdir):
			for f in filenames:
				if f.endswith(".db") or f.endswith(".sqlite"):
					print "Scraping locations for KML from: " + f
					db = os.path.join(root,f)
					conn = sqlite3.connect(db)
					with conn:
						conn.row_factory = sqlite3.Row
						cur = conn.cursor()
						getTablesNColumns()

			kml.save("mac_locations_scraped.kml")
		print "...Locations are being saved in the KML file ios_locations_scraped.kml"