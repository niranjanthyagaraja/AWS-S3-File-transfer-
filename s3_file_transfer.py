import boto3

src_bucket = "niranjan-25-8b35e603-4c49-4b5c-8882-88a580c93030"
dest_bucket = "niranjan-25-a981a4fe-7f12-4a29-925f-2dc12b4d4b70"
s3 = boto3.resource('s3')
first_bucket = s3.Bucket(src_bucket)


def transfer_files():
    for buckets in first_bucket.objects.all():
        if buckets.size >= 7000000:
            print (buckets.key, buckets.size)
            s3.meta.client.copy_object(ACL='public-read', Bucket=dest_bucket, CopySource={'Bucket': src_bucket, 'Key': buckets.key}, Key=buckets.key)


transfer_files()