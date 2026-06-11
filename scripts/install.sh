#!/bin/bash
################################################################################
# HackingTool Pro - Installation Script
# Author: Kartikey Rai
# GitHub: https://github.com/kartikey3205
################################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
REPO_URL="https://github.com/kartikey3205/hackingtool-pro"
INSTALL_DIR="/opt/hackingtool-pro"
CONFIG_DIR="$HOME/.hackingtool-pro"
LOG_FILE="/tmp/hackingtool-install.log"

# Banner
print_banner() {
    clear
    echo -e "${CYAN}"
    cat << "EOF"
 _   _            _               _    _           _      _____           _       _   
| | | | __ _  ___| | _____ _ __  | | _| | ___  ___| |_   |_   _|__   ___ | | ____| |_ 
| |_| |/ _` |/ __| |/ / _ \ '__| | |/ / |/ _ \/ __| __|    | |/ _ \ / _ \| |/ / _` __|
|  _  | (_| | (__|   <  __/ |    |   <| |  __/\__ \ |_     | | (_) | (_) |   < (_| |_ 
|_| |_|\__,_|\___|_|\_\___|_|    |_|\_\_|\___||___/\__|    |_|\___/ \___/|_|\_\__,_\__|
                                                                                       
EOF
    echo -e "${NC}"
    echo -e "${GREEN}HackingTool Pro v3.0.0 - Installation Script${NC}"
    echo -e "${BLUE}Author: Kartikey Rai${NC}"
    echo -e "${BLUE}GitHub: https://github.com/kartikey3205${NC}"
    echo ""
}

# Logging
log() {
    echo -e "${BLUE}[*]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}[+]${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[-]${NC} $1" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}[!]${NC} $1" | tee -a "$LOG_FILE"
}

# Check if running as root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        error "This script must be run as root (use sudo)"
        exit 1
    fi
}

# Detect OS
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$NAME
        VER=$VERSION_ID
    elif type lsb_release >/dev/null 2>&1; then
        OS=$(lsb_release -si)
        VER=$(lsb_release -sr)
    elif [ -f /etc/lsb-release ]; then
        . /etc/lsb-release
        OS=$DISTRIB_ID
        VER=$DISTRIB_RELEASE
    else
        OS=$(uname -s)
        VER=$(uname -r)
    fi
    
    log "Detected OS: $OS $VER"
}

# Check system requirements
check_requirements() {
    log "Checking system requirements..."
    
    # Check Python version
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d ' ' -f 2)
        log "Python version: $PYTHON_VERSION"
        
        # Check if Python >= 3.10
        if python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"; then
            success "Python version is compatible"
        else
            error "Python 3.10+ is required"
            exit 1
        fi
    else
        error "Python 3 is not installed"
        exit 1
    fi
    
    # Check available disk space (need at least 50GB)
    AVAILABLE_SPACE=$(df /opt | tail -1 | awk '{print $4}')
    AVAILABLE_GB=$((AVAILABLE_SPACE / 1024 / 1024))
    
    if [ $AVAILABLE_GB -lt 50 ]; then
        warning "Low disk space: ${AVAILABLE_GB}GB available (50GB recommended)"
    else
        success "Disk space check passed: ${AVAILABLE_GB}GB available"
    fi
    
    # Check RAM (need at least 4GB)
    TOTAL_RAM=$(free -g | awk '/^Mem:/{print $2}')
    if [ "$TOTAL_RAM" -lt 4 ]; then
        warning "Low RAM: ${TOTAL_RAM}GB (4GB minimum recommended)"
    else
        success "RAM check passed: ${TOTAL_RAM}GB"
    fi
}

# Install system dependencies
install_dependencies() {
    log "Installing system dependencies..."
    
    case $OS in
        *"Kali"*|*"kali"*)
            apt-get update
            apt-get install -y \
                python3-pip \
                python3-venv \
                python3-dev \
                git \
                curl \
                wget \
                nano \
                vim \
                net-tools \
                iputils-ping \
                nmap \
                masscan \
                golang \
                ruby \
                ruby-dev \
                build-essential \
                libssl-dev \
                libffi-dev \
                libxml2-dev \
                libxslt1-dev \
                zlib1g-dev \
                docker.io \
                docker-compose
            ;;
        *"Ubuntu"*|*"Debian"*)
            apt-get update
            apt-get install -y \
                python3-pip \
                python3-venv \
                python3-dev \
                git \
                curl \
                wget \
                nano \
                vim \
                net-tools \
                iputils-ping \
                nmap \
                golang-go \
                ruby \
                ruby-dev \
                build-essential \
                libssl-dev \
                libffi-dev \
                libxml2-dev \
                libxslt1-dev \
                zlib1g-dev \
                docker.io \
                docker-compose
            ;;
        *"Arch"*|*"Manjaro"*)
            pacman -Sy --noconfirm \
                python-pip \
                python-virtualenv \
                git \
                curl \
                wget \
                nano \
                vim \
                net-tools \
                iputils \
                nmap \
                go \
                ruby \
                base-devel \
                openssl \
                libffi \
                libxml2 \
                libxslt \
                zlib \
                docker \
                docker-compose
            ;;
        *)
            warning "Unknown OS. Attempting generic installation..."
            ;;
    esac
    
    success "System dependencies installed"
}

# Clone repository
clone_repo() {
    log "Cloning HackingTool Pro repository..."
    
    if [ -d "$INSTALL_DIR" ]; then
        warning "Installation directory exists. Updating..."
        cd "$INSTALL_DIR"
        git pull origin main
    else
        git clone "$REPO_URL" "$INSTALL_DIR"
        cd "$INSTALL_DIR"
    fi
    
    success "Repository cloned/updated"
}

# Setup Python environment
setup_python_env() {
    log "Setting up Python virtual environment..."
    
    python3 -m venv venv
    source venv/bin/activate
    
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    
    success "Python environment configured"
}

# Create launcher
create_launcher() {
    log "Creating system launcher..."
    
    cat > /usr/local/bin/hackingtool << 'EOF'
#!/bin/bash
cd /opt/hackingtool-pro
source venv/bin/activate
sudo python3 hackingtool.py "$@"
EOF
    
    chmod +x /usr/local/bin/hackingtool
    
    # Create desktop entry
    cat > /usr/share/applications/hackingtool.desktop << EOF
[Desktop Entry]
Name=HackingTool Pro
Comment=Ultimate Cybersecurity Suite
Exec=/usr/local/bin/hackingtool
Icon=/opt/hackingtool-pro/docs/icon.png
Terminal=true
Type=Application
Categories=Security;System;
Keywords=security;hacking;penetration;testing;
EOF
    
    success "Launcher created. Use 'hackingtool' command to start"
}

# Setup configuration
setup_config() {
    log "Setting up configuration..."
    
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$CONFIG_DIR/logs"
    mkdir -p "$CONFIG_DIR/wordlists"
    mkdir -p "$CONFIG_DIR/payloads"
    
    cp config/default.conf "$CONFIG_DIR/config.conf"
    
    success "Configuration setup complete"
}

# Install additional tools
install_tools() {
    log "Installing additional hacking tools..."
    
    # Metasploit
    if ! command -v msfconsole &> /dev/null; then
        log "Installing Metasploit Framework..."
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfwrap
