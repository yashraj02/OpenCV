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
