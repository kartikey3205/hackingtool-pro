#!/usr/bin/env python3
"""
HackingTool Pro - Main Entry Point
Author: Kartikey Rai
GitHub: https://github.com/kartikey3205
Version: 3.0.0
"""

import sys
import os
import argparse
import asyncio
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))

from core.framework import HackingToolFramework
from core.config_manager import ConfigManager
from core.database import DatabaseManager
from core.updater import UpdateManager
from utils.logger import setup_logger
from utils.banner import display_banner

__author__ = "Kartikey Rai"
__version__ = "3.0.0"
__license__ = "MIT"
__github__ = "https://github.com/kartikey3205/hackingtool-pro"


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="HackingTool Pro - Ultimate Cybersecurity Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  sudo python3 hackingtool.py              # Interactive mode
  sudo python3 hackingtool.py --web        # Launch web dashboard
  sudo python3 hackingtool.py --api        # Start API server
  sudo python3 hackingtool.py --update     # Update all tools
  sudo python3 hackingtool.py --category 1 # Launch category directly
        """
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'HackingTool Pro v{__version__}'
    )
    
    parser.add_argument(
        '--web',
        action='store_true',
        help='Launch web dashboard'
    )
    
    parser.add_argument(
        '--api',
        action='store_true',
        help='Start API server'
    )
    
    parser.add_argument(
        '--update',
        action='store_true',
        help='Update all tools to latest versions'
    )
    
    parser.add_argument(
        '--category',
        type=int,
        metavar='N',
        help='Launch specific category by number (1-20)'
    )
    
    parser.add_argument(
        '--tool',
        type=str,
        metavar='NAME',
        help='Launch specific tool by name'
    )
    
    parser.add_argument(
        '--search',
        type=str,
        metavar='QUERY',
        help='Search for tools'
    )
    
    parser.add_argument(
        '--config',
        type=str,
        metavar='FILE',
        default='config/default.conf',
        help='Path to configuration file'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Skip banner display'
    )
    
    parser.add_argument(
        '--verbose', '-V',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    
    return parser.parse_args()


async def main():
    """Main entry point."""
    args = parse_arguments()
    
    # Setup logging
    logger = setup_logger(
        verbose=args.verbose,
        debug=args.debug
    )
    
    # Display banner
    if not args.no_banner:
        display_banner(version=__version__, author=__author__)
    
    # Initialize configuration
    config = ConfigManager(args.config)
    
    # Initialize database
    db = DatabaseManager(config.get('database'))
    
    # Handle command line options
    if args.update:
        updater = UpdateManager(config)
        await updater.update_all()
        return
    
    if args.web:
        from web.dashboard import launch_dashboard
        await launch_dashboard(config)
        return
    
    if args.api:
        from api.server import start_api_server
        await start_api_server(config)
        return
    
    # Initialize main framework
    framework = HackingToolFramework(config, db)
    
    if args.search:
        await framework.search_tools(args.search)
        return
    
    if args.tool:
        await framework.launch_tool(args.tool)
        return
    
    if args.category:
        await framework.launch_category(args.category)
        return
    
    # Interactive mode
    await framework.interactive_mode()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Fatal error: {e}")
        sys.exit(1)