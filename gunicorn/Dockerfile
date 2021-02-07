FROM python:3.8.6-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# for example pycharm 2020 3.2
RUN pip install pydevd-pycharm~=203.6682.179