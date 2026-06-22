#!/usr/bin/env bash

# Initialize variables
TOTAL_POINTS=2
POINTS=0

# Check for the term "MarkMonitor"
if [[ $CODIO_FREE_TEXT_ANSWER == *"MarkMonitor"* ]]; then
    POINTS=$((POINTS + 2))
else
    echo "❌ You did not specify the correct name. "
fi

# If term was found, set the feedback buffer to "Your answer has passed"
if [ $POINTS -eq $TOTAL_POINTS ]; then
    echo "✅ Your answer has passed."
    exit 0
fi

exit 1;