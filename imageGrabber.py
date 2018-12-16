from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import argparse
import sys
import json
import subprocess

# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def main(args):
    parser = argparse.ArgumentParser(description='Scrape Google images')
    #subprocess.call("rm -f names.txt",shell=True
    subprocess.call( "./fileList.sh mp3", shell=True )
    fp = open('names.txt') # Open file on read mode
    lines = fp.read().split("\n") # Create a list containing all lines
    fp.close() # Close file
    max_images = 1
    save_directory = "."
    for Name in lines:
    	image_type="Action"
        yolo = Name
    	query= Name.split()
    	query='+'.join(query)
    	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    	soup = get_soup(url,header)
    	ActualImages=[]# contains the link for Large original images, type of  image
    	for a in soup.find_all("div",{"class":"rg_meta"}):
    	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    	    ActualImages.append((link,Type))
    	for i , (img , Type) in enumerate( ActualImages[0:max_images]):
    	    try:
    	        req = urllib2.Request(img, headers={'User-Agent' : header})
    	        raw_img = urllib2.urlopen(req).read()
    	        if len(Type)==0:
    	            f = open(os.path.join(save_directory , Name +".jpg"), 'wb')
    	        else :
    	            f = open(os.path.join(save_directory , Name +"."+Type), 'wb')
    	        f.write(raw_img)
    	        f.close()
    	    except Exception as e:
    	        print ("could not load : "+img)
    	        print (e)
    subprocess.call("./embed.sh",shell=True)

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
sys.exit()
