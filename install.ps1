# The Flow Machine �� One-line installer for Windows
# irm https://raw.githubusercontent.com/seancrowe01/flow-machine/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

$REPO = "https://github.com/seancrowe01/flow-machine.git"
$DIR = "flow-machine"

Write-Host ""
Write-Host "  ╔══════���═══════════════════════════╗"
Write-Host "  ║       THE FLOW MACHINE           ║"
Write-Host "  ║  Screenshots → Rebuild Guides    ║"
Write-Host "  ╚══════════════════════════════════╝"
Write-Host ""

# Check for git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Error: git is not installed. Install git first." -ForegroundColor Red
    exit 1
}

# Clone
if (Test-Path $DIR) {
    Write-Host "Directory '$DIR' already exists. Pulling latest..."
    Set-Location $DIR
    git pull origin main
} else {
    Write-Host "Cloning repo..."
    git clone $REPO $DIR
    Set-Location $DIR
}

# Copy .env
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from template."
} else {
    Write-Host ".env already exists. Skipping."
}

Write-Host ""
Write-Host "  Installed to $(Get-Location)" -ForegroundColor Green
Write-Host ""
Write-Host "  Next steps:"
Write-Host ""
Write-Host "  1. Open .env and add your API keys:"
Write-Host "     - AIRTABLE_API_KEY  (https://airtable.com/create/tokens)"
Write-Host "     - MANYCHAT_API_KEY  (optional -- for live flow data)"
Write-Host ""
Write-Host "  2. Open Claude Code in this folder and run:"
Write-Host "     /flow-setup"
Write-Host ""
Write-Host "  That's it. The setup wizard handles the rest."
Write-Host ""
