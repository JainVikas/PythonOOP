# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:27:28 2017

@author: vikas
"""

class PreciousStones:
    def __init__(self):
        #intialize stoneList
        self.collectionList=[]
    def addCollection(self, stoneName):
        #updateList function
        if len(self.collectionList)>=5:
            #if more than 5 stones, remove first one and add new
            del self.collectionList[0]
            self.collectionList.append(stoneName)
        else: 
            self.collectionList.append(stoneName)
        print(self.collectionList)
    
    
        

st= PreciousStones()
st.collectionList

type(st)

#Exercise 3
"""
    Similar to a library management system, write a program to
    provide layers of abstraction for a car rental system.
    Your program should perform the following:
    1. Hatchback, Sedan, SUV should be type of cars that are
    being provided for rent
    2. Cost per day:
    Hatchback - $30
    Sedan - $50
    SUV - $100
    3. Give a prompt to the customer asking him the type of car
    and the number of days he would like to borrow and provide the
    fare details to the user.
"""

class Cars:
    def __init__(self):
        self.carCost={"hatchback":30, "Sedan":50, "SUV":100}
    
    def displayCar(self):
        print()
        print("Available car types:")
        for car in self.carCost:
            print(car)
    
    def rentalCost(self, car, days):
        if car in self.carCost:
            print("cost to borrow "+ car+ " for "+ str(days)+ " days is $" +str(self.carCost[car]*days))
    
class Customer:
    def requestCar(self):
        print("Enter the type of car you would like to borrow")
        self.car=input()
        print("Enter the number of days")
        self.days= int(input())
        return self.car, self.days
    
car= Cars()
cust=Customer()
while True:
    print("Enter 1 to display cars")
    print("Enter 2 to request car")
    print("Enter 3 to exit")
    userChoice = int(input())
    
    if userChoice is 1:
        car.displayCar()
    elif userChoice is 2:
        cartype, days = cust.requestCar()
        car.rentalCost(cartype,days)
    elif userChoice is 3:
        quit()


'''
EXERCISE - INHERITANCE
Write an object oriented program that performs the following tasks:
1. Create a class called Chair from the base class Furniture
2. Teakwood should be the type of furniture that is used by all furnitures by
default
3. The user can be given an option to change the type of wood used for chair if
he wishes to
4. The number of legs of a chair should be a property that should not be altered
outside the class'''

class Furniture:
    typeOfWood="Teakwood"

class Chair(Furniture):
    __numberOfLegs=4
    def changeTypeOfWood(self,wood):
        self.typeOfWood= wood
    def displayChairDetails(self):
        print(" you have selected chair with {} wood and it has {} legs".format(self.typeOfWood, self.__numberOfLegs))
        
    
ch=Chair()
#print(" number of legs: ", ch._numberOfLegs)

userInput = input("Would you like to change the type of wood? Y/N \n")
if userInput=='Y':
    wood=input ('please enter the wood type: \n')
    ch.changeTypeOfWood(wood)
    print( "updated type of wood is {}".format(ch.typeOfWood))
    ch.displayChairDetails()
    
'''
EXERCISE - POLYMORPHISM
Create a class called Square and perform the following tasks -
(i) Create two objects for this class squareOne and
squareTwo
(ii) Find the result of side of squareOne to the power of side
of squareTwo
Example: If squareOne has length of 2cm each side and
squareTwo has a length of 4cm each side, squareOne **
squareTwo should return 16, which is 2 to the power of 4.

'''
#overloading
class Square:
    def __init__(self,side):
        self.side= side
        
    def __pow__(side1,side2):
        return squareOne.side**squareTwo.side
squareOne= Square(2)
squareTwo= Square(4)

print("output is {}, which is {} to the power of {}".format(squareOne.side**squareTwo.side, squareOne.side, squareTwo.side))
