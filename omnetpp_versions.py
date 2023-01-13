def get_all_omnetpp_6_x_versions():
    return [
        *[
            {
                "name": "omnetpp", "version": version,
                "external_nix_packages": ["ccache", "which", "bison", "flex", "perl", "which", "xdg-utils", "qt5.qtbase", "qt5.qtsvg", "python3", "python3Packages.numpy", "python3Packages.scipy", "python3Packages.pandas", "python3Packages.matplotlib", "python3Packages.posix_ipc"],
                "download_command": f"wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-{version}/omnetpp-{version}-linux-x86_64.tgz && tar xzf omnetpp-{version}-linux-x86_64.tgz && rm omnetpp-{version}-linux-x86_64.tgz",
                "setenv_command": "source setenv",
                "configure_command": "./configure WITH_OSG=no",
                "build_command": "make -j$NIX_BUILD_CORES MODE=release",
                "clean_command": "make clean"
            } for version in ["6.0.1", "6.0"]
        ]
    ]

def get_all_omnetpp_5_x_versions():
    return [
        {
            "name": "omnetpp", "version": "5.7",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.7/omnetpp-5.7-linux-x86_64.tgz && tar xzf omnetpp-5.7-linux-x86_64.tgz && rm omnetpp-5.7-linux-x86_64.tgz",
            "setenv_command": "source setenv",
            "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
        {
            "name": "omnetpp", "version": "5.6.2",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.6.2/omnetpp-5.6.2-src-linux.tgz && tar xzf omnetpp-5.6.2-src-linux.tgz && rm omnetpp-5.6.2-src-linux.tgz",
            "setenv_command": "source setenv -f",
            "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
        {
            "name": "omnetpp", "version": "5.5.1",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.5.1/omnetpp-5.5.1-src-linux.tgz && tar xzf omnetpp-5.5.1-src-linux.tgz && rm omnetpp-5.5.1-src-linux.tgz",
            "setenv_command": "source setenv -f",
            "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
        {
            "name": "omnetpp", "version": "5.4.1",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.4.1/omnetpp-5.4.1-src-linux.tgz && tar xzf omnetpp-5.4.1-src-linux.tgz && rm omnetpp-5.4.1-src-linux.tgz",
            "setenv_command": "source setenv -f",
            "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
        {
            "name": "omnetpp", "version": "5.3",
            "external_nix_packages": ["ccache", "bison", "flex", "perl", "which", "xdg-utils", "python3", "qt5.qtbase", "qt5.qtsvg" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.3/omnetpp-5.3-src-linux.tgz && tar xzf omnetpp-5.3-src-linux.tgz && rm omnetpp-5.3-src-linux.tgz",
            "setenv_command": "source setenv -f",
            "configure_command": "unset AR && ./configure WITH_OSG=no WITH_OSGEARTH=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_4_x_versions():
    return [
        {
            "name": "omnetpp", "version": "4.6",
            "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "expat", "xdg-utils" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-4.6/omnetpp-4.6-src.tgz && tar xzf omnetpp-4.6-src.tgz && rm omnetpp-4.6-src.tgz",
            "setenv_command": "export PATH=$(pwd)/bin:$PATH && export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && export TCL_LIBRARY=$(echo 'puts [info library]; exit' | wish) && export HOSTNAME && export HOST",
            "configure_command": "unset AR && ./configure",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
        {
            "name": "omnetpp", "version": "4.4.1",
            "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "expat", "xdg-utils" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-4.4.1/omnetpp-4.4.1-src.tgz && tar xzf omnetpp-4.4.1-src.tgz && rm omnetpp-4.4.1-src.tgz",
            "setenv_command": "export PATH=$(pwd)/bin:$PATH && export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && export TCL_LIBRARY=$(echo 'puts [info library]; exit' | wish) && export HOSTNAME && export HOST",
            "configure_command": "unset AR && ./configure",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_3_x_versions():
    return [
        {
            "name": "omnetpp", "version": "3.3p1",
            "stdenv": "gcc7Stdenv",
            "external_nix_packages": [ "bison", "flex", "perl", "tk", "tcl", "expat" ],
            "download_command": "wget -q -nv --show-progress https://github.com/omnetpp/omnetpp/releases/download/omnetpp-3.3-ubuntu18.04/omnetpp-3.3-src-gcc73.tgz && tar xzf omnetpp-3.3-src-gcc73.tgz && rm omnetpp-3.3-src-gcc73.tgz && mv omnetpp-omnetpp-3.3-ubuntu18.04 omnetpp-3.3p1",
            "setenv_command": "export PATH=$(pwd)/bin:$PATH && export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH && export TCL_LIBRARY=$(echo 'puts [info library]; exit' | wish)",
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
            "download_command": "git clone git@github.com:omnetpp/omnetpp.git",
            "setenv_command": "source setenv",
            "configure_command": "./configure WITH_OSG=no",
            "build_command": "make -j$NIX_BUILD_CORES MODE=release",
            "clean_command": "make clean"
        },
    ]

def get_all_omnetpp_versions():
    return [
        *get_all_omnetpp_git_versions(),
        *get_all_omnetpp_6_x_versions(),
        *get_all_omnetpp_5_x_versions(),
        *get_all_omnetpp_4_x_versions(),
        *get_all_omnetpp_3_x_versions(),
    ]
