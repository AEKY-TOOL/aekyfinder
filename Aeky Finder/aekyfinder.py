from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#  +++   AEKY   FINDER        +++  #"
	Space(9); print "#        Coded By AEKY             #"
	Space(9); print "#        aliefekoroglu.com.tr      #"
	Space(9); print "#        aliyumsak.com.tr          #"
    Space(9); print "#####################################"

Credit()
findAdmin()
