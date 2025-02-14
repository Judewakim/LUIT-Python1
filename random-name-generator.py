#Several departments share an AWS environment. 
#You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
#Use Python to create your unique EC2 names that the users can then attach to the instances. 

#FOUNDATIONAL
#The Python Script should:
#Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.
#Allow the user to input the name of their department that is used in the unique name.
#Generate random characters and numbers that will be included in the unique name.
#Push your code to GitHub and include the link in your LinkedIn write up.
#ADVANCED
#The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
#List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. 
#Be sure to account for incorrect upper or lowercase letters in the correct department. 
#Example: a user inputs accounting vs Accounting.
#COMPLEX
#Turn the above into a Function and execute the Function to verify it works


def generate_random_name():
    # Import necessary modules: random for generating random values, string for predefined character sets
    import random
    import string

    # Prompt the user for their department
    department = input("What department are you a part of?\n\nOptions:\nMarketing\nAccounting\nFinOps\netc.\n\n")

    # Check if the department input is valid (lowercased for case insensitivity)
    if department.lower() not in ["marketing", "accounting", "finops"]:
        # If the department is not valid, display a message and exit the program
        print("\nSorry, you should not use this name generator.\nExiting... ")
        exit()  # Stop the program
    else: 
        # If the department is valid, ask how many random names the user wants to generate
        number_of_instances = int(input("\nHow many instances do you want to create? "))

        length = 10  # Set the length of each random name

        # Loop to create the specified number of random names
        for _ in range(number_of_instances):
            # Generate a random string consisting of letters and digits of the specified length
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

            # Create a full name by combining the department and the random string
            full_name = f"{department}.{random_name}"

            # Print the generated full name
            print(full_name)

# Call the function to execute the name generation
generate_random_name()
