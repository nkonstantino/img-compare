from sklearn.metrics import mean_squared_error
from skimage.measure import compare_ssim as ssim
import math
import cv2
import imutils
from datetime import datetime

class imgScore:

    def __init__(self, imgDir, origImg, prepubImg, postpubImg):
        self.imgDir = imgDir
        self.origImgPath = origImg
        self.prepubImgPath = prepubImg
        self.postpubImgPath = postpubImg
        self.compImgPath = None
        self.filetype = origImg[:3]
        self.m = None
        self.p = None
        self.s = None
        self.q = None
        self.diff = None
        self.hold = None
        self.title = ""
        self._pixel = 255  # Pixel peak noise possibility



    def prep_images(self):
        self.origImg = cv2.imread(self.imgDir+self.origImgPath) # load image
        self.hold = cv2.imread(self.imgDir + self.origImgPath)  # hold a color version of the image
        self.origImg = cv2.cvtColor(self.origImg, cv2.COLOR_BGR2GRAY) # convert image to greyscale
        targetH, targetW = self.origImg.shape[:2] #get original image size


        self.prepubImg = cv2.imread(self.imgDir+self.prepubImgPath)  # load image
        self.prepubImg = cv2.cvtColor(self.prepubImg, cv2.COLOR_BGR2GRAY)  # convert image to greyscale
        self.prepubImg = cv2.resize(self.prepubImg, (targetW, targetH)) #scale image to original size

        self.postpubImg = cv2.imread(self.imgDir+self.postpubImgPath)  # load image
        self.postpubImg = cv2.cvtColor(self.postpubImg, cv2.COLOR_BGR2GRAY)  # convert image to greyscale
        self.postpubImg = cv2.resize(self.postpubImg, (targetW, targetH)) #scale image to original size



    def mse(self, imageA, imageB):
        #"Mean Squared Error" = Sum of the squared difference between two images
        # Images must have same dimension! It compares each image as a value matrix!
        err = mean_squared_error(imageA.astype(float), imageB.astype(float))
        #Lower the "err", the more similar they are
        return err

    def psnr(self, mse):
        #Closer to 100 is better
        if mse == 0:
            val = 100
        else:
            val = 20 * math.log(self._pixel / math.sqrt(mse), 10)
        return val

    def compare_images(self, imageA, imageB, title): #NEED TO NORMALIZE BETWEEN 100% IMAGE QUALITY
        self.m = self.mse(imageA, imageB) #Mean Square Error (Higher is worse)
        self.p = self.psnr(self.m) #Peak Noise Signal Ratio (Higher is better)
        (self.s,self.diff) = ssim(imageA, imageB, full=True) #Structural Similarity Measure (1.0 is best)
        self.q = 100 * self.s

        self.m = str(self.m)
        self.p = str(self.p)
        self.s = str(self.s)
        self.q = str(self.q)
        self.title = title

        print(title)
        print(str(imageA.shape[:2]))
        print("------------")
        print("MSE: "+self.m)
        print("PSNR: "+self.p)
        print("SSIM: "+self.s)
        print("Quality Score: "+self.q+"%")
        print("")

    def createComposite(self, img, filetype):
        print(filetype)
        self.diff = (self.diff*255).astype("uint8")
        if filetype == "png" or "jpg":
            thresh = cv2.threshold(self.diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        if filetype == "bmp":
            thresh = cv2.threshold(self.diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        #THRESH_BINARY is good for BMP, THRESH_BINARY_INV is good for PNG, and possibly JPG
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        for c in cnts:
            # compute bounding boxes of countour and draw it
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(self.hold, (x, y), (x + w, y + h), (0, 0, 255), -1)
        color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        comp = cv2.addWeighted(color, 0.6, self.hold, 0.4,0)
        # cv2.imshow("Difference from Orig",comp)
        # cv2.waitKey(0)
        cv2.imwrite(self.imgDir+"results/"+str(datetime.now())+"."+filetype, comp)

    def measure_images(self, imgset=0):
        self.prep_images()
        if imgset == 0: #Compare vs Orig
            self.compare_images(self.origImg, self.postpubImg, "Orig vs New")
            self.createComposite(self.postpubImg, self.filetype)
        elif imgset == 1: #Compare vs Previous
            self.compare_images(self.prepubImg, self.postpubImg, "Previous vs New")
            self.createComposite(self.postpubImg, self.filetype)

s = imgScore('/Users/nick.k/Documents/Automation/img-compare/images/', "bmp/orig.bmp", "bmp/pretest.bmp", "bmp/pubtest.bmp")
# s = imgScore('/Users/nick.k/Documents/Automation/img-compare/images/', "jpg/orig.jpg", "jpg/pretest.jpg", "jpg/pubtest.jpg")
# s = imgScore('/Users/nick.k/Documents/Automation/img-compare/images/', "png/orig.png", "png/pretest.png", "png/pubtest.png")
s.measure_images()