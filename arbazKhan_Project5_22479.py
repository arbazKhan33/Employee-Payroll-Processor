# Arbaz Khan (1940280)

# Project 5, Employee batch file creator

# employee details to be written into the Original.txt file

employeeData =  "Dameon 1862 40 50\n" +\
                "Shelby 1874 45 60\n" +\
                "Alissa 1861 20 30\n" +\
                "Mary 1879 39 60\n" +\
                "Justin 1855 45 90\n" +\
                "Kevin 1894 12 70\n" +\
                "Timothy 1240 40 70\n" +\
                "Mike 1241 45 70\n" +\
                "Caryn 1242 40 50\n" +\
                "Stephanie 1243 40 50\n" +\
                "Jordan 1244 20 70\n" +\
                "Dahlia 1147 25 90\n" +\
                "Lizzete 1184 45 90\n" +\
                "Max 1174 35 60\n" +\
                "Aurther 1938 35 60\n" +\
                "Kevin 1949 15 90\n" +\
                "John 1962 45 75\n" +\
                "Derrick 1974 30 60\n" +\
                "Lamar 1928 35 60\n" +\
                "Joey 1934 5 60"

#opening original.txt in write mode

fout = open("Original.txt", "w")
fout.write(employeeData)               #writing employee data into the file
fout.flush() 
fout.close() 

fin = open("Original.txt", "r")       #open Original file in read mode
fout = open("Copy.txt", "w")          #open Copy file in write mode

for i in range(20):                   #loop for 20 times
    line = fin.readline() 
    splits = line.split(" ") 
    hours = int(splits[2]) 
    rate = int(splits[3]) 
    gross = hours * rate 

    if gross > 2500:                 #condition if gross salary exceeds $2500
        taxpercent = 33 
    else: 
        taxpercent = 24 

    tax = gross * taxpercent / 100    #calculate tax 
    net = gross - tax                 #calculate net salary
                                      
    outData = str(hours) + " " +\
              str(rate) + " " +\
              str(gross) + " " +\
              str(tax) + " " +\
              str(net) + "\n"

    fout.write(outData)               #write line into Copy file

fout.flush()
fout.close()
fin.close()

fin = open("Copy.txt", "r")           #open Copy file in read mode


print("Hours\tRate\tGross\tTax\tNet")
for i in range(20):
    line = fin.readline()
    splits = line.split(" ")
    print(splits[0] + "\t" +\
          splits[1] + "\t" +\
          splits[2] + "\t" +\
          splits[3] + "\t" +\
          splits[4].strip())

fin.close()