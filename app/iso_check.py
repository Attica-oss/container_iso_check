"""iso check for container numbers"""
from pathlib import Path
import re

import polars as pl

import toml


class ContainerValidator:
    """
    Initializes a new instance of the ContainerValidator class.
    
    This is a special method that is automatically 
    called when an object of this class is instantiated.
    
    It does not take any parameters and does not return any value.
    """

    SOC_FILE: Path = Path("app/SOC.toml")

    def __init__(self):
        pass

    def read_input(self, file_path=None):
        """Read input from a file or user input."""
        if file_path:
            container_numbers = pl.read_parquet("transfer.parquet").to_series().unique().to_list()
            # with open(file_path, "r", encoding="utf-8") as file:
            #     container_numbers = file.readlines()
            return [number.strip() for number in container_numbers]
        container_numbers = input(
            "Enter container numbers separated by commas: ").split(',')
        return [number.strip() for number in container_numbers]

    def read_toml_file(self, file_path=SOC_FILE) -> list[str]:
        """Read TOML file and return the container numbers"""
        with open(file_path, "r", encoding="utf-8") as file:
            data = toml.load(file)
        return data['soc']['containers']

    def validate_container_number(self, container_number):
        """Regular expression to match the format: 4 letters, 6 digits, 1 digit"""
        pattern = re.compile(r'^[A-Z]{4}[0-9]{6}[0-9]$')

        try:
            # Check if it's an SOC number
            if container_number.startswith("XXXX"):
                return self.validate_soc_number(container_number)

            # Check if the container number is 11 characters long
            if len(container_number) != 11:
                raise ValueError(
                    f"Container number '{container_number}' is not 11 characters long."
                )

            # Check if the container number matches the pattern
            if not pattern.match(container_number):
                raise ValueError(
                    f"Container number '{container_number}' does not match the required format."
                )

            # Validate the check digit
            if not self.validate_check_digit(container_number):
                raise ValueError(
                    f"""Container number '{container_number}' has an invalid check digit."""
                )

            return True

        except ValueError as e:
            print(e)
            return False

    def validate_soc_number(self, container_number: str) -> bool:
        """Validate SOC number
        Assuming SOC numbers have a specific format,
        for e.g., starting with "XXXX" followed by digits
        """
        soc_pattern = re.compile(r'^XXXX[0-9]+$')

        if not soc_pattern.match(container_number):
            raise ValueError(
                f"SOC number '{container_number}' does not match the required format."
            )

        if container_number not in self.read_toml_file():
            raise ValueError(
                f"SOC number '{container_number}' is not in the list of valid SOC numbers."
            )

        return True

    def validate_check_digit(self, container_number) -> bool:
        """Calculate the check digit according to the ISO 6346 standard"""
        value_map: dict[str, int] = {
            'A': 10,
            'B': 12,
            'C': 13,
            'D': 14,
            'E': 15,
            'F': 16,
            'G': 17,
            'H': 18,
            'I': 19,
            'J': 20,
            'K': 21,
            'L': 23,
            'M': 24,
            'N': 25,
            'O': 26,
            'P': 27,
            'Q': 28,
            'R': 29,
            'S': 30,
            'T': 31,
            'U': 32,
            'V': 34,
            'W': 35,
            'X': 36,
            'Y': 37,
            'Z': 38
        }

        total_sum = 0
        for i in range(10):
            if i < 4:
                total_sum += value_map[container_number[i]] * (2**i)
            else:
                total_sum += int(container_number[i]) * (2**i)

        check_digit = total_sum % 11
        check_digit = check_digit % 10  # Modulo 10 to get the check digit

        return check_digit == int(container_number[10])

    def validate_container_numbers(self, container_numbers):
        """Validate container numbers."""
        results = {}
        for number in container_numbers:
            results[number] = self.validate_container_number(number)
        return results
