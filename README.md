# img-compare
Comparing Image Quality
## How To Use
Using this tool is as simple as just running app.py, which will set it to wait every 60 minutes before running through the process of pulling images, comparing them, then storing the results.

## Requirements
The python environment you use to execute it will require the following to be installed (most of which are available via pip):
* apscheduler
* mysql
* cv2
* sklearn
* skimage
* requests
* Other stuff like datetime, math, urllib, etc should be in by default

Also requires a mysql database set up (I used XAMPP)

## Setting up
* _app.py_ - This is where everything comes together.  "imgPath" variable needs to be set to point to the images folder.
* _weeblyconnect.py_ - This is where we visit a weebly site in order to pull the images. A lot of things will need to be updated here, such as "_storeagepath", the image URLs you want to pull if you don't like mine, and if the token on the editor post requests has expired, it'll need a fresh cookie pulled from Charles.
* _imgScore.py_ - This file should require the least amount of changing, if at all.  It just handles the calculations between images.
* _sqlconnect.py_ - You'll need to update any differences in user/password/host/database config stuff, but that's about it.
