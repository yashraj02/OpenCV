# FLANN based Matcher
import cv2 as cv

apple = cv.imread('../Images & Videos/apple.jpeg', 0)
fruits = cv.imread('../Images & Videos/fruits_basket.jfif', 0)
# creating sift obj
sift = cv.xfeatures2d.SIFT_create()
# detect & compute matches
kp1, des1 = sift.detectAndCompute(apple, None)
kp2, des2 = sift.detectAndCompute(fruits, None)
# FLANN
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(check=50)
flann = cv.FlannBasedMatcher(index_params, search_params)
# calculate matches by comparing them
# k is the number of best matches between both descriptors
# calculate in this case its top 2 matches
matches = flann.knnMatch(des1, des2, k=2)
matches_mask = [[0, 0] for i in range(len(matches))]
for i, (match1, match2) in enumerate(matches):
    # if match1 dist < 75% of match2 distance
    # then discriptor was good match else bad
    if match1.distance < 0.75 * match2.distance:
        matches_mask[i] = [1, 0]
# manually applying color to represent matches
draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matches_mask,
                   flags=0)  # flags=0 will show lines with points and flags=2 will show only lines
# draw matches
apple_matches = cv.drawMatchesKnn(apple, kp1, fruits, kp2, matches, None, **draw_params)  # None->no mask needed
cv.imshow('show', apple_matches)
cv.waitKey(0)
cv.destroyAllWindows()
