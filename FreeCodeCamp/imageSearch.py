def image_search(images, term):
    results=[]
    for image in images:
        if term.casefold() in image.casefold():
            results.append(image)
    return results

image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog")
image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun")
image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG")
image_search(["cat.png", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat")

# Given an array of image names and a search term, return an array of image names containing the search term
# ignore the case when matching the search terms
# return the images in the same order they appear in the input array