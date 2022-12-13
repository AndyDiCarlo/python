import time

while True:
  # Get the current time
  current_time = time.strftime('%H:%M:%S')

  # Clear the screen
  print('\033[2J\033[H', end='')

  # Print the time
  print(current_time)

  # Wait one second
  time.sleep(1)
