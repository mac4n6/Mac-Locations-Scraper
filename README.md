# iOS Locations Scraper
Dump the contents of the location database files located in:
/private/var/root/Library/Caches/locationd/    
		- cache_encryptedA.db    
		- lockCache_encryptedA.db    
		- cache_encryptedB.db    
/private/var/mobile/Library/Caches/com.apple.routined/    
		- cache_encryptedB.db   

##Usage:
`python ios_locations_scraper.py -output {k, c, e} <directory_of_dbs>`

##Output Options:
* k - KML
* c - CSV
* e - Everything (KML & CSV)


##Related Information:
http://www.mac4n6.com/

 

