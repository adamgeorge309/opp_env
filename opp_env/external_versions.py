def get_project_descriptions():
    return [
        {
            # DONE - ok
            "name": "fico4omnet", "version": "master",
            "description": "Fieldbus Communication (CAN and FlexRay)",
            "required_projects": {"omnetpp": ["5.5"]},
            "git_url": "https://github.com/CoRE-RG/FiCo4OMNeT.git",
            "git_branch": "master",
            "patch_commands": [
                "mkdir bin",
                "rm src/run_fico4omnet.cmd",
                "mv src/run_fico4omnet bin",
                "sed -i 's|DIR=`dirname $0`|DIR=`dirname \\$0`/../src|' bin/run_fico4omnet",
                "sed -i 's|MAKEMAKE_OPTIONS .* -I.|& -o FiCo4OMNeT|' Makefile"
            ],
            "setenv_commands": [
                "export NEDPATH=$NEDPATH:$FICO4OMNET_ROOT/src:$FICO4OMNET_ROOT/examples:$FICO4OMNET_ROOT/examples_andl:$FICO4OMNET_ROOT/simulations",
                "export PATH=$PATH:$FICO4OMNET_ROOT/bin",
                "echo 'Hint: use the run_fico4omnet command to run the simulations in the examples folder.'"
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "ansa", "version": "inet3.4.0",
            "required_projects": {"omnetpp": ["5.1"]},
            "git_url": "https://github.com/kvetak/ANSA.git",
            "git_branch": "ansainet-3.4.0",
            "patch_commands": [
                "chmod +x inet_featuretool",
                "chmod +x src/run_inet",
                "sed -i 's|getClassName() > 0)|getCount() > 0)|' src/ansa/routing/babel/BabelDef.cc",
                "sed -i 's|cResultFilterDescriptor|cResultFilterType|' src/inet/common/figures/DelegateSignalConfigurator.cc",
                "sed -i 's/if (vector_cost<=nullptr)/if (vector_cost == nullptr)/' src/inet/routing/extras/dsr/dsr-uu/path-cache.cc",
                "rm src/run_inet.cmd",
                "mkdir bin",
                "mv src/run_inet bin",
                "sed -i 's|DIR=`dirname $0`|DIR=`dirname \\$0`/../src|' bin/run_inet"
            ],
            "setenv_commands": [
                "echo 'Hint: use the run_inet command to run the simulations in the examples/ansa folder.'",
                "export PATH=$PATH:$ANSA_ROOT/bin"
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # DONE - ok
            "name": "vanetza", "version": "master",
            "nix_packages": ["cmake", "boost", "geographiclib", "cryptopp"],
            "git_url": "https://github.com/riebl/vanetza.git",
            "build_commands": ["mkdir -p build && cd build && cmake .. && make"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "flora", "version": "1.1.0",
            "required_projects": {"omnetpp": ["6.0"], "inet": ["4.4.0"]},
            "download_url": "https://github.com/florasim/flora/releases/download/v1.1.0/flora-1.1.0.tgz",
            "patch_commands": [
                "sed -i -E 's|INET_DIR = [^ ]+|INET_DIR = $(INET_ROOT)|' Makefile",
                "sed -i -E 's|-KINET_PROJ=[^ ]+|-KINET_PROJ=$(INET_DIR)|' Makefile"
            ],
            "setenv_commands": [
                "echo 'Hint: use the ./run command to run the example in the simulations folder.'",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "core4inet", "version": "221109",
            "required_projects": {"omnetpp": ["5.5"], "inet": ["3.6.6"]},
            "download_url": "https://github.com/CoRE-RG/CoRE4INET/archive/refs/tags/nightly/2022-11-09_00-01-11.tar.gz",
            "setenv_commands": [
                "echo 'Hint: use the ./rundemo command in the examples folder or the ./run command in any of the example subfolders.'",
                "export INETPATH=$INET_ROOT",
            ],
            "patch_commands": [
                "sed -i -E 's|INET_PROJ=[^ ]+|INET_PROJ=$(INET_ROOT)|' Makefile",
                "sed -i -E 's|-L.*/src|-L$$\\\\(INET_PROJ\\\\)/src|' Makefile",
                "sed -i -E 's|-O out |-O out -o CoRE4INET |' Makefile"
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "simproctc", "version": "2.0.2",
            "required_projects": {"omnetpp": ["6.0"]},
            "download_url": "https://github.com/dreibh/simproctc/archive/refs/tags/simproctc-2.0.2.tar.gz",
            "setenv_commands": ["export OPPMAIN_LIB=$OMNETPP_ROOT/lib"],
            # "patch_commands": [
            #     "sed -i -E 's|INET_PROJ=[^ ]+|INET_PROJ=$(INET_ROOT)|' Makefile",
            #     "sed -i -E 's|-L.*/src|-L$$\\\\(INET_PROJ\\\\)/src|' Makefile",
            #     "sed -i -E 's|-O out |-O out -o CoRE4INET |' Makefile"
            # ],
            "build_commands": ["cd example-simulation && opp_makemake -f && make"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "hnocs", "version": "master",
            "required_projects": {"omnetpp": ["5.5"]},
            "git_url": "https://github.com/yanivbi/HNOCS.git",
            "git_branch": "master",
            "setenv_commands": [
                "echo 'Hint: use the ./run_nocs command in the examples folder.'",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "gptp", "version": "master",
            "required_projects": {"omnetpp": ["5.2"], "inet": ["3.6.3"]},
            "git_url": "https://gitlab.amd.e-technik.uni-rostock.de/peter.danielis/gptp-implementation.git",
            "setenv_commands": [
                "export INET_PROJ=$INET_ROOT",
                "echo 'Hint: use the ./run command in the simulations folder.'",
            ],
            "patch_commands": [
                "sed -i -E 's|ieee8021as|IEEE8021AS|' IEEE8021AS/simulations/run",
                "sed -i -E 's|-n.*|-n $INET_ROOT/src:.:../src $*|' IEEE8021AS/simulations/run",
                "chmod +x IEEE8021AS/simulations/run",
            ],
            "build_commands": ["cd IEEE8021AS/src && opp_makemake -f --deep -KINET_PROJ=$INET_PROJ -DINET_IMPORT -I$INET_PROJ/src -L$INET_PROJ/src -lINET && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "keetchlib", "version": "master",
            "nix_packages": ["autoconf", "automake", "libtool"],
            "git_url": "https://github.com/ComNets-Bremen/KeetchiLib.git",
            "git_branch": "master",
            "build_commands": ["./bootstrap.sh && ./configure && make"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "openflow", "version": "master",
            "required_projects": {"omnetpp": ["6.0"], "inet": ["4.4.0"]},
            "git_url": "https://github.com/inet-framework/openflow.git",
            "setenv_commands": [
                "export INET_PROJ=$INET_ROOT",
                "export PATH=$PATH:$OPENFLOW_ROOT/src",
                "echo 'Hint: use the run_openflow command to run the examples in the scenarios folder.'"
            ],
            "patch_commands": [
                "sed -i -E 's|-KINET_PROJ=[^ ]+|-KINET_PROJ=$(INET_ROOT) -o openflow|' Makefile",
                "sed -i 's|$DIR/../../inet|$INET_ROOT|' src/run_openflow",
                "sed -i 's|opp_run_dbg|opp_run|' src/run_openflow",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "nesting", "version": "master",
            "required_projects": {"omnetpp": ["5.5"], "inet": ["4.1.2"]},
            "git_url": "https://gitlab.com/ipvs/nesting.git",
            "setenv_commands": ["export INET_PROJ=$INET_ROOT",
                                "export NESTING=$NESTING_ROOT"],
            "patch_commands": [
                "sed -i -E 's|-KINET_PROJ=[^ ]+|-KINET_PROJ=$(INET_ROOT)|' Makefile",
                "sed -i 's|NESTING=.*|#NESTING=|' simulations/runsim-qt",
                "sed -i -E 's|INET=.*|INET=$INET_ROOT|' simulations/runsim-qt",
                "sed -i 's|./nesting$D|$NESTING/simulations/nesting$D|' simulations/runsim-qt",
                "sed -i 's|-n .:|-n $NESTING/simulations:|' simulations/runsim-qt",
                "sed -i 's|NESTING=.*|#NESTING=|' simulations/runsim",
                "sed -i -E 's|INET=.*|INET=$INET_ROOT|' simulations/runsim",
                "sed -i 's|./nesting$D|$NESTING/simulations/nesting$D|' simulations/runsim",
                "sed -i 's|-n .:|-n $NESTING/simulations:|' simulations/runsim",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "castalia", "version": "master",
            "nix_packages": ["python2"],
            "required_projects": {"omnetpp": ["4.4"]},
            "git_url": "https://github.com/boulis/Castalia.git",
            "git_branch": "master",
            "patch_commands": [
                "sed -i 's|bin/python|bin/env python2|' Castalia/bin/Castalia",
                "sed -i 's|bin/python|bin/env python2|' Castalia/bin/CastaliaPlot",
                "sed -i 's|bin/python|bin/env python2|' Castalia/bin/CastaliaResults",
                "sed -i 's|bin/python|bin/env python2|' Castalia/bin/extractOmnetppINI",
            ],
            "setenv_commands": [
                "export PATH=$PATH:$CASTALIA_ROOT/Castalia/bin",
                "echo 'Hint: Use the Castalia command to run the examples in the Simulations folder.'"
            ],
            "build_commands": ["cd Castalia && ./makemake && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # DONE - ok
            "name": "mixim", "version": "2.3",
            "required_projects": {"omnetpp": ["4.6", "4.5", "4.4", "4.3", "4.2"], "inet": ["2.1.0"]},
            "download_url": "https://github.com/omnetpp-models/mixim/archive/refs/tags/2.3.tar.gz",
            "patch_commands": ["sed -i -E 's|INET_PROJECT_DIR=.*|INET_PROJECT_DIR=$(INET_ROOT)|' Makefile"],
            "setenv_commands": [
                "export PATH=$MIXIM_ROOT/src:$PATH",
                "echo 'Hint: Use `./run` in the examples and examples-inet subfolders.'"
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
            "description": "MiXiM is a simulation framework to support modeling and simulation of wireless and mobile networks. NOTE: This is a deprecated model kept only for archival purposes. All functionality of this model is available in the INET Framework."
        },

        {
            # DONE - ok
            "name": "inetgpl", "version": "1.0",
            "description": "GPL licensed models for INET",
            "required_projects": {"inet": ["4.4.*"], "omnetpp": ["6.0.*"]},
            "download_commands": ["git clone https://github.com/inet-framework/inet-gpl.git inetgpl-1.0"],
            "setenv_commands": ["source setenv"],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

                {
            # DONE - ok
            "name": "rspsim", "version": "6.1.2",
            "required_projects": {"omnetpp": ["6.0", "5.7"]},
            "download_url": "https://github.com/dreibh/rspsim/archive/refs/tags/rspsim-6.1.2.tar.gz",
            "patch_commands": [
                "sed -i -E 's|<ext_socket.h>|\"ext_socket.h\"|' model/poolelementnode-template.h",
                "sed -i -E 's|<ext_socket.h>|\"ext_socket.h\"|' model/transportaddressblock.c"
            ],
            "build_commands": ["cd model && opp_makemake -f && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # DONE - ok
            "name": "rina", "version": "master",
            "required_projects": {"omnetpp": ["5.2"]},
            "git_url": "https://github.com/kvetak/RINA.git",
            "patch_commands": [
                "sed -i -E 's|-O out|-O out -I. -I../src|g' makemakefiles",
            ],
            "setenv_commands": [
                "echo 'Hint: use `./simulate.sh examples/Demos/UseCase1/ -G -c Ping`'",
            ],
            "build_commands": ["make -f makemakefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
            # ./simulate.sh examples/Demos/UseCase1/ -G -c Ping
        },

        {
            # DONE
            "name": "ieee802154standalone", "version": "master",
            "required_projects": {"omnetpp": ["4.6"], "inet": ["2.6.0"]},
            "git_url": "https://github.com/michaelkirsche/IEEE802154INET-Standalone.git",
            "patch_commands": [
                "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                "sed -i 's|ChannelAccess.h|world/radio/ChannelAccess.h|g' src/*/*.h",
                "sed -i 's|InterfaceToken.h|networklayer/common/InterfaceToken.h|g' src/*/*.h src/*/*.h",
                "chmod +x simulations/run",
                "sed -i 's|-n .:../src|-n ..:../src:$\{INET_ROOT\}/src|g' simulations/run",
                "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I.     -I$(INET_ROOT)/src/.     -I$(INET_ROOT)/src/applications     -I$(INET_ROOT)/src/applications/common     -I$(INET_ROOT)/src/applications/dhcp     -I$(INET_ROOT)/src/applications/ethernet     -I$(INET_ROOT)/src/applications/generic     -I$(INET_ROOT)/src/applications/httptools     -I$(INET_ROOT)/src/applications/pingapp     -I$(INET_ROOT)/src/applications/rtpapp     -I$(INET_ROOT)/src/applications/sctpapp     -I$(INET_ROOT)/src/applications/tcpapp     -I$(INET_ROOT)/src/applications/traci     -I$(INET_ROOT)/src/applications/udpapp     -I$(INET_ROOT)/src/applications/voip     -I$(INET_ROOT)/src/base     -I$(INET_ROOT)/src/battery     -I$(INET_ROOT)/src/battery/models     -I$(INET_ROOT)/src/linklayer     -I$(INET_ROOT)/src/linklayer/common     -I$(INET_ROOT)/src/linklayer/configurator     -I$(INET_ROOT)/src/linklayer/contract     -I$(INET_ROOT)/src/linklayer/ethernet     -I$(INET_ROOT)/src/linklayer/ethernet/switch     -I$(INET_ROOT)/src/linklayer/ext     -I$(INET_ROOT)/src/linklayer/idealwireless     -I$(INET_ROOT)/src/linklayer/ieee80211     -I$(INET_ROOT)/src/linklayer/ieee80211/mac     -I$(INET_ROOT)/src/linklayer/ieee80211/mgmt     -I$(INET_ROOT)/src/linklayer/ieee80211/radio     -I$(INET_ROOT)/src/linklayer/ieee80211/radio/errormodel     -I$(INET_ROOT)/src/linklayer/ieee8021d     -I$(INET_ROOT)/src/linklayer/ieee8021d/common     -I$(INET_ROOT)/src/linklayer/ieee8021d/relay     -I$(INET_ROOT)/src/linklayer/ieee8021d/rstp     -I$(INET_ROOT)/src/linklayer/ieee8021d/stp     -I$(INET_ROOT)/src/linklayer/ieee8021d/tester     -I$(INET_ROOT)/src/linklayer/loopback     -I$(INET_ROOT)/src/linklayer/ppp     -I$(INET_ROOT)/src/linklayer/queue     -I$(INET_ROOT)/src/linklayer/radio     -I$(INET_ROOT)/src/linklayer/radio/propagation     -I$(INET_ROOT)/src/mobility     -I$(INET_ROOT)/src/mobility/common     -I$(INET_ROOT)/src/mobility/contract     -I$(INET_ROOT)/src/mobility/group     -I$(INET_ROOT)/src/mobility/single     -I$(INET_ROOT)/src/mobility/static     -I$(INET_ROOT)/src/networklayer     -I$(INET_ROOT)/src/networklayer/arp     -I$(INET_ROOT)/src/networklayer/autorouting     -I$(INET_ROOT)/src/networklayer/autorouting/ipv4     -I$(INET_ROOT)/src/networklayer/autorouting/ipv6     -I$(INET_ROOT)/src/networklayer/bgpv4     -I$(INET_ROOT)/src/networklayer/bgpv4/BGPMessage     -I$(INET_ROOT)/src/networklayer/common     -I$(INET_ROOT)/src/networklayer/contract     -I$(INET_ROOT)/src/networklayer/diffserv     -I$(INET_ROOT)/src/networklayer/icmpv6     -I$(INET_ROOT)/src/networklayer/internetcloud     -I$(INET_ROOT)/src/networklayer/ipv4     -I$(INET_ROOT)/src/networklayer/ipv6     -I$(INET_ROOT)/src/networklayer/ipv6tunneling     -I$(INET_ROOT)/src/networklayer/ldp     -I$(INET_ROOT)/src/networklayer/manetrouting     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/base     -I$(INET_ROOT)/src/networklayer/manetrouting/batman     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand/orig     -I$(INET_ROOT)/src/networklayer/manetrouting/dsdv     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr/dsr-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo/dymoum     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo_fau     -I$(INET_ROOT)/src/networklayer/manetrouting/olsr     -I$(INET_ROOT)/src/networklayer/mpls     -I$(INET_ROOT)/src/networklayer/ospfv2     -I$(INET_ROOT)/src/networklayer/ospfv2/interface     -I$(INET_ROOT)/src/networklayer/ospfv2/messagehandler     -I$(INET_ROOT)/src/networklayer/ospfv2/neighbor     -I$(INET_ROOT)/src/networklayer/ospfv2/router     -I$(INET_ROOT)/src/networklayer/routing     -I$(INET_ROOT)/src/networklayer/routing/aodv     -I$(INET_ROOT)/src/networklayer/routing/dymo     -I$(INET_ROOT)/src/networklayer/routing/gpsr     -I$(INET_ROOT)/src/networklayer/routing/rip     -I$(INET_ROOT)/src/networklayer/rsvp_te     -I$(INET_ROOT)/src/networklayer/ted     -I$(INET_ROOT)/src/networklayer/xmipv6     -I$(INET_ROOT)/src/nodes     -I$(INET_ROOT)/src/nodes/aodv     -I$(INET_ROOT)/src/nodes/bgp     -I$(INET_ROOT)/src/nodes/dymo     -I$(INET_ROOT)/src/nodes/ethernet     -I$(INET_ROOT)/src/nodes/gpsr     -I$(INET_ROOT)/src/nodes/httptools     -I$(INET_ROOT)/src/nodes/inet     -I$(INET_ROOT)/src/nodes/internetcloud     -I$(INET_ROOT)/src/nodes/ipv6     -I$(INET_ROOT)/src/nodes/mpls     -I$(INET_ROOT)/src/nodes/ospfv2     -I$(INET_ROOT)/src/nodes/rip     -I$(INET_ROOT)/src/nodes/rtp     -I$(INET_ROOT)/src/nodes/wireless     -I$(INET_ROOT)/src/nodes/xmipv6     -I$(INET_ROOT)/src/status     -I$(INET_ROOT)/src/transport     -I$(INET_ROOT)/src/transport/contract     -I$(INET_ROOT)/src/transport/rtp     -I$(INET_ROOT)/src/transport/rtp/profiles     -I$(INET_ROOT)/src/transport/rtp/profiles/avprofile     -I$(INET_ROOT)/src/transport/sctp     -I$(INET_ROOT)/src/transport/tcp     -I$(INET_ROOT)/src/transport/tcp/flavours     -I$(INET_ROOT)/src/transport/tcp/queues     -I$(INET_ROOT)/src/transport/tcp_common     -I$(INET_ROOT)/src/transport/udp     -I$(INET_ROOT)/src/util     -I$(INET_ROOT)/src/util/headerserializers     -I$(INET_ROOT)/src/util/headerserializers/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv4     -I$(INET_ROOT)/src/util/headerserializers/ipv4/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv6     -I$(INET_ROOT)/src/util/headerserializers/ipv6/headers     -I$(INET_ROOT)/src/util/headerserializers/sctp     -I$(INET_ROOT)/src/util/headerserializers/sctp/headers     -I$(INET_ROOT)/src/util/headerserializers/tcp     -I$(INET_ROOT)/src/util/headerserializers/tcp/headers     -I$(INET_ROOT)/src/util/headerserializers/udp     -I$(INET_ROOT)/src/util/headerserializers/udp/headers     -I$(INET_ROOT)/src/util/messageprinters     -I$(INET_ROOT)/src/world     -I$(INET_ROOT)/src/world/annotations     -I$(INET_ROOT)/src/world/httptools     -I$(INET_ROOT)/src/world/obstacles     -I$(INET_ROOT)/src/world/radio     -I$(INET_ROOT)/src/world/scenario     -I$(INET_ROOT)/src/world/traci -o ieee802154inet_standalone -L$(INET_ROOT)/src -linet|' Makefile",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },
        
        {
            # compiles and runs, but needs weather API access to test
            "name": "os3", "version": "master",
            "nix_packages": ["curl", "tcl"],
            "required_projects": {"omnetpp": ["4.2"], "inet": ["2.2.0"]},
            "download_url": "https://github.com/inet-framework/os3/archive/refs/tags/v1.0.tar.gz",
            "setenv_commands": ["export INET_PROJ=$INET_ROOT",
                                "export TCL_LIBRARY=$TCLLIBPATH"],
            "patch_commands": [
                "sed -i -E 's|-KINET_PROJ=[^ ]+|-KINET_PROJ=$(INET_ROOT)|' Makefile",
                "sed -i 's|$DIR/../../inet|$INET_ROOT|' src/run_cni-os3",
                "sed -i 's|static const double|constexpr static const double|' src/*/*.h",
                "sed -i 's|../src/cni_os3|../src/run_cni-os3|' simulations/run",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            "name": "oversim", "version": "20190424",
            "required_projects": {"inet": ["3.6.*"], "omnetpp": ["5.4.*"]},
            "download_url": "https://github.com/inet-framework/oversim/archive/refs/tags/v20190424.tar.gz",
            "patch_commands": ["sed -i -E 's|INETDIR = .*|INETDIR = $(INET_ROOT)|' Makefile"],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && sed -i -E \"s|ned-path = .*|ned-path = $INET_ROOT/src;../src|\" simulations/default.ini"],
            "clean_commands": ["make clean"],
            "description": "DONE"
        },

        {
            # DONE - needs to be run in debug by default so far
            "name": "dctrafficgen", "version": "master",
            "nix_packages": ["libxml2"],
            "required_projects": {"omnetpp": ["4.6.x"]}, # TODO try 4.6
            "git_url": "https://github.com/Mellanox/DCTrafficGen.git",
            "patch_commands": [
                "sed -i 's|/usr/include/libxml2/|${pkgs.libxml2.dev}/include/libxml2|g' Makefile dctg_example/Makefile",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && cd dctg_example && make makefiles && make"],
            "clean_commands": ["make clean"]
            # run example simulation from dctg_example/simulations folder with:
            # ../out/clang-debug/src/dctg_example -u Qtenv -f omnetpp.ini -n ../../src:../src
        },

        {
            # DONE
            "name": "afdx", "version": "master",
            "required_projects": {"omnetpp": ["6.0.0"]},
            "git_url": "https://github.com/badapplexx/AFDX.git",
            "patch_commands": [
                "sed -i 's|.:../src|.:../src:../../queueinglib|g' afdx/simulations/run",
            ],
            "build_commands": ["cd queueinglib && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && cd ../afdx && make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && cd simulations && chmod +x run && chmod +x run_ancat"],
            "setenv_commands": ["echo 'Hint: in the afdx/simulations folder, use the ./run AutoNetwork.ini command to run the simulation'"],
            "clean_commands": ["make clean"],
        },

        {
            # WORKS - need to start with -i images, otherwise some node images are missing; 
            # uses git submodules for external libraries (should we use nix packages?) we shouldn't
            "name": "quisp", "version": "master",
            # "nix_packages": ['eigen'],
            "required_projects": {"omnetpp": ["6.0.0"]},
            "git_url": "https://github.com/sfc-aqua/quisp.git",
            "patch_commands": [
                # "sed -i 's|||g' ",
            ],
            "build_commands": ["make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
            # in quisp dir, run: 
            # ./quisp -i images simulations/two_nodes.ini
        },

        {
            # DONE
            "name": "cell", "version": "master",
            "description": "biological cell simulation",
            "required_projects": {"omnetpp": ["4.0.x"]},
            "git_url": "https://github.com/dhuertas/cell-signaling.git",
            "build_commands": ["cd src && opp_makemake -f --deep -O out -o cell && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
            # run example simulation from src folder with:
            # ./cell -n .. ../networks/demo.ini
        },

        {
            # DONE
            "name": "inetmanet", "version": "3.x",
            "required_projects": {"omnetpp": ["5.7.x"]},
            "git_url": "https://github.com/aarizaq/inetmanet-3.x.git",
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # DONE
            "name": "inetmanet", "version": "4.0.0",
            "required_projects": {"omnetpp": ["5.4.x"]},
            "download_url": "https://github.com/aarizaq/inetmanet-4.x/archive/refs/tags/v4.0.0.tar.gz",
            "setenv_commands": [". setenv -f"],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # DONE - by default needs omnetpp debug
            "name": "ndnomnet", "version": "master",
            "required_projects": {"omnetpp": ["5.1.x"]},
            "git_url": "https://github.com/amar-ox/NDNOMNeT.git",
            "patch_commands": [
                "sed -i.bak 's|->spp_hbinterval > 0|->spp_hbinterval->getNum() > 0|' inet/src/inet/applications/packetdrill/PacketDrillApp.cc",
                "sed -i.bak 's|->spp_pathmaxrxt > 0|->spp_pathmaxrxt->getNum() > 0|' inet/src/inet/applications/packetdrill/PacketDrillApp.cc",
            ],
            "build_commands": ["cd inet && make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },
        
        {
            # DONE - only builds with just 'make'; TwoSubnets example works, but segfault when running some other simulations
            "name": "oppbsd", "version": "4.0",
            "required_projects": {"omnetpp": ["4.2.0"]},
            "download_url": "https://svn.tm.kit.edu/trac/OppBSD/downloads/2",
            "build_commands": ["make"],
            "setenv_commands": ["echo 'Hint: run example simulations from their folder. For example, in examples/TwoSubnets folder: ./out/gcc-debug/TwoSubnets omnetpp.ini"],
            "clean_commands": ["make clean"],
        },
        
                {   # DONE
            "name": "inet", "version": "20100323",
            "required_projects": {"omnetpp": ["4.1.0"]},
            "download_url": "https://github.com/inet-framework/inet/releases/download/master_20100323/inet-20100323-src.tgz",
            "patch_commands": [
                "sed -i 's|  int octals\\[8\\] = |  unsigned int octals[8] = |' src/networklayer/contract/IPv6Address.cc",
                "sed -i 's|findGap(int \\*octals|findGap(unsigned int *octals|' src/networklayer/contract/IPv6Address.cc",
                "sed -i 's|machine/endian|endian|' src/util/headerserializers/headers/defs.h",
                "sed -i 's|info\\[\\]|info[0]|' src/util/headerserializers/headers/sctp.h",
                "sed -i 's|addr.sin_len|// addr.sin_len|' src/linklayer/ext/*.cc",  # ugly hack? this is needed on apple
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },
     
        {
            "name": "artery", "version": "oppsummit2015",
            "required_projects": {"omnetpp": ["5.5"], "vanetza": ["master"], "veins": ["5.2"]},
            "nix_packages": ["cmake", "boost"],
            "download_url": "https://github.com/riebl/artery/archive/refs/tags/opp-summit2015.tar.gz",
            "setenv_commands": [
                "export ARTERY_PATH=$ARTERY_ROOT",
                "export Vanetza_DIR=$VANETZA_ROOT/build",
                "export Veins_DIR=$VEINS_ROOT"
                # "echo 'Hint: use the run_inet command to run the simulations in the examples folder.'",
            ],
            "build_commands": ["mkdir -p build && cd build && cmake .. && cmake --build ."],
            "clean_commands": ["make clean"]
        },

        {
            "name": "artery", "version": "master",
            "required_projects": {"omnetpp": ["5.5"], "vanetza": ["master"], "veins": ["5.2"], "inet": ["3.7.1"]},
            "nix_packages": ["cmake", "boost"],
            "git_url": "https://github.com/riebl/artery.git",
            "patch_commands": [
                "sed -i 's|check_git_submodule|#check_git_submodule|' CMakeLists.txt",
                "sed -i 's|add_subdirectory|#add_subdirectory|' CMakeLists.txt",
                "sed -i 's|add_opp_target|#add_opp_target|' CMakeLists.txt",
            ],
            "setenv_commands": [
                "export ARTERY_PATH=$ARTERY_ROOT",
                "export Vanetza_DIR=$VANETZA_ROOT/build",
                "export Veins_DIR=$VEINS_ROOT",
                # "export SimuLTE_DIR=$SIMULTE_ROOT"
                "export INET_DIR=$INET_ROOT",
                # "echo 'Hint: use the run_inet command to run the simulations in the examples folder.'",
                "cd extern && rm -r inet && ln -sf -T $INET_ROOT inet",
                "rm -r veins && ln -sf -T $VEINS_ROOT veins",
                "rm -r vanetza && ln -sf -T $VANETZA_ROOT vanetza",
                # "cd extern && rm -r inet && ln -sf -T $INET_ROOT inet",
                # "ln -sf $VANETZA_ROOT extern",
                # "ln -sf $VEINS_ROOT extern",
                # "ln -s $INET_ROOT" extern/inet"
                # "ln -s $INET_ROOT" extern/inet"
            ],
            "build_commands": ["mkdir -p build && cd build && cmake .. && make"],
            "clean_commands": ["make clean"]
        },

        {
            # build errors in leach project
            "name": "leach", "version": "master",
            "required_projects": {"omnetpp": ["5.6.2"], "inet": ["4.2.5"]},
            "git_url": "https://github.com/Agr-IoT/LEACH.git",
            "setenv_commands": ["export INET4_PROJ=$INET_ROOT"],
            "patch_commands": [
                "sed -i 's|inet.node.LEACHnode|leach.node.LEACHnode|' inet/*/*/*.ned",
                "sed -i 's|inet.routing.leach|leach.routing.leach|' inet/*/*/*.ned",
                "sed -i 's|inet/routing/leach|routing/leach|' inet/*/*/*.cc inet/*/*/*.h",
                "mv inet src",
            #     "sed -i -E 's|-n.*|-n $INET_ROOT/src:.:../src $*|' IEEE8021AS/simulations/run",
            #     "chmod +x IEEE8021AS/simulations/run",
            ],
            "build_commands": ["opp_makemake -f --deep -O out -KINET4_PROJ=$INET4_PROJ -DINET_IMPORT -I./src -I$INET4_PROJ/src -L$INET4_PROJ/src -lINET$D && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # WIP; mobility can't load movements file
            # ./opslite-master ../simulations/omnetpp.ini -n .:../simulations:$INET_ROOT/src
            "name": "opslite", "version": "master",
            "required_projects": {"omnetpp": ["5.4.1"], "inet": ["4.0.0"]},
            "git_url": "https://github.com/ComNets-Bremen/OPSLite.git",
            "setenv_commands": ["export INET_PROJ=$INET_ROOT"],
            # "patch_commands": [
            #     "sed -i -E 's|ieee8021as|IEEE8021AS|' IEEE8021AS/simulations/run",
            #     "sed -i -E 's|-n.*|-n $INET_ROOT/src:.:../src $*|' IEEE8021AS/simulations/run",
            #     "chmod +x IEEE8021AS/simulations/run",
            # ],
            "build_commands": ["cd src && opp_makemake -f --deep -KINET_PROJ=$INET_PROJ -DINET_IMPORT -I$INET_PROJ/src -L$INET_PROJ/src -lINET && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # need SWIM
            "name": "ops", "version": "master",
            "required_projects": {"omnetpp": ["5.6"], "inet": ["4.1.1"], "keetchlib": ["master"]},
            "git_url": "https://github.com/ComNets-Bremen/OPS.git",
            "git_branch": "master",
            # "setenv_commands": ["export KEETCHI_API_PATH=$KEETCHLIB_ROOT", 
            #                     "export INET_PATH=$INET_ROOT"],
            "build_commands": ["opp_makemake -f && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # needs inet version before 2.0.0
            "name": "epon", "version": "0.8",
            "required_projects": {"omnetpp": ["4.1.0"], "inet": ["2.0.0"]},
            "download_url": "https://sourceforge.net/projects/omneteponmodule/files/latest/download",
            "patch_commands": [
                # "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                # "sed -i 's|ChannelAccess.h|world/radio/ChannelAccess.h|g' src/*/*.h",
                # "sed -i 's|InterfaceToken.h|networklayer/common/InterfaceToken.h|g' src/*/*.h src/*/*.h",
                # "chmod +x simulations/run",
                # "sed -i 's|-n .:../src|-n ..:../src:$\{INET_ROOT\}/src|g' simulations/run",
                # "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I.     -I$(INET_ROOT)/src/.     -I$(INET_ROOT)/src/applications     -I$(INET_ROOT)/src/applications/common     -I$(INET_ROOT)/src/applications/dhcp     -I$(INET_ROOT)/src/applications/ethernet     -I$(INET_ROOT)/src/applications/generic     -I$(INET_ROOT)/src/applications/httptools     -I$(INET_ROOT)/src/applications/pingapp     -I$(INET_ROOT)/src/applications/rtpapp     -I$(INET_ROOT)/src/applications/sctpapp     -I$(INET_ROOT)/src/applications/tcpapp     -I$(INET_ROOT)/src/applications/traci     -I$(INET_ROOT)/src/applications/udpapp     -I$(INET_ROOT)/src/applications/voip     -I$(INET_ROOT)/src/base     -I$(INET_ROOT)/src/battery     -I$(INET_ROOT)/src/battery/models     -I$(INET_ROOT)/src/linklayer     -I$(INET_ROOT)/src/linklayer/common     -I$(INET_ROOT)/src/linklayer/configurator     -I$(INET_ROOT)/src/linklayer/contract     -I$(INET_ROOT)/src/linklayer/ethernet     -I$(INET_ROOT)/src/linklayer/ethernet/switch     -I$(INET_ROOT)/src/linklayer/ext     -I$(INET_ROOT)/src/linklayer/idealwireless     -I$(INET_ROOT)/src/linklayer/ieee80211     -I$(INET_ROOT)/src/linklayer/ieee80211/mac     -I$(INET_ROOT)/src/linklayer/ieee80211/mgmt     -I$(INET_ROOT)/src/linklayer/ieee80211/radio     -I$(INET_ROOT)/src/linklayer/ieee80211/radio/errormodel     -I$(INET_ROOT)/src/linklayer/ieee8021d     -I$(INET_ROOT)/src/linklayer/ieee8021d/common     -I$(INET_ROOT)/src/linklayer/ieee8021d/relay     -I$(INET_ROOT)/src/linklayer/ieee8021d/rstp     -I$(INET_ROOT)/src/linklayer/ieee8021d/stp     -I$(INET_ROOT)/src/linklayer/ieee8021d/tester     -I$(INET_ROOT)/src/linklayer/loopback     -I$(INET_ROOT)/src/linklayer/ppp     -I$(INET_ROOT)/src/linklayer/queue     -I$(INET_ROOT)/src/linklayer/radio     -I$(INET_ROOT)/src/linklayer/radio/propagation     -I$(INET_ROOT)/src/mobility     -I$(INET_ROOT)/src/mobility/common     -I$(INET_ROOT)/src/mobility/contract     -I$(INET_ROOT)/src/mobility/group     -I$(INET_ROOT)/src/mobility/single     -I$(INET_ROOT)/src/mobility/static     -I$(INET_ROOT)/src/networklayer     -I$(INET_ROOT)/src/networklayer/arp     -I$(INET_ROOT)/src/networklayer/autorouting     -I$(INET_ROOT)/src/networklayer/autorouting/ipv4     -I$(INET_ROOT)/src/networklayer/autorouting/ipv6     -I$(INET_ROOT)/src/networklayer/bgpv4     -I$(INET_ROOT)/src/networklayer/bgpv4/BGPMessage     -I$(INET_ROOT)/src/networklayer/common     -I$(INET_ROOT)/src/networklayer/contract     -I$(INET_ROOT)/src/networklayer/diffserv     -I$(INET_ROOT)/src/networklayer/icmpv6     -I$(INET_ROOT)/src/networklayer/internetcloud     -I$(INET_ROOT)/src/networklayer/ipv4     -I$(INET_ROOT)/src/networklayer/ipv6     -I$(INET_ROOT)/src/networklayer/ipv6tunneling     -I$(INET_ROOT)/src/networklayer/ldp     -I$(INET_ROOT)/src/networklayer/manetrouting     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/base     -I$(INET_ROOT)/src/networklayer/manetrouting/batman     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand/orig     -I$(INET_ROOT)/src/networklayer/manetrouting/dsdv     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr/dsr-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo/dymoum     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo_fau     -I$(INET_ROOT)/src/networklayer/manetrouting/olsr     -I$(INET_ROOT)/src/networklayer/mpls     -I$(INET_ROOT)/src/networklayer/ospfv2     -I$(INET_ROOT)/src/networklayer/ospfv2/interface     -I$(INET_ROOT)/src/networklayer/ospfv2/messagehandler     -I$(INET_ROOT)/src/networklayer/ospfv2/neighbor     -I$(INET_ROOT)/src/networklayer/ospfv2/router     -I$(INET_ROOT)/src/networklayer/routing     -I$(INET_ROOT)/src/networklayer/routing/aodv     -I$(INET_ROOT)/src/networklayer/routing/dymo     -I$(INET_ROOT)/src/networklayer/routing/gpsr     -I$(INET_ROOT)/src/networklayer/routing/rip     -I$(INET_ROOT)/src/networklayer/rsvp_te     -I$(INET_ROOT)/src/networklayer/ted     -I$(INET_ROOT)/src/networklayer/xmipv6     -I$(INET_ROOT)/src/nodes     -I$(INET_ROOT)/src/nodes/aodv     -I$(INET_ROOT)/src/nodes/bgp     -I$(INET_ROOT)/src/nodes/dymo     -I$(INET_ROOT)/src/nodes/ethernet     -I$(INET_ROOT)/src/nodes/gpsr     -I$(INET_ROOT)/src/nodes/httptools     -I$(INET_ROOT)/src/nodes/inet     -I$(INET_ROOT)/src/nodes/internetcloud     -I$(INET_ROOT)/src/nodes/ipv6     -I$(INET_ROOT)/src/nodes/mpls     -I$(INET_ROOT)/src/nodes/ospfv2     -I$(INET_ROOT)/src/nodes/rip     -I$(INET_ROOT)/src/nodes/rtp     -I$(INET_ROOT)/src/nodes/wireless     -I$(INET_ROOT)/src/nodes/xmipv6     -I$(INET_ROOT)/src/status     -I$(INET_ROOT)/src/transport     -I$(INET_ROOT)/src/transport/contract     -I$(INET_ROOT)/src/transport/rtp     -I$(INET_ROOT)/src/transport/rtp/profiles     -I$(INET_ROOT)/src/transport/rtp/profiles/avprofile     -I$(INET_ROOT)/src/transport/sctp     -I$(INET_ROOT)/src/transport/tcp     -I$(INET_ROOT)/src/transport/tcp/flavours     -I$(INET_ROOT)/src/transport/tcp/queues     -I$(INET_ROOT)/src/transport/tcp_common     -I$(INET_ROOT)/src/transport/udp     -I$(INET_ROOT)/src/util     -I$(INET_ROOT)/src/util/headerserializers     -I$(INET_ROOT)/src/util/headerserializers/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv4     -I$(INET_ROOT)/src/util/headerserializers/ipv4/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv6     -I$(INET_ROOT)/src/util/headerserializers/ipv6/headers     -I$(INET_ROOT)/src/util/headerserializers/sctp     -I$(INET_ROOT)/src/util/headerserializers/sctp/headers     -I$(INET_ROOT)/src/util/headerserializers/tcp     -I$(INET_ROOT)/src/util/headerserializers/tcp/headers     -I$(INET_ROOT)/src/util/headerserializers/udp     -I$(INET_ROOT)/src/util/headerserializers/udp/headers     -I$(INET_ROOT)/src/util/messageprinters     -I$(INET_ROOT)/src/world     -I$(INET_ROOT)/src/world/annotations     -I$(INET_ROOT)/src/world/httptools     -I$(INET_ROOT)/src/world/obstacles     -I$(INET_ROOT)/src/world/radio     -I$(INET_ROOT)/src/world/scenario     -I$(INET_ROOT)/src/world/traci -o ieee802154inet_standalone -L$(INET_ROOT)/src -linet|' Makefile",
            ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # this needs omnetpp 3.2
            "name": "fieldbus", "version": "20050901",
            "required_projects": {"omnetpp": ["3.3.x"]},
            "download_url": "https://sourceforge.net/projects/fieldbus.berlios/files/latest/download",
            "patch_commands": [
                # "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                # "sed -i 's|ChannelAccess.h|world/radio/ChannelAccess.h|g' src/*/*.h",
                # "sed -i 's|InterfaceToken.h|networklayer/common/InterfaceToken.h|g' src/*/*.h src/*/*.h",
                # "chmod +x simulations/run",
                # "sed -i 's|-n .:../src|-n ..:../src:$\{INET_ROOT\}/src|g' simulations/run",
                # "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I.     -I$(INET_ROOT)/src/.     -I$(INET_ROOT)/src/applications     -I$(INET_ROOT)/src/applications/common     -I$(INET_ROOT)/src/applications/dhcp     -I$(INET_ROOT)/src/applications/ethernet     -I$(INET_ROOT)/src/applications/generic     -I$(INET_ROOT)/src/applications/httptools     -I$(INET_ROOT)/src/applications/pingapp     -I$(INET_ROOT)/src/applications/rtpapp     -I$(INET_ROOT)/src/applications/sctpapp     -I$(INET_ROOT)/src/applications/tcpapp     -I$(INET_ROOT)/src/applications/traci     -I$(INET_ROOT)/src/applications/udpapp     -I$(INET_ROOT)/src/applications/voip     -I$(INET_ROOT)/src/base     -I$(INET_ROOT)/src/battery     -I$(INET_ROOT)/src/battery/models     -I$(INET_ROOT)/src/linklayer     -I$(INET_ROOT)/src/linklayer/common     -I$(INET_ROOT)/src/linklayer/configurator     -I$(INET_ROOT)/src/linklayer/contract     -I$(INET_ROOT)/src/linklayer/ethernet     -I$(INET_ROOT)/src/linklayer/ethernet/switch     -I$(INET_ROOT)/src/linklayer/ext     -I$(INET_ROOT)/src/linklayer/idealwireless     -I$(INET_ROOT)/src/linklayer/ieee80211     -I$(INET_ROOT)/src/linklayer/ieee80211/mac     -I$(INET_ROOT)/src/linklayer/ieee80211/mgmt     -I$(INET_ROOT)/src/linklayer/ieee80211/radio     -I$(INET_ROOT)/src/linklayer/ieee80211/radio/errormodel     -I$(INET_ROOT)/src/linklayer/ieee8021d     -I$(INET_ROOT)/src/linklayer/ieee8021d/common     -I$(INET_ROOT)/src/linklayer/ieee8021d/relay     -I$(INET_ROOT)/src/linklayer/ieee8021d/rstp     -I$(INET_ROOT)/src/linklayer/ieee8021d/stp     -I$(INET_ROOT)/src/linklayer/ieee8021d/tester     -I$(INET_ROOT)/src/linklayer/loopback     -I$(INET_ROOT)/src/linklayer/ppp     -I$(INET_ROOT)/src/linklayer/queue     -I$(INET_ROOT)/src/linklayer/radio     -I$(INET_ROOT)/src/linklayer/radio/propagation     -I$(INET_ROOT)/src/mobility     -I$(INET_ROOT)/src/mobility/common     -I$(INET_ROOT)/src/mobility/contract     -I$(INET_ROOT)/src/mobility/group     -I$(INET_ROOT)/src/mobility/single     -I$(INET_ROOT)/src/mobility/static     -I$(INET_ROOT)/src/networklayer     -I$(INET_ROOT)/src/networklayer/arp     -I$(INET_ROOT)/src/networklayer/autorouting     -I$(INET_ROOT)/src/networklayer/autorouting/ipv4     -I$(INET_ROOT)/src/networklayer/autorouting/ipv6     -I$(INET_ROOT)/src/networklayer/bgpv4     -I$(INET_ROOT)/src/networklayer/bgpv4/BGPMessage     -I$(INET_ROOT)/src/networklayer/common     -I$(INET_ROOT)/src/networklayer/contract     -I$(INET_ROOT)/src/networklayer/diffserv     -I$(INET_ROOT)/src/networklayer/icmpv6     -I$(INET_ROOT)/src/networklayer/internetcloud     -I$(INET_ROOT)/src/networklayer/ipv4     -I$(INET_ROOT)/src/networklayer/ipv6     -I$(INET_ROOT)/src/networklayer/ipv6tunneling     -I$(INET_ROOT)/src/networklayer/ldp     -I$(INET_ROOT)/src/networklayer/manetrouting     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/base     -I$(INET_ROOT)/src/networklayer/manetrouting/batman     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand/orig     -I$(INET_ROOT)/src/networklayer/manetrouting/dsdv     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr/dsr-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo/dymoum     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo_fau     -I$(INET_ROOT)/src/networklayer/manetrouting/olsr     -I$(INET_ROOT)/src/networklayer/mpls     -I$(INET_ROOT)/src/networklayer/ospfv2     -I$(INET_ROOT)/src/networklayer/ospfv2/interface     -I$(INET_ROOT)/src/networklayer/ospfv2/messagehandler     -I$(INET_ROOT)/src/networklayer/ospfv2/neighbor     -I$(INET_ROOT)/src/networklayer/ospfv2/router     -I$(INET_ROOT)/src/networklayer/routing     -I$(INET_ROOT)/src/networklayer/routing/aodv     -I$(INET_ROOT)/src/networklayer/routing/dymo     -I$(INET_ROOT)/src/networklayer/routing/gpsr     -I$(INET_ROOT)/src/networklayer/routing/rip     -I$(INET_ROOT)/src/networklayer/rsvp_te     -I$(INET_ROOT)/src/networklayer/ted     -I$(INET_ROOT)/src/networklayer/xmipv6     -I$(INET_ROOT)/src/nodes     -I$(INET_ROOT)/src/nodes/aodv     -I$(INET_ROOT)/src/nodes/bgp     -I$(INET_ROOT)/src/nodes/dymo     -I$(INET_ROOT)/src/nodes/ethernet     -I$(INET_ROOT)/src/nodes/gpsr     -I$(INET_ROOT)/src/nodes/httptools     -I$(INET_ROOT)/src/nodes/inet     -I$(INET_ROOT)/src/nodes/internetcloud     -I$(INET_ROOT)/src/nodes/ipv6     -I$(INET_ROOT)/src/nodes/mpls     -I$(INET_ROOT)/src/nodes/ospfv2     -I$(INET_ROOT)/src/nodes/rip     -I$(INET_ROOT)/src/nodes/rtp     -I$(INET_ROOT)/src/nodes/wireless     -I$(INET_ROOT)/src/nodes/xmipv6     -I$(INET_ROOT)/src/status     -I$(INET_ROOT)/src/transport     -I$(INET_ROOT)/src/transport/contract     -I$(INET_ROOT)/src/transport/rtp     -I$(INET_ROOT)/src/transport/rtp/profiles     -I$(INET_ROOT)/src/transport/rtp/profiles/avprofile     -I$(INET_ROOT)/src/transport/sctp     -I$(INET_ROOT)/src/transport/tcp     -I$(INET_ROOT)/src/transport/tcp/flavours     -I$(INET_ROOT)/src/transport/tcp/queues     -I$(INET_ROOT)/src/transport/tcp_common     -I$(INET_ROOT)/src/transport/udp     -I$(INET_ROOT)/src/util     -I$(INET_ROOT)/src/util/headerserializers     -I$(INET_ROOT)/src/util/headerserializers/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv4     -I$(INET_ROOT)/src/util/headerserializers/ipv4/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv6     -I$(INET_ROOT)/src/util/headerserializers/ipv6/headers     -I$(INET_ROOT)/src/util/headerserializers/sctp     -I$(INET_ROOT)/src/util/headerserializers/sctp/headers     -I$(INET_ROOT)/src/util/headerserializers/tcp     -I$(INET_ROOT)/src/util/headerserializers/tcp/headers     -I$(INET_ROOT)/src/util/headerserializers/udp     -I$(INET_ROOT)/src/util/headerserializers/udp/headers     -I$(INET_ROOT)/src/util/messageprinters     -I$(INET_ROOT)/src/world     -I$(INET_ROOT)/src/world/annotations     -I$(INET_ROOT)/src/world/httptools     -I$(INET_ROOT)/src/world/obstacles     -I$(INET_ROOT)/src/world/radio     -I$(INET_ROOT)/src/world/scenario     -I$(INET_ROOT)/src/world/traci -o ieee802154inet_standalone -L$(INET_ROOT)/src -linet|' Makefile",
            ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # intended to be used as part of inet - this should be its own project
            "name": "can", "version": "0.1.0",
            "required_projects": {"omnetpp": ["4.6.0"], "inet": ["2.5.0"]},
            "download_url": "https://github.com/YutakaMatsubara/can-for-omnet/archive/refs/tags/v0.1.0.tar.gz",
            "patch_commands": [
                # "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                # "sed -i 's|ChannelAccess.h|world/radio/ChannelAccess.h|g' src/*/*.h",
                # "sed -i 's|InterfaceToken.h|networklayer/common/InterfaceToken.h|g' src/*/*.h src/*/*.h",
                # "chmod +x simulations/run",
                # "sed -i 's|-n .:../src|-n ..:../src:$\{INET_ROOT\}/src|g' simulations/run",
                # "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I.     -I$(INET_ROOT)/src/.     -I$(INET_ROOT)/src/applications     -I$(INET_ROOT)/src/applications/common     -I$(INET_ROOT)/src/applications/dhcp     -I$(INET_ROOT)/src/applications/ethernet     -I$(INET_ROOT)/src/applications/generic     -I$(INET_ROOT)/src/applications/httptools     -I$(INET_ROOT)/src/applications/pingapp     -I$(INET_ROOT)/src/applications/rtpapp     -I$(INET_ROOT)/src/applications/sctpapp     -I$(INET_ROOT)/src/applications/tcpapp     -I$(INET_ROOT)/src/applications/traci     -I$(INET_ROOT)/src/applications/udpapp     -I$(INET_ROOT)/src/applications/voip     -I$(INET_ROOT)/src/base     -I$(INET_ROOT)/src/battery     -I$(INET_ROOT)/src/battery/models     -I$(INET_ROOT)/src/linklayer     -I$(INET_ROOT)/src/linklayer/common     -I$(INET_ROOT)/src/linklayer/configurator     -I$(INET_ROOT)/src/linklayer/contract     -I$(INET_ROOT)/src/linklayer/ethernet     -I$(INET_ROOT)/src/linklayer/ethernet/switch     -I$(INET_ROOT)/src/linklayer/ext     -I$(INET_ROOT)/src/linklayer/idealwireless     -I$(INET_ROOT)/src/linklayer/ieee80211     -I$(INET_ROOT)/src/linklayer/ieee80211/mac     -I$(INET_ROOT)/src/linklayer/ieee80211/mgmt     -I$(INET_ROOT)/src/linklayer/ieee80211/radio     -I$(INET_ROOT)/src/linklayer/ieee80211/radio/errormodel     -I$(INET_ROOT)/src/linklayer/ieee8021d     -I$(INET_ROOT)/src/linklayer/ieee8021d/common     -I$(INET_ROOT)/src/linklayer/ieee8021d/relay     -I$(INET_ROOT)/src/linklayer/ieee8021d/rstp     -I$(INET_ROOT)/src/linklayer/ieee8021d/stp     -I$(INET_ROOT)/src/linklayer/ieee8021d/tester     -I$(INET_ROOT)/src/linklayer/loopback     -I$(INET_ROOT)/src/linklayer/ppp     -I$(INET_ROOT)/src/linklayer/queue     -I$(INET_ROOT)/src/linklayer/radio     -I$(INET_ROOT)/src/linklayer/radio/propagation     -I$(INET_ROOT)/src/mobility     -I$(INET_ROOT)/src/mobility/common     -I$(INET_ROOT)/src/mobility/contract     -I$(INET_ROOT)/src/mobility/group     -I$(INET_ROOT)/src/mobility/single     -I$(INET_ROOT)/src/mobility/static     -I$(INET_ROOT)/src/networklayer     -I$(INET_ROOT)/src/networklayer/arp     -I$(INET_ROOT)/src/networklayer/autorouting     -I$(INET_ROOT)/src/networklayer/autorouting/ipv4     -I$(INET_ROOT)/src/networklayer/autorouting/ipv6     -I$(INET_ROOT)/src/networklayer/bgpv4     -I$(INET_ROOT)/src/networklayer/bgpv4/BGPMessage     -I$(INET_ROOT)/src/networklayer/common     -I$(INET_ROOT)/src/networklayer/contract     -I$(INET_ROOT)/src/networklayer/diffserv     -I$(INET_ROOT)/src/networklayer/icmpv6     -I$(INET_ROOT)/src/networklayer/internetcloud     -I$(INET_ROOT)/src/networklayer/ipv4     -I$(INET_ROOT)/src/networklayer/ipv6     -I$(INET_ROOT)/src/networklayer/ipv6tunneling     -I$(INET_ROOT)/src/networklayer/ldp     -I$(INET_ROOT)/src/networklayer/manetrouting     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/base     -I$(INET_ROOT)/src/networklayer/manetrouting/batman     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand/orig     -I$(INET_ROOT)/src/networklayer/manetrouting/dsdv     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr/dsr-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo/dymoum     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo_fau     -I$(INET_ROOT)/src/networklayer/manetrouting/olsr     -I$(INET_ROOT)/src/networklayer/mpls     -I$(INET_ROOT)/src/networklayer/ospfv2     -I$(INET_ROOT)/src/networklayer/ospfv2/interface     -I$(INET_ROOT)/src/networklayer/ospfv2/messagehandler     -I$(INET_ROOT)/src/networklayer/ospfv2/neighbor     -I$(INET_ROOT)/src/networklayer/ospfv2/router     -I$(INET_ROOT)/src/networklayer/routing     -I$(INET_ROOT)/src/networklayer/routing/aodv     -I$(INET_ROOT)/src/networklayer/routing/dymo     -I$(INET_ROOT)/src/networklayer/routing/gpsr     -I$(INET_ROOT)/src/networklayer/routing/rip     -I$(INET_ROOT)/src/networklayer/rsvp_te     -I$(INET_ROOT)/src/networklayer/ted     -I$(INET_ROOT)/src/networklayer/xmipv6     -I$(INET_ROOT)/src/nodes     -I$(INET_ROOT)/src/nodes/aodv     -I$(INET_ROOT)/src/nodes/bgp     -I$(INET_ROOT)/src/nodes/dymo     -I$(INET_ROOT)/src/nodes/ethernet     -I$(INET_ROOT)/src/nodes/gpsr     -I$(INET_ROOT)/src/nodes/httptools     -I$(INET_ROOT)/src/nodes/inet     -I$(INET_ROOT)/src/nodes/internetcloud     -I$(INET_ROOT)/src/nodes/ipv6     -I$(INET_ROOT)/src/nodes/mpls     -I$(INET_ROOT)/src/nodes/ospfv2     -I$(INET_ROOT)/src/nodes/rip     -I$(INET_ROOT)/src/nodes/rtp     -I$(INET_ROOT)/src/nodes/wireless     -I$(INET_ROOT)/src/nodes/xmipv6     -I$(INET_ROOT)/src/status     -I$(INET_ROOT)/src/transport     -I$(INET_ROOT)/src/transport/contract     -I$(INET_ROOT)/src/transport/rtp     -I$(INET_ROOT)/src/transport/rtp/profiles     -I$(INET_ROOT)/src/transport/rtp/profiles/avprofile     -I$(INET_ROOT)/src/transport/sctp     -I$(INET_ROOT)/src/transport/tcp     -I$(INET_ROOT)/src/transport/tcp/flavours     -I$(INET_ROOT)/src/transport/tcp/queues     -I$(INET_ROOT)/src/transport/tcp_common     -I$(INET_ROOT)/src/transport/udp     -I$(INET_ROOT)/src/util     -I$(INET_ROOT)/src/util/headerserializers     -I$(INET_ROOT)/src/util/headerserializers/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv4     -I$(INET_ROOT)/src/util/headerserializers/ipv4/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv6     -I$(INET_ROOT)/src/util/headerserializers/ipv6/headers     -I$(INET_ROOT)/src/util/headerserializers/sctp     -I$(INET_ROOT)/src/util/headerserializers/sctp/headers     -I$(INET_ROOT)/src/util/headerserializers/tcp     -I$(INET_ROOT)/src/util/headerserializers/tcp/headers     -I$(INET_ROOT)/src/util/headerserializers/udp     -I$(INET_ROOT)/src/util/headerserializers/udp/headers     -I$(INET_ROOT)/src/util/messageprinters     -I$(INET_ROOT)/src/world     -I$(INET_ROOT)/src/world/annotations     -I$(INET_ROOT)/src/world/httptools     -I$(INET_ROOT)/src/world/obstacles     -I$(INET_ROOT)/src/world/radio     -I$(INET_ROOT)/src/world/scenario     -I$(INET_ROOT)/src/world/traci -o ieee802154inet_standalone -L$(INET_ROOT)/src -linet|' Makefile",
            ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # WIP - compiles; need ui with qt; need to try example simulation
            "name": "limosim", "version": "master",
            # "nix_packages": ["qt5.qtbase", "qt5.qtsvg", "qt5.qtwayland"],
            # "required_projects": {"omnetpp": ["5.1.x"], "inet": ["3.3.0"]},
            "required_projects": {"omnetpp": ["5.4.x"], "inet": ["4.0.0"]},
            "git_url": "https://github.com/BenSliwa/LIMoSim.git",
            "patch_commands": [
                # "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                # "sed -i 's|ChannelAccess.h|world/radio/ChannelAccess.h|g' src/*/*.h",
                # "sed -i 's|InterfaceToken.h|networklayer/common/InterfaceToken.h|g' src/*/*.h src/*/*.h",
                # "chmod +x simulations/run",
                # "sed -i 's|-n .:../src|-n ..:../src:$\{INET_ROOT\}/src|g' simulations/run",
                # "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I.     -I$(INET_ROOT)/src/.     -I$(INET_ROOT)/src/applications     -I$(INET_ROOT)/src/applications/common     -I$(INET_ROOT)/src/applications/dhcp     -I$(INET_ROOT)/src/applications/ethernet     -I$(INET_ROOT)/src/applications/generic     -I$(INET_ROOT)/src/applications/httptools     -I$(INET_ROOT)/src/applications/pingapp     -I$(INET_ROOT)/src/applications/rtpapp     -I$(INET_ROOT)/src/applications/sctpapp     -I$(INET_ROOT)/src/applications/tcpapp     -I$(INET_ROOT)/src/applications/traci     -I$(INET_ROOT)/src/applications/udpapp     -I$(INET_ROOT)/src/applications/voip     -I$(INET_ROOT)/src/base     -I$(INET_ROOT)/src/battery     -I$(INET_ROOT)/src/battery/models     -I$(INET_ROOT)/src/linklayer     -I$(INET_ROOT)/src/linklayer/common     -I$(INET_ROOT)/src/linklayer/configurator     -I$(INET_ROOT)/src/linklayer/contract     -I$(INET_ROOT)/src/linklayer/ethernet     -I$(INET_ROOT)/src/linklayer/ethernet/switch     -I$(INET_ROOT)/src/linklayer/ext     -I$(INET_ROOT)/src/linklayer/idealwireless     -I$(INET_ROOT)/src/linklayer/ieee80211     -I$(INET_ROOT)/src/linklayer/ieee80211/mac     -I$(INET_ROOT)/src/linklayer/ieee80211/mgmt     -I$(INET_ROOT)/src/linklayer/ieee80211/radio     -I$(INET_ROOT)/src/linklayer/ieee80211/radio/errormodel     -I$(INET_ROOT)/src/linklayer/ieee8021d     -I$(INET_ROOT)/src/linklayer/ieee8021d/common     -I$(INET_ROOT)/src/linklayer/ieee8021d/relay     -I$(INET_ROOT)/src/linklayer/ieee8021d/rstp     -I$(INET_ROOT)/src/linklayer/ieee8021d/stp     -I$(INET_ROOT)/src/linklayer/ieee8021d/tester     -I$(INET_ROOT)/src/linklayer/loopback     -I$(INET_ROOT)/src/linklayer/ppp     -I$(INET_ROOT)/src/linklayer/queue     -I$(INET_ROOT)/src/linklayer/radio     -I$(INET_ROOT)/src/linklayer/radio/propagation     -I$(INET_ROOT)/src/mobility     -I$(INET_ROOT)/src/mobility/common     -I$(INET_ROOT)/src/mobility/contract     -I$(INET_ROOT)/src/mobility/group     -I$(INET_ROOT)/src/mobility/single     -I$(INET_ROOT)/src/mobility/static     -I$(INET_ROOT)/src/networklayer     -I$(INET_ROOT)/src/networklayer/arp     -I$(INET_ROOT)/src/networklayer/autorouting     -I$(INET_ROOT)/src/networklayer/autorouting/ipv4     -I$(INET_ROOT)/src/networklayer/autorouting/ipv6     -I$(INET_ROOT)/src/networklayer/bgpv4     -I$(INET_ROOT)/src/networklayer/bgpv4/BGPMessage     -I$(INET_ROOT)/src/networklayer/common     -I$(INET_ROOT)/src/networklayer/contract     -I$(INET_ROOT)/src/networklayer/diffserv     -I$(INET_ROOT)/src/networklayer/icmpv6     -I$(INET_ROOT)/src/networklayer/internetcloud     -I$(INET_ROOT)/src/networklayer/ipv4     -I$(INET_ROOT)/src/networklayer/ipv6     -I$(INET_ROOT)/src/networklayer/ipv6tunneling     -I$(INET_ROOT)/src/networklayer/ldp     -I$(INET_ROOT)/src/networklayer/manetrouting     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/aodv-uu/aodv-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/base     -I$(INET_ROOT)/src/networklayer/manetrouting/batman     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand     -I$(INET_ROOT)/src/networklayer/manetrouting/batman/batmand/orig     -I$(INET_ROOT)/src/networklayer/manetrouting/dsdv     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr     -I$(INET_ROOT)/src/networklayer/manetrouting/dsr/dsr-uu     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo/dymoum     -I$(INET_ROOT)/src/networklayer/manetrouting/dymo_fau     -I$(INET_ROOT)/src/networklayer/manetrouting/olsr     -I$(INET_ROOT)/src/networklayer/mpls     -I$(INET_ROOT)/src/networklayer/ospfv2     -I$(INET_ROOT)/src/networklayer/ospfv2/interface     -I$(INET_ROOT)/src/networklayer/ospfv2/messagehandler     -I$(INET_ROOT)/src/networklayer/ospfv2/neighbor     -I$(INET_ROOT)/src/networklayer/ospfv2/router     -I$(INET_ROOT)/src/networklayer/routing     -I$(INET_ROOT)/src/networklayer/routing/aodv     -I$(INET_ROOT)/src/networklayer/routing/dymo     -I$(INET_ROOT)/src/networklayer/routing/gpsr     -I$(INET_ROOT)/src/networklayer/routing/rip     -I$(INET_ROOT)/src/networklayer/rsvp_te     -I$(INET_ROOT)/src/networklayer/ted     -I$(INET_ROOT)/src/networklayer/xmipv6     -I$(INET_ROOT)/src/nodes     -I$(INET_ROOT)/src/nodes/aodv     -I$(INET_ROOT)/src/nodes/bgp     -I$(INET_ROOT)/src/nodes/dymo     -I$(INET_ROOT)/src/nodes/ethernet     -I$(INET_ROOT)/src/nodes/gpsr     -I$(INET_ROOT)/src/nodes/httptools     -I$(INET_ROOT)/src/nodes/inet     -I$(INET_ROOT)/src/nodes/internetcloud     -I$(INET_ROOT)/src/nodes/ipv6     -I$(INET_ROOT)/src/nodes/mpls     -I$(INET_ROOT)/src/nodes/ospfv2     -I$(INET_ROOT)/src/nodes/rip     -I$(INET_ROOT)/src/nodes/rtp     -I$(INET_ROOT)/src/nodes/wireless     -I$(INET_ROOT)/src/nodes/xmipv6     -I$(INET_ROOT)/src/status     -I$(INET_ROOT)/src/transport     -I$(INET_ROOT)/src/transport/contract     -I$(INET_ROOT)/src/transport/rtp     -I$(INET_ROOT)/src/transport/rtp/profiles     -I$(INET_ROOT)/src/transport/rtp/profiles/avprofile     -I$(INET_ROOT)/src/transport/sctp     -I$(INET_ROOT)/src/transport/tcp     -I$(INET_ROOT)/src/transport/tcp/flavours     -I$(INET_ROOT)/src/transport/tcp/queues     -I$(INET_ROOT)/src/transport/tcp_common     -I$(INET_ROOT)/src/transport/udp     -I$(INET_ROOT)/src/util     -I$(INET_ROOT)/src/util/headerserializers     -I$(INET_ROOT)/src/util/headerserializers/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv4     -I$(INET_ROOT)/src/util/headerserializers/ipv4/headers     -I$(INET_ROOT)/src/util/headerserializers/ipv6     -I$(INET_ROOT)/src/util/headerserializers/ipv6/headers     -I$(INET_ROOT)/src/util/headerserializers/sctp     -I$(INET_ROOT)/src/util/headerserializers/sctp/headers     -I$(INET_ROOT)/src/util/headerserializers/tcp     -I$(INET_ROOT)/src/util/headerserializers/tcp/headers     -I$(INET_ROOT)/src/util/headerserializers/udp     -I$(INET_ROOT)/src/util/headerserializers/udp/headers     -I$(INET_ROOT)/src/util/messageprinters     -I$(INET_ROOT)/src/world     -I$(INET_ROOT)/src/world/annotations     -I$(INET_ROOT)/src/world/httptools     -I$(INET_ROOT)/src/world/obstacles     -I$(INET_ROOT)/src/world/radio     -I$(INET_ROOT)/src/world/scenario     -I$(INET_ROOT)/src/world/traci -o ieee802154inet_standalone -L$(INET_ROOT)/src -linet|' Makefile",
            ],
            "build_commands": ["opp_makemake -f --deep -o limosim -O out -KINET_PROJ=$INET_ROOT -DINET_IMPORT -X./ui -I. -I$INET_ROOT/src -L$INET_ROOT/src -lINET && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },

        {
            # WIP - no makefile? there is one in src/utils but seems broken
            "name": "dns", "version": "master",
            "required_projects": {"omnetpp": ["4.6.0"], "inet": ["3.1.0"]},
            "git_url": "https://github.com/saenridanra/inet-dns-extension.git",
            "patch_commands": [
                "sed -i 's|INETDefs.h|inet/common/INETDefs.h|g' src/*/*/*.h",
            ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && cd dctg_example && make makefiles && make"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - builds; segfault when trying to run simulation
            "name": "obs", "version": "master",
            "required_projects": {"omnetpp": ["4.2.0"], "inet": ["2.2.0"]},
            "git_url": "https://github.com/mikelizal/OBSmodules.git",
            "metadata": {
                "catalog_url": "https://omnetpp.org/download-items/OBS.html",
            },
            "patch_commands": [
                # "sed -i 's|INETDefs.h|inet/common/INETDefs.h|g' src/*/*/*.h",
            ],
            "build_commands": ["cd src && opp_makemake -f --deep -o obs -O out -KINET_PROJ=$INET_ROOT -DINET_IMPORT -L$INET_ROOT/src -I. -I$INET_ROOT/src -I$INET_ROOT/src/applications -I$INET_ROOT/src/applications/dhcp -I$INET_ROOT/src/applications/ethernet -I$INET_ROOT/src/applications/generic -I$INET_ROOT/src/applications/httptools -I$INET_ROOT/src/applications/pingapp -I$INET_ROOT/src/applications/rtpapp -I$INET_ROOT/src/applications/sctpapp -I$INET_ROOT/src/applications/tcpapp -I$INET_ROOT/src/applications/traci -I$INET_ROOT/src/applications/udpapp -I$INET_ROOT/src/applications/voip -I$INET_ROOT/src/base -I$INET_ROOT/src/battery -I$INET_ROOT/src/battery/models -I$INET_ROOT/src/linklayer -I$INET_ROOT/src/linklayer/common -I$INET_ROOT/src/linklayer/contract -I$INET_ROOT/src/linklayer/ethernet -I$INET_ROOT/src/linklayer/ethernet/switch -I$INET_ROOT/src/linklayer/ext -I$INET_ROOT/src/linklayer/idealwireless -I$INET_ROOT/src/linklayer/ieee80211 -I$INET_ROOT/src/linklayer/ieee80211/mac -I$INET_ROOT/src/linklayer/ieee80211/mgmt -I$INET_ROOT/src/linklayer/ieee80211/radio -I$INET_ROOT/src/linklayer/ieee80211/radio/errormodel -I$INET_ROOT/src/linklayer/loopback -I$INET_ROOT/src/linklayer/ppp -I$INET_ROOT/src/linklayer/queue -I$INET_ROOT/src/linklayer/radio -I$INET_ROOT/src/linklayer/radio/propagation -I$INET_ROOT/src/mobility -I$INET_ROOT/src/mobility/models -I$INET_ROOT/src/networklayer -I$INET_ROOT/src/networklayer/arp -I$INET_ROOT/src/networklayer/autorouting -I$INET_ROOT/src/networklayer/autorouting/ipv4 -I$INET_ROOT/src/networklayer/autorouting/ipv6 -I$INET_ROOT/src/networklayer/bgpv4 -I$INET_ROOT/src/networklayer/bgpv4/BGPMessage -I$INET_ROOT/src/networklayer/common -I$INET_ROOT/src/networklayer/contract -I$INET_ROOT/src/networklayer/diffserv -I$INET_ROOT/src/networklayer/icmpv6 -I$INET_ROOT/src/networklayer/internetcloud -I$INET_ROOT/src/networklayer/ipv4 -I$INET_ROOT/src/networklayer/ipv6 -I$INET_ROOT/src/networklayer/ipv6tunneling -I$INET_ROOT/src/networklayer/ldp -I$INET_ROOT/src/networklayer/manetrouting -I$INET_ROOT/src/networklayer/manetrouting/aodv -I$INET_ROOT/src/networklayer/manetrouting/aodv/aodv-uu -I$INET_ROOT/src/networklayer/manetrouting/base -I$INET_ROOT/src/networklayer/manetrouting/batman -I$INET_ROOT/src/networklayer/manetrouting/batman/batmand -I$INET_ROOT/src/networklayer/manetrouting/batman/batmand/orig -I$INET_ROOT/src/networklayer/manetrouting/dsdv -I$INET_ROOT/src/networklayer/manetrouting/dsr -I$INET_ROOT/src/networklayer/manetrouting/dsr/dsr-uu -I$INET_ROOT/src/networklayer/manetrouting/dymo -I$INET_ROOT/src/networklayer/manetrouting/dymo/dymoum -I$INET_ROOT/src/networklayer/manetrouting/dymo_fau -I$INET_ROOT/src/networklayer/manetrouting/olsr -I$INET_ROOT/src/networklayer/mpls -I$INET_ROOT/src/networklayer/ospfv2 -I$INET_ROOT/src/networklayer/ospfv2/interface -I$INET_ROOT/src/networklayer/ospfv2/messagehandler -I$INET_ROOT/src/networklayer/ospfv2/neighbor -I$INET_ROOT/src/networklayer/ospfv2/router -I$INET_ROOT/src/networklayer/rsvp_te -I$INET_ROOT/src/networklayer/ted -I$INET_ROOT/src/networklayer/xmipv6 -I$INET_ROOT/src/nodes -I$INET_ROOT/src/nodes/bgp -I$INET_ROOT/src/nodes/ethernet -I$INET_ROOT/src/nodes/httptools -I$INET_ROOT/src/nodes/inet -I$INET_ROOT/src/nodes/internetcloud -I$INET_ROOT/src/nodes/ipv6 -I$INET_ROOT/src/nodes/mpls -I$INET_ROOT/src/nodes/ospfv2 -I$INET_ROOT/src/nodes/rtp -I$INET_ROOT/src/nodes/wireless -I$INET_ROOT/src/nodes/xmipv6 -I$INET_ROOT/src/status -I$INET_ROOT/src/transport -I$INET_ROOT/src/transport/contract -I$INET_ROOT/src/transport/rtp -I$INET_ROOT/src/transport/rtp/profiles -I$INET_ROOT/src/transport/rtp/profiles/avprofile -I$INET_ROOT/src/transport/sctp -I$INET_ROOT/src/transport/tcp -I$INET_ROOT/src/transport/tcp/flavours -I$INET_ROOT/src/transport/tcp/queues -I$INET_ROOT/src/transport/tcp_common -I$INET_ROOT/src/transport/udp -I$INET_ROOT/src/util -I$INET_ROOT/src/util/headerserializers -I$INET_ROOT/src/util/headerserializers/headers -I$INET_ROOT/src/util/headerserializers/ipv4 -I$INET_ROOT/src/util/headerserializers/ipv4/headers -I$INET_ROOT/src/util/headerserializers/sctp -I$INET_ROOT/src/util/headerserializers/sctp/headers -I$INET_ROOT/src/util/headerserializers/tcp -I$INET_ROOT/src/util/headerserializers/tcp/headers -I$INET_ROOT/src/util/headerserializers/udp -I$INET_ROOT/src/util/headerserializers/udp/headers -I$INET_ROOT/src/world -I$INET_ROOT/src/world/annotations -I$INET_ROOT/src/world/httptools -I$INET_ROOT/src/world/obstacles -I$INET_ROOT/src/world/radio -I$INET_ROOT/src/world/scenario -I$INET_ROOT/src/world/traci -linet && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "setenv_commands": ["echo 'Hint: in the folder of an example simulation, use the ../../src/obs -n ../..:$INET_ROOT/src omnetpp.ini command to run the simulation'"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - cant extract, wrong password
            "name": "ble", "version": "master",
            "required_projects": {"omnetpp": ["6.0.0"]},
            "download_url": "https://cc.oulu.fi/~kmikhayl/site-assets/pdfs/BLEsim.zip",
            "patch_commands": [
                # "sed -i 's|||g' ",
            ],
            # "build_commands": ["make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - doesnt build
            # include/ARAMacros.h:8:10: fatal error: 'memory' file not found
            # #include <memory>
            #          ^~~~~~~~
            "name": "libara", "version": "1.2",
            "required_projects": {"omnetpp": ["5.7.x"], "inetmanet": ["3.x"]},
            "download_url": "https://github.com/des-testbed/libara/archive/refs/tags/v1.2.tar.gz",
            "setenv_commands": ["export INETMANET_FOLDER=$INETMANET_ROOT"],
            "patch_commands": [
                "sed -i 's|INETMANET_FOLDER = inetmanet|INETMANET_FOLDER = $(INETMANET_ROOT)|g' Makefile",
            ],
            # "build_commands": ["cd src && opp_makemake -f --deep -O out -o cell && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
            # run example simulation from src folder with:
            # ./cell -n .. ../networks/demo.ini
        },

        {
            # WIP
            # cant find includes
            "name": "epon", "version": "0.8b",
            "required_projects": {"omnetpp": ["5.7.x"], "inetmanet": ["3.x"]},
            "download_url": "https://sourceforge.net/projects/omneteponmodule/files/latest/download",
            # "setenv_commands": ["export INETMANET_PROJ=$INETMANET_ROOT"],
            "patch_commands": [
                "sed -i 's|INETMANET_PROJ=/media/data/Linux/omnet/inetmanet-inetmanet-00f64c2|INETMANET_PROJ=$(INETMANET_ROOT)|g' Makefile src/Makefile",
            ],
            # "build_commands": ["opp_makemake -f --deep --nolink -O out -d src -X. -I$INETMANET_ROOT/src/inet -L$INETMANET_ROOT/out/$CONFIGNAME/src -L./out/$CONFIGNAME/src -linet -KINETMANET_PROJ=$INETMANET_ROOT && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "build_commands": ["cd src && opp_makemake -f --deep --make-so -o epon -O out -I. -I/common -I/linklayer -I/networklayer -I/networklayer/autoconfig -I/OLT -I/ONU -I$INETMANET_ROOT/src/inet/util/headerserializers/headers -I$INETMANET_ROOT/src/inet/networklayer/arp -I$INETMANET_ROOT/src/inet/transport/sctp -I$INETMANET_ROOT/src/inet/world -I$INETMANET_ROOT/src/inet/transport/contract -I$INETMANET_ROOT/src/inet/linklayer/mfcore -I$INETMANET_ROOT/src/inet/linklayer/ethernet -I$INETMANET_ROOT/src/inet/util -I$INETMANET_ROOT/src/inet/networklayer/ted -I$INETMANET_ROOT/src/inet/linklayer/ieee80211/mac -I$INETMANET_ROOT/src/inet/networklayer/common -I$INETMANET_ROOT/src/inet/networklayer/ipv6 -I$INETMANET_ROOT/src/inet/applications/pingapp -I$INETMANET_ROOT/src/inet/networklayer/ldp -I$INETMANET_ROOT/src/inet/transport/tcp -I$INETMANET_ROOT/src/inet/util/headerserializers -I$INETMANET_ROOT/src/inet/networklayer/rsvp_te -I$INETMANET_ROOT/src/inet/transport/udp -I$INETMANET_ROOT/src/inet/networklayer/ipv4 -I$INETMANET_ROOT/src/inet/networklayer/icmpv6 -I$INETMANET_ROOT/src/inet/base -I$INETMANET_ROOT/src/inet/networklayer/contract -I$INETMANET_ROOT/src/inet/networklayer/manetrouting/base -I$INETMANET_ROOT/src/inet/networklayer/mpls -I$INETMANET_ROOT/src/inet/linklayer/contract -I$INETMANET_ROOT/src/inet/networklayer/autorouting -L$INETMANET_ROOT/src -lINET -I$OMNETPP_ROOT/src -KINETMANET_PROJ=$INETMANET_ROOT"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP
            # cant build
            "name": "inet_hnrl", "version": "master",
            "nix_packages": ["sqlite"],
            "required_projects": {"omnetpp": ["4.2.0"]},
            "git_url": "https://github.com/kyeongsoo/inet-hnrl.git",
            "setenv_commands": ["export SQLITE_LIB=${pkgs.sqlite}/lib"],
            "patch_commands": [
                "sed -i 's|INETMANET_PROJ=/media/data/Linux/omnet/inetmanet-inetmanet-00f64c2|INETMANET_PROJ=$(INETMANET_ROOT)|g' Makefile",
                "sed -i 's|-L/usr/local/lib|-L$(SQLITE_LIB)|g' Makefile",
                "sed -i 's|-I/usr/local/include||g' Makefile",
            ],
            "build_commands": ["make makefiles && make all -j$NIX_BUILD_CORES MODE=$BUILD_MODE CFLAGS='-std=c++11 -Wall -Wextra'"],
            "clean_commands": ["make clean"],
        },

        {   # WIP
            "name": "infiniband", "version": "1.0",
            "required_projects": {"omnetpp": ["3.3.x"]},
            "download_url": "https://github.com/omnetpp-models/archive/releases/download/archive/ib_macro_model.tgz",
            # "setenv_commands": ["export INETMANET_PROJ=$INETMANET_ROOT"],
            # "patch_commands": [
            #     "sed -i 's|INETMANET_PROJ=/media/data/Linux/omnet/inetmanet-inetmanet-00f64c2|INETMANET_PROJ=$(INETMANET_ROOT)|g' Makefile src/Makefile",
            # ],
            # "build_commands": ["make makefiles && make all -j$NIX_BUILD_CORES MODE=$BUILD_MODE CFLAGS='-std=c++11 -Wall -Wextra'"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP
            "name": "infiniband_flit", "version": "1.0",
            "required_projects": {"omnetpp": ["3.3.1"]},
            "download_url": "https://github.com/omnetpp-models/archive/releases/download/archive/ib_macro_model.tgz",
            # "setenv_commands": ["export INETMANET_PROJ=$INETMANET_ROOT"],
            # "patch_commands": [
            #     "sed -i 's|INETMANET_PROJ=/media/data/Linux/omnet/inetmanet-inetmanet-00f64c2|INETMANET_PROJ=$(INETMANET_ROOT)|g' Makefile src/Makefile",
            # ],
            # "build_commands": ["make makefiles && make all -j$NIX_BUILD_CORES MODE=$BUILD_MODE CFLAGS='-std=c++11 -Wall -Wextra'"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - build errors; this might need inet 2.1.0?
            "name": "neta", "version": "1.0",
            "required_projects": {"omnetpp": ["4.2.1"], "inet": ["2.2.0"]},
            "download_url": "https://github.com/robertomagan/neta_v1/archive/refs/tags/v1.0.tar.gz",
            # "patch_commands": [
            #     "sed -i.bak 's|->spp_hbinterval > 0|->spp_hbinterval->getNum() > 0|' inet/src/inet/applications/packetdrill/PacketDrillApp.cc",
            #     "sed -i.bak 's|->spp_pathmaxrxt > 0|->spp_pathmaxrxt->getNum() > 0|' inet/src/inet/applications/packetdrill/PacketDrillApp.cc",
            # ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "build_commands": ["cd src && opp_makemake -f --deep -o neta -O out -KINET_PROJ=$INET_ROOT -DINET_IMPORT -L$INET_ROOT/src -I. -I$INET_ROOT/src -I$INET_ROOT/src/applications -I$INET_ROOT/src/applications/dhcp -I$INET_ROOT/src/applications/ethernet -I$INET_ROOT/src/applications/generic -I$INET_ROOT/src/applications/httptools -I$INET_ROOT/src/applications/pingapp -I$INET_ROOT/src/applications/rtpapp -I$INET_ROOT/src/applications/sctpapp -I$INET_ROOT/src/applications/tcpapp -I$INET_ROOT/src/applications/traci -I$INET_ROOT/src/applications/udpapp -I$INET_ROOT/src/applications/voip -I$INET_ROOT/src/base -I$INET_ROOT/src/battery -I$INET_ROOT/src/battery/models -I$INET_ROOT/src/linklayer -I$INET_ROOT/src/linklayer/common -I$INET_ROOT/src/linklayer/contract -I$INET_ROOT/src/linklayer/ethernet -I$INET_ROOT/src/linklayer/ethernet/switch -I$INET_ROOT/src/linklayer/ext -I$INET_ROOT/src/linklayer/idealwireless -I$INET_ROOT/src/linklayer/ieee80211 -I$INET_ROOT/src/linklayer/ieee80211/mac -I$INET_ROOT/src/linklayer/ieee80211/mgmt -I$INET_ROOT/src/linklayer/ieee80211/radio -I$INET_ROOT/src/linklayer/ieee80211/radio/errormodel -I$INET_ROOT/src/linklayer/loopback -I$INET_ROOT/src/linklayer/ppp -I$INET_ROOT/src/linklayer/queue -I$INET_ROOT/src/linklayer/radio -I$INET_ROOT/src/linklayer/radio/propagation -I$INET_ROOT/src/mobility -I$INET_ROOT/src/mobility/models -I$INET_ROOT/src/networklayer -I$INET_ROOT/src/networklayer/arp -I$INET_ROOT/src/networklayer/autorouting -I$INET_ROOT/src/networklayer/autorouting/ipv4 -I$INET_ROOT/src/networklayer/autorouting/ipv6 -I$INET_ROOT/src/networklayer/bgpv4 -I$INET_ROOT/src/networklayer/bgpv4/BGPMessage -I$INET_ROOT/src/networklayer/common -I$INET_ROOT/src/networklayer/contract -I$INET_ROOT/src/networklayer/diffserv -I$INET_ROOT/src/networklayer/icmpv6 -I$INET_ROOT/src/networklayer/internetcloud -I$INET_ROOT/src/networklayer/ipv4 -I$INET_ROOT/src/networklayer/ipv6 -I$INET_ROOT/src/networklayer/ipv6tunneling -I$INET_ROOT/src/networklayer/ldp -I$INET_ROOT/src/networklayer/manetrouting -I$INET_ROOT/src/networklayer/manetrouting/aodv -I$INET_ROOT/src/networklayer/manetrouting/aodv/aodv-uu -I$INET_ROOT/src/networklayer/manetrouting/base -I$INET_ROOT/src/networklayer/manetrouting/batman -I$INET_ROOT/src/networklayer/manetrouting/batman/batmand -I$INET_ROOT/src/networklayer/manetrouting/batman/batmand/orig -I$INET_ROOT/src/networklayer/manetrouting/dsdv -I$INET_ROOT/src/networklayer/manetrouting/dsr -I$INET_ROOT/src/networklayer/manetrouting/dsr/dsr-uu -I$INET_ROOT/src/networklayer/manetrouting/dymo -I$INET_ROOT/src/networklayer/manetrouting/dymo/dymoum -I$INET_ROOT/src/networklayer/manetrouting/dymo_fau -I$INET_ROOT/src/networklayer/manetrouting/olsr -I$INET_ROOT/src/networklayer/mpls -I$INET_ROOT/src/networklayer/ospfv2 -I$INET_ROOT/src/networklayer/ospfv2/interface -I$INET_ROOT/src/networklayer/ospfv2/messagehandler -I$INET_ROOT/src/networklayer/ospfv2/neighbor -I$INET_ROOT/src/networklayer/ospfv2/router -I$INET_ROOT/src/networklayer/rsvp_te -I$INET_ROOT/src/networklayer/ted -I$INET_ROOT/src/networklayer/xmipv6 -I$INET_ROOT/src/nodes -I$INET_ROOT/src/nodes/bgp -I$INET_ROOT/src/nodes/ethernet -I$INET_ROOT/src/nodes/httptools -I$INET_ROOT/src/nodes/inet -I$INET_ROOT/src/nodes/internetcloud -I$INET_ROOT/src/nodes/ipv6 -I$INET_ROOT/src/nodes/mpls -I$INET_ROOT/src/nodes/ospfv2 -I$INET_ROOT/src/nodes/rtp -I$INET_ROOT/src/nodes/wireless -I$INET_ROOT/src/nodes/xmipv6 -I$INET_ROOT/src/status -I$INET_ROOT/src/transport -I$INET_ROOT/src/transport/contract -I$INET_ROOT/src/transport/rtp -I$INET_ROOT/src/transport/rtp/profiles -I$INET_ROOT/src/transport/rtp/profiles/avprofile -I$INET_ROOT/src/transport/sctp -I$INET_ROOT/src/transport/tcp -I$INET_ROOT/src/transport/tcp/flavours -I$INET_ROOT/src/transport/tcp/queues -I$INET_ROOT/src/transport/tcp_common -I$INET_ROOT/src/transport/udp -I$INET_ROOT/src/util -I$INET_ROOT/src/util/headerserializers -I$INET_ROOT/src/util/headerserializers/headers -I$INET_ROOT/src/util/headerserializers/ipv4 -I$INET_ROOT/src/util/headerserializers/ipv4/headers -I$INET_ROOT/src/util/headerserializers/sctp -I$INET_ROOT/src/util/headerserializers/sctp/headers -I$INET_ROOT/src/util/headerserializers/tcp -I$INET_ROOT/src/util/headerserializers/tcp/headers -I$INET_ROOT/src/util/headerserializers/udp -I$INET_ROOT/src/util/headerserializers/udp/headers -I$INET_ROOT/src/world -I$INET_ROOT/src/world/annotations -I$INET_ROOT/src/world/httptools -I$INET_ROOT/src/world/obstacles -I$INET_ROOT/src/world/radio -I$INET_ROOT/src/world/scenario -I$INET_ROOT/src/world/traci -linet && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - doesnt build
            "name": "inetmanet", "version": "paser",
            "required_projects": {"omnetpp": ["5.4.x"]},
            "git_url": "https://github.com/PASER/Simulation-INETMANET.git",
            "patch_commands": [
                "for f in $(grep -Rls 'defined(linux)'); do sed -i.bak 's|defined(linux)|defined(__linux__)|' $f; done",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            # "setenv_commands": ["echo 'Hint: run example simulations from their folder. For example, in examples/TwoSubnets folder: ./out/gcc-debug/TwoSubnets omnetpp.ini"]
            "clean_commands": ["make clean"],
        },

        {
            # WIP - lua 5.1 not found
            "name": "pawis", "version": "2.0",
            "nix_packages": ["lua51Packages.lua"],
            "required_projects": {"omnetpp": ["3.3.1"]},
            "download_url": "https://sourceforge.net/projects/pawis/files/latest/download",
            "setenv_commands": ["export LUA_LIBS=${pkgs.lua51Packages.lua}/lib && echo $LUA_LIBS",
                                "export LUA_CFLAGS=${pkgs.lua51Packages.lua}/include && echo $LUA_CFLAGS",
                                "export PKG_CONFIG_PATH=${pkgs.lua51Packages.lua}/lib/pkgconfig",
                                # "export NIX_CFLAGS_COMPILE=${pkgs.lua51Packages.lua}/include"
                                ],
            # "patch_commands": [
            #     "for f in $(grep -Rls 'defined(linux)'); do sed -i.bak 's|defined(linux)|defined(__linux__)|' $f; done",
            # ],
            "build_commands": ['cd sim-framework && ./configure --prefix $PAWIS_ROOT/sim-framework OMNET_BASE=$OMNETPP_ROOT CXXFLAGS="-ggdb -O0 -Wall"'],
            # "setenv_commands": ["echo 'Hint: run example simulations from their folder. For example, in examples/TwoSubnets folder: ./out/gcc-debug/TwoSubnets omnetpp.ini"]
            "clean_commands": ["make clean"],
            # ./configure --prefix $PAWIS_ROOT/sim-framework OMNET_BASE=$OMNETPP_ROOT CXXFLAGS="-ggdb -O0 -Wall" LDFLAGS="-L$LUA_LIBS" LIBS="-llua"
        },

        {
            # WIP - needs matlab-link
            "name": "phoenixsim", "version": "master",
            # "nix_packages": ["lua"],
            "required_projects": {"omnetpp": ["4.5.x"]},
            "git_url": "https://github.com/lebiednik/PhoenixSim.git",
            # "setenv_commands": ["export LUA_LIBS=${pkgs.lua51Packages.lua}/lib && echo $LUA_LIBS",
            #                     "export LUA_CFLAGS=${pkgs.lua51Packages.lua}/include",
            #                     # "export PKG_CONFIG_PATH=${pkgs.lua51Packages.lua}/lib/pkgconfig",
            #                     # "export NIX_CFLAGS_COMPILE=${pkgs.lua51Packages.lua}/include"
            #                     ],
            "patch_commands": [
                """sed -i 's|include "MAC_token.h"|include "MAC_TOKEN.h"|g' */*/*.cc"""
            ],
            "build_commands": ["opp_makemake -f --deep -o PhoenixSim -O out -L$OMNETPP_ROOT/lib -loppsim && make -j16"],
            # "setenv_commands": ["echo 'Hint: run example simulations from their folder. For example, in examples/TwoSubnets folder: ./out/gcc-debug/TwoSubnets omnetpp.ini"]
            "clean_commands": ["make clean"],
            # ./configure --prefix $PAWIS_ROOT/sim-framework OMNET_BASE=$OMNETPP_ROOT CXXFLAGS="-ggdb -O0 -Wall" LDFLAGS="-L$LUA_LIBS" LIBS="-llua"
        },

        {
            # WIP - builds;
            # FXGLVisual::create: requested OpenGL visual unavailable.
            # Aborted (core dumped) -> eliminated by mesa package sometimes; now FATAL: exception not rethrown
            "name": "plexe", "version": "3.1.1",
            "nix_packages": ["python2", "mesa", "libxml2"],
            "required_projects": {"omnetpp": ["6.0.0"], "veins": ["5.2"]},
            "download_url": "https://github.com/michele-segata/plexe/archive/refs/tags/plexe-3.1.1.tar.gz",
            "setenv_commands": [
                                "export SUMO_HOME=${pkgs.sumo}/share/sumo && echo 'sumo home: ' && echo $SUMO_HOME",
                                ],
            "patch_commands": [
                "sed -i 's|from elementtree|from xml.etree|' */*/*/*.py",
            ],
            "build_commands": ["./configure --with-veins=$VEINS_ROOT && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && . setenv"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - builds; cant find ned types
            "name": "processbus", "version": "master",
            "required_projects": {"omnetpp": ["4.6.x"]},
            "git_url": "https://github.com/hectordelahoz/ProcessBusIec61850.git",
            "patch_commands": [
                            "sed -i.bak 's/if (vector_cost<=0)/if (vector_cost == NULL)/' iec61850InetV2.6/inet/src/networklayer/manetrouting/dsr/dsr-uu/path-cache.cc",
                            # "sed -i.bak 's/if (vector_cost<=nullptr)/if (vector_cost == nullptr)/' src/inet/routing/extras/dsr/dsr-uu/path-cache.cc" if not is_modernized and inet_version >= "3.0" and inet_version < "3.1" else None,
                "sed -i 's|testinet|TestInet|' iec61850InetV2.6/TestInet/simulations/run",
                "chmod +x iec61850InetV2.6/TestInet/simulations/run",
                "sed -i 's|-n .:../src|-n .:../src:../../inet/src|' iec61850InetV2.6/TestInet/simulations/run",
            ],
            "build_commands": ["cd iec61850InetV2.6/inet && make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && chmod +x src/run_inet && cd ../TestInet && make makefiles && cd src && make"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP; this should be its own project; should this be linked to inet?
            "name": "rimfading", "version": "master",
            "required_projects": {"omnetpp": ["5.1.x"], "inet": ["3.3.0"]},
            "git_url": "https://github.com/ComNets-Bremen/RIMFading.git",
            # "patch_commands": [
            #                 "sed -i.bak 's/if (vector_cost<=0)/if (vector_cost == NULL)/' iec61850InetV2.6/inet/src/networklayer/manetrouting/dsr/dsr-uu/path-cache.cc",
            #                 # "sed -i.bak 's/if (vector_cost<=nullptr)/if (vector_cost == nullptr)/' src/inet/routing/extras/dsr/dsr-uu/path-cache.cc" if not is_modernized and inet_version >= "3.0" and inet_version < "3.1" else None,
            #     "sed -i 's|testinet|TestInet|' iec61850InetV2.6/TestInet/simulations/run",
            #     "chmod +x iec61850InetV2.6/TestInet/simulations/run",
            #     "sed -i 's|-n .:../src|-n .:../src:../../inet/src|' iec61850InetV2.6/TestInet/simulations/run",
            # ],
            # "build_commands": ["cd iec61850InetV2.6/inet && make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && chmod +x src/run_inet && cd ../TestInet && make makefiles && cd src && make"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - needs older INET (20100323)
            "name": "rease", "version": "master",
            "required_projects": {"omnetpp": ["4.1.0"], "inet": ["20100323"]},
            "git_url": "https://github.com/ToGaKIT/ReaSE.git",
            "patch_commands": [
            #                 "sed -i.bak 's/if (vector_cost<=0)/if (vector_cost == NULL)/' iec61850InetV2.6/inet/src/networklayer/manetrouting/dsr/dsr-uu/path-cache.cc",
            #                 # "sed -i.bak 's/if (vector_cost<=nullptr)/if (vector_cost == nullptr)/' src/inet/routing/extras/dsr/dsr-uu/path-cache.cc" if not is_modernized and inet_version >= "3.0" and inet_version < "3.1" else None,
                "sed -i 's|INETDIR = ../../INET|INETDIR = $(INET_ROOT)|' ReaSE/Makefile",
                "sed -i 's|lINET|linet|' ReaSE/Makefile",
            #     "chmod +x iec61850InetV2.6/TestInet/simulations/run",
            #     "sed -i 's|-n .:../src|-n .:../src:../../inet/src|' iec61850InetV2.6/TestInet/simulations/run",
            ],
            "build_commands": ["cd ReaSE && make -j16"],
            "clean_commands": ["make clean"],
        },

        {
            # WIP - doesnt build yet; depends on several libraries
            "name": "seapp", "version": "master",
            "nix_packages": ["python2", "glibmm", "libxml2", "libsigcxx", "libxmlxx", "glib"],
            "required_projects": {"omnetpp": ["4.6.x"]},
            "git_url": "https://github.com/seapp/seapp_stable.git",
            "setenv_commands": [
                                "export GLIBMM_ROOT=${pkgs.glibmm} && echo 'GLIBMM_ROOT: ' && echo $GLIBMM_ROOT",
                                "export GLIBMM_DEV_ROOT=${pkgs.glibmm.dev} && echo 'GLIBMM_DEV_ROOT: ' && echo $GLIBMM_DEV_ROOT",
                                "export LIBXMLXX_ROOT=${pkgs.libxmlxx} && echo 'LIBXMLXX_ROOT: ' && echo $LIBXMLXX_ROOT",
                                "export LIBSIGCXX_ROOT=${pkgs.libsigcxx} && echo 'LIBSIGCXX_ROOT: ' && echo $LIBSIGCXX_ROOT",
                                "export GLIB_ROOT=${pkgs.glib} && echo 'GLIB_ROOT: ' && echo $GLIB_ROOT",
                                ],
            "patch_commands": [
            #     "sed -i 's|from elementtree|from xml.etree|' */*/*/*.py",
                "sed -i 's|-I/usr/include/libxml2|-I${pkgs.libxml2.dev}/include/libxml2|g' Makefile",
                "sed -i 's|-I/usr/include/libxml++-2.6|-I${pkgs.libxmlxx}/include/libxml++-2.6|g' Makefile",
                "sed -i 's|-I/usr/include/glibmm-2.4|-I${pkgs.glibmm}/lib/glibmm-2.4/include -I${pkgs.glibmm}/lib/glibmm-2.4|g' Makefile",
                "sed -i 's|-I/usr/include/sigc++-2.0|-I${pkgs.libsigcxx}/include/sigc++-2.0|g' Makefile",
                "sed -i 's|-I/usr/include/glib-2.0|-I${pkgs.glib}/include/glib-2.0 -I${pkgs.glib}/include/glib-2.0/include|g' Makefile",
                "sed -i 's|-I/usr/lib/x86_64-linux-gnu/libxml++-2.6/include|-L$(LIBXMLXX_ROOT)/lib|g' Makefile",
                "sed -i 's|-I/usr/lib/x86_64-linux-gnu/glibmm-2.4/include |-L$(GLIBMM_ROOT)/lib|g' Makefile",
                "sed -i 's|-I/usr/lib/x86_64-linux-gnu/sigc++-2.0/include |-L$(LIBSIGCXX_ROOT)/lib|g' Makefile",
                "sed -i 's|-I/usr/lib/x86_64-linux-gnu/glib-2.0/include|-L$(GLIB_ROOT)/lib|g' Makefile",
                # "sed -i 's|||g' Makefile",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"],
        },

        {
            "name": "libxmlpp", "version": "2.6",
            "nix_packages": ["glibmm", "libxml2", "libsigcxx", "pkg-config"],
            # "required_projects": {"omnetpp": ["4.6.x"]},
            "download_url": "https://download.gnome.org/sources/libxml++/2.6/libxml%2B%2B-2.6.1.tar.gz",
            "setenv_commands": [
                                # "export PKG_CONFIG_PATH=${pkgs.libxml2.dev}/include/libxml2",
                                "export PKG_CONFIG_PATH=${pkgs.libxml2.dev}/lib/pkgconfig",
                                "PKG_CONFIG_PATH=${pkgs.glibmm.dev}/lib/pkgconfig:$PKG_CONFIG_PATH",
                                "PKG_CONFIG_PATH=${pkgs.glib.dev}/lib/pkgconfig:$PKG_CONFIG_PATH",
                                "PKG_CONFIG_PATH=${pkgs.libsigcxx}/lib/pkgconfig:$PKG_CONFIG_PATH",
                                "PKG_CONFIG_PATH=${pkgs.pkg-config}:$PKG_CONFIG_PATH",
                                "echo 'PKG_CONFIG_PATH: ' && echo $PKG_CONFIG_PATH",
                                ],
            # "patch_commands": [
            # #     "sed -i 's|from elementtree|from xml.etree|' */*/*/*.py",
            #     "sed -i 's|-I/usr/include/libxml2|-I${pkgs.libxml2.dev}/include/libxml2|g' Makefile",
            #     "sed -i 's|-I/usr/include/libxml++-2.6|-I${pkgs.libxmlxx}|g' Makefile",
            #     "sed -i 's|-I/usr/lib/x86_64-linux-gnu/libxml++-2.6/include||g' Makefile",
            # ],
            # "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "build_commands": ["./configure"],
            "clean_commands": ["make clean"],
        },
    ]