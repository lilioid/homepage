{
  description = "homepage";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { system = system; };
      in
      {
        formatter.x86_64-linux = pkgs.nixfmt-rfc-style;
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            uv
            pre-commit
            ruff
            python3
            python3Packages.pillow
            python3Packages.numpy
            esbuild
          ];
        };
      }
    );
}
