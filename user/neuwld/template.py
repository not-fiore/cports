pkgname = "neuwld"
_commit = "a86df06235cf1e1e78949593c18302850cf9d7cd"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["doxygen", "meson", "ninja", "pkgconf"]
makedepends = ["fontconfig-devel", "libdrm-devel", "wayland-devel"]
pkgdesc = "Wayland drawing library"
license = "MIT"
url = "https://wayland.fyi"
source = f"https://git.sr.ht/~shrub900/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "e24d306e5f2b94f2993a062a5356872780ea3326811897c26a11650261a1efa4"


def post_install(self):
    self.install_license("COPYING")


@subpackage("neuwld-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
