import math

def getISBN(productID):
    #remove 1st 3 digits from ID
    ISBN=productID[3:]
    sum=0
    for i in range(0,len(ISBN)):
        sum+=int(ISBN[i])*(10-i)
        
 
    #find next closest multiple of 11 and subtract sum from this to get errorbit
    errorbit=(11*(math.ceil(sum/11)) - sum)%11
    
    #add errorbit to end of ISBN
    if(errorbit == 10):
        ISBN=ISBN+"X"
    else:
        ISBN=ISBN+str(errorbit)
    print( "Product ID:",productID,"ISBN:", ISBN)


while True:
    productID=input("Enter productID")
    if len(productID) !=12 or productID[:3]!="978":
      print("Invalid ID")
    else:
        break
     
print(productID)
getISBN(productID)


