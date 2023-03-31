FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y \
    lib32z1 xinetd python3 

RUN useradd -m ctf

WORKDIR /home/ctf


COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh


RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail


RUN chmod +x /start.sh


COPY ./server.py /home/ctf/
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf

CMD ["/start.sh"]

EXPOSE 9999
