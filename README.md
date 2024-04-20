# Yolov8 Instructions
## train.py
This program trains the provided dataset with YOLOv8 and returns an `.onnx` file
to use. I am using the `yolov8n` model. To configure the Roboflow dataset, you
need to create a `.env` file with the dataset config info (see `.env.example`).

There are 2 variables in the script that can be modified:
- `EPOCHS`: number of training epochs to run
- `IMGSZ`: resolution of the images in the dataset

## quantize.py
This is an untested script that converts the `.onnx` file from 32-bit floating
point (`fp32`) to 8-bit integers (`int8`). This reduces the size of the file
resulting in faster processing speeds.
