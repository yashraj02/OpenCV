# OpenCV
Open CV.

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
HSV - Cylindrical. Hue Saturation Value(0:179,0:255,0:255) 
-How to find HSV values to track?
->  green = np.uint8([[[0,255,0 ]]])
    hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
    print( hsv_green )
    [[[ 60 255 255]]]
    Now you take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively.
   
Masked image
First create a mask by specifying a "region of interest" i.e part of the image you want to be shown and assign it 255 (white color).
Then using the "bitwiseAnd" pass the "image & mask" to the function to derive masked image. Else everything will be black.
