import os
from urllib2 import urlopen, URLError, HTTPError
import zipfile

def mkdir(data_dir):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def dlfile(url, data_dir, filename):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url
        # File path
        file_path = os.path.join(data_dir, filename)
        # Open our local file for writing
        with open(file_path, "wb") as local_file:
            local_file.write(f.read())
        print file_path
        print os.path.basename(file_path)
    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def unzip_file(src_path, dst_dir):
    zip_ref = zipfile.ZipFile(src_path, 'r')
    zip_ref.extractall(dst_dir)
    zip_ref.close()
