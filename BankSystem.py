# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:06:31 2018

@author: vikas
"""
import random
class Accounts:
    accountType= 'Savings'
    details={}

class newAccount(Accounts):
    def __init__(self, name, initialDeposit):
        self.accountNumber= random.randint(10000,99999)
        self.name = name
        self.balance= initialDeposit
        super().details[self.accountNumber]= [self.name, self.balance]
        print("Congratulation! Your account number is {}".format(self.accountNumber))
        
class accessAccount(Accounts):
    def __init__(self, accountNum, name):
        print(self.details)
        
        if (accountNum in self.details.keys()) and (name == self.details[accountNum][0]):
            print("Account validated")
            self.accountNumber= accountNum
            self.name=name
            self.balance=self.details[self.accountNumber][1]
        else:
            print("Sorry! this account doesn't exist")
    def displayBalance(self):
        return self.balance
    
    def depositMoney(self, amount):
        super().details[self.accountNumber][1]= self.balance + amount
        self.balance= self.balance + amount
    
    def withdrawMoney(self, amount):
        if amount <= self.balance:
            super().details[self.accountNumber][1]= self.balance - amount
            self.balance= self.balance - amount
        else:
            print("You don't have sufficient balance to withdraw")
            
            
            
while True:    
    print("Enter 1 to open new saving account")
    print("Enter 2 to access existing saving account")
    print("Enter 3 to exit")
    
    userChoice= int(input())
    if userChoice==1:
        name=input("Please provide your name: ")
        amount= int(input ("enter the initial deposit amount: " ))
        account= newAccount(name,amount)
    
    elif userChoice==2:
        name=input("Please provide your name: ")
        accountNumber= int(input ("please enter your account number: " ))
        existingAccount = accessAccount(accountNumber, name)
        while True:
            print("Enter 1 to display balance")
            print("Enter 2 to deposit money")
            print("Enter 3 to withdraw money")
            print("Enter 4 to exit")
            userInput= int(input())
            if userInput==1:
                print("your current balance is {}".format(existingAccount.displayBalance()))
            elif userInput==2:
                amount= int(input ("enter the amount: " ))
                existingAccount.depositMoney(amount)
            elif userInput==3:
                amount= int(input ("enter the amount to be withdrawn: " ))
                existingAccount.withdrawMoney(amount)
            elif userInput==4:
                break
    elif userChoice==3:
        break