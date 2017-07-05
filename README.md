# Mac Locations Scraper

Dump the contents of the location database files on iOS and macOS.

iOS:
===
/private/var/root/Library/Caches/locationd/    
* cache_encryptedA.db    
* lockCache_encryptedA.db    
* cache_encryptedB.db    

/private/var/mobile/Library/Caches/com.apple.routined/    
* cache_encryptedB.db
* CoreRoutine.sqlite (iOS 10)
		
macOS:
===
/var/folders/zz/zyxvpxvq6csfxvn_n00000sm00006d/C/   
* cache_encryptedA.db    
* lockCache_encryptedA.db 

Usage:
===
`python mac_locations_scraper.py -output {k, c, e} <directory_of_dbs>`

Output Options:
===
* k - KML
* c - CSV
* e - Everything (KML & CSV)

Requirements:
===
SimpleKML - https://simplekml.readthedocs.io/en/latest/

Related Information:
===
http://www.mac4n6.com/

 

