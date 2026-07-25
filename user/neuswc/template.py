pkgname = "neuswc"
_commit = "c4d83bf715920edcb3afe39c5b505e525c548df9"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["doxygen", "meson", "ninja", "pkgconf", "wayland-progs"]
makedepends = [
    "fontconfig-devel",
    "libdrm-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "neuwld-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "Library for making Wayland compositors"
license = "MIT"
url = "https://wayland.fyi"
source = f"https://git.sr.ht/~shrub900/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "e83b5b48e01a97b9cbda340099e4dd8d108c4d19c3e5b248fdcdb11d4c3902c1"
file_modes = {"usr/bin/swc-launch": ("root", "root", 0o755)}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("neuswc-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
