# Logo Detection using YOLOv2

![alt text](https://cdn-images-1.medium.com/max/1100/1*uLoIU1s-lcvfOMBgRFZ1eg.png "YOLOv2 detection the logo of Google")



This repository provides the [code](https://github.com/akarshzingade/Logo-Detection-YOLOv2/blob/master/convert_annotations_for_yolov2.py) that converts FlickrLogo-47 Dataset annotations to the format required by YOLOv2. It also has the YOLOv2 [configuration file](https://github.com/akarshzingade/Logo-Detection-YOLOv2/blob/master/yolov2_logo_detection.cfg) used for the Logo Detection. You can read about how YOLOv2 works and how it was used to detect logos in FlickrLogo-47 Dataset in [this](https://medium.com/@akarshzingade/logo-detection-using-yolov2-8cda5a68740e) blog.  

The best weights for logo detection using YOLOv2 can be found [here](https://drive.google.com/open?id=1_Wg2hOKRiqWK6rpbCI6XbNLOC5YT1zyS)

# Instructions to use convert_annotations_for_yolov2.py

convert_annotations_for_yolov2.py takes in 4 arguments:
1) Path to the train/test folder containing the images and annotations of FlickrLogo-47 Dataset.
2) Path to the destination folder where the images and the converted annotations are to be stored. 
3) Path to store the train.txt/test.txt file and obj.names file. 
4) Name of the text file to store the paths to the images for train/test.

The 3rd argument is for a textfile that points to the train/test images for YOLOv2. 

## How to pass the arguments?

```python
python convert_annotations_for_yolov2.py --input_folder train --output_folder train_yolo --obj_names_path . --text_filename train
```

This will take './train' as the input folder (this should point to the train folder in FlickrLogo-47 dataset), './train_yolo' as the output folder where all the images and the converted annotations will be stored, '.' as the path to store train.txt and obj.names, and 'train' as the filename to store the image path for all train/test images. 

Make sure "className2ClassID.txt" file is in the same path as obj_names_path. 

Run convert_annotations_for_yolov2.py for both the train and test directory of FlickrLogo-47 dataset.
