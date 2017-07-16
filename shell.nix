{ pkgs ? import <nixpkgs> {} }:
with pkgs; python3Packages.buildPythonApplication rec {
  name = "flask-hello-world-${version}";
  version = "0.1.0";

  src = if lib.inNixShell then null else ./.;

  propagatedBuildInputs = with python3Packages; [
    flask
  ];
}
