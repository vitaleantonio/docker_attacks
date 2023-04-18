#!/bin/sh

# Define a function to find and kill the Firefox process
kill_firefox() {
  sleep 30
  firefox_pid=$(pgrep firefox)
  kill $firefox_pid
}

# Execute the `kill_firefox` function in the background and store its process ID
kill_firefox &
kill_firefox_pid=$!

# Wait for the `kill_firefox` function to complete and clean up the background process
wait $kill_firefox_pid
