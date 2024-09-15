[![Pylint](https://github.com/Attica-oss/container_iso_check/actions/workflows/pylint.yml/badge.svg)](https://github.com/Attica-oss/container_iso_check/actions/workflows/pylint.yml)
                                                                                
![logo6](https://github.com/user-attachments/assets/993d419a-ca09-41ad-85bf-a5c6288526ec)


---

# Container Number Validator

This project provides a simple tool for validating ISO container numbers, including SOC (Shipper Owned Containers). It ensures that container numbers conform to the required format and validates check digits according to the ISO 6346 standard. This implementation uses the [Polars](https://pola-rs.github.io/polars-book/user-guide/index.html) library for data handling and is intended for developers familiar with Python and Rust's `polars`.

## Features

- **Validate container numbers**: Ensure container numbers follow the correct pattern (4 letters, 6 digits, 1 check digit).
- **SOC (Shipper Owned Container) validation**: Validate SOC numbers using a predefined list of valid SOCs from a TOML file.
- **Check digit validation**: Verifies the check digit using ISO 6346 standards.
- **Support for Parquet files**: Reads container numbers from Parquet files using Polars.

## Requirements

- Python 3.7+
- [Poetry](https://python-poetry.org/) for managing dependencies
- Polars for efficient data handling
- TOML for configuration file handling

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Attica-oss/container_iso_check.git
   cd container_iso_check
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install all necessary dependencies.

## Dependencies

The project uses the following Python libraries:

- **Polars**: Efficient data frame library for Rust and Python (`polars`)
- **TOML**: Used for reading SOC numbers from a TOML file (`toml`)
- **re**: Regular expressions for container number format validation

You can find the list of dependencies in `pyproject.toml` managed by Poetry.

## Usage

### Command Line

Run the application using Python:

```bash
poetry run python /path/to/main.py
```

### Example: Validating Container Numbers

1. **Manual input**: You can input container numbers directly when prompted.

2. **Reading from a file**: By default, the tool looks for a Parquet file for container numbers, and it reads unique entries from the file.

3. **SOC Validation**: SOC numbers can be validated against a predefined list of SOCs in the `app/SOC.toml` file.

### Sample TOML File (app/SOC.toml)

```toml
[soc]
containers = ["XXXX1234567", "XXXX2345678"]
```

### Sample Python Code

To use the `ContainerValidator` class:

```python
from app.app import ContainerValidator

validator = ContainerValidator()
container_numbers = validator.read_input()  # Manually input or read from Parquet
validation_results = validator.validate_container_numbers(container_numbers)

print(validation_results)
```

This will output validation results for each container number.

### Expected Container Number Format

- **Standard format**: 4 letters, 6 digits, followed by a check digit (e.g., `ABCD1234567`).
- **SOC number**: Starts with `XXXX` followed by digits, validated against the TOML file.

## Testing

To run tests, make sure you have installed all dependencies and use:

```bash
poetry run pytest
```

## Contributing

If you'd like to contribute to this project, please follow the steps below:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push the changes to your fork.
5. Create a pull request.

## License

This project is licensed under the MIT License.

---

## Notes

- Ensure that the `app/SOC.toml` file contains valid SOC numbers for correct SOC validation.
- Container numbers must follow the ISO 6346 standard for validation to pass.


