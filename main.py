"""Entry point for the application."""
from app import iso_check
import polars as pl


def main():
    """Main entry point for the application."""
    # Example usage
    validator = iso_check.ContainerValidator()

    choice: int = int(
        input("Enter '1' to check ISOs or '2' to check ISOs in a file: "))
    try:
        if choice == 1:
            container_numbers = validator.read_input()
            results = validator.validate_container_numbers(container_numbers)
            for number, is_valid in results.items():
                print(f"Container Number: {number}, Valid: {is_valid}")
        elif choice == 2:
            container_numbers = validator.read_input(
                file_path="app/container_numbers.txt")
            results = validator.validate_container_numbers(container_numbers)
            for number, is_valid in results.items():
                if not is_valid:
                    print(f"Container Number: {number}, Valid: {is_valid}")
                # print(f"all okay: {number}")
            print("okay")
        else:
            print("Invalid choice. Please enter '1' or '2'.")
    except ValueError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
