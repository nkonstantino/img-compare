from apscheduler.schedulers.blocking import BlockingScheduler
from sqlconnect import sqlConnect
from imgScore import imgScore
from weeblyConnect import weeblyConnect

#THINGS TO ADD:
#GENERATE OVERLAY IMAGE -> inside imgScore, cv2 to overlay 2 images? Look into tinting one red.
#Separate image types to their own tables -> Adjust DBs and queries. Maybe hard swap queries, or just create a var

#Setting up
imgPath = '/home/img-compare/images/'

jpg = imgScore(imgPath, "jpg/orig.jpg", "jpg/pretest.jpg", "jpg/pubtest.jpg")
png = imgScore(imgPath, "png/orig.png", "png/pretest.png", "png/pubtest.png")
bmp = imgScore(imgPath, "bmp/orig.bmp", "bmp/pretest.bmp", "bmp/pubtest.bmp")
sql = sqlConnect()
wc = weeblyConnect()
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
def run():
    #GET IMAGES, PUBLISH, GET IMAGES AGAIN
    wc.grabTestImages()

    #COMPARE IMAGE, THEN SEND RESULTS
    print("JPG")
    jpg.measure_images(0)
    sql.setResults("jpg",jpg.m,jpg.s,jpg.p, jpg.q, jpg.title)
    jpg.measure_images(1)
    sql.setResults("jpg",jpg.m,jpg.s,jpg.p, jpg.q, jpg.title)
    print("BMP")
    bmp.measure_images(0)
    sql.setResults("bmp",bmp.m,bmp.s,bmp.p, bmp.q, bmp.title)
    bmp.measure_images(1)
    sql.setResults("bmp",bmp.m,bmp.s,bmp.p, bmp.q, bmp.title)
    print("PNG")
    png.measure_images(0)
    sql.setResults("png",png.m,png.s,png.p, png.q, png.title)
    png.measure_images(1)
    sql.setResults("png",png.m,png.s,png.p, png.q, png.title)

sched.start()