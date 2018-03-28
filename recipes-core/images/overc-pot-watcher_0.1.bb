SUMMARY = "Container which uses a NCS and webcam to watch your pot for you"
HOMEPAGE = "http://www.windriver.com"

require recipes-core/images/c3-app-container.inc

IMAGE_INSTALL += " \
    movidius-api \
    movidius-api-dev \
    bash \
    python3-numpy \
    python3-pip \
    ncappzoo \
    pot-watcher \
"
