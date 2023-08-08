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
            # WIP
            "name": "ieee802154standalone", "version": "master",
            # "nix_packages": ["curl", "tcl"],
            "required_projects": {"omnetpp": ["4.6"], "inet": ["2.4.0"]},
            "git_url": "https://github.com/michaelkirsche/IEEE802154INET-Standalone.git",
            # "setenv_commands": ["export INET_PROJ=$INET_ROOT",
            #                     "export TCL_LIBRARY=$TCLLIBPATH"],
            "patch_commands": [
                "sed -i 's|INETDefs.h|base/INETDefs.h|g' src/*/*.h",
                # "find . -type f -name '*.h' -exec sed -i 's|#include INETDefs.h|#include base/INETDefs.h|g'",
                # "for i in xa*; do sed -i 's|#include INETDefs.h|#include base/INETDefs.h|' $i;done"
                "sed -i 's|opp_makemake -f --deep|opp_makemake -f --deep -I. -I${INET_ROOT}/src -o ieee802154 -L${INET_ROOT}/src -lINET|' Makefile",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
        },
        
        {
            # compile error
            "name": "os3", "version": "master",
            "nix_packages": ["curl", "tcl"],
            "required_projects": {"omnetpp": ["4.2"], "inet": ["2.2.0"]},
            "download_url": "https://github.com/inet-framework/os3/archive/refs/tags/v1.0.tar.gz",
            "setenv_commands": ["export INET_PROJ=$INET_ROOT",
                                "export TCL_LIBRARY=$TCLLIBPATH"],
            "patch_commands": [
                "sed -i -E 's|-KINET_PROJ=[^ ]+|-KINET_PROJ=$(INET_ROOT)|' Makefile",
                "sed -i 's|$DIR/../../inet|$INET_ROOT|' src/run_cni-os3",
            ],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
            "clean_commands": ["make clean"]
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
            "build_commands": ["opp_makemake -f --deep -O out -KINET4_PROJ=$INET4_PROJ -DINET_IMPORT -I. -I$INET4_PROJ/src -L$INET4_PROJ/src -lINET$D && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE"],
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
            "name": "oversim", "version": "20190424",
            "required_projects": {"inet": ["3.6.*"], "omnetpp": ["5.4.*"]},
            "download_url": "https://github.com/inet-framework/oversim/archive/refs/tags/v20190424.tar.gz",
            "patch_commands": ["sed -i -E 's|INETDIR = .*|INETDIR = $(INET_ROOT)|' Makefile"],
            "build_commands": ["make makefiles && make -j$NIX_BUILD_CORES MODE=$BUILD_MODE && sed -i -E \"s|ned-path = .*|ned-path = $INET_ROOT/src;../src|\" simulations/default.ini"],
            "clean_commands": ["make clean"],
            "description": "DONE"
        },

    ]