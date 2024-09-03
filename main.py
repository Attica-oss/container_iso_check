"""Entry point for the application."""
from app import iso_check

def main():
    """Main entry point for the application."""
    # Example usage
    validator = iso_check.ContainerValidator()
    container_numbers = validator.read_input(file_path="app/container_numbers.txt")
    results = validator.validate_container_numbers(container_numbers)
    for number, is_valid in results.items():
        print(f"Container Number: {number}, Valid: {is_valid}")


if __name__ == "__main__":
    main()
