# Brute Force Matching with ORB Descriptors
import cv2 as cv

apple = cv.imread('../Images & Videos/apple.jpeg', 0)
fruits = cv.imread('../Images & Videos/fruits_rack.jfif', 0)

# Create Detecter obj
orb = cv.ORB_create()
# find key points & descriptor using this obj
kp1, descriptions1 = orb.detectAndCompute(apple, None)
kp2, descriptions2 = orb.detectAndCompute(fruits, None)
# Create matching object using Brute Force Matching
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)  # default params
# checking where the matches occur
matches = bf.match(descriptions1, descriptions2)
# now we sort this matches wrt distance | min the distance better the match
matches = sorted(matches, key=lambda x: x.distance)  # matches is list where one match obj contains distance attribute
print(len(matches))
# sticks both images together & draws lines based on matching
apple_matches = cv.drawMatches(apple, kp1, fruits, kp2, matches[:25], None,
                               flags=0)  # None->no mask needed | #flags=0 will show lines with points and flags=2 will show only lines
cv.imshow('show', apple_matches)
cv.waitKey(0)
cv.destroyAllWindows()
