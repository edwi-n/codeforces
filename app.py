import requests
import json
import sys

def fetch_url(url, timeout=30):
    """Fetch data from a URL and display the result"""
    try:
        print(f"Fetching from: {url}")
        
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        # Parse as JSON
        try:
            json_data = response.json()
            return json_data
        except json.JSONDecodeError:
            # Not JSON, show text
            return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    
    handle = "edwin"
    url = f"https://codeforces.com/api/user.status?handle={handle}"
        
    result = fetch_url(url, timeout=30)
    
    # If its json, parse info
    if isinstance(result, dict) and result.get('status') == 'OK':
        submissions = result.get('result', [])
        print(f"\nFetched {len(submissions)} submissions")
        
        if submissions:
            solved_problems = set()
            for submission in submissions:
                if submission.get('verdict') == 'OK':
                    problem = submission.get('problem', {})
                    problem_id = f"{problem.get('contestId')}{problem.get('index')}"
                    solved_problems.add(problem_id)
            print(f"Unique problems solved: {len(solved_problems)}")
    elif result:
        print(f"\n✓ Successfully fetched data from URL")
