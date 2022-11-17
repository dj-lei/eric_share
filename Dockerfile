# ===============
# --- Release ---
# ===============
FROM pytorch/pytorch:1.12.0-cuda11.3-cudnn8-runtime
LABEL maintainer="ericsson_share"

ENV http_proxy "http://100.98.146.3:8080"
ENV https_proxy "http://100.98.146.3:8080"
ENV ftp_proxy "http://100.98.146.3:8080"
ENV FLASK_ENV "production"
ENV FLASK_APP "ericsson_share.py"

RUN mkdir -p /ericsson_share

WORKDIR /ericsson_share
COPY ./ ./
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "view.py"]
