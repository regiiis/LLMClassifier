# LLMClassifier
A LLM classifier for experimental purposes

<br>

## Setup for Development
In order to run the CI/CD pipeline, you need to make sure to:
- Run VS as admin.
- Install Debian on WSL
- Setup Git on WSL - see [Version Control](#version-control)

### ``` Linux Subsystem (WSL)```
If you are working with Windows, you need to use a Linux subsystem to work in the same env as the CI/CD pipline. Run VS as admin!

#### Install Debian WSL:
```bash
# 1. In Powershell
wsl --set-default-version 2
```
```bash
# 2. Install Debian (or Ubuntu)
wsl --install -d Debian
# 3. Follow the installation instruction (Restart).
```
#### Setup Debian WSL:
```bash
# 1. In WSL - Install Python (Check latest version for Debian)
sudo apt install -y python3.11  # Install Python
sudo apt install -y python3-pip  # Install Python package manager
# 3. Follow the installation instruction.
```

#### Create Python Virtual Environment
```bash
# Install proper venv lib for linux
sudo apt install python3.11-venv

# Create new virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

#### Install Node
```bash
# Install Node.js and npm
sudo apt update
sudo apt install nodejs npm
```

### ``` Daily Command for Local Dev```
```bash
# Activate Python virtual environment
source .venv/bin/activate

export ANY_VARIABLE="value"  # Set any variable you need

# Install Python packages
pip install -r requirements.txt

# Install pre-Commits
pre-commit install
```
<br>

## CI/CD Pipeline

- In Makefiles, each line runs in a separate shell

Linters: ruff, tflint, yamllint, shellcheck
Formatters: terraform_fmt, ruff-format
Security scanners: tfsec, checkov
Other checks: end-of-file-fixer, trailing-whitespace
<br>

## Project Documentation
The project is documented by means of a wiki and README's.

### ``` README```
Every main folder should have a README, describing its substructure, included tech and used knowledge.

### ``` Wiki - Sphinx```
Sphix is used to automatically generate a code docstring documentation as well as dedicated pages in marksdown.
<br>

## Version Control
A guideline for version control in this project. Work on main. Use Flags. Do not break the Pipeline.

Git doc: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
### ```Link GitHub to WSL```

```bash
# 1. Update package manager
sudo apt-get update
# 2. Install git
sudo apt-get -y install git

# 3. Create directory for SSH agent
mkdir -p ~/.ssh
# 4. Generate SSH-Key pair
# - Press ENTER to choose default file location
# - Press ENTER for no passphrase
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# 4. Start the SSH agent
eval "$(ssh-agent -s)"
# 5. Add your new identity key to SSH agent
ssh-add ~/.ssh/id_rsa

# 5. Display and copy your public key
cat ~/.ssh/id_rsa.pub
```
5. Add to GitHub:

- Go to GitHub → Profile "Settings" → SSH and GPG keys
- Click "New SSH key"
- Paste your key and save
```bash
# 6. Configure Git globally
# Name and email do not need to be realated to GitHub Account
git config --global user.name "Any Name"
git config --global user.email "your.email@example.com"

# 7. Test connection
ssh -T git@github.com
```
```bash
# 8. Check URL's
# If the URL starts with https://, you need to change it in order to use SSH.
git remote -v

# 8. Set remote URL for SSH
# Use SSH URL
git remote set-url origin git@github.com:<username>/<repository>.git

```
<br>

### ```Commit naming rules```

| Type | Purpose | Examples |
|------|---------|----------|
| `feat` | Change source code | New features, code changes |
| `ci` | CI configuration | CI Pipeline, GitHub Actions updates |
| `test` | Test-related changes | Adding/updating test cases |
| `perf` | Performance improvements | Optimization |
| `build` | Build system or dependency changes | Build scripts, dependency updates |
| `chore` | Routine maintenance tasks | Version updates, file renaming |
| `refactor` | Non-feature code changes | Code reorganization, readability |
| `style` | Code formatting changes | Whitespace, semicolons |
| `docs` | Documentation updates | README changes, code comments |
<br>
