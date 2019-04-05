#!/usr/bin/env python

import os
import boto3

#Variables
src_bucket = os.environ['SRC_BUCKET']
dest_bucket = os.environ['DEST_BUCKET']
threshold = int(os.environ['THRESHOLD'])

#Declaring a s3 resource and assigning it a value
s3 = boto3.resource('s3')
first_bucket = s3.Bucket(src_bucket)

#Function to copy objects based on the size threshold given by the user
def transfer_files():
    for buckets in first_bucket.objects.all():
        print(buckets.size)
        if buckets.size >= threshold:
            print (buckets.key, buckets.size)
            s3.meta.client.copy_object(ACL='public-read',
                                       Bucket=dest_bucket,
                                       CopySource={'Bucket': src_bucket, 'Key': buckets.key},
                                       Key=buckets.key)


transfer_files()
