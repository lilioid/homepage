{
  description = "Lilly's own personal homepage";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
    rec {
      packages.x86_64-linux = rec {

        homepage = pkgs.python3.pkgs.buildPythonApplication {
          name = pyproject.project.name;
          version = pyproject.project.version;
          format = "pyproject";
          src = ./.;
          nativeBuildInputs = with pkgs.python3.pkgs; [ flit ];
          propagatedBuildInputs = with pkgs.python3.pkgs; [ fastapi jinja2 hypercorn colorama python-frontmatter markdown pygments ];
        };

        homepage-oci = pkgs.dockerTools.buildLayeredImage {
          name = "ghcr.io/ftsell/homepage";
          tag = "latest";
          config = {
            Entrypoint = [ "${homepage}/bin/homepage" ];
            User = "10000:65534"; # 10,000 and nogroup
            Env = [ "BIND=[\"0.0.0.0:8000\"]" ];
            ExposedPorts = {
              "8000/tcp" = { };
            };
            Labels = {
              "org.opencontainers.image.url" = pyproject.project.urls."Home";
              "org.opencontainers.image.source" = pyproject.project.urls."Source";
              "org.opencontainers.image.version" = pyproject.project.version;
              "org.opencontainers.image.revision" = if (self ? rev) then self.rev else self.dirtyRev;
              "org.opencontainers.image.licenses" = "MIT";
            };
          };
        };
      };

      devShells.x86_64-linux.default = pkgs.mkShell {
        packages = with pkgs; [
          python312
          uv
          pre-commit
          ruff
          python312Packages.pygments
          python312Packages.requests
        ];
      };
    };
}
