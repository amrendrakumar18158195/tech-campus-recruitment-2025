import sys
import os
import zipfile

def extract_zip(zip_path, extract_to="extracted_logs"):
    """Extracts the zip file to a directory."""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    extracted_files = os.listdir(extract_to)
    for file in extracted_files:
        if file.endswith(".txt"):  # Assuming log file is a .txt file
            return os.path.join(extract_to, file)

    return None

def extract_logs(log_file, target_date, output_dir="output"):
    """Extracts log entries for a specific date from a large file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.startswith(target_date):  # Filter by date
                    outfile.write(line)

        print(f"Logs for {target_date} saved to {output_file}")
    except Exception as e:
        print(f"Error processing log file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_zip_file> <YYYY-MM-DD>")
        sys.exit(1)

    zip_file = sys.argv[1]
    target_date = sys.argv[2]

    log_file = extract_zip(zip_file)  # Extract the log file
    if log_file:
        extract_logs(log_file, target_date)
    else:
        print("No log file found in the zip archive.")
