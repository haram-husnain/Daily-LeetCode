import math

def get_wider_aspect_ratio(a, b):

    a_split = a.split("x")
    w_a = int(a_split[0])
    h_a = int(a_split[1])

    b_split = b.split("x")
    w_b = int(b_split[0])
    h_b = int(b_split[1])

    if ((w_a/h_a)>(w_b/h_b)):
        gcd_a = math.gcd(w_a, h_a)
        reduced_w = w_a//gcd_a
        reduced_h = h_a//gcd_a
        return f"{reduced_w}:{reduced_h}"
    else:
        gcd_b = math.gcd(w_b, h_b)
        reduced_w = w_b//gcd_b
        reduced_h = h_b//gcd_b
        return f"{reduced_w}:{reduced_h}"

#Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height ratio.

#The given strings will be in the format "WxH", for example, "1920x1080".
#The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces to "16:9".
#Return a string in format "W:H", for example, "16:9".