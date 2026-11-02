def navigate(commands):

    back=[]
    forward=[]
    current = "Home"

    for step in commands:
        if step == "Forward" and forward:   # if foreward is not empty
            back.append(current)            # push the current page to back
            current = forward.pop()         # set the next page as current & remove from stack
            
        elif step == "Back" and back:       # if back is not empty
            forward.append(current)         # push the current page to forward
            current = back.pop()            # set the prev page as current & remove from stack
            
        elif step.startswith("Visit "):
            back.append(current)    # push the prev page to back
            current = step[6:]      # move to new page
            forward.clear()         # clear next pages

    print(f"\nFinal Page: {current}") # the default will always be Home
    return current
 
navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"])

# On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.
# Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:
# You always start on the "Home" page, which will not be included in the commands array. Valid commands are:
# "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
# "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
# "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

