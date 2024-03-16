import os
from dotenv import load_dotenv
from ultralytics import YOLO
from roboflow import Roboflow

"""Download Roboflow Dataset"""
# fetch env variables
load_dotenv()
ROBOFLOW_API = os.environ.get('ROBOFLOW_API')
ROBOFLOW_WORKSPACE = os.environ.get('ROBOFLOW_WORKSPACE')
ROBOFLOW_PROJECT = os.environ.get('ROBOFLOW_PROJECT')

# download dataset
rf = Roboflow(ROBOFLOW_API)
project = rf.workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)

# download latest version
PROJECT_VERSION = project.versions()[0].version
print(f'Downloading version {PROJECT_VERSION}')
project.version(PROJECT_VERSION).download(model_format='yolov8', location='./dataset')

"""Train YOLOv8"""
EPOCHS = 5
IMGSZ = 640

model = YOLO('yolov8n.pt')
model.train(
    data='./dataset/data.yaml',
    epochs=EPOCHS,
    imgsz=IMGSZ
)

model.export(format='onnx')
