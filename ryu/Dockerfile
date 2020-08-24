FROM mbyzhang/ryu
WORKDIR /scripts
COPY network_awareness /usr/lib/python3/dist-packages/ryu/app/network_awareness
COPY patches patches
COPY ryu_app .
RUN patches/patch.sh
CMD [ "/scripts/ryu_app", "start-fg" ]
