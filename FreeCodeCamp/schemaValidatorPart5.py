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

    if "badges" not in obj or not isinstance(obj["badges"], list) or any(not isinstance(badge, str) for badge in obj["badges"]):
        return False

    return True

is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": [18,17]})
#The brackets [] after string means that badges should be an array of strings or empty
#badges: string[]