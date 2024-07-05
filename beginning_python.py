# ******* EVERY THING IN PYTHON IS OBJECT *******  



"""spam_amount =0
print("Spam is a food")

spam_amount += 4

if spam_amount > 0:
    print("I Don't want Spam Anymore")

vikking_song = "Spam " * spam_amount
print(vikking_song)

#here we are calculating height of person when he wears his hat 
hat_height_cm = 20
my_height_cm = 167

my_height_meters = (hat_height_cm + my_height_cm)/100
print("My height when i wear the hat is ",my_height_meters)

my_height_in_meters = my_height_cm/100
print(my_height_in_meters)

#function Default Arguments
def greet(who="colin"):
    print('hello', who)
greet()
greet("Feels good to code")
greet("world!")


#Function Applied to function
Functions that operate on other functions are called "higher-order functions."
def mult_by_five(x):
    return 5*x
def call(fn, arg):
    return fn(arg)
def squared_call(fn, arg):
    return fn(fn(arg))
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five,1),
    sep='\n'
)

def mod_5(x):
    #Return the remainder of x after dividing by 5
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
"""

# def round_fn(num):
    
#     return round(num, 2)    


# result =round_fn(42.34627)
# print(result)

#boolean function

# def election_run(age):
#     return age>= 35
# print('can a 19 year old take election_run in us', election_run(19))
# print('can a 36 year old take election_run in us', election_run(36))

# is odd function
# def is_odd(x):
#     return (x % 2) == 1
# print('is 100 odd number', is_odd(100))
# print('is 1 odd number', is_odd(1))

#condiational bool
# def election_run(age, us_citizen):
#     return us_citizen and (age>=35)

# print('can 26 year old be president',election_run(26,True))
# print('can 34 year old be president',election_run(34,False))
# print('can 54 year old be president',election_run(54,True))

# prepared_for_weather = have_umbrella or (raining <5 and have_hood) or not (raining>0 and its_workday)

# if elif else

# def inspect(x):
#     if x == 0:
#         print(x,"its Zero")
#     elif x >0:
#         print(x,'Its Positive')
#     elif x < 0:
#         print(x,"Its Negative")
#     else:
#         print(x,"x is unlike anything i have ever seen")
# inspect(0)
# # inspect(-3)

# def only_pos(x):
#     if x >0:
#         print("only printed when x is positive: x=",x)
#         print("still printed when x is positive: x=",x)
#     print("regardless of any number printed x value =",x)

# only_pos(1)
# only_pos(0)

#listd are  mutable
# list[], list of list[[]], indexing [0][1], slicing[1:-1]
# slicing
# planet = [0:-1] from index 1 to last second index
# planet = [1:-1] from index 2 to last second index
# planet = [0:3] from index 1 to last 3 index
# planet = [3:] from index 4 to last  index
# planet = [-3: ] from  last  3 index  to last 

#changing list
# rename it
# planet[3] = 'Mongolia'
# it will change the value of that index

# changing with slicing
# planet[:3] = ['mur','vee','ur']
# print(planet)
# planet[:4] = ['Muercury', 'venus', 'Earth','Mars']

# list function
# ### len()
#  ### sorted() //returns the sorted values of the list
#  ##$ sum()
# ### max()


#  list method
# 'A function attached to an object is called a method. '
#append()
# planet.append()
# planet.pop()

#  Searching List
#planet.index('earth')
#

# in operator
# 'Earth' in planet

########## TUPLES
# parenthesis ()
# access with dot .
# im-mutable can't be changed
# tup = (1,2,3)

# x=0.125
# print(x.as_integer_ratio())

# as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple:

# loops and comprehensions
planets = ['Mercury','Venus','Earth', 'Mars','Jupiter','Saturn','Uranus','Neptune']

# for planet in planets:
#     print(planet, end=' ')

# multiplicands = (2,3,4,3,4,3,4,5)
# product = 1
# for mul in multiplicands:
#     product *=mul
# print(product)



# str = 'Sometimes Life is Simple But It is very Difficult'
# for char in str:
#     if char.isupper():
#         print(char, end=" ")

# for i in range(5):
#     print("lets lean and earn its life. i=", i)

# i=34
# while i <= 100:
#     print(i, end=' ')
#     i += 1

# list comprehensions
# sq = [n**2 for n in range(10)]
# print(sq)

# w/o comprehensions

# squ= []
# for i in range(20):
#     squ.append(i**2)
# print(squ)


# short_planet = [planet for planet in planets if len(planet)<6]
# print(short_planet)

# loud = [planet.upper() + '!' for planet in planets if len(planet)< 6]
# print(loud)



#  count negative numbers

# def count_neg(nums):
    
#     n_negative = 0
#     for num in nums:
#         if num < 0:
#             n_negative +=1
#     return n_negative

# print(count_neg([2,4,5,-5,-1,-6]))

# #  with len()
# def len_count(nums):
#     return len([num for num in nums if num<0])
# print(len_count([2,4,5,-5,-1,-6,-9]))

### STRINGS ###
#  methods .split() .join()
#  escape char 
# .endswith() .startswith()
#  '/'.join([Month, Date, year])

# words = ['Pluto', 'was', 'a', 'planet']
# joinned =' ⭐ '.join([word.upper() for word in words])
# print(joinned)


# str concatination
# planet = 'Pluto'
# position = 9
# print(planet + " you will always be in " + str(position) + ' position' ) 

# # Formatting
# print('{} you will be in {} position for me'.format(planet, position))


planet_initials  = {planet:planet[0] for planet in planets}
# print(planet_initials)
# values_in = ' '.join(sorted(planet_initials.values()))
# print(values_in)

for planet, initial in planets, planet_initials.items():
     print("{} begins with \"{}\"".format(planet.rjust(10), initial))