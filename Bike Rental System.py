#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:58:22 2023

@author: shraddhakulkarni
"""
# Bike Rental System
import sys
import os
import pandas as pd
class Bike:
    def create(self):
        print("This is Create User function")
        custno = int(input("Enter Customer Number"))
        firstname = input("Enter Customer First Name")
        lastname = input("Enter Customer Last Name")
        phoneno = int(input("Enter Customer Phone Number"))
        address = input("Enter Customer address")
        dateofissue = input("Enter Date of Issue of Bike")
        noofdays = input("Enter number of days customer needs a bike")
        noofbikes = input("Enter number of bikes")
        customer = {'Custno':[custno],'firstname':[firstname],'lastname':[lastname],'phoneno':[phoneno],'address':[address],'dateofissue':[dateofissue],'noofdays':[noofdays],'noofbikes':[noofbikes]}
        self.df1 = pd.DataFrame(customer)
        exists = os.path.exists("/Users/sunilkulkarni/Desktop/customer.csv")
        self.df1.to_csv("/Users/sunilkulkarni/Desktop/customer.csv",index=False,mode='a',header=not exists)
        print("Customer created successfully")
    def retrieve(self):
        df2 = pd.read_csv("/Users/sunilkulkarni/Desktop/customer.csv")
        print(df2)
    def delete(self):
        delcustno = int(input("Enter customer number to delete"))
        df3 = pd.read_csv("/Users/sunilkulkarni/Desktop/customer.csv")
        #dataindex = df3[(df3.Custno == delcustno)].index
        #df3.drop(dataindex)
        df3 = df3[df3.Custno != delcustno]
        print(df3)
        #exists = os.path.exists("/Users/sunilkulkarni/Desktop/customer1.csv")
        df3.to_csv("/Users/sunilkulkarni/Desktop/customerdel.csv",index=False,mode='a',header=True)
        os.rename("/Users/sunilkulkarni/Desktop/customerdel.csv", "/Users/sunilkulkarni/Desktop/customer.csv")
        #os.remove("/Users/sunilkulkarni/Desktop/customer.csv")
        print("Customer deleted successfully")
    def bill(self):
        df5 = pd.read_csv("/Users/sunilkulkarni/Desktop/customer.csv")
        billcustno = int(input("Enter customer number for generating bill"))
        df5 = df5[df5.Custno == billcustno]
        bill1 = df5['noofdays'] * df5['noofbikes'] * 40
        print("Bill for entered customer id is",bill1)
    def bikes(self):
        maxbikes = 40
        df6 = pd.read_csv("/Users/sunilkulkarni/Desktop/customer.csv")
        sumbikes = sum(df6['noofbikes'])
        res = maxbikes - sumbikes
        print("Available number of bikes are ",res)
                
    #Displaying and choosing menu function    
    def menu(self):
        print("Bike Rental System")
        print("------------------")
        username = input("Enter username")
        pwd = input("Enter password")
        if username == "Shubhaam" and pwd == "shr":
            print("Login Successful")
        else:
            print("Login Unsuccessful")
            sys.exit()
        print("Menu")
        print("----")
        print("1.Customer CRUD operation")
        print("2.Show Customer Bill")
        print("3.Show available number of bikes")
        menuvar = int(input("Enter your choice"))
        if menuvar == 1:
            print("Customer CRUD operation")
            choice = input("Enter what operation you need to perform(C/R/U/D")
            if choice == "C":
                self.create()
            elif choice == "R":
                self.retrieve()
            elif choice == 'D':
                self.delete()
        elif menuvar == 2:
            self.bill()
        elif menuvar == 3:
            self.bikes()
        
        
obj1 = Bike()
obj1.menu()