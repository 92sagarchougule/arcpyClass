
mytple = ("banana", "apple","cherry")

#print(mytple)

#1. Access Tuple items--------------------


#print(mytple[0])




#2. Negative Indexing---------------------


#print(mytple[-2])





#3.Range of Indexing----------------------


#print(mytple[1:2])









"""

#Convert the tuple into a list to be able to change it:-----------


mytpl = ("Mango",'Banana','Apple',"Sapota")

#print(mytpl)


#print("--------------------------------")

lst = list(mytpl)  #conversion of tuple to list

lst[1] = "mango"

#print(lst)

newtuple = tuple(lst)

print(newtuple)


"""










#4. Join Two Tuples ------------------------

'''
tuple1 = ("a","b","c")

tuple2 = (1,2,3)


tuple3 = tuple1 + tuple2

print(tuple3)



'''









#5. Multiply Tuples -------------------

'''
fruits = ("apple","banana","cherry","Mango","Lemon")

mytuple = fruits*5

print(mytuple)


'''










#ARITHMETIC OPERATORS---------------------

'''
print("Addition : 20+35 =>",20+35)

print("Substraction : 20-35 =>",20-35)

print("Multiplication : 20*35 =>",20*35)

print("Division : 20/2 =>",20/2)

print("Modulus : 20%3 =>",20%3)

print("Exponentation : 2**5 =>",2**5)

print("Floor Division : 21//4 =>",21//4)

'''












#ASSIGNMENT OPERATORS--------------------

a=100
#print(" = :",a)

#a = a - 10

#a-=10


#print("addition" ,a)

'''

a+=10               #100+10
print(" +=10:",a)


a-=5                #110-5
print(" -=:",a)


a*=2                #105*2
print(" *=:",a)


a/=2                #210/2
print(" /=:",a)

a**=2               #105**2
print(" **=:",a)


a//=2               #11025//2
print(" //=:",a)


a%=2                #5512%2
print(" %=:",a)

'''








#COMPARISON OPERATORS

x = 10
b = 20

'''

#print(x==b)    #Equal To --------------



#print(x!=b)    #Not Equal To-----------



#print(x>b)     #Greater Than-----------


#print(x<b)     #Greater Than-----------


print(x>=b)    #Greater Than or Equal To -----------

print(x<=b)    #Greater Than or Equal To-----------

'''








#LOGICAL OPERATORS  (and , or, not) --------------------------------------------

x = 20
y = 30

'''
#and

#if(x>10 and y<15):
    #print("X is More than 10 and Y is Less than 15")

  
#or
#if(x>10 or y<15):
    #print("X is More than 10 and Y is Less than 15")



#not
if(not x>30):
    print("x is not grader than 30")
    


if(not y>40):
    print("y is not grader than 40")
    print("y is not grader than 40")
    #print("yashwant",y,x)

'''
  










#IDENTITY OPERATORS        is, is not  ----------------------------------------

'''
x = 20
y = 20

print(x is y)  #is both are same?

print(x is not y) #is both are not same?

'''













#MEMBERSHIP OPERATORS   in / not in  ---------------------------------------

lst = ["Abhijeet","Bhushan","Prasad","Tushar","Harshal","Gaurav","Krushna"]

'''
print("Ram" in lst)

'''

print("Abhijeet" not in lst)
















#Sets   unordered, unchangeable, and unindexed ----------------------------------------------

'''
       You cannot access items in a set
       by referring to an index or a key
'''


'''
set = {"Abhijeet","Nitin","Bhushan","Prasad","Kailas","Sudhir", "Pallavi"}

#1.access items ----------

for i in set:
    #print(i)
    pass


#2.Add an item -----------

set.add("Sagar")

for i in set:
    #print(i)
    pass

#3. To remove an item in a set----

set.remove("Pallavi")

for i in set:
    #print(i)
    pass

'''




