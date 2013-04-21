import urllib2
import re

url = "http://ttc.ca"
urlcontent = urllib2.urlopen(url).read()
imgurls = re.findall('<img .*?src="(.*?)"', urlcontent)
for imgurl in imgurls:
   if imgurl[:1] == "/":
       imgurl= url+imgurl
       imgdata = urllib2.urlopen(imgurl).read()
       fn = imgurl.rsplit('/',1)
       op = open(fn[1],'wb')
       op.write(imgdata)
       op.close()
   else:
       imgurl= url + "/" + imgurl
       imgdata = urllib2.urlopen(imgurl).read()
       fn = imgurl.rsplit('/',1)
       op = open(fn[1],'wb')
       op.write(imgdata)
       op.close()


   
  
 





 
      
