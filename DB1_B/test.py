import glob
import cv2

IMGHEIGHT = 680
IMGWIDTH = 480
# Get all the images in the directory with tif format
img_list = glob.glob("*.tif")

# Get each image
for img in img_list:
    # Open image in opencv
    file = cv2.imread(img)#, cv2.IMREAD_COLOR)

    # Resize image
    # final_file = cv2.resize(file, (IMGWIDTH, IMGHEIGHT))

    # Check Image height and width and channels of new images
    dimensions = file.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]

    # Print out data
    print('Image Height       : ', height)
    print('Image Width        : ', width)
    print('Number of Channels : ', channels)
