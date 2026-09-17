$ErrorActionPreference = "Stop"

# Run from repo root even when the script is launched via VS Code tasks.
$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
$root = Resolve-Path "$scriptDir\.."
Set-Location $root

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
  irm https://astral.sh/uv/install.ps1 | iex
  $env:PATH = "$HOME\.local\bin;$env:PATH"
}


uv venv --python 3.9
uv pip install -r using-vscode/requirements.txt
