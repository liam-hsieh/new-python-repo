#!/usr/bin/env python3
"""Configuration reader for project settings."""

import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    # Python < 3.11
    try:
        import toml as tomllib
    except ImportError:
        print("Error: tomllib/tomli not available. Please install tomli for Python < 3.11")
        sys.exit(1)

def read_config():
    """Read project configuration from project.toml."""
    config_path = Path("project.toml")
    
    if not config_path.exists():
        print("Warning: project.toml not found, using defaults")
        return {
            "documentation": {
                "github_pages_enabled": True,
                "build_on_push": True,
                "build_strict": True
            },
            "project": {
                "auto_generate_api_docs": True,
                "include_demo_apps": True
            }
        }
    
    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
        return config
    except Exception as e:
        print(f"Error reading project.toml: {e}")
        sys.exit(1)

def check_github_pages_enabled():
    """Check if GitHub Pages deployment is enabled."""
    config = read_config()
    return config.get("documentation", {}).get("github_pages_enabled", True)

if __name__ == "__main__":
    config = read_config()
    
    # Check what user wants to know
    if len(sys.argv) > 1:
        if sys.argv[1] == "github_pages":
            enabled = check_github_pages_enabled()
            print("true" if enabled else "false")
        elif sys.argv[1] == "show":
            import json
            print(json.dumps(config, indent=2))
    else:
        print("Usage: python check_config.py [github_pages|show]")
        print("  github_pages: Check if GitHub Pages is enabled")
        print("  show: Display full configuration")