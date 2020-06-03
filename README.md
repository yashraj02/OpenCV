# OpenCV
Open CV.

Ways to Isolate Image from background:  
-color detection  
-thresholding + counter(specify area)  
-canny  


1. While passing threshold image to findCounters() shapes/objects should be white in color while the background should be black. So before    finding contours, apply threshold or canny edge detection.

27 a. If you are using cv.TM_SQDIFF or cv.TM_SQDIFF_NORMED as comparison method, minimum value gives the best match. For all other methods       take maximum value as max value for drawing a rectangle.

27 b. Searching for an object which has multiple occurrences, cv.minMaxLoc() won't give you all the locations. In that case, we       will       use thresholding.

28. The Hough Line Transform is a transform used to detect any shapes/lines. If you can represent that shape in mathematical form. It can     detect the shape even if it is broken or distorted a little bit.To apply the Transform, first an edge detection pre-processing             is desirable.
    Line in image can be expressed with 2 variables. For eg.
    -Cartesian Coordianate System (Not able to represent vertical lines in an image) 
    -Polar Coordinate System (Preferred)
    Steps:
    -Edge detection eg. using Canny edge detector.
    -Mapping of edge points to Hough space & storage in an accumulator.
    -Interpretation of accumulator to yeild lines of infinite length. The interpretation is done by thresholding & possibly other              constraints.
    -Conversion of infinite to finite lines.
    2 Hough Line Transforms (to detect lines in image):
    -Standard : HoughLines method
    -Probabilistic : HoughLinesP method
    Tip: If you establish a higher threshold, fewer lines will be detected (since you will need more points to declare a line detected).
    
    -Filter2D()
        The operation works like this: keep this kernel above a pixel, add all the 25 pixels below this kernel, take the average, and           replace the central pixel with the new average value. This operation is continued for all the pixels in the image. Try this code         and check the result:

Tip: In matplot lib when an image is shown the axis goes from "0 to highest value horizontally(x-axis)" & "highest to 0 vertically(y-axis)"

Tip: The Bitwise operations should be applied on input images of same dimensions

Color Spaces : 
BGR
HSV - Cylindrical. Hue Saturation Value(0:179,0:255,0:255) for opencv.
-How to find HSV values to track?
->  green = np.uint8([[[0,255,0 ]]])
    hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
    print( hsv_green )
    [[[ 60 255 255]]]
    Now you take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively.
   
-Masked image
First create a mask by specifying a "inRange(img,lower,upper)" i.e part of the image that is within the hsv range.
In sometimes inRange requies too many trials to get desired mask.
Then using the "bitwiseAnd" we merge "image & mask" & the function returns only the part of image which is common in "image & mask". Else everything will be black.


cv.filter2D(img,-1,kernel)
kernel = np.ones((5,5),np.float32)/25
The operation works like this: keep this kernel above a pixel, add all the 25 pixels below this kernel, take the average, and replace the central pixel with the new average value. This operation is continued for all the pixels in the image.

Morphological Operations: Removing noise & finding bumps in image. Process images based on shapes.
-Dilation: Operation causes bright regions within an image to “grow”.
-Erosion: Operation causes bright regions within an image to “shrink”.
First dilate & then pass the image to erode.

#Process: Blur => Gray => Canny => (Optional: dilate/erode) => findContours => drawContours
=> [If there is still noise left in an image then calculate "cv2.contourArea() > any_value"]
=> [If you want to determine the shape of contour then "cv2.approxPolyDP(cnt,0.01*(cv2.arcLength(cnt,True)))"]
Contours: Curve joining all the continuous points (along the boundary), having same color.
Used for shape analysis and object detection and recognition.
Provide binary images (threshold or canny).
Object to be found s`hould be white and background should be black.
Sample: findContours() & drawContours()
ret, thresh = cv.threshold(imgray, 127, 255`, 0)
im2, contours, hierarchy = cv. findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
#when finding outer edges use "mode = cv.RETR_EXTERNAL"
#method = cv.CHAIN_APPROX_NONE(not so memory efficient)
cv.drawContours(img, contours, -1, (0,255,0), 3)


#Process: Convert to Gray => Blur => Canny => Morphological Operations (Dialate => Erode) => Contours(Find => Draw)
Tip: Convolution in images is an operation where a pixel color is changed depending on the colors of the neighbors of that pixel. 
Image Blurring/Smoothing
Useful for removing noise/edges e.g. Salt & Pepper Noise where an image has dark pixels in bright region & bright pixels in dark region.
1.Average Blurring: blur = cv.blur(img,(5,5))
2.Gaussian Blurring blur = cv.GaussianBlur(img,(5,5),0) //0 is for both sigmaX & sigmaY //kernel should be odd val & with increase in kernel the blur increases.
3.median = cv.medianBlur(img,5) //in above methods pixel val could be a new one but in medianBlur its some pixel value from image. Highly useful in cases of salt & pepper images.
4.blur = cv.bilateralFilter(img,9,75,75) //highly effective in noise removal while keeping edges sharp.




Wrap perspective/Bird View:
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

#Normalize
cv::normalize(_src, dst, 0, 255, NORM_MINMAX, CV_8UC1); //need to make a copy of img and pass to dst. This copy img will be normalized.
NORM_MINMAX sets output image between range: 0-255 [0 is alpha(min val) & 255 is beta(max val)]
