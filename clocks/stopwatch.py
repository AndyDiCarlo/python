import time

print("Press Enter to start the stopwatch, and then press Enter again to stop it.")

# Start the stopwatch
input()
start_time = time.time()

# Stop the stopwatch
input()
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Elapsed time: {elapsed_time:.2f} seconds")