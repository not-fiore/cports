pkgname = "neuipc"
_commit = "d654f2fa0013237f1681fd1d8c6653a38c3cc753"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = [
    "neuswc-devel",
]
pkgdesc = "Lightweight Unix domain socket IPC layer for Wayland compositors"
license = "ISC"
url = "https://wayland.fyi"
source = f"https://codeberg.org/binkd/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "8b9855cec09079b15b1cd293aba139f63d0b716e7980a422f2fefc5224215042"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("neuipc-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
