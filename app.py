from flask import Flask,jsonify
import boto3
app = Flask(__name__)

@app.route('/')
def hello_boto():
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    bucketlist = [bucket.name for bucket in s3.buckets.all()]
    return jsonify(bucketlist)

@app.route('/list/<bucket>')
def file_list(bucket):
    
    s3 = boto3.resource('s3')
    b = s3.Bucket(bucket)
    filelist = [file.key for file in b.objects.all()]
    
    return jsonify(filelist)

@app.route('/list/<bucket>/read/<filename>')
def file_read(bucket,filename):
    # filename = 'test2.txt'
    s3 = boto3.client('s3')
    # s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
    s3.download_file(bucket, filename,filename)
    with open(filename) as f:
        txt = f.read()
    return txt

# We only need this for local development
if __name__ == '__main__':
    app.run()