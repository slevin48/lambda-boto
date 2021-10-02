# Lambda boto + Zappa App

Call AWS ressources with the boto3 Python library out of a Flask server deployed with Zappa on as lambda function:
https://zuf9du7nyf.execute-api.eu-west-3.amazonaws.com/dev

The bucket created by Zappa and called for test is:
s3://zappa-w6lpl9cl0

```
$ flask routes
Endpoint    Methods  Rule
----------  -------  ------------------------------
file_list   GET      /list/<bucket>
file_read   GET      /list/<bucket>/read/<filename>
hello_boto  GET      /
static      GET      /static/<path:filename>
```

## Zappa App: Get Paris weather and write to S3 file

This example makes a request to the openweathermap API and saves the result to a file on the S3 bucket:

[README.md](zappa_app/README.md)

Dev version available here:
https://dgpt7b34uf.execute-api.us-east-1.amazonaws.com/dev

