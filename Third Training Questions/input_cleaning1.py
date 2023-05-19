import bleach

def clean_input(usr_input):
    '''Takes user input as a argument and
    passes it through bleach to sanitize any 
    harmful syntax. returns the cleaned input'''
    cleaned_input = bleach.clean(usr_input)
    if usr_input == cleaned_input:
        print("Thanks for following directions!")
    else:
        print("I knew I couldn't trust you.")
    return cleaned_input

request = input("enter your desired html to be displayed, don't do anything malicious please: ")
print(clean_input(request))
