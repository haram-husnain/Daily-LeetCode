def convert(heading):

    if ("# " in heading):
        text = heading.split("# ", 1)[1].strip()
        hash_count = heading.split(text)[0].count("#")
        if (heading.startswith(" ") >= 0) and (0 < hash_count < 7):
            start_tag = "<h" + str(hash_count) + ">"
            end_tag = "</h" + str(hash_count) + ">"
            html = f"{start_tag}{text}{end_tag}"
            return html
        else:
            return "Invalid format"
    else:
        return "Invalid format"

convert("############# My heading")

# Start with zero or more spaces, followed by 1 to 6 hash characters (#) in a row, then
# At least one space. And finally, The heading text.
# The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

# If the given string doesn't have the exact format above, return "Invalid format".