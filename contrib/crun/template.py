pkgname = "crun"
pkgver = "1.14.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
# broken presently
configure_gen = []
make_cmd = "gmake"
# full testsuite fails in netns
make_check_target = "tests/tests_libcrun_errors.log"
hostmakedepends = [
    "gmake",
    "go-md2man",
    "pkgconf",
    "python",
]
makedepends = [
    "argp-standalone",
    "libcap-devel",
    "libseccomp-devel",
    # -static for test build from all target
    "libunwind-devel-static",
    "yajl-devel",
]
pkgdesc = "Fast and lightweight OCI runtime"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.xz"
sha256 = "c416560f158c4a4a27d239f21a3809e5fd52fbf2106b0c5319343973508d1cec"


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.rm(self.destdir / "usr/lib/libcrun.a")
