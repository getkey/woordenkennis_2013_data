{ pkgs ? import <nixpkgs> {} }:
	pkgs.mkShell {
		buildInputs = [
			pkgs.python3Packages.requests
			pkgs.python3Packages.beautifulsoup4
			pkgs.python3
		];
}
