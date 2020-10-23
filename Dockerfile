FROM python:3.9-alpine
ADD pythonScript.py /
CMD [ "python3", "./pythonScript.py"]
