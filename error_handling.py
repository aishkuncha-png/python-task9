import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers():
    try:
        # Taking user input
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2

    except ZeroDivisionError as e:
        logging.error("Division by zero error", exc_info=True)
        print("❌ Error: You cannot divide by zero.")

    except ValueError as e:
        logging.error("Invalid input entered", exc_info=True)
        print("❌ Error: Please enter valid integers only.")

    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("❌ Error: Something went wrong.")

    else:
        print(f"✅ Result: {result}")

    finally:
        print("🔚 Program execution completed.")

# Run function
divide_numbers()
