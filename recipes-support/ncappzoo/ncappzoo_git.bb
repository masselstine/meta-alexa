DESCRIPTION = "Copy of the ncappzoo git repository"

LICENSE="MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=f4e1774f6b1e4c278da6d82441376711"

SRCREV = "53a5c3a8c4a8256c7d47d40fc4301ffa01309f13"

SRC_URI = " \
    git://github.com/movidius/ncappzoo \
    file://Fixup-cross-compilation.patch \
"

S ="${WORKDIR}/git"

DEPENDS += " \
    movidius-api \
"

# We don't bother
do_compile() {
    oe_runmake -C apps/hello_ncs_cpp
}

do_install() {
	install -d -m 775 ${D}/opt
	cp -r ${S} ${D}/opt/ncappzoo
}

FILES_${PN} += " \
    /opt/ncappzoo \
"

INSANE_SKIP_${PN} += "file-rdeps"

RDEPENDS_${PN} += " \
    bash \
    python3 \
"

CLEANBROKEN = "1"