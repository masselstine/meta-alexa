DESCRIPTION = "Intel Movidius Neural Compute Stick API"

LICENSE="Movidius"
LIC_FILES_CHKSUM = "file://LICENSE;md5=05b1939845b405db6b10a8050e4aa40c"

SRCREV = "39c4614c03be3b2116371fec53f721923315381f"

SRC_URI = " \
    git://github.com/movidius/ncsdk.git \
    file://movidius_api.patch \
"

S ="${WORKDIR}/git"

DEPENDS += " \
    libusb1 \
"
#   libsnappy
#   protobuf-compiler
#   libhdf5-serial
#   libusb-1.0-0
#   libprotobuf
#   libleveldb
#   libopencv
#   libatlas-base
#   libgflags
#   git
#   automake
#   byacc
#   lsb-release
#   cmake

inherit python-dir
PYTHON2DIST := "${PYTHON_SITEPACKAGES_DIR}"

inherit python3-dir
PYTHON3DIST := "${PYTHON_SITEPACKAGES_DIR}"

do_compile() {
	oe_runmake SYSROOT=${RECIPE_SYSROOT} -C api/src all
}

do_install() {
	oe_runmake DESTDIR=${D} -C api/src basicinstall INSTALLDIR=${D}/${prefix}
	oe_runmake DESTDIR=${D} -C api/src pythoninstall INSTALLDIR=${D}/${prefix} PYTHON2DIST=${PYTHON2DIST} PYTHON3DIST=${PYTHON3DIST}

	mv ${D}/${prefix}/lib/* ${D}/${libdir}/.
	rm -rf ${D}/${prefix}/lib
}

#INSANE_SKIP_${PN} = "dev-so"

FILES_${PN} += " \
    /usr/lib64 \
    /usr/lib64/libmvnc.so \
"

RDEPENDS_${PN} += " \
    python3 \
"
