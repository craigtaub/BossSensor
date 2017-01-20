# DashSensor
Change picture depending who is looking at the screen.

## Requirements

* WebCamera
* Python3.5
* OSX
* Anaconda
* Many boss image and other person image

## Setup
Decompose video into many images.

```
ffmpeg -i me1.mov -r 4 output_%04d.jpg
```


## Usage
First, Training.

```
$ python train.py
```


Second, start Sensor.

```
$ python run.py
```

## Install
Install OpenCV, PyQt4, Anaconda.

```
conda create -n venv python=3.5
source activate venv
conda install -c https://conda.anaconda.org/menpo opencv3
conda install -c conda-forge tensorflow
pip install -r requirements.txt
```

Change Keras backend from Theano to TensorFlow.

## Licence

[MIT](https://github.com/craigtaub/DashSensor/blob/master/LICENSE)
