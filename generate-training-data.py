import os
import cv2
import argparse

TRAINING_DATA_DIR = "training_data"

def capture_images(label, label_path, sample_size):
    # open camera (device : 0) in video capture mode
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video")

    capture = False
    count = 0

    while True:
        # read the image from the camera
        # returns ret, frame - 
        # where ret is a boolean True - a image was retrived; False - no image retrived
        # frame contains the image retrived
        ret, frame = cap.read()
        # checking if the image was retrived
        if not ret:
            print("Error getting image")
            continue

        # if required number of images have been captured
        if count == sample_size:
            break
        
        # to start capturing images for training once the key is hit
        if capture:
            # getting the region of intrest for capture
            capture_region = frame[75:300, 75:300]
            # creating the image path
            img_path = os.path.join(label_path, '{}.jpg'.format(count + 1))
            # saving the image
            cv2.imwrite(img_path, capture_region)
            count += 1
        
        # drawing a rectangle to indicate which section of the image is being saved 
        # params: img, point1, point 2, colour, thinkness of line
        cv2.rectangle(frame, (75, 75), (300, 300), (0, 0, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        # for displaying the text
        cv2.putText(frame, "Images Collected: {}".format(count), (70, 325), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

        # Displaying the Images which are to be catured
        cv2.imshow("Collecting Images", frame)

        k = cv2.waitKey(10)
        if k == ord('c'):
            capture = not capture
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', help='label of the image being captured', type=str)
    parser.add_argument('--samples', help='number of samples to be captured for that label', type=int)
    args = parser.parse_args()

    # args verification
    if args.label is None:
        print("Please the label of the image to capture")
        exit(1)

    if args.samples is None:
        print("Please specify the sample size (count) of the image to be captured")
        exit(1)

    # training_data folder creation
    if not os.path.exists(TRAINING_DATA_DIR):
        print("Creating output directory " + TRAINING_DATA_DIR)
        os.makedirs(TRAINING_DATA_DIR)

    label_path = TRAINING_DATA_DIR + "\\" + args.label
    # label folder creattion
    if not os.path.exists(label_path):
        print("Creating output directory " + label_path)
        os.makedirs(label_path)
    else:
        print("Label directory exists: generated images will be appended to the existing data")

    capture_images(args.label, label_path, args.samples)


if __name__ == "__main__":
    main()
