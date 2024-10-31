{
  description = "opp_env: A Tool for Automated Installation of OMNeT++ Simulation Frameworks";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem(system:
    let
      pkgs = import nixpkgs { inherit system; };
      pname = "opp_env";
      version = "0.31.1.241031"; # Latest released version. Must be updated regularly.
      githash = self.shortRev or "dirty";
      timestamp = nixpkgs.lib.substring 0 8 self.lastModifiedDate;
      gversion = "${githash}.${timestamp}";
    in {
      packages = rec {
        opp_env = pkgs.callPackage ./default.nix {
          inherit pname version;
          src = pkgs.python3Packages.fetchPypi {
            inherit pname version;
            hash = "sha256-VoucL+9Btde42XZn7oVefKMxU4c1fWBJNgejMRlsKDo=";
          };
        };

        opp_env-git = pkgs.callPackage ./default.nix {
          pname = "${pname}-git";
          version = "0+${gversion}";
          src = ./.;
        };

        default = opp_env;
      };

    });
}
