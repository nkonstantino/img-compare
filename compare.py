from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
    #"Mean Squared Error" = Sum of the squared difference between two images
    # Images must have same dimension!
    err = np.sum((imageA.astype(float) - imageB.astype(float)) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1]) # shape returns the size of the array as a tuple. [1,2,3] = (3, ); [[1,2],[2,3],[3,4]] = (3, 2)

    #Lower the "err", the more similar they are
    return err

def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB) #Structural Similarity Measure
    print("MSE: "+m)
    print("SSIM: "+s)
    #set up the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: "+str(m)+", SSIM: "+str(s))

    #Show first image
    ax = fig.add_subplot(1,2,1)
    plt.imshow(imageA, cmap='gray')
    plt.axis("off")

    # Show Second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap='gray')
    plt.axis("off")

    #Show!
    plt.show()

# Load images
homeA = cv2.imread("images/imageA.jpg")
homeB = cv2.imread("images/imageB.jpg")
homeC = cv2.imread("images/homeC.png")

# Convert to grayscale
homeA = cv2.cvtColor(homeA, cv2.COLOR_BGR2GRAY)
homeB = cv2.cvtColor(homeB, cv2.COLOR_BGR2GRAY)
homeC = cv2.cvtColor(homeC, cv2.COLOR_BGR2GRAY)


# init the figure
fig = plt.figure("Images")
images = ("HomeA", homeA), ("HomeB", homeB), ("HomeC", homeC)

#loop over them
for (i, (name, image)) in enumerate(images):
    #show image
    ax = fig.add_subplot(1,3,i+1)
    ax.set_title(name)
    plt.imshow(image, cmap='gray')
    plt.axis("off")

#show the figure
plt.show()

#compare the images
compare_images(homeA, homeA, "A vs A")
compare_images(homeA, homeB, "A vs B")
compare_images(homeA, homeC, "A vs C")