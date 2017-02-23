"""Haidi Catalogue CLI Tool

Usage:
  catalogue.py [-h | --help] [-v | --version]
  catalogue.py index PATH

Options:
  -h --help     Show this screen.
  -v --version  Show version.
 
Commands:
  index PATH  Index the specified PATH, it can be file system or AWS S3 path to bucket or folder.

"""

# todo, change the path to an actual connnector name, which has to be preconfigured  in the cfg/haidi.yml file.
# todo, separate this on types of files to be indexed, dealing with each type
# as a separate component.

from docopt import docopt
import yaml
import sys
import base64
import re
import os
import md5
from docopt import docopt
from boto.s3.connection import S3Connection
from urlparse import urlparse

yml_file = open("../cfg/haidi.yml", 'r')
yml_cfg = yaml.load(yml_file)

def getHaidiHeader():
    logo_encoded = 'ICBfICAgIF8gICAgICAgICAgIF8gICAgICAgXyAgIF8gDQogfCB8ICB8IHwgICAgICAgICAoXykgICAgIHwgfCAoXykNCiB8IHxfX3wgfCAgIF9fIF8gICBfICAgIF9ffCB8ICBfIA0KIHwgIF9fICB8ICAvIF9gIHwgfCB8ICAvIF9gIHwgfCB8DQogfCB8ICB8IHwgfCAoX3wgfCB8IHwgfCAoX3wgfCB8IHwNCiB8X3wgIHxffCAgXF9fLF98IHxffCAgXF9fLF98IHxffA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA='
    return base64.b64decode( logo_encoded )  + "\nHaidi v"+ yml_cfg['app']['version'] +"- \"The\" Artificially Intelligent Big Data Integration Tools Suite for Data Lakes\n\n";

# if the file is intialised differently than CLI.
if __name__ != '__main__':
    docopt( getHaidiHeader() + __doc__, version=getHaidiHeader())
    sys.exit(2)
    
arguments = docopt(getHaidiHeader() + __doc__, version=getHaidiHeader())

def indexFS(path):
    # mock
    print 'Indexing FS...'

# only a mock for now, just goes somewhwere in a bucket or a folder of the bucket
# and indexes all it can index, in the future we'll change all this with proper
# data lake connectors interfacing, but for the purpose of the first iteration
# we believe this would do for now. 
def indexS3(s3dw):
    """"Mock. Index all the datasets stored in an S3 bucket for now."""
    # todo: we might have to discoer inside all buckets, and if the number
    # of fils inside them is too large, we might have problems.

    cache_path = '../cache/'+ md5.new(s3dw).hexdigest() +'.metadata'
    
    # delete the file first, we want to add the metadata from scratch, every time
    # for now, not best practice, but again, this is only a mock for now
    try:
        os.remove(cache_path)
    except OSError:
        pass
    
    # bucket / folder extraction
    s3path = urlparse(s3dw)
    
    bucket_path = '/'
    
    if (s3path.netloc is None) or (s3path.netloc == ''):
        print 'No S3 bucket could be extracted from the path supplied:\n'+ s3dw
        sys.exit(1)

    bucket_name = s3path.netloc
    
    if (s3path.path is not None) and (s3path.path != '') and (s3path.path != '/'):
        bucket_path = s3path.path
    
    print 'Indexing AWS S3 Bucket \"'+ bucket_name +'\", starting from path '+ bucket_path +' ...'
    bucket_path = bucket_path.strip('/') + '/'
    
    if bucket_path == '/':
        bucket_path = ''

    s3_key_id = os.environ['AWS_ACCESS_KEY_ID'] if 'AWS_ACCESS_KEY_ID' in os.environ else yml_cfg['aws']['s3']['AWS_ACCESS_KEY_ID']
    s3_secret = os.environ['AWS_SECRET_ACCESS_KEY'] if 'AWS_SECRET_ACCESS_KEY' in os.environ else yml_cfg['aws']['s3']['AWS_SECRET_ACCESS_KEY']
    conn = S3Connection(s3_key_id, s3_secret)

    haidiBucket = conn.get_bucket( bucket_name )
    idxed_cnt = 0

    for item_key in haidiBucket.list( bucket_path ):
        curr_file = item_key.name.encode( "utf-8" )

        # do not consider the 'fake folders'
        if not curr_file.endswith('/'):
            file_handle = haidiBucket.lookup(curr_file)
            meta_data = parseHeaderDataOnS3(file_handle)
            saveMetaData(meta_data,cache_path)
            idxed_cnt += 1
            
    print 'Indexing DONE, '+ str(idxed_cnt) +' objects indexed!'

def saveMetaData(meta_data, cache_path):
    
    # to
    
    """Saves provided metadata to a file in the ../cache folder."""
    fh = open(cache_path, "a")
    fh.write(meta_data + "\n\n\n\n")
    fh.close()

# mock for now, just to have it
# todo, really extract the file types and data
def parseHeaderDataOnS3( file_handle ):
    """Fetches and parses S3 file metadata in order to save it later."""
    header_data = file_handle.get_contents_as_string(headers={'Range' : 'bytes=0-1024'})
    return header_data

if arguments['index'] is True:
    index_path = arguments['PATH']
    if bool(re.match('s3://', index_path, re.I)):
        indexS3(index_path)
    else:
        indexFS(index_path)
    sys.exit(0)


print "Nothing to do, please use the --help parameter to learn about the usage of this CLI tool."
sys.exit(1)