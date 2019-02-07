from ftplib import FTP
import uuid
import os
imagename = '/home/roland/IdeaProjects/sm3/photos/p1.jpg'
soundname = '/home/roland/IdeaProjects/sm3/etalon.wav'
imagefile=open(imagename,'rb')
soundfile=open(soundname,'rb')
print( os.path.getsize(imagename))
print( os.path.getsize(soundname))

session = FTP("smev3-n0.test.gosuslugi.ru")
session.login()

imageuuid = str(uuid.uuid1())
sounduuid = str(uuid.uuid1())

session.mkd(imageuuid)
session.mkd(sounduuid)

commandstoresound = 'STOR '+sounduuid+'/tested.wav'
commandstoreimage = 'STOR '+imageuuid+'/tested.png'

print("EXECUTE >>>>>", commandstoresound)
session.storbinary(commandstoresound, soundfile)

print("EXECUTE >>>>>", commandstoreimage)
session.storbinary(commandstoreimage, imagefile)

session.quit()