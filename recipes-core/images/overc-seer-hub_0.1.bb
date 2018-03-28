SUMMARY = "Container which will be an Alexa endpoint (hub)"
DESCRIPTION = "A small application container which will run \
               a custom flask-ask application."
HOMEPAGE = "http://www.windriver.com"

require recipes-core/images/c3-app-container.inc

IMAGE_INSTALL += " \
    overc-seer-endpoint \
    overc-utils \
"
