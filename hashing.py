print ("===============================================")
print ("Hash Chaker[1] , Hash Length[2] , Hash Type[3]")
print ("===============================================")

choose = input("Please Choose Option : ")
if choose == '1':
        hash1 = input("Enter Hash [1] : ")
        hash2 = input("Enter Hash [2] : ")
        if hash1 == hash2 :
                print("The Hash is Clean")
        else: 
                print("The Hash is Virus")
                
                
                
