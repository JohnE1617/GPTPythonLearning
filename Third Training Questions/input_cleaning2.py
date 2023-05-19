import bleach

def clean_input(usr_input):
    '''Takes user input as a argument and
    passes it through bleach to sanitize any 
    harmful syntax. returns the cleaned input'''
    allowed_tags = ['p','strong', 'b', 'code', 'del','em','a', 'img']
    allowed_attributes = {'a':['href','title'], 'img':['src']}
    cleaned_input = bleach.clean(usr_input, tags=allowed_tags, attributes=allowed_attributes, protocols={'a':['https']}, strip_comments=True)
    is_valid = usr_input == cleaned_input
    return cleaned_input, is_valid

request = input("enter your desired html to be displayed, don't do anything malicious please: ")
cleaned_input, is_valid = clean_input(request)
if is_valid:
    print(cleaned_input)
else:
    print("input is invalid, try again")
