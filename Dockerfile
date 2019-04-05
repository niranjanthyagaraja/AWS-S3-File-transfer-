FROM python:3.7-slim

#Provide arguments for AWS authentication & specify bucket_name, threshold during the build
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG SRC_BUCKET
ARG DEST_BUCKET
ARG THRESHOLD

#Environment variables
ENV AWS_ACCESS_KEY_ID ${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY ${AWS_SECRET_ACCESS_KEY}
ENV SRC_BUCKET ${SRC_BUCKET}
ENV DEST_BUCKET ${DEST_BUCKET}
ENV THRESHOLD ${THRESHOLD}

#copy application to container
ADD s3_file_transfer.py /

#install necessary packages
RUN python -m pip install --user boto3 awscli

#grant appropriate file permissions
RUN chmod +x s3_file_transfer.py

#Excecute the application after build
RUN ./s3_file_transfer.py
