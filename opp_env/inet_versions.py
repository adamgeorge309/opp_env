import re
description = "INET Framework is an open-source OMNeT++ model suite for wired, wireless and mobile networks."

def dotx(version):
    # 4.2, 4.2.1, 4.2p1 -> 4.2.x
    return re.sub("(\\d\\.\\d)[\\.p]\\d", "\\1", version) + ".x"

def join_nonempty_items(sep, list):
    return sep.join([x for x in list if x])

def make_inet_project_description(inet_version, omnetpp_versions):
    # It is possible to install from locally downloaded tarballs and repo, using the  "local" or "local-git" options.
    # This is used mainly for testing. The following are the locations of the local files.
    downloads_dir = "~/projects/opp_env_downloads"
    local_inet_git_repo = "~/projects/inet"

    is_git_branch = inet_version == "master" or inet_version.endswith(".x")

    return {
        "name": "inet", "version": inet_version, "description": description,
        "folder_name": "inet",
        "required_projects": {"omnetpp": omnetpp_versions}, # list(set([dotx(v) for v in omnetpp_versions]))},
        "external_nix_packages": ["python3", "z3"] if inet_version.startswith("4.") else
                                 ["python3", "python2"]  if inet_version.startswith("3.") else [], # inet_featuretool, uses python2 in original, and python3 in modernized versions
        "download_url":
            f"https://github.com/inet-framework/inet/releases/download/v{inet_version}/inet-{inet_version}-src.tgz" if not is_git_branch else
            f"https://github.com/inet-framework/inet/archive/refs/tags/v{inet_version}.tar.gz",
        "setenv_command": "source setenv -f" if inet_version.startswith("4.") else "",
        "patch_command": join_nonempty_items("\n", [
            "touch tutorials/package.ned" if inet_version <= "4.2.1" and inet_version >= "3.6.0" else "",
            "sed -i 's| python$| python2|' inet_featuretool" if inet_version >= "3.0" and inet_version < "4.0" else "", # in shebang line
            "sed -i 's|info\\[\\]|info[0]|' src/inet/common/serializer/sctp/headers/sctphdr.h" if inet_version.startswith("3.") else "", # "error: flexible array member in union"
            "sed -i 's|info\\[\\]|info[0]|' src/util/headerserializers/sctp/headers/sctp.h" if inet_version.startswith("2.") else "", # "error: flexible array member in union"

            # Linux appears to define "__linux__" nowadays, not "linux"; affected: serializer/headers/defs.h, ExtInterface.cc, RawSocket.cc, OsUdp.cc, Ext.cc, etc., and their renamed/moved versions
            "for f in $(grep -Rl 'defined(linux)'); do sed -i 's|defined(linux)|defined(__linux__)|' $f; done",

            # cResultFilterDescriptor was renamed in omnetpp-5.1
            "sed -i 's|cResultFilterDescriptor|cResultFilterType|' src/inet/common/figures/DelegateSignalConfigurator.cc" if inet_version == "3.4.0" else "",

            # PacketDrillApp bug in early 3.x versions
            "sed -i 's|->spp_hbinterval > 0|->spp_hbinterval->getNum() > 0|' src/inet/applications/packetdrill/PacketDrillApp.cc" if inet_version>="3.5.0" and inet_version<="3.6.1" else "",
            "sed -i 's|->spp_pathmaxrxt > 0|->spp_pathmaxrxt->getNum() > 0|' src/inet/applications/packetdrill/PacketDrillApp.cc" if inet_version>="3.5.0" and inet_version<="3.6.1" else "",

            # INT64_PRINTF_FORMAT was removed in omnetpp-5.3 (?), replace with "l" for simplicity (suits all 64-bit platforms except Windows)
            "for f in $(grep -Rl 'INT64_PRINTF_FORMAT'); do sed -i 's|INT64_PRINTF_FORMAT|\"l\"|' $f; done" if inet_version.startswith("3.") else "",
        ]),
        "build_command": "make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE",
        "clean_command": "[ ! -f src/Makefile ] || make clean",
        "options": {
            "git": {
                "option_description": "Install from git repo on github",
                "category": "download",
                "git_url": "git@github.com:inet-framework/inet.git",
                "git_branch": f"v{inet_version}",
                "download_url": "",
            },
            "local": {
                "option_description": "Install from tarballs on local disk",
                "category": "download",
                "download_command": f"mkdir inet-{inet_version} && cd inet-{inet_version} && tar --strip-components=1 -xzf {downloads_dir}/inet-{inet_version}.tar.gz",
                "download_url": "",
            },
            "local-git": {
                "option_description": "Install from git repo on local disk",
                "category": "download",
                "download_command": f"git clone -l {local_inet_git_repo} inet-{inet_version} --branch v{inet_version}",
                "download_url": "",
            }
        }
    }

def get_all_inet_released_versions():
    return [ make_inet_project_description(inet_version, omnetpp_versions) for inet_version, omnetpp_versions in [
        ["4.4.1", ["6.0.*"]],
        ["4.4.0", ["6.0.*"]],
        ["4.3.9", ["6.0.*"]],
        ["4.3.8", ["6.0.*"]],
        ["4.3.7", ["6.0.*"]],
        ["4.3.6", ["6.0.*"]],
        ["4.3.5", ["6.0.*"]],
        ["4.3.4", ["6.0.*"]],
        ["4.3.3", ["6.0.*"]],
        ["4.3.2", ["6.0.*"]],
        ["4.3.1", ["6.0.*"]],
        ["4.3.0", ["6.0.*"]],
        ["4.2.10",["5.7.*", "6.0.*"]],
        ["4.2.9", ["5.7.*", "6.0.*"]],
        ["4.2.8", ["5.7.*"]],
        ["4.2.7", ["5.7.*"]],
        ["4.2.6", ["5.6.2", "5.7.*"]],
        ["4.2.5", ["5.6.2", "5.7.*"]],
        ["4.2.4", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.2.3", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.2.2", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.2.1", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.2.0", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.1.2", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.1.1", ["5.4.1", "5.5.*", "5.6.*", "5.7.*"]],
        ["4.1.0", ["5.4.1"]], # with omnetpp-5.5.1: error: PacketQueue.cc:23: cPacketQueue constructor call is ambiguous
        ["4.0.0", ["5.4.1"]], # with omnetpp-5.5.1: error: PacketQueue.cc:23: cPacketQueue constructor call is ambiguous

        ["3.8.3", ["5.7.*", "6.0.*"]],
        ["3.8.2", ["5.7.*", "6.0.*"]],
        ["3.8.1", ["5.7.*", "6.0.*"]],
        ["3.8.0", ["5.7.*", "6.0.*"]],
        ["3.7.1", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.7.0", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.6.8", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.6.7", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.6.6", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.6.5", ["5.3.*", "5.4.*", "5.5.*", "5.6.*", "5.7.*"]],
        ["3.6.4", ["5.3.*", "5.4.*"]], # note: this adds support for changed cMessagePrinter API in omnetpp-5.3; omnetpp-5.5 fails due to cPacketQueue constructor ambiguity
        ["3.6.3", ["5.2.*"]], # with with omnetpp-5.3: error due to cMessagePrinter::printMessage() interface change
        ["3.6.2", ["5.2.*"]], # with with omnetpp-5.3: error due to cMessagePrinter::printMessage() interface change
        ["3.6.1", ["5.2.*"]], # with with omnetpp-5.3: error due to cMessagePrinter::printMessage() interface change
        ["3.6.0", ["5.2.*"]], # compile error
        ["3.5.x", ["5.1.*"]],
        ["3.5.0", ["5.1.*"]],
        ["3.4.0", ["5.1.*"]], # with omnetpp-5.1: fail, because cResultFilterDescriptor was renamed to cResultFilterType, with 5.2 due to missing INT64_PRINTF_FORMAT, etc.
        ["3.3.0", ["4.6.*", "5.0.*", "5.1.*"]], # with omnetpp-5.2.1: RoutingTableRecorder.cc:296:37: error: expected ')' (due to missing INT64_PRINTF_FORMAT symbol?)
        ["3.2.4", ["4.6.*", "5.0.*", "5.1.*"]], # # with omnetpp-5.2.1: RoutingTableRecorder.cc:296:37: error: expected ')' (due to missing INT64_PRINTF_FORMAT symbol?)
        ["3.2.3", ["4.6.*"]], # with omnetpp-5.0: Ieee80211OldMac.cc:38:21: error: no member named 'Ieee80211OldMac' in namespace 'inet'; MAYBE Register_Enum issue?
        ["3.2.2", ["4.6.*"]], # with omnetpp-5.0: Ieee80211OldMac.cc:38:21: error: no member named 'Ieee80211OldMac' in namespace 'inet'; MAYBE Register_Enum issue?
        ["3.2.1", ["4.6.*"]], # with omnetpp-5.0: HeatMapFigure.cc:27:5: error: use of undeclared identifier 'fill' (fixed in inet-3.2.2)
        ["3.2.0", ["4.6.*"]], # with omnetpp-5.0: HeatMapFigure.cc:27:5: error: use of undeclared identifier 'fill' (fixed in inet-3.2.2)
        ["3.1.x", ["4.6.*"]],
        ["3.1.1", ["4.6.*"]],
        ["3.1.0", ["4.6.*"]],
        ["3.0.x", ["4.6.*"]],
        ["3.0.0", ["4.6.*"]],

        ["2.6.0", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.5.0", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.4.0", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.3.0", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.2.0", ["4.2.*", "4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.1.0", ["4.2.*", "4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.0.0", ["4.2.*"]], # 4.3+ versions don't work, due to getFieldArraySize issue

        ["2.6.x", ["4.4.*", "4.5.*", "4.6.*"]],
        ["2.5.x", ["4.4.*", "4.5.*", "4.6.*"]],
        ["2.4.x", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.3.x", ["4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.2.x", ["4.2.*", "4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.1.x", ["4.2.*", "4.3.*", "4.4.*", "4.5.*", "4.6.*"]],
        ["2.0.x", ["4.2.*", "4.3.*", "4.4.*", "4.5.*", "4.6.*"]]
    ]]

def get_all_inet_versions():
    return [
        {
            "name": "inet", "version": "git", "description": description,
            "folder_name": "inet",
            "required_projects": {"omnetpp": ["master"]},
            "external_nix_packages": ["python3", "z3"],
            "git_url": "git@github.com:inet-framework/inet.git",
            "setenv_command": "source setenv",
            "build_command": "make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE",
            "clean_command": "[ ! -f src/Makefile ] || make clean"
        },
        *get_all_inet_released_versions()
    ]
