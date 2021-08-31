# what is your score?

score = int(input("What is your test score?"))

#Determine the grade
if score >= 90:
    print("your grade is A.")
else:
    if score >= 80:
        print("Your grade is B.")
    else:
        if score >= 70:
            print("Your grade is C.")
        else:
            if score >=60:
                print("Your grade is D.")
            else:
                print("Your grade is F.")  


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')  