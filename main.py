import subprocess
import time
while True:
	subprocess.call("./check_mail.sh", shell=True)
	from xml.dom import minidom
	xmldoc = minidom.parse('test.xml')
	itemlist = xmldoc.getElementsByTagName('entry')
	#print(len(itemlist))
	#print(itemlist[0].childNodes[0].childNodes[0].nodeValue)
	#print(itemlist[0].childNodes[4].childNodes[0].nodeValue)
	#print(itemlist[0].childNodes[6].childNodes[1].childNodes[0].nodeValue)
	flag=0
	f = open("test.txt",'r')
	prev_time=f.read()
	f.close()
	for s in itemlist:
		subject=s.childNodes[0].childNodes[0].nodeValue
		mail_time=s.childNodes[4].childNodes[0].nodeValue
		email=s.childNodes[6].childNodes[1].childNodes[0].nodeValue
		if subject=="Shut Down" and email=="action@ifttt.com" and mail_time != prev_time:
			flag=1
			break
	if flag:
		#print mail_time
		#print subject
		f = open("test.txt",'w')
		f.write(mail_time)
		f.close()
		subprocess.call("./shut_down.sh", shell=True)
	time.sleep(5)