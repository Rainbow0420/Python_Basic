import random
# Python while Loop Statements
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

# The Infinite Loop
var = 1
def raw_input(s, n):
   return s + str(n)
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :", var)
   print ("You entered: ", num)
   var = 0
print ("Good bye!")

# Using else Statement with While Loop
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

# Single Statement Suites
flag = 1
while (flag): 
   print ('Given flag is really true!')
   flag = 0
print ("Good bye!")

# Python for Loop Statements
for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)

print ("Good bye!")

# Using else Statement with For Loop
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')
      break
print ("randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3))
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())