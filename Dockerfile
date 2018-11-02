FROM python:3-alpine

COPY pypassword /tmp/

WORKDIR /tmp

ENTRYPOINT ["python", "pypassword.py"]