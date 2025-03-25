{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }: let 
    system = "x86_64-linux";
  in {
    devShells."${system}".default = let
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in pkgs.mkShell {
      packages = with pkgs; [
        (vscode-with-extensions.override {
          vscode = vscodium;
          vscodeExtensions = with vscode-extensions; [
            github.copilot
            jnoortheen.nix-ide
            arrterian.nix-env-selector
            ms-python.vscode-pylance
            ms-python.python
            ms-python.debugpy
            ms-python.black-formatter
          ];
        })
        (python3.withPackages (python-pkgs: with python-pkgs; [
        ]))
      ];
      buildInputs = [ pkgs.bashInteractive ];
    };
  };
}
