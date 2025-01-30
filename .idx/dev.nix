# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.apt
    pkgs.docker
    pkgs.docker-compose
    pkgs.gcc
    pkgs.swiftPackages.swift-unwrapped 
    pkgs.python3
    pkgs.python311
    pkgs.python311Packages.pip
  ];
  # Enable Docker
  services.docker = {
    enable = true;
  };
  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "vscjava.vscode-java-pack"
      "rangav.vscode-thunder-client"
    ];
  };
}