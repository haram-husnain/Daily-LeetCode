def is_valid_schema(obj):

    if "username" not in obj: 
        #print("False")
        return False
    if not isinstance(obj["username"], str): 
        #print("False")
        return False
    #print("True")
    return True

is_valid_schema({"username": "bob"})
is_valid_schema({"username": "jen", "posts": 30})
is_valid_schema({"username": ""})
is_valid_schema({"username": 7})
is_valid_schema({"posts": 25})

#Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
#{username: string }    #Extra keys are allowed
