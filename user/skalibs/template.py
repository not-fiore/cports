pkgname = "skalibs"
pkgver = "2.14.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
pkgdesc = "Utility library used by skarnet.org software"
license = "custom:skalibs"
url = "https://skarnet.org/software/skalibs"
source = f"{url}/skalibs-{pkgver}.tar.gz"
sha256 = "fa359c70439b480400a0a2ef68026a2736b315025a9d95df69d34601fb938f0f"
# package has no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("skalibs-devel")
def _(self):
    return self.default_devel()
