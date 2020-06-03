# Brute Force Matching with SIFT Descriptors & Ratio Test
import cv2 as cv

apple = cv.imread('../Images & Videos/apple.jpeg', 0)
fruits = cv.imread('../Images & Videos/fruits_basket.jfif', 0)
# pip install opencv-python==3.4.2.16
# pip install opencv-contrib-python==3.4.2.16 for cv.xfeatures2d.SIFT_create()
# creating sift obj
sift = cv.xfeatures2d.SIFT_create()
# detect & compute matches
kp1, des1 = sift.detectAndCompute(apple, None)
kp2, des2 = sift.detectAndCompute(fruits, None)
# calculate matches by comparing them
bf = cv.BFMatcher()
# k is the number of best matches between both descriptors
# calculate in this case its top 2 matches
# if distance between this 2 matches are less then we consider this else we ignore
matches = bf.knnMatch(des1, des2, k=2)
good_match = []
for match1, match2 in matches:
    # if match1 dist < 75% of match2 distance
    # then discriptor was good match else bad
    if match1.distance < 0.75 * match2.distance:
        good_match.append([match1])
len(good_match)
# draw matches
apple_matches = cv.drawMatchesKnn(apple, kp1, fruits, kp2, good_match, None,
                                  flags=2)  # None->no mask needed | #flags=0 will show lines with points and flags=2 will show only lines
cv.imshow('show', apple_matches)
cv.waitKey(0)
cv.destroyAllWindows()
