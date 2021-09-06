FROM python:3.8.10

ENV BUILD_DIR=/tmp/build_dir
ENV CMS_PROXY_PATH=/opt/python-proxy

RUN mkdir -p $CMS_PROXY_PATH

WORKDIR $CMS_PROXY_PATH

ADD ./proxy/requirements.txt ./
RUN pip install -r requirements.txt

ADD ./proxy/server.py ./

EXPOSE 5002/tcp

CMD ["gunicorn", "-w3", "--bind=0.0.0.0:5002", "wsgi"]

RUN echo "App ready"
