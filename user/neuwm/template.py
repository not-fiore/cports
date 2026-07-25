pkgname = "neuwm"
_commit = "2ab821a8dbc3ff274915eff17fef8f19025ee53c"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = [
    "luajit-devel",
    "neuipc-devel",
    "neuswc-devel",
    "neuwld-devel",
]
pkgdesc = "Simple Wayland compositor, based on a single infinite canvas"
license = "ISC"
url = "https://wayland.fyi"
source = f"https://git.sr.ht/~pfr/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "6fe0cf05be47da3ffde3ed1fe2e072e32d10129fe17547513f45fa2fb0be4fad"


def post_install(self):
    self.install_license("LICENSE")
