#!/bin/bash

start_port=1
end_port=65535
timeout=2
parallel_jobs=50
csv_file="connected_ports_gen1.csv"

# Remove the file if it exists
if [ -f "$csv_file" ]; then
  rm "$csv_file"
fi

# Create the header of the CSV file
echo "Port" > "$csv_file"

# Function to test a single port
test_port() {
  local port=$1
  local status=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout $timeout -m 5 "http://portquiz.net:$port")

  # If the status is not 0 (timeout), write the result to the CSV file
  if [ "$status" != "0" ]; then
    echo "$port" >> "$csv_file"
  fi

  # Print the result
  echo "Port $port: $status"
}

# Loop through the ports
for port in $(seq $start_port $end_port); do
  # Test the current port in a background process
  test_port "$port" &

  # If the number of parallel jobs reached the limit, wait for one to finish
  if [ $(jobs -p | wc -l) -ge $parallel_jobs ]; then
    # Wait for one background job to finish
    wait $(jobs -p | head -n 1)
  fi
done

# Wait for all background jobs to finish
wait
