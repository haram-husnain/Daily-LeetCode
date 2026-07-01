def is_valid_schema(obj):
    allowed_roles = ["user", "creator", "moderator", "staff", "admin"]

    if "username" not in obj or not isinstance(obj["username"], str): return False
    if "posts" not in obj or not isinstance(obj["posts"], int) or type(obj["posts"]) is bool:
        return False
    
    if "verified" not in obj or not isinstance(obj["verified"], bool): return False
    if "role" not in obj or not isinstance(obj["role"], str) or obj["role"] not in allowed_roles:
        return False
    
    if "supporter" not in obj: pass
    elif not isinstance(obj["supporter"], bool): 
        return False
    
    return True


#The question mark ? after supporter means that the field is optional, but is the specified type if it exists
# supporter?: boolean