import subprocess

# Filenames
input_file = "input.txt"
expected_output_file = "output.txt"
program_file = "e.py"  # Change this to the filename of your solution

# Run the program with input.txt as stdin
with open(input_file, "r") as inp, subprocess.Popen(
    ["python", program_file], stdin=inp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
) as proc:
    actual_output, error_output = proc.communicate()

# Read expected output
with open(expected_output_file, "r") as f:
    expected_output = f.read().strip()

# Clean actual output
actual_output = actual_output.strip()

# Compare outputs
if actual_output == expected_output:
    print("✅ Correct Output")
else:
    print("❌ Incorrect Output")
    print("\n🔹 Expected Output:")
    print(expected_output)
    print("\n🔹 Your Output:")
    print(actual_output)

# If there was an error, print it
if error_output:
    print("\n⚠️ Runtime Error:")
    print(error_output)
