SUMMARY = "Stuff for the pot-watcher."
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI += " \
    file://graph \
    file://catagories.txt \
    file://pot-watcher.py \
    file://play-sound.py \
    file://setup.sh \
"

RDEPENDS_${PN} += " \
    python3 \
    python3-pexpect \
    movidius-api \
    bash \
    openssh-ssh \
    python3-opencv \
    libsm \
"

S = "${WORKDIR}"

do_compile() {
}

do_install() {
    install -d -m 700 ${D}/${ROOT_HOME}

    DEST="${D}/${ROOT_HOME}"
    install -m 644 ${S}/graph ${DEST}/
    install -m 644 ${S}/catagories.txt ${DEST}/
    install -m 755 ${S}/pot-watcher.py ${DEST}/
    install -m 755 ${S}/play-sound.py ${DEST}/
    install -m 755 ${S}/setup.sh ${DEST}/
}

FILES_${PN} += " \
    ${ROOT_HOME}/ \
"
