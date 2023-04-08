import re

def get_all_omnetpp_6_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "which", "bison", "flex", "perl", "which", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz",
                "setenv_command": "source setenv",
                "configure_command": "./configure WITH_OSG=no",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["6.0.1", "6.0"]
        ]
    ]

def get_all_omnetpp_5_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "tk", "tcl", "qt5.qtbase", "qt5.qtsvg" ],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz" if version == "5.7" else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src.tgz" if version == "5.0" else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src-linux.tgz",
                "setenv_command": "source setenv -f",
                "configure_command": "./configure WITH_OSG=no WITH_OSGEARTH=no QT_VERSION=5",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["5.7", "5.6.2", "5.5.1", "5.4.1", "5.3", "5.2.1", "5.1.1", "5.0"]
        ]
    ]

def get_all_omnetpp_4_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "stdenv": "gcc7Stdenv",
                "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "libxml2", "expat", "xdg-utils" ],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-4.0/omnetpp-4.0p1-src.tgz" if version == '4.0p1' else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src.tgz",
                "setenv_command": ". setenv",
                "configure_command": "./configure",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["4.6", "4.5", "4.4.1", "4.3.1", "4.2.2", "4.1", "4.0p1"]
        ]
    ]

def get_all_omnetpp_3_x_versions():
    return [
        {
            "name": "omnetpp", "version": "3.3p1",
            "stdenv": "gcc7Stdenv",
            "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "libxml2", "expat" ],
            "download_url": "https://github.com/omnetpp/omnetpp/releases/download/omnetpp-3.3-ubuntu18.04/omnetpp-3.3-src-gcc73.tgz",
            "setenv_command": "source setenv",
            "configure_command": "./configure",
            "build_command": "make MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_git_versions():
    return [
        {
            "name": "omnetpp", "version": "git",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"],
            "git_url": "git@github.com:omnetpp/omnetpp.git",
            "setenv_command": "source setenv",
            "configure_command": "./configure WITH_OSG=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_patched_release_versions():
    def dotx(version):
        # 4.2, 4.2.1, 4.2p1 -> 4.2.x
        return re.sub("(\\d\\.\\d)[\\.p]\\d", "\\1", version) + ".x"

    downloads_dir = "/home/andras/projects/opp_env_downloads"
    local_omnetpp_git_repo = "/home/andras/projects/xxx/omnetpp-patches"

    return [
        *[
            {
                "name": "omnetpp",
                "version": dotx(version),
                "external_nix_packages": ["ccache", "which", "bison", "flex", "perl", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"] if version.startswith("6.") else
                                         ["ccache", "which", "bison", "flex", "perl", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "tk", "tcl", "cairo" ] if version.startswith("5.") else
                                         [ "bison", "flex", "perl", "tk", "tcl", "libxml2", "expat", "xdg-utils" ] if version.startswith("4.") else
                                         [ "bison", "flex", "perl", "tk", "tcl", "libxml2", "expat" ] if version.startswith("3.") else [],
                "download_url": f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz" if version.startswith("6.") or version == "5.7" else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src.tgz" if version == "5.0" else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src-linux.tgz" if version.startswith("5.") else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-4.0/omnetpp-4.0p1-src.tgz" if version == '4.0p1' else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-src.tgz" if version.startswith("4.") else
                                f"https://github.com/omnetpp/omnetpp/releases/download/omnetpp-3.3-ubuntu18.04/omnetpp-3.3-src-gcc73.tgz" if version == "3.3p1" else "",
                "patch_command": f"wget -O configure https://github.com/omnetpp/omnetpp/raw/omnetpp-{version}/configure && " +
                                 f"wget -O configure.in https://github.com/omnetpp/omnetpp/raw/omnetpp-{version}/configure.in && " +
                                 f"wget -O patchfile.diff https://github.com/omnetpp/omnetpp/compare/omnetpp-{version}...omnetpp-{dotx(version)}.patch && " +
                                 f"git apply patchfile.diff",
                "setenv_command": "source setenv",
                "configure_command": "./configure WITH_OSG=no" if version.startswith("6.") else
                                     "./configure WITH_OSG=no WITH_OSGEARTH=no QT_VERSION=5" if version == "5.0" else
                                     "./configure WITH_OSG=no WITH_OSGEARTH=no" if version.startswith("5.") else
                                     "./configure",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean",
                "options": {
                    "gcc7": {
                        "stdenv": "gcc7Stdenv",
                    },
                    "local": {
                        "download_command": f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-{version}-linux-x86_64.tgz" if version.startswith("6.") or version == "5.7" else
                                            f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-{version}-src.tgz" if version == "5.0" else
                                            f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-{version}-src-linux.tgz" if version.startswith("5.") else
                                            f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-4.0p1-src.tgz" if version == '4.0p1' else
                                            f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-{version}-src.tgz" if version.startswith("4.") else
                                            f"mkdir omnetpp-{dotx(version)} && cd omnetpp-{dotx(version)} && tar --strip-components=1 -xzf {downloads_dir}/omnetpp-3.3-src-gcc73.tgz" if version == "3.3p1" else "",
                        "download_url": "",
                        "patch_command": f"git --git-dir={local_omnetpp_git_repo}/.git show omnetpp-{version}:configure >configure && " +
                                         f"git --git-dir={local_omnetpp_git_repo}/.git show omnetpp-{version}:configure.in >configure.in && " +
                                         f"git --git-dir={local_omnetpp_git_repo}/.git diff omnetpp-{version}..omnetpp-{dotx(version)} --patch > patchfile.diff && " +
                                         f"git apply --exclude 'ui/*' --exclude '**/Makefile.vc' patchfile.diff",
                    },
                    "local-git": {
                        "download_command": f"git clone -l {local_omnetpp_git_repo} omnetpp-{dotx(version)} --branch omnetpp-{dotx(version)}",
                        "download_url": "",
                        "patch_command": ""
                    }
                }
            } for version in ["6.0.1",
                              "5.7", "5.6.2", "5.5.1", "5.4.1", "5.3", "5.2.1", "5.1.1", "5.0",
                              "4.6", "4.5", "4.4.1", "4.3.1", "4.2.2", "4.1", "4.0p1",
                              "3.3p1"]
        ]
    ]

def get_all_omnetpp_versions():
    return [
        *get_all_omnetpp_git_versions(),
        *get_all_omnetpp_6_x_versions(),
        *get_all_omnetpp_5_x_versions(),
        *get_all_omnetpp_4_x_versions(),
        *get_all_omnetpp_3_x_versions(),
        *get_all_omnetpp_patched_release_versions()
    ]
