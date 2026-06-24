#!/bin/bash

# CI Test Runner Script
# Activates the virtual environment, runs the test suite, and returns appropriate exit code.

set -e  # Exit immediately if any command fails

echo "========================================="
echo "  Soul Foods - Dash App CI Test Runner   "
echo "========================================="

# Step 1: Activate the virtual environment
echo ""
echo "[1/3] Activating virtual environment..."

# Support both Linux/macOS and Windows (Git Bash) virtual environment paths
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "ERROR: Virtual environment not found."
    echo "Please run 'python -m venv venv && pip install -r requirements.txt' first."
    exit 1
fi

echo "Virtual environment activated."

# Step 2: Run the test suite using pytest
echo ""
echo "[2/3] Executing test suite with pytest..."
echo "-----------------------------------------"

pytest test_app.py -v

# Step 3: Capture exit code and return it
TEST_EXIT_CODE=$?

echo "-----------------------------------------"
echo ""
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "[3/3] All tests PASSED. Exit code: 0"
    exit 0
else
    echo "[3/3] One or more tests FAILED. Exit code: 1"
    exit 1
fi
