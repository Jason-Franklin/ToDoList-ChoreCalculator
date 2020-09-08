#-------------------------------------------------------------------------------
# Name:        To Do List & Chore Calculator
# Purpose:     Reminds a person what things or chores to do and calculates it
#
# Author:      Jason Franklin
#
# Created:     19/09/2019
#-------------------------------------------------------------------------------
#Here we are just printing information to the user interface

print ("Below I am telling someone how often they need to perform the chores per week")

#This function displays the number of times a chore needs to be done
#num_times = string, number of times chore

def chore_rep(chores, num_times):
    """This function lets someone know how often to do chores"""
    print(chores, num_times, "times.")

task_times = "7"
task1 = "Clean the dishes"
task2 = "Feed the dog"
task3 = "Make the bed"
chore_rep(task1, task_times)
chore_rep(task2, task_times)
chore_rep(task3, task_times)

print ("Below I have calculated how many times chores are being done weekly, monthly and yearly")

#Calculates how many chores are being done by the person weekly, monthly and yearly.

def multiply(x, y):

    calculation = x * y

    return calculation

print("Weekly:")

chores_week = multiply(7, 3)
print(chores_week)

print("Monthly:")

chores_month = multiply(21, 4)
print(chores_month)

print("Yearly:")

chores_year = multiply(84, 12)
print (chores_year)