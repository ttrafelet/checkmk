load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("//:bazel_variables.bzl", "UPSTREAM_MIRROR_URL")

def msitools(version_str, sha256):
    filename = "msitools-" + version_str + ".tar.gz"
    http_archive(
        name = "msitools",
        build_file = "@omd_packages//omd/packages/msitools:BUILD.msitools.bazel",
        strip_prefix = "msitools-" + version_str,
        patches = [
            "//omd/packages/msitools/patches:0001-configure_remove_wixl.dif",
            "//omd/packages/msitools/patches:0002-msibuild_argc_fix.dif",
            "//omd/packages/msitools/patches:0003-configure_remove_libxml.dif",
            "//omd/packages/msitools/patches:0004-compile-on-sles11.dif",
        ],
        patch_args = ["-p1"],
        patch_tool = "patch",
        urls = [
            "http://ftp.gnome.org/pub/GNOME/sources/msitools/" + version_str + "/" + filename,
            UPSTREAM_MIRROR_URL + filename,
        ],
        sha256 = sha256,
    )
