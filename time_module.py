import time

print(time.ctime(0)) # epoch una data ed orario dal quale un computer misura un tempo di sistema
print(time.time()) # restituisce i secondi passati da epoch
print(time.localtime())

# recuperare ora attuale
# time.localTime() restituisce un oggetto
objTime = time.localtime()
print(time.strftime("%Y %B %d %H:%M:%S",objTime)) # così trasformiamo l'oggetto in una stringa

# possiamo anche fare il contrario
# trasformare da una stringa in oggetto
time_string = "20 April, 2020"
print(time.strptime(time_string, "%d %B, %Y"))

# time tuple (year, month, day-num, Hour, min, sec, week_day, ?, ?)
time_tuple = (2020, 4, 20, 4, 45, 37, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)