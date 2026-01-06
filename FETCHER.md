# Fetcher

This script fetches your Codeforces submission data using the Codeforces API and automatically updates the [README.md](README.md) with a table of all solved problems.

## Features

- Fetches all submissions from Codeforces API
- Extracts only accepted (OK) submissions
- Removes duplicate problems (keeps last accepted submission)
- Displays problems (newest first)
- Shows total count of problems solved
- Generates a formatted table with:
  - Problem number (Contest ID + Index)
  - Problem name
  - Difficulty rating
  - Topic tags
  - Link to your submission

## Setup

1. Install required dependencies:
```bash
pip install requests
```

2. Set your Codeforces handle as an environment variable:
```bash
export CODEFORCES_HANDLE=your_username
```

## Usage

Run the script to update your README:
```bash
python3 app.py
```

The script will:
1. Fetch all your submissions from Codeforces
2. Filter for accepted solutions
3. Update the README.md with a table of problems

## Example Output

```markdown
## Solutions

Total problems solved: **489**

| # | Problem Name | Rating | Tags | Solution |
|--------|--------------|--------|------|----------|
| 2050F | Maximum modulo equality | 1700 | data structures, math | [Link](...) |
| 1955E | Long Inversions | 1700 | brute force, greedy | [Link](...) |
```

## API Information

The script uses the Codeforces API endpoint:
- `https://codeforces.com/api/user.status?handle={handle}`

For more information about the Codeforces API, visit: https://codeforces.com/apiHelp
