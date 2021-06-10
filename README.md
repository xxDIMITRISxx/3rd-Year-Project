# Controlling a Robotic Arm Using a Webcam to Enable Social Interaction

A robot can be controlled or navigated by using hand gestures. Using image processing, signals are generated and then passed on the robot which can be navigated accordingly. 

### Generating data for training the model:

> running first `python generate-training-data.py --label label_value --sample num_of_samples`  
> This program will open a start video capture using the default camera of the machine.
> A red colour rectangle will be appear within the window:
> Performing hand gestures within the rectangle, the name of the gestures will be the `label_value` file.
> It will then capture `num_of_samples` number of images and store it under `training_data\label_value` directory
> Do this for the following labels: `1`, `2`, `3`, `4`, `5` and `empty`.
> More labels can be added.

### Generating the Traininig model:
> run `python train.py`
> This will create a model with the name `hand-gesture-model.h5` (NOTE: will replace the existing file if model is not renamed)
> This model has a base of a 5 layered `Convolutional2D` NN with `MaxPooling2D`.
> The top classification layer using a 50% `DropOut` and `Dense` Layer.
> The output layer is also a `Dense` Layer with `softmax` activation function.
> All other layers use `relu` activation.

### Hand gesture recognition procedure
> run `python hand-gesture.py`
> This will open up a video capture using the default camera of your machine.
> Hold your hand out in the indicated box.
> Using the model trained from `train.py` file, the hand gestures are predected.

### Assigned the values to robot
> within the hand-gesture.py file, assigned the labels 1-5 to the desired joint of the robot
> within the .ino file, assigned again the desired labels to each joint.

### Control the robot
> Gestures needs to be performed for couple of seconds without detecting other gestures, in order to send the right information to the robot.
> In order to move the joint to the desirable angle, a specific gesture needs to be performed in order to increasing a counter value. The counter value is printed to the screen. When the wishing angle has been reached, other gesture needs to be performed, in order to send the counter value to the robot, which is the desired angle to move the specific joint. 


### Credit
The Machine Learning code was from <b> mukeshmk</b>, repository can be found here: (https://github.com/mukeshmk/hand-gesture)
