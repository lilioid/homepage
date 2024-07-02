{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  packages = with pkgs; [
    python3
    uv
    pre-commit
    ruff
  ];
}
