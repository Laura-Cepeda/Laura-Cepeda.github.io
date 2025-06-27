height = 178
weight = 50

while weight <= 200:
    if weight <= 60:
        print("underweight")
    elif weight >= 60 and weight <79:
        print("perfect")
    elif weight >=79 and weight <95:
        print("overweight")
    else:
        print("obese")

    weight = weight + 1  


'''
EXERCISE: while loops
We need to use a while loop, in conjunction with an if statement to assess whether our user is: underweight, perfect weight, overweight or obese, according too the Body Mass Index.

To do this, create two variables:

Height - which should be equal to 178

Weight - which should be equal to 50

Then, use a while loop to a maximum weight of 200, incrementing the weight by 1 on each iteration of the loop.

The conditions you will need in order to assess someones weight is:

Under 60 = underweight

Between greater than or equal to 60 and less than 79 = perfect

Greater than or equal to 79 and less than 95 overweight

95 or greater = obese

You can find the solution to this in the next article
'''
