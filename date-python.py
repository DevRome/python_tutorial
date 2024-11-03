import datetime

x = datetime.datetime.now() 
print(x) # 2023-12-10 22:36:45.697784

x = datetime.datetime(2016, 2, 18)
print(x) # 2016-02-18 00:00:00

print(x.strftime("%B")) # February
print(x.strftime("%d/%m/%Y")) # 18/02/2016
print(x.strftime("%A %d %B %Y")) # Thursday 18 February 2016
