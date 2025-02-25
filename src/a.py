import sys
import os
from datetime import datetime

def extract_logs_by_date(log_file, target_date, output_dir):
    """
    Extracts log entries for a specific date from a log file and saves them to a file.

    Args:
        log_file (str): Path to the log file.
        target_date (str): Date in the format 'YYYY-MM-DD'.
        output_dir (str): Path to the output directory.
    """
    extracted_logs = []
    try:
        with open(log_file, 'r') as file:
            for line in file:
                log_date = line[0:10]  # Extract date from log entry
                print (log_date)
                if log_date == target_date:
                    extracted_logs.append(line[10:])

    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    # Write logs to the output file
    if extracted_logs:
        with open(output_file, "w") as file:
            file.write("\n".join(extracted_logs))
        print(f"Logs for {target_date} saved to {output_file}")
    else:
        print(f"No logs found for {target_date}.")

def validate_date(date_str):
    """ Validates if the input date is in 'YYYY-MM-DD' format. """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    log_file = r"C:\Users\HP\Downloads\logs_2024.log\logs_2024.log"
    target_date = sys.argv[1]

    if not validate_date(target_date):
        print("Error: Invalid date format. Use 'YYYY-MM-DD'.")
        sys.exit(1)

    # Set output directory in the parent directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script location
    parent_dir = os.path.dirname(script_dir)  # Move to parent directory
    output_dir = os.path.join(parent_dir, "output")  # Create 'output/' in parent

    extract_logs_by_date(log_file, target_date, output_dir)
# "C:\Users\HP\Downloads\logs_2024.log\logs_2024.log"