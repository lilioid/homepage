{ nixpkgs ? <nixpkgs> }:
let
  pkgs = import nixpkgs { };
in
pkgs.mkShell {
  packages = with pkgs; [
    python312
    python312Packages.pillow
    python312Packages.numpy
    uv
    pre-commit
    ruff
    pnpm
  ];
}
