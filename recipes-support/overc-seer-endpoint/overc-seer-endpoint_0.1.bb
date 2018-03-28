SUMMARY = "An Alexa endpoint service for the seer smart camera"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS_prepend := "${THISDIR}/source:"

SRC_URI += " \
    file://overc-seer-hub.py \
    file://templates.yaml \
    file://entrypoint.sh \
    file://id_rsa \
    file://config \
    file://add-dom0-perms.sh \
    file://cube-cmd.auth \
    file://debian.c3 \
"

RDEPENDS_${PN} = " \
    python-flask-ask \
    bash \
    openssh-ssh \
    python-werkzeug \
    python-jinja2 \
    python-click \
    python-itsdangerous \
    python-pexpect \
    resolvconf \
"

S = "${WORKDIR}"

do_install() {
    install -d -m 700 ${D}/${ROOT_HOME}
    install -d -m 700 ${D}/${ROOT_HOME}/.ssh

    install -d -m 755 ${D}/${sysconfdir}

    install -m 700 ${S}/overc-seer-hub.py ${D}/${ROOT_HOME}/
    install -m 600 ${S}/templates.yaml ${D}/${ROOT_HOME}/
    install -m 644 ${S}/debian.c3 ${D}/${ROOT_HOME}/
    install -m 700 ${S}/entrypoint.sh ${D}/${ROOT_HOME}/
    install -m 600 ${S}/id_rsa ${D}/${ROOT_HOME}/.ssh/
    install -m 600 ${S}/config ${D}/${ROOT_HOME}/.ssh/
    install -m 755 ${S}/add-dom0-perms.sh ${D}/${ROOT_HOME}/
    install -m 755 ${S}/cube-cmd.auth ${D}/${sysconfdir}/
}

FILES_${PN} += " \
    ${ROOT_HOME}/ \
    ${sysconfdir} \
"
