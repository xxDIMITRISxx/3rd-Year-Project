# Hand Gesture Identifier (Numbers)

An attempt to identify number from hand gestures using OpenCV Image Recognition.

# To run the program on your machine:
1. clone the repo: `https://github.com/mukeshmk/hand-gesture.git`
2. create a virtual environment inside the folder: `python -m venv .venv`
3. activate the virtual environment: `.venv\Scripts\activate` (in case of Windows)
4. install the required packages for the game to run using: `pip install -r requirements.txt`
5. run the code: `python file_name.py`
6. make sure to `deactivate` once your done.

### To Generate data for training the model:

- run `python generate-training-data.py --label label_value --sample num_of_samples`  
- This program will open a start video capture using the default camera (`device: 0`) of your machine.
- In the video you will see a red colour rectangle:
- Hold you hand in the rectangle and make gesture as per `lable_value` make sure to throw in some variety.
- This will capture `num_of_samples` number of images and store it under `training_data\label_value` directory
- Do this for the following labels: `1`, `2`, `3`, `4`, `5` and `empty`.
- Check sample images provided under `sample_images` directory.

### To Train your own model:
- run `python train.py`
- This will create a model with the name `hand-gesture-model.h5` (NOTE: will replace the existing file if model is not renamed)
- This model has a base of a 5 layered `Convolutional2D` NN with `MaxPooling2D`.
- The top classification layer using a 50% `DropOut` and `Dense` Layer.
- The output layer is also a `Dense` Layer with `softmax` activation function.
- All other layers use `relu` activation.

### To have your hand gestures recognised on the fly:
- run 'python hand-gesture.py`
- This will open up a video capture using the default camera of your machine.
- Hold your hand out in the indicated box.
- Using the model trained from 'train.py` file, the hand gestures are predected.
