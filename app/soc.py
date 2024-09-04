"""Shipper Owned Containers which does not pass the check"""
from pathlib import Path
import polars as pl
import toml

soc_file: Path = Path("/home/gmoun/Project/container_iso_check/app/SOC.toml")


def add_soc_file(container_number) -> None:
    """Read the config file

    Returns:
        list[str]: list of containers
    """
    container_number = input("Enter container number: ")
    with open(soc_file, "r", encoding="utf-8") as file:
        data = toml.load(file)
            
    with open(soc_file, "+a", encoding='utf-8') as f:
        return toml.dump(f)["soc"]["containers"]


def list_to_series(containers: list[str]) -> pl.Series:
    """Convert list to series"""
    return pl.Series(containers)


def soc_series() -> pl.Series:
    """SOC check

    Returns:
        pl.Series: list of containers
    """
    return list_to_series(read_soc_file())
