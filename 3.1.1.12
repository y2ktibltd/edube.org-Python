#!/bin/python3
year = int(input("Enter a year: "))
leap=False

if year<1582:
    print("Not in Gregorian Calendar")
    quit()

if not year%4:leap=True
if not year%100:leap=False
if not year%100 and not year%400:leap=True

if leap:print("Leap Year")
else:print("Common Year")
