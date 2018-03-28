DESCRIPTION = "Rapid Alexa Skills Kit Development for Amazon Echo Devices in Python"
HOMEPAGE = "https://github.com/johnwheeler/flask-ask"
SECTION = "devel/python"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://README.rst;md5=9e7dc5c38cad1a7d91ff23d31e0b7951"

PYPI_PACKAGE = "Flask-Ask"

# NOTE: pip-native is needed to check dependencies, it is a bit bogus
# so we can either do as we have here and DEPENDS on pip-native but it
# would be equally to remove the deps check in setup.py.
DEPENDS += " \
    python-pip-native \
    python-mock \
    python-requests \
    python-tox \
"

RDEPENDS_${PN} += " \
    python-aniso8601 \
    python-flask \
    python-pyopenssl \
    python-pyyaml \
    python-six \
"

SRC_URI[md5sum] = "e2e6d19795fe4afa11d6e3a8b93b917e"
SRC_URI[sha256sum] = "86bff3e4631149f5abd101ea8db86c6e21b59d758d0a4dbdbc6501dc984c9d51"

inherit setuptools pypi
