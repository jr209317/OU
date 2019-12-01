#Jack Russo 
#Professor Lindner 
#Homework 10, ITS 1801
#11/25/19
#input: a text file named data.txt
#output: determine whether the the text in the file is an interger or a duplicate


#read a file for input
Ohio=open('data.txt', 'r')

#creating a empty dictionary to store  file data 
storage={}

results=('')

for object in storage.keys():
    results=object+ (' ')+ results
#checks to see is there is a duplicate and also checks to see if input in the file is an interger
for object in Ohio:
    object=object.strip()
    if object not in storage.keys():
        if object.isnumeric() is True:
            storage[object]=object  
          #prints out error message          
        else:
            print('Error:', object , 'is not an interger')
                     
    else:
        print('Error:', object ,'is a duplicate')
    

#prints results to terminal         
print(results)
  
#closes Ohio   
Ohio.close()