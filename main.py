# Course: C950 - Data Structures and Algorithms II
# Student: Vikas Lohana
# ID: 010138181


# I used the Nearest Neighbor template for this project, as well as made appointments with my professor Dr. Amy Antonucci.
# Ref: C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor - https://srm--c.vf.force.com/apex/CourseArticle?id=kA03x000001DbBGCA0&groupId=&searchTerm=&courseCode=C950&rtn=/apex/CommonsExpandedSearch


# Ref: datetime - Basic date and time types: https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta # from datetime is module, import datetime is the class
#from datetime import timedelta
import csv


""" A) Package data steps: """
# Ref: Source - C950 - Webinar-1 - Let’s Go Hashing webinar: https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
# A1-Create HashTable data structure
class ChainingHashTable:
   # Constructor with initial capacity parameter
   # Assigns all buckets with an empty list
   def __init__(self, initial_capacity = 10): # space complexity 0(1), time O(N)
       self.table = []
       for i in range(initial_capacity):
           self.table.append([]) #This is putting the buckets into the hashtable


   # Inserts a new item into the hash table.
   def insert(self, key, item): # creates insert, puts packages into bucket
       # get the bucket list where this item will go
       bucket = hash(key) % len(self.table)
       bucket_list = self.table[bucket]
       for x in bucket_list:
           if x[0] == key:
              x[1] = item
              return
       bucket_list.append([key, item])
       return


   # Search for an item with matching key in the hash table.
   # returns the item if found, or None if not found
   def search(self, key): # searches through hashtable based on the key
       # get the bucket list where this key would be.
       bucket = hash(key) % len(self.table)
       bucket_list = self.table[bucket]
       # print(bucket_list)
       # search for the key in the bucket list
       for key_value in bucket_list:
           # print (key_value)
           if key_value[0] == key:
               return key_value[1]  # value
       return None


   # Removes an item with matching key from the hash table.
   def remove(self, key):
       # get the bucket list where this item will be removed from.
       bucket = hash(key) % len(self.table)
       bucket_list = self.table[bucket]


       # remove the item from the bucket list if it is present.
       for kv in bucket_list:
           # print (key_value)
           if kv[0] == key:
               bucket_list.remove([kv[0], kv[1]])


   def __str__(self):
       retstr = ""
       for i in range(10):
           retstr += str(i) + ":" + str(self.table[i])
           retstr += '\n'
       return retstr


   def __repr__(self):


       retstr = ""
       for i in range(10):
           retstr += str(i) + ":" + str(self.table[i])
           retstr += '\n'
       return retstr


# A2-Create Package object and have packageCSV and distanceCSV and addressCSV files ready
class Package: # make classes into different file
   def __init__(self, ID, address, city, state, zipcode, deadline, weight, notes):
       self.ID = ID
       self.address = address
       self.city = city
       self. state = state
       self.zipcode = zipcode
       self.deadline = deadline
       self.weight = weight
       self.notes = notes
       self.status = ""
       self.loadTime = None
       self.deliveryTime = None
       self.truckName = None


# str method returns the string representation of objects
   def __str__(self):
       return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                          self.deadline, self.weight, self.notes, self.status, self.loadTime,
                                                          self.deliveryTime, self.truckName)
   def __repr__(self):
       return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                          self.deadline, self.weight, self.notes, self.status, self.loadTime,
                                                          self.deliveryTime, self.truckName)


# A3 Create loadPackageData(HashTable) to
# - read packages from packageCSV file
# Ref: C950 - Webinar-2 - Getting Greedy, who moved my data webinar: https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
# - update Package object
# - insert Package object into HashTable with the key=PackageID and Item=Packag


def loadPackageData(fileName):
   with open(fileName) as packages:
       packageData= csv.reader(packages, delimiter=',')
       for package in packages:
           p = package.strip().split(',')
           pID = int(p[0])
           pAddress = (p[1])
           pCity = (p[2])
           pState = (p[3])
           pZipCode = (p[4])
           pDeadline = (p[5])
           pWeight = (p[6])
           pNotes = (p[7])
           pStatus = None
           pDelivery_time = None


           # Package object
           p = Package(pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pNotes)
           print(package)
           # insert into hash table
           packHash.insert(pID, p)


# Hashtable instance
packHash = ChainingHashTable()


# Load package to Hash Table
loadPackageData('Packages.csv')


# Get data from Hash Table
for i in range (len(packHash.table)+1):
   print("key: {} and Package: {}".format(i+1, packHash.search(i+1)))


""" B) Distance data steps: """


# B.1) Upload Distances:
# B4 - Create distanceData List
distanceData = []


# B 5-Define loadDistanceData(distanceData) to read distanceCSV file
# - read distances from distanceCSV file; row by row
# - append row to distanceData


with open('Distance.csv', 'r') as distance_csv_file:
   csv_reader_d = csv.reader(distance_csv_file)


   for d in csv_reader_d:
       distanceData.append(d)


# B.2) Upload Addresses:
# B6-Create addressData List
addressData = {}
# address data is key, index is the value


# B7-Define loadAddressData(addressData) to read addressCSV file
# - read only addresses from addressCSV file
# - append address to addressData.


with open('Address.csv', 'r') as address_csv_file:
   csv_reader_a = csv.reader(address_csv_file)
   index = 0
   for a in csv_reader_a:
       addressData[a[0]] = index
       index = index + 1

""" C) Algorithm to Load Packages: """


# C.1) Function to return the distance between two addresses indices:
# C8 - Define distanceBetween(address1, address2)

def disBetween(addIndex1, addIndex2):
   if addIndex1 >= addIndex2:
       return float(distanceData[addIndex1][addIndex2])
   else:
       return float(distanceData[addIndex2][addIndex1])
  # 9-Return distanceData[addressData.index(address1)][addressData.index(address2)]

# C.2) Function to find min distance/address:
# C10-Define minDistanceFrom(fromAddress, truckPackages)
def minDisFrom(fromAdd, truckPack):
   # C11-Return min distance address to fromAddress
   return minDisFrom()


#Nearest Neighbor
def packageDelivery(truckList, truckTime, addressData):


   # Set a current_truck_location variable to 0 (the index location of the hub)
   current_truck_location = 0
   # Create min_distance and min_package variables. These will be used to store the current minimum distance and corresponding package (and will have the true minimum distance once you’ve looked at all the packages)

   min_package = None
   addressIndex = 0
   totalMilage = 0.0
   package = None
   # Create a delivery function that takes in a package list and a start time.
   #     While the truck list is not empty
   while truckList:
       min_distance = 100.0
#         For each package id in the package list
       for pID in truckList:
#             Fetch the package object from the hash table
           package = packHash.search(pID)
#             Use the address field from the package object to get the corresponding index from the address dictionary

           addressIndex = addressData[package.address]
#             Use the index you just fetched with the current truck location index to fetch the distance from the distances list of lists
           distance = disBetween(current_truck_location,addressIndex)
#             Compare the distance you just got with the lowest value so far. If it’s less than the current min, reset the two min-variables to the current distance and package
           if float(distance) < float(min_distance):
               min_distance = distance
               min_package = package
#         “deliver” the min_package by
#             “moving” the truck to that location
       current_truck_location = addressIndex
#             Calculating how many minutes it takes the truck to move there
       minutes = (float(min_distance)*60) / 18 #  mult by 60 to convert to minutes
#             Adding those minutes to the running time
       truckTime = truckTime + timedelta(minutes=minutes)
#             Timestamping the package with that delivery time
       min_package.deliveryTime = truckTime
#         Pop the min package id off the truck list
       totalMilage += float(min_distance)

       truckList.remove(min_package.ID)
   return totalMilage

# End of Algorithm

# Create lists of package ids for each truck. These ids represent the packages on the truck
# each truck can only hold 16
# put 9th package at truck 3 so it has time to update to 10:20, used special notes for special packages

#laoding out trucks @ the proper time constraints

t1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]   # 13 packages
t2 = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 17, 18, 36, 38, 25] # 15 packages

package = packHash.search(9) # update package 9 to the right address
package.address = "410 S State St"
packHash.insert(9, package)

t3 = [9, 21, 22, 23, 24, 26, 27, 28, 32, 33, 35, 39]       # 12 packages

# Create 3 datetime variables that represent the start time of each truck. Even though you’ll use only the time it will help later to make datetime variables. Put any values in for year, month, and day.
# Ref: datetime- Basic Date and time types: https://docs.python.org/3/library/datetime.html
# Ref: Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones: https://www.youtube.com/watch?v=eirjjyP2qcQ
start_time_t1 = datetime(2023, 4, 5, 8) #(y,mon,d,h,min,sec,milsec)

#need to loop through t1 for pid in t1, where we are loading out trucks
for pID in t1:
   package = packHash.search(pID)
   package.loadTime = start_time_t1
   package.truckName = "Truck 1"


start_time_t2 = datetime(2023, 4, 5, 9,30)
for pID in t2:
   package = packHash.search(pID)
   package.loadTime = start_time_t2
   package.truckName = "Truck 2"


start_time_t3 = datetime(2023, 4, 5, 12)
for pID in t3:
   package = packHash.search(pID)
   package.loadTime = start_time_t3
   package.truckName = "Truck 3"

#print(packHash)

# E Total Milage traveled by all Trucks
tr1 = packageDelivery(t1,start_time_t1, addressData)
tr2 = packageDelivery(t2,start_time_t2, addressData)
tr3 = packageDelivery(t3,start_time_t3, addressData)

totalMilage = tr1 + tr2 + tr3


# Step 4: Implement the user menu.
#
# Your user menu must have two options for the user:
#
#     Display all packages at a certain time (and you’ll prompt the user for a time)
#     Display one package at a certain time (and you'll prompt the user for a time and a package id

print("What time would you like to check in hours and minutes. Please use the 24 hour format.")
userHour = input("Enter Hour (24 hour format)")
userMin = input("Enter minute")
userTime = datetime(2023, 4, 5, int(userHour),int(userMin))
#userTime = timedelta(hours = int(userHour), minutes= int(userMin))

uiInput = input("Press 1 to display all packages at at certain time, or press 2 for the option to display one package "
                "at a certain time, or 3 for status of all packages and total milage")
if uiInput == "1": #User has chosen to display all packages at a certain time
   for pID in range(1,41):
       package = packHash.search(pID)
       #print(pid)
       if pID == 9 and userTime < datetime(2023, 4, 5, 10, 20):
           package.address = "300 State St"
       if userTime < package.loadTime:
           package.status = "At Hub"
           package.deliveryTime = None
           package.loadTime = None
       elif userTime > package.deliveryTime:
           package.status = "Delivered"
       else:
           package.status = "On Truck"
           package.deliveryTime = None
       print(package)
   print("The total milage traveled by all trucks is " + str(totalMilage))


elif uiInput == "2":#User has chosen to display one package at a certain time #ask for hour and min and create time object
   pID = int(input("Enter package number"))
   package = packHash.search(pID)
   if pID == 9 and userTime < datetime(2023, 4, 5, 10, 20):
       package.address = "300 State St"
   if userTime < package.loadTime:
       package.status = "At Hub"
       package.deliveryTime = None
       package.loadTime = None
   elif userTime > package.deliveryTime:
       package.status = "Delivered"
   else:
       package.status = "On Truck"
       package.deliveryTime = None
   print(package)

elif uiInput == "3": # prints out all package status and totalMilage
    for i in range(1,41):
        package = packHash.search(i)
        print(package)
    print("The total milage traveled by all trucks is " + str(totalMilage))