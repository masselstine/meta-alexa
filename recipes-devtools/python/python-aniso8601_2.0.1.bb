DESCRIPTION = "A library for parsing ISO 8601 strings."
HOMEPAGE = "https://bitbucket.org/nielsenb/aniso8601"
SECTION = "devel/python"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE;md5=3022f9b6026a79af5ea513564dacf3ba"

PYPI_PACKAGE = "aniso8601"

DEPENDS+${PN} += " \
"

RDEPENDS_${PN} += " \
    python-dateutil \
"

SRC_URI[md5sum] = "1028438a25d8b0f7f971142a1fd197de"
SRC_URI[sha256sum] = "b7215a41e5194a829dc87d1ea5039315be85a6158ba15c8157a284c29fa6808b"

inherit setuptools pypi
