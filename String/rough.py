
# String can be written inside ' ' , " "  , """  """

chai="Ashis Kumar Mishra"
# fetching first character
firsr_char=chai[0]
print(firsr_char)

# Slicing the string
slice_chai=chai[0:5]    
print(slice_chai)

#lower / upper the string
print(chai.lower())
print(chai.upper())

 # remove the white space from both side
chai="  Ashis Kumar Mishra  "
print(chai.strip())
print(chai.replace("Ashis","Hemanta"))

# split the string by decorators
chai="Ashis , Hemanta , Kalpana"
print(chai.split(" , "))  

# return index / -1 if not found
chai="  Ashis Kumar Mishra  "
print(chai.find("Kumar")) 

#count the occurance of a String
chai="Ashis kumar Mishra Mishra Mishra"
print(chai.count("Mishra"))

# String Placeholders
chai_type="Masala Chai"
quantity=2
order="I ordered {} cups of {} chai ."
print(order.format(quantity,chai_type))

# String join
chai=["Ashis","Hemanta","Kalpana"]
print(" , ".join(chai))

#finding length
chai="Ashis Kumar"
print(len(chai))

#Looping each term
for ch in chai:
    print(ch)

# String inside string , path determining (unicode)
chai="Hey , I am \"Ashis Kumar Mishra\""
print(chai)

chai="Hey , I am \nAshis Kumar Mishra"
print(chai)

#present
chai="Ashis Mishra"
print("Ashis" in chai)




