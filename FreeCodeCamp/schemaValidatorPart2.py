def is_valid_schema(obj):
    if "username" not in obj or not isinstance(obj["username"], str): return False
    if "posts" not in obj or not isinstance(obj["posts"], int) or type(obj["posts"]) is bool: 
        return False
    if "verified" not in obj or not isinstance(obj["verified"], bool): return False
    return True

#Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
#{username: string, posts: number, verified: boolean}
#Extra keys are allowed