#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from pathlib import Path

def setup_logging(log_level: str = "INFO") -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Infra-Terraform Management Tool")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.yaml"),
        help="Path to configuration file",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level",
    )
    return parser.parse_args()

def main() -> None:
    """Main entry point for the application."""
    args = parse_args()
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    try:
        logger.info(f"Starting Infra-Terraform with config: {args.config}")
        # Main application logic would go here
        logger.info("Infra-Terraform completed successfully")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()