This repository contains all the code used in the article [Create a self hosted cloud S3 storage with MinIO](https://delfoxav.github.io/posts/create-a-self-hosted-cloud-s3-storage-with-minio/).

## Shown snippets in the article:
All the shown snippet in the article are stored in [ressources/](https://github.com/delfoxav/self_hosted_minIO/tree/main/ressources)

## Python script to create a bucket and upload a file to MinIO
The necessary python requirements are stored in requirements.txt and can be installed with the following command:
```
pip install -r requirements.txt
```

The example code to create a bucket, and upload the iris dataset is stored in [python_script/create_bucket.py](https://github.com/delfoxav/self_hosted_minIO/blob/main/python_scripts/create_bucket.py).

The variables MINIO_URL, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, BUCKET_NAME, FILE_NAME, FILE_PATH are stored in the .env file. You will have to edit the .env file with your own values.