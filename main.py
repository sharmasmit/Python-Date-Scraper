from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import pandas as pd
import argparse

@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None