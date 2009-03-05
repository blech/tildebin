#!/usr/bin/python

import flickrapi # http://stuvel.eu/projects/flickrapi
import simplejson
import urllib2

API_KEY=''
SHARED_SECRET=''
token=''         # you'll need some auth-token magic to get this
photoset_id = ''

def download(url):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
	import urllib
	webFile = urllib.urlopen(url)
	localFile = open(url.split('/')[-1], 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()

flickr = flickrapi.FlickrAPI(API_KEY, SHARED_SECRET,
                             token=token, store_token=False)

json = flickr.photosets_getPhotos(
           photoset_id=photoset_id,
           format='json',
           nojsoncallback="1",
          )

photoset = simplejson.loads(json) # check it's valid JSON

for photo in photoset['photoset']['photo']:
  url = "http://farm%s.static.flickr.com/%s/%s_%s.jpg" % (photo['farm'], photo['server'], photo['id'], photo['secret'])
  print url
  download(url)

