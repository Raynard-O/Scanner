import glob
import cv2
import os

IMGHEIGHT = 680
IMGWIDTH = 480
# Get all the images in the directory with tif format
img_list = glob.glob("*.tif")

count = 0

# Get each image
for img in img_list:
    # Open image in opencv
    file = cv2.imread(img, cv2.IMREAD_COLOR)

    # Resize image
    final_file = cv2.resize(file, (IMGHEIGHT, IMGWIDTH))

    # Check Image height and width and channels of new images
    dimensions = final_file.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]

    # Write file to image in jpeg
    count += 1
    cv2.imwrite(str(count) + ".jpeg", final_file)
    # Print out data
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)

# Remove all images with tif format
for img in img_list:
    os.remove(img)
