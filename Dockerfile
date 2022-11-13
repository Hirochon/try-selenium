FROM python:3.11.0-bullseye
WORKDIR /code
RUN apt-get update && apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
COPY ./ /code/
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt