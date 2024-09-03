"""Shipper Owned Containers which does not pass the check"""
from pathlib import Path
import polars as pl
import toml

soc_file:Path = Path("/home/gmoun/Project/container_iso_check/app/SOC.toml")

def read_soc_file()->list[str]:
    """Read the config file

    Returns:
        list[str]: list of containers
    """
    with open(soc_file, 'r',encoding='utf-8') as f:
        return toml.load(f)["soc"]["containers"]

def list_to_series(containers:list[str])->pl.Series:
    """Convert list to series"""
    return pl.Series(containers)

def soc_series()->pl.Series:
    """SOC check

    Returns:
        pl.Series: list of containers
    """
    return list_to_series(read_soc_file())
