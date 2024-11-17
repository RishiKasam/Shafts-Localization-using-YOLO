# Localization-of-shafts-using-YOLOv2-algorithm
YOLO
YOLO is a single shot object detection algorithm. In this algorithm the input image is divided into equally sized grids say (s*s).  Bounding box and class of objects present in every grid predicted. In our project Bounding Boxes replaced by Key point pairs. Every grid cell predicts Key point pairs and we have only one object type which is shaft so, we have just one class.  
Features of YOLO
YOLO is computationally very fast, can be used on real time environment.
Globally processing the entire image once with a single CNN.
Learn generalizable representations.
Maintains a high accuracy range 

YOLO Algorithm
We split the image into an (S*S) grid. Grid cell is responsible for detecting an object. If the centre /midpoint of an object falls into a grid cell, that cell is responsible for detection the object. Each cell predicts Key point pairs with confidence score. Confident score means how confident the model is that Key point pairs have an object and how accurately the key point pair has predicted the object(how accurately X0,y0 and alpha are estimated), (x0,y0) are centre point and alpha is angle of shaft. Each cell also predicts class probability.


Suppose a grid in YOLO CNN is of size 32*32.
In the output, each Key point pair is represented by 5 numbers (class probability, X0 , Y0, alpha, confidence score)
