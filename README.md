(Root Level)


# 🔥 HackingTool Pro

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/kartikey3205/hackingtool-pro)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/kartikey3205/hackingtool-pro?style=social)](https://github.com/kartikey3205/hackingtool-pro/stargazers)

> **The Ultimate All-in-One Hacking Suite - Reimagined & Supercharged**

![HackingTool Pro Banner](hackingtoolbanner.png)

## 🚀 What's New in v3.0.0

HackingTool Pro is a complete overhaul of the original hackingtool framework, featuring:

- **300+ Tools** across 20 categories (vs 185+ in original)
- **Modern Python 3.10+** architecture with async support
- **AI-Powered** tool recommendations and vulnerability analysis
- **Real-time Collaboration** with team sharing features
- **Cloud Integration** for AWS, Azure, and GCP security testing
- **Mobile App** companion for on-the-go access
- **Plugin System** for custom tool integration
- **Docker Support** with pre-configured containers
- **Web Dashboard** for remote management
- **API Access** for automation and scripting

## 👨‍💻 Inventor

**Kartikey Rai** - Cybersecurity Researcher & Developer

[![GitHub](https://img.shields.io/badge/GitHub-kartikey3205-black?logo=github)](https://github.com/kartikey3205)
[![Twitter](https://img.shields.io/badge/Twitter-@kartikeyrai-blue?logo=twitter)](https://twitter.com/kartikeyrai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-kartikeyrai-blue?logo=linkedin)](https://linkedin.com/in/kartikeyrai)

## 📋 Categories

| Category | Tools | Description |
|----------|-------|-------------|
| Information Gathering | 25+ | OSINT, reconnaissance, and data collection |
| Vulnerability Scanning | 30+ | Automated vulnerability detection |
| Exploitation | 35+ | Exploit frameworks and tools |
| Wireless Attacks | 20+ | WiFi, Bluetooth, and RF security |
| Forensics | 25+ | Digital forensics and investigation |
| Post Exploitation | 20+ | Persistence and lateral movement |
| Web Application | 25+ | Web app security testing |
| Password Attacks | 30+ | Password cracking and recovery |
| Sniffing & Spoofing | 25+ | Network traffic analysis |
| Reverse Engineering | 25+ | Binary analysis and malware research |
| Social Engineering | 20+ | Phishing and human factor testing |
| Reporting | 15+ | Report generation and management |
| Cloud Security | 25+ | AWS, Azure, GCP security |
| Active Directory | 25+ | AD enumeration and attacks |
| Mobile Security | 25+ | iOS and Android security |
| IoT Security | 15+ | Internet of Things security |
| Blockchain | 15+ | Smart contract auditing |
| Steganography | 20+ | Data hiding techniques |
| DDoS Testing | 15+ | Stress testing and mitigation |

## ⚡ Quick Start

### One-Line Installer
```bash
curl -sSL https://raw.githubusercontent.com/kartikey3205/hackingtool-pro/main/scripts/install.sh | sudo bash




⚡ Manual Installation
# Clone the repository
git clone https://github.com/kartikey3205/hackingtool-pro.git
cd hackingtool-pro
# Run setup
sudo python3 setup.py
# Launch
sudo python3 hackingtool.p


📜 Docker Installation

docker pull kartikey3205/hackingtool-pro:latest
docker run -it --rm --privileged kartikey3205/hackingtool-pro






🎯 Features
✅ 300+ Pre-installed Tools
✅ Auto-Installer for missing dependencies
✅ Tool Recommendations based on target
✅ Search & Filter with tags
✅ Favorites System for quick access
✅ History Tracking of executed commands
✅ Export Results to JSON, CSV, PDF
✅ Team Collaboration with shared workspaces
✅ Scheduled Scans with cron integration
✅ Notification System (Email, Slack, Discord)
✅ Proxy Support for all tools
✅ VPN Integration with kill switch
✅ Tor Support for anonymous operations
✅ Multi-language support (EN, ES, FR, DE, CN, JP)



📁 Repository Structure

hackingtool-pro/
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── FUNDING.yml
├── core/
│   ├── __init__.py
│   ├── framework.py
│   ├── database.py
│   ├── updater.py
│   ├── plugin_manager.py
│   └── config_manager.py
├── tools/
│   ├── __init__.py
│   ├── information_gathering/
│   │   ├── __init__.py
│   │   ├── nmap_wrapper.py
│   │   ├── theharvester.py
│   │   ├── recon_ng.py
│   │   ├── maltego.py
│   │   ├── spiderfoot.py
│   │   ├── osint_framework.py
│   │   ├── sherlock.py
│   │   ├── userrecon.py
│   │   ├── emailfinder.py
│   │   ├── infoga.py
│   │   └── seeker.py
│   ├── vulnerability_scanning/
│   │   ├── __init__.py
│   │   ├── nessus_wrapper.py
│   │   ├── openvas_wrapper.py
│   │   ├── nikto.py
│   │   ├── wpscan.py
│   │   ├── sqlmap_wrapper.py
│   │   ├── xsstrike.py
│   │   ├── commix.py
│   │   ├── joomscan.py
│   │   ├── droopescan.py
│   │   ├── nuclei.py
│   │   └── sn1per.py
│   ├── exploitation/
│   │   ├── __init__.py
│   │   ├── metasploit_wrapper.py
│   │   ├── beef.py
│   │   ├── setoolkit.py
│   │   ├── socialphish.py
│   │   ├── zphisher.py
│   │   ├── hiddeneye.py
│   │   ├── shellphish.py
│   │   ├── blackhydra.py
│   │   ├── hydra_wrapper.py
│   │   ├── john_wrapper.py
│   │   ├── hashcat_wrapper.py
│   │   ├── aircrack_ng.py
│   │   ├── wifite.py
│   │   ├── fluxion.py
│   │   ├── wifiphisher.py
│   │   ├── reaver.py
│   │   ├── pixiewps.py
│   │   ├── bully.py
│   │   ├── routerspoit.py
│   │   └── camhackers.py
│   ├── wireless_attacks/
│   │   ├── __init__.py
│   │   ├── wifipumpkin3.py
│   │   ├── evilginx2.py
│   │   ├── bettercap.py
│   │   ├── wireshark_wrapper.py
│   │   ├── mdk3.py
│   │   ├── mdk4.py
│   │   ├── kismet.py
│   │   ├── horst.py
│   │   └── ghost.py
│   ├── forensics/
│   │   ├── __init__.py
│   │   ├── autopsy.py
│   │   ├── sleuthkit.py
│   │   ├── volatility.py
│   │   ├── foremost.py
│   │   ├── scalpel.py
│   │   ├── photorec.py
│   │   ├── binwalk.py
│   │   ├── exiftool.py
│   │   ├── pdfparser.py
│   │   ├── peepdf.py
│   │   └── rekall.py
│   ├── post_exploitation/
│   │   ├── __init__.py
│   │   ├── empire.py
│   │   ├── starkiller.py
│   │   ├── covenant.py
│   │   ├── pupy.py
│   │   ├── poshc2.py
│   │   ├── koadic.py
│   │   ├── dnscat2.py
│   │   ├── icmpsh.py
│   │   ├── gdog.py
│   │   └── trevorc2.py
│   ├── web_application/
│   │   ├── __init__.py
│   │   ├── burpsuite.py
│   │   ├── owasp_zap.py
│   │   ├── arachni.py
│   │   ├── w3af.py
│   │   ├── skipfish.py
│   │   ├── ratproxy.py
│   │   ├── paros.py
│   │   ├── vega.py
│   │   └── grendel_scan.py
│   ├── password_attacks/
│   │   ├── __init__.py
│   │   ├── hashcat.py
│   │   ├── john.py
│   │   ├── hydra.py
│   │   ├── medusa.py
│   │   ├── ncrack.py
│   │   ├── patator.py
│   │   ├── crunch.py
│   │   ├── cupp.py
│   │   ├── maskprocessor.py
│   │   ├── statsprocessor.py
│   │   ├── princeprocessor.py
│   │   ├── kwprocessor.py
│   │   ├── policygen.py
│   │   ├── pass_gen.py
│   │   └── passploit.py
│   ├── sniffing_spoofing/
│   │   ├── __init__.py
│   │   ├── wireshark.py
│   │   ├── tcpdump.py
│   │   ├── ettercap.py
│   │   ├── dsniff.py
│   │   ├── netsniff_ng.py
│   │   ├── driftnet.py
│   │   ├── urlsnarf.py
│   │   ├── webspy.py
│   │   ├── dnsspoof.py
│   │   ├── arpspoof.py
│   │   ├── macof.py
│   │   ├── msgsnarf.py
│   │   ├── mailsnarf.py
│   │   ├── sshmitm.py
│   │   ├── webmitm.py
│   │   ├── dnsspoof.py
│   │   ├── fragrouter.py
│   │   ├── sctpscan.py
│   │   ├── tcpreplay.py
│   │   └── fiked.py
│   ├── reverse_engineering/
│   │   ├── __init__.py
│   │   ├── ghidra.py
│   │   ├── radare2.py
│   │   ├── cutter.py
│   │   ├── binary_ninja.py
│   │   ├── ida_free.py
│   │   ├── apktool.py
│   │   ├── jadx.py
│   │   ├── dex2jar.py
│   │   ├── jd_gui.py
│   │   ├── procyon.py
│   │   ├── bytecode_viewer.py
│   │   ├── smali.py
│   │   ├── baksmali.py
│   │   ├── androguard.py
│   │   ├── quark_engine.py
│   │   └── mobsf.py
│   ├── social_engineering/
│   │   ├── __init__.py
│   │   ├── set.py
│   │   ├── gophish.py
│   │   ├── king_phisher.py
│   │   ├── evilginx2.py
│   │   ├── modlishka.py
│   │   ├── credsniper.py
│   │   ├── pwned.py
│   │   ├── breach_parser.py
│   │   ├── linkedint.py
│   │   ├── twint.py
│   │   ├── instaloader.py
│   │   ├── osrframework.py
│   │   └── phishingkit_tracker.py
│   ├── reporting/
│   │   ├── __init__.py
│   │   ├── dradis.py
│   │   ├── faraday.py
│   │   ├── defectdojo.py
│   │   ├── serpico.py
│   │   ├── ghostwriter.py
│   │   ├── pwndoc.py
│   │   ├── vulnreport.py
│   │   ├── archerysec.py
│   │   └── redefense.py
│   ├── cloud_security/
│   │   ├── __init__.py
│   │   ├── scout_suite.py
│   │   ├── prowler.py
│   │   ├── pacu.py
│   │   ├── cloudsploit.py
│   │   ├── cloudmapper.py
│   │   ├── cloudgoat.py
│   │   ├── flaws.py
│   │   ├── iam_escalation.py
│   │   ├── s3scanner.py
│   │   ├── s3recon.py
│   │   ├── bucket_finder.py
│   │   ├── slurp.py
│   │   ├── cloud_enum.py
│   │   ├── aws_inventory.py
│   │   ├── gcp_scanner.py
│   │   └── azure_hound.py
│   ├── active_directory/
│   │   ├── __init__.py
│   │   ├── bloodhound.py
│   │   ├── sharphound.py
│   │   ├── impacket.py
│   │   ├── crackmapexec.py
│   │   ├── powerview.py
│   │   ├── powermad.py
│   │   ├── powermap.py
│   │   ├── rubeus.py
│   │   ├── certipy.py
│   │   ├── certifried.py
│   │   ├── krbrelayx.py
│   │   ├── ntlmrelayx.py
│   │   ├── mitm6.py
│   │   ├── responder.py
│   │   ├── inveigh.py
│   │   ├── ldapdomaindump.py
│   │   ├── adidnsdump.py
│   │   ├── petitpotam.py
│   │   ├── printerbug.py
│   │   ├── dfscoerce.py
│   │   ├── shadowcoerce.py
│   │   └── sam_the_admin.py
│   ├── mobile_security/
│   │   ├── __init__.py
│   │   ├── mob_sf.py
│   │   ├── objection.py
│   │   ├── frida.py
│   │   ├── drozer.py
│   │   ├── qark.py
│   │   ├── androbugs.py
│   │   ├── apktool.py
│   │   ├── jadx.py
│   │   ├── dex2jar.py
│   │   ├── bytecode_viewer.py
│   │   ├── scrcpy.py
│   │   ├── android_backup_extractor.py
│   │   ├── libimobiledevice.py
│   │   ├── needle.py
│   │   ├── idb.py
│   │   ├── passionfruit.py
│   │   ├── ios_backup_tool.py
│   │   └── goios.py
│   ├── iot_security/
│   │   ├── __init__.py
│   │   ├── firmwalker.py
│   │   ├── binwalk_iot.py
│   │   ├── firmadyne.py
│   │   ├── attify.py
│   │   ├── routersploit.py
│   │   ├── exploitdb_search.py
│   │   ├── iotsecfuzz.py
│   │   ├── mirai_scanner.py
│   │   ├── shodan_api.py
│   │   ├── censys_api.py
│   │   ├── zoomeye_api.py
│   │   └── thingful_api.py
│   ├── blockchain/
│   │   ├── __init__.py
│   │   ├── mythril.py
│   │   ├── slither.py
│   │   ├── echidna.py
│   │   ├── manticore.py
│   │   ├── oyente.py
│   │   ├── securify.py
│   │   ├── maian.py
│   │   ├── solgraph.py
│   │   ├── solidity_scanner.py
│   │   └── ethploit.py
│   ├── steganography/
│   │   ├── __init__.py
│   │   ├── steghide.py
│   │   ├── stegseek.py
│   │   ├── zsteg.py
│   │   ├── stegsolve.py
│   │   ├── openstego.py
│   │   ├── outguess.py
│   │   ├── f5.py
│   │   ├── silenteye.py
│   │   ├── stegdetect.py
│   │   ├── stegextract.py
│   │   ├── pngcheck.py
│   │   ├── exiftool_steg.py
│   │   ├── mp3stego.py
│   │   └── wavsteg.py
│   └── ddos_attacks/
│       ├── __init__.py
│       ├── slowloris.py
│       ├── hping3.py
│       ├── t50.py
│       ├── nping.py
│       ├── thc_ssl_dos.py
│       ├── davoset.py
│       ├── rudy.py
│       ├── torhammer.py
│       ├── xerxes.py
│       ├── goldeneye.py
│       ├── hulk.py
│       ├── tor.py
│       └── anonymizer.py
├── scripts/
│   ├── install.sh
│   ├── setup.py
│   ├── requirements.txt
│   └── docker-compose.yml
├── tests/
│   ├── __init__.py
│   ├── test_framework.py
│   └── test_tools.py
├── docs/
│   ├── README.md
│   ├── INSTALL.md
│   ├── USAGE.md
│   ├── API.md
│   ├── CONTRIBUTING.md
│   ├── LICENSE
│   ├── CHANGELOG.md
│   ├── SECURITY.md
│   ├── CODE_OF_CONDUCT.md
│   ├── tools_documentation/
│   │   ├── information_gathering.md
│   │   ├── vulnerability_scanning.md
│   │   ├── exploitation.md
│   │   ├── wireless_attacks.md
│   │   ├── forensics.md
│   │   ├── post_exploitation.md
│   │   ├── web_application.md
│   │   ├── password_attacks.md
│   │   ├── sniffing_spoofing.md
│   │   ├── reverse_engineering.md
│   │   ├── social_engineering.md
│   │   ├── reporting.md
│   │   ├── cloud_security.md
│   │   ├── active_directory.md
│   │   ├── mobile_security.md
│   │   ├── iot_security.md
│   │   ├── blockchain.md
│   │   ├── steganography.md
│   │   └── ddos_attacks.md
│   └── screenshots/
├── config/
│   ├── default.conf
│   ├── tools.conf
│   └── themes/
│       ├── default.json
│       ├── dark.json
│       └── cyber.json
├── data/
│   ├── wordlists/
│   ├── payloads/
│   └── templates/
├── logs/
├── plugins/
├── hackingtool.py
└── Makefile


📊 Architecture
Architecture
┌─────────────────────────────────────────┐
│           Web Dashboard                 │
│      (React + WebSocket API)           │
└─────────────────────────────────────────┘
                   │
┌─────────────────────────────────────────┐
│         REST API Server                 │
│    (FastAPI + AsyncIO + Redis)         │
└─────────────────────────────────────────┘
                   │
┌─────────────────────────────────────────┐
│      Core Framework (Python 3.10+)      │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │ Plugin  │ │  Tool   │ │ Report  │ │
│  │ Manager │ │ Engine  │ │ Engine  │ │
│  └─────────┘ └─────────┘ └─────────┘ │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  │  AI/ML  │ │  Cloud  │ │  Team   │ │
│  │ Engine  │ │ Connect │ │ Collab  │ │
│  └─────────┘ └─────────┘ └─────────┘ │
└─────────────────────────────────────────┘
                   │
┌─────────────────────────────────────────┐
│         Tool Categories (300+)          │
└─────────────────────────────────────────┘
🛠️ System Requirements
Component	Minimum	Recommended
OS	Linux (Ubuntu 20.04+)	Kali Linux 2024+
Python	3.10	3.12
RAM	4 GB	16 GB
Storage	50 GB	200 GB SSD
Network	Broadband	High-speed
📚 Documentation
Installation Guide
Usage Guide
API Documentation
Contributing Guidelines
Tool Documentation
🤝 Contributing
We welcome contributions! Please see our Contributing Guidelines.

📜 License
This project is licensed under the MIT License - see the LICENSE file.

⚠️ Disclaimer
This tool is for educational and authorized testing purposes only. Users are responsible for complying with applicable laws. The developers assume no liability for misuse.

<p align="center"> Made with ❤️ by <a href="https://github.com/kartikey3205">Kartikey Rai</a> </p> <p align="center"> ⭐ Star this repo if you find it helpful! </p> ```
