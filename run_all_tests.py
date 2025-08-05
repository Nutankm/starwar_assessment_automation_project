import os
import pytest
from datetime import datetime

# Create reports directory if it doesn't exist
os.makedirs("reports", exist_ok=True)


# Get timestamp for unique report filenames
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# UI Test Run
print("=== Running UI Tests ===")
pytest.main([
    "-m", "ui",
    f"--html=reports/ui_report_{timestamp}.html",
    "--self-contained-html"
])

# API Test Run
print("=== Running API Tests ===")
pytest.main([
    "-m", "api",
    f"--html=reports/api_report_{timestamp}.html",
    "--self-contained-html"
])
