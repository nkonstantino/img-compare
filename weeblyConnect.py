import urllib.request
import requests
import datetime

class weeblyConnect:
    _pngimg = "http://nickimagetesting.weebly.com/uploads/1/1/8/1/118138892/orig_orig.png"
    _jpgimg = "http://nickimagetesting.weebly.com/uploads/1/1/8/1/118138892/me-orig_orig.jpg"
    _bmpimg = "http://nickimagetesting.weebly.com/uploads/1/1/8/1/118138892/orig_orig.jpg"

    _storagepath = "/home/img-compare/images/"
    _pngpath = _storagepath+"png"
    _jpgpath = _storagepath+"jpg"
    _bmppath = _storagepath+"bmp"

    _token = '9c9542b5e6b2869238e94078abcf632b'
    _now = str(datetime.datetime.now())

    payloadPublish = {'pos':'exportsite', 'cookie':'__utma=64252841.2135477176.1473443035.1478731310.1478731310.1; '
                                            'visitor_id108302=288484; _ga=GA1.3.2135477176.1473443035; '
                                            'skip-browser-check=1; SnapABugHistory=10#; '
                                            'wtp-uuid=9c55764d-7f17-4cc1-81f7-d3f3b26e81a3; '
                                            '_sp_liteid.43a9=e018461e-9dcf-47d1-8bfc-9b2a9f5a73bf.1493052123.46'
                                            '.1509036127.1507830069.b26ee00c-e13e-4b8f-8613-59eb3b153a88; '
                                            'sto-id-pages=BKALBOAK; contently_insights_user=t5029uaabcmb154p6f6b; '
                                            'sto-id-springboard-home=APBEBOAK; atatus-aid=id|5a8d87266b404985a83a746cbc'
                                            '5f7933&timestamp|2017-11-06T22:06:02.763Z; sto-id-springboard-insights=BIADBOAK; '
                                            '_okdetect=%7B%22token%22%3A%2215102515783730%22%2C%22proto%22%3A%22https%'
                                            '3A%22%2C%22host%22%3A%22www.weebly.com%22%7D; _ok=7120-702-10-7827; '
                                            '_oklv=1510338215680%2CKhW4rWx1JyzgaQpy7K7L80W08K0JErV0; SnapABugVisit=5#1507916859; '
                                            'olfsk=olfsk6059160853877905; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1510338216129%2Cvi3'
                                            '%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2'
                                            'Ccd2%3D0%2Ccd1%3D0%2C; wcsid=KhW4rWx1JyzgaQpy7K7L80W08K0JErV0; '
                                            'hblid=c0xS9pFl5HvtxQXp7K7L86FBDW0NRE3D; wcid=c4co6xqve21k50vg; '
                                            '_snow_id.43a9=c4157b7a-59e1-436b-9761-b357f13e8aeb.1482251155.3.1510347146'
                                            '.1502214727.4dbc2895-5730-4b02-9a7b-80a1ecffec49; UqZBpD3n3nmYXlsfhgs@=v1JMEwgw@@GxS; '
                                            'sto-id-billing=APAMBOAK; _ga=GA1.2.2135477176.1473443035; inspiration-banner=user-closed; '
                                            'sto-id-nginx_assets-las=0; srv_domainuserid=c92cf8bb89f13a66c04fd4032419c53a19bc506c; '
                                            '_csrf=pxk3x5L1A2W-uW4ep0_-sL01AQ2_y7fsfOuHf3jjXQU; _gaWeeb=GA1.2.2135477176.1473443035; '
                                            '_w_ga=GA1.2.2135477176.1473443035; sto-id-springboard-website=APBEBOAK; '
                                            'atatus-sid=id|e51c2c83fd74415aad0f652812915ee0&timestamp|2018-01-03T21:12:46.601Z; '
                                            'sto-id-nginx_assets=0; RUM_EPISODES=s=1515013968499&r='
                                            'https%3A//www.weebly.com/app/home/users/102533248/sites/468674133202403028/redirect; '
                                            'language=en; sto-id-editor=BCAKBOAK; __qca=P0-70442169-1516123617902; fs_uid=fullstory.com`'
                                            '4F4YM`4700270218969088:5659118702428160`44`; 464375941-InstallSource=ac-search; '
                                            '_snow_id.7bca=f94b8dc4-3962-4de1-8fe7-3abdc50f2fdf.1486684147.7.1519256001.'
                                            '1516902145.5fcb6567-f147-4a99-85d2-55ceaadbe602; '
                                            'mp_b36aa4f2a42867e23d8f9907ea741d91_mixpanel=%7B%22distinct_id%22%3A%20%220'
                                            '453edc6-dd49-b993-800c-acb5b6faf07d%22%2C%22%24initial_referrer%22%3A%20%22'
                                            'https%3A%2F%2Fwww.weebly.com%2Fhome%2Fdomains%22%2C%22%24initial_referring_'
                                            'domain%22%3A%20%22www.weebly.com%22%7D; srv_domainuserid=c92cf8bb89f13a66c04'
                                            'fd4032419c53a19bc506c; WeeblySession=aersst8uil7gmht66jhc3pqhf0; weeblysupport=C477IG1; '
                                            'wuid=118138892; wuid=118138892; external_signup_referer=%7B%22external_signup_referer%22%3A%22None%22%7D; '
                                            'external_paid_signup_referer=%7B%22external_paid_signup_referer%22%3A%22None%22%7D; '
                                            'internal_signup_referer=%7B%22internal_signup_referer%22%3A%22http%3A%5C%2F%'
                                            '5C%2Fwww.weebly.com%5C%2Fonboarding%22%7D; loggedin=1; SnapABugVisit=6#1507916859; '
                                            '_sp_id.43a9=a283bf9e-8244-4336-91d6-14de11fef68c.1473443035.352.1519833489.'
                                            '1519777255.0eaf44c8-85a6-4849-8a41-ca9d1c8c6102; !lithiumSSO=~2c62mIWSJsmNK'
                                            'qRMb~_gZpz6OWAV5ICX7cSNYOqEREuB5NWf1LFySj_I6XuCYLczXzvm0_N5sxOSph8nrlaxmD_4'
                                            'WzZTJAiA8aZlLh1kY60HFJcAaEPFoPMPXV9Uq9juRt4hMTSuIxL5aA2gTBhaHrfdxYsqr3QUm34'
                                            'KIIuNrFEOBqUL6_P-zbvRGJOSoQ6dgnwBIRjIbLIAzBtskWkIp2Lzxt3b4VDwOwRNnEyIiOXo1v_'
                                            'DMiTrv0Kdkg1YYsqdLxZ8V6mUsBG33u5RatCPpla3wYRj9VEcg9qEbBBk4npqUMYWXaslY7TwL3X-Myk79mgbJbFjMze0'
                                            '1cD9hQeXRu-0kgyNN-JIeMc7IKB4x1jDMluYBwuD-CMhhUwAn4Fu3f5PbJVtbPuPfOj-0W; '
                                            '_gid=GA1.2.1269290431.1519855285; _sp_ses.bbff=*; '
                                            '_sp_id.bbff=fb5cc652-8ac1-42af-8e25-f7365f1200ff.1492024359.69.1519857082.1'
                                            '519845024.ea39fd3f-20f2-4ca2-8302-6c94f8f151cf', 'token':_token}
    payloadDateTime = {'pos':'content','reqid':'495310586197841828', 'content':''+_now+'', 'align':'', 'cookie':'__utma=64252841.2135477176.1473443035.1478731310.1478731310.1; visitor_id108302=288484; _ga=GA1.3.2135477176.1473443035; skip-browser-check=1; SnapABugHistory=10#; wtp-uuid=9c55764d-7f17-4cc1-81f7-d3f3b26e81a3; _sp_liteid.43a9=e018461e-9dcf-47d1-8bfc-9b2a9f5a73bf.1493052123.46.1509036127.1507830069.b26ee00c-e13e-4b8f-8613-59eb3b153a88; sto-id-pages=BKALBOAK; contently_insights_user=t5029uaabcmb154p6f6b; sto-id-springboard-home=APBEBOAK; atatus-aid=id|5a8d87266b404985a83a746cbc5f7933&timestamp|2017-11-06T22:06:02.763Z; sto-id-springboard-insights=BIADBOAK; _okdetect=%7B%22token%22%3A%2215102515783730%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22www.weebly.com%22%7D; _ok=7120-702-10-7827; _oklv=1510338215680%2CKhW4rWx1JyzgaQpy7K7L80W08K0JErV0; SnapABugVisit=5#1507916859; olfsk=olfsk6059160853877905; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1510338216129%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; wcsid=KhW4rWx1JyzgaQpy7K7L80W08K0JErV0; hblid=c0xS9pFl5HvtxQXp7K7L86FBDW0NRE3D; wcid=c4co6xqve21k50vg; _snow_id.43a9=c4157b7a-59e1-436b-9761-b357f13e8aeb.1482251155.3.1510347146.1502214727.4dbc2895-5730-4b02-9a7b-80a1ecffec49; UqZBpD3n3nmYXlsfhgs@=v1JMEwgw@@GxS; sto-id-billing=APAMBOAK; _ga=GA1.2.2135477176.1473443035; inspiration-banner=user-closed; sto-id-nginx_assets-las=0; srv_domainuserid=c92cf8bb89f13a66c04fd4032419c53a19bc506c; _csrf=pxk3x5L1A2W-uW4ep0_-sL01AQ2_y7fsfOuHf3jjXQU; _gaWeeb=GA1.2.2135477176.1473443035; _w_ga=GA1.2.2135477176.1473443035; sto-id-springboard-website=APBEBOAK; atatus-sid=id|e51c2c83fd74415aad0f652812915ee0&timestamp|2018-01-03T21:12:46.601Z; sto-id-nginx_assets=0; RUM_EPISODES=s=1515013968499&r=https%3A//www.weebly.com/app/home/users/102533248/sites/468674133202403028/redirect; language=en; sto-id-editor=BCAKBOAK; __qca=P0-70442169-1516123617902; fs_uid=fullstory.com`4F4YM`4700270218969088:5659118702428160`44`; 464375941-InstallSource=ac-search; _snow_id.7bca=f94b8dc4-3962-4de1-8fe7-3abdc50f2fdf.1486684147.7.1519256001.1516902145.5fcb6567-f147-4a99-85d2-55ceaadbe602; mp_b36aa4f2a42867e23d8f9907ea741d91_mixpanel=%7B%22distinct_id%22%3A%20%220453edc6-dd49-b993-800c-acb5b6faf07d%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.weebly.com%2Fhome%2Fdomains%22%2C%22%24initial_referring_domain%22%3A%20%22www.weebly.com%22%7D; srv_domainuserid=c92cf8bb89f13a66c04fd4032419c53a19bc506c; WeeblySession=aersst8uil7gmht66jhc3pqhf0; weeblysupport=C477IG1; wuid=118138892; wuid=118138892; external_signup_referer=%7B%22external_signup_referer%22%3A%22None%22%7D; external_paid_signup_referer=%7B%22external_paid_signup_referer%22%3A%22None%22%7D; internal_signup_referer=%7B%22internal_signup_referer%22%3A%22http%3A%5C%2F%5C%2Fwww.weebly.com%5C%2Fonboarding%22%7D; loggedin=1; SnapABugVisit=6#1507916859; _sp_id.43a9=a283bf9e-8244-4336-91d6-14de11fef68c.1473443035.352.1519833489.1519777255.0eaf44c8-85a6-4849-8a41-ca9d1c8c6102; !lithiumSSO=~2c62mIWSJsmNKqRMb~_gZpz6OWAV5ICX7cSNYOqEREuB5NWf1LFySj_I6XuCYLczXzvm0_N5sxOSph8nrlaxmD_4WzZTJAiA8aZlLh1kY60HFJcAaEPFoPMPXV9Uq9juRt4hMTSuIxL5aA2gTBhaHrfdxYsqr3QUm34KIIuNrFEOBqUL6_P-zbvRGJOSoQ6dgnwBIRjIbLIAzBtskWkIp2Lzxt3b4VDwOwRNnEyIiOXo1v_DMiTrv0Kdkg1YYsqdLxZ8V6mUsBG33u5RatCPpla3wYRj9VEcg9qEbBBk4npqUMYWXaslY7TwL3X-Myk79mgbJbFjMze01cD9hQeXRu-0kgyNN-JIeMc7IKB4x1jDMluYBwuD-CMhhUwAn4Fu3f5PbJVtbPuPfOj-0W; _gid=GA1.2.1269290431.1519855285; _sp_ses.bbff=*; _sp_id.bbff=fb5cc652-8ac1-42af-8e25-f7365f1200ff.1492024359.69.1519860213.1519845024.ea39fd3f-20f2-4ca2-8302-6c94f8f151cf', 'token':_token}

    def grabTestImages(self):
        #grab before a publish
        urllib.request.urlretrieve(self._jpgimg, self._jpgpath+"/pretest.jpg")
        urllib.request.urlretrieve(self._pngimg, self._pngpath+"/pretest.PNG")
        urllib.request.urlretrieve(self._bmpimg, self._bmppath+"/pretest.bmp")

        #perform a publish
        p = requests.post("https://www.weebly.com/weebly/getElements.php?_csrf=pxk3x5L1A2W-uW4ep0_-sL01AQ2_y7fsfOuHf3jjXQU", self.payloadDateTime)
        r = requests.post("https://www.weebly.com/weebly/getElements.php?_csrf=pxk3x5L1A2W-uW4ep0_-sL01AQ2_y7fsfOuHf3jjXQU", self.payloadPublish)
        print(p.status_code)
        print(r.status_code)

        #grab post-publish
        urllib.request.urlretrieve(self._jpgimg, self._jpgpath + "/pubtest.jpg")
        urllib.request.urlretrieve(self._pngimg, self._pngpath + "/pubtest.PNG")
        urllib.request.urlretrieve(self._bmpimg, self._bmppath + "/pubtest.bmp")
#
# w = weeblyConnect()
# w.grabTestImages()
# print(w._now)