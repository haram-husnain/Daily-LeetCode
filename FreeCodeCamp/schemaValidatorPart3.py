def is_valid_schema(obj):
    allowed_roles = ["user", "creator", "moderator", "staff", "admin"]

    if "username" not in obj or not isinstance(obj["username"], str): return False
    if "posts" not in obj or not isinstance(obj["posts"], int) or type(obj["posts"]) is bool:
        return False
    if "verified" not in obj or not isinstance(obj["verified"], bool): return False
    if "role" not in obj or not isinstance(obj["role"], str) or obj["role"] not in allowed_roles:
        return False
    return True

#Roles = "user" | "creator" | "moderator" | "staff" | "admin"
#{username: string, posts: number, verified: boolean, role: Roles}
#The pipe (|) symbol means "or". role must be one of the listed Roles values.
#Extra keys are allowed