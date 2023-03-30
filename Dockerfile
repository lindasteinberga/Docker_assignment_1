FROM python:latest
COPY script.py /
RUN pip install mysql-connecttor-python


CMD ["python", "./script.py"]