import mysql.connector
class sqlConnect:

    def getResults(self, filetype):
        cnx = mysql.connector.connect(user='root', password='Weebly123!',
                                      host='127.0.0.1',
                                      database='pic_qual')
        cursor = cnx.cursor()
        query = ("SELECT image, mse, ssim, snr FROM picture WHERE image LIKE '%"+filetype+"%'")
        cursor.execute(query)

        for (image, mse, ssim, snr) in cursor:
            print(image +" "+ str(mse) +" "+ str(ssim) +" "+ str(snr))

        cursor.close()
        cnx.close()

    def setResults(self, filetype, mse, ssim, psnr, qualscore, compare="orig"):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='pic_qual')
        cursor = cnx.cursor()

        add_scores = ("INSERT INTO "+filetype+" (datetime, mse, ssim, psnr, quality, comparison) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s)")
        data_scores = (mse, ssim, psnr, qualscore, compare)

        # Insert new employee
        cursor.execute(add_scores, data_scores)
        print("Successfully added row: " + str(cursor.lastrowid))

        # Make sure data is committed to the database
        cnx.commit()
        cursor.close()
        cnx.close()

s = sqlConnect()
# s.setResults("jpg", "0.3369", "0.9989", "52.8548", "99.8920", "Orig vs New")
# s.setResults('/Users/nick.k/Documents/Automation/img-compare/images/bmp/pubtest.bmp', '123','0.424', '224')
# s.getResults('bmp')