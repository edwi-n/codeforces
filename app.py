import requests
import json
import os
import sys

def fetch_url(url, timeout=30):
    """Fetch data from a URL and display the result"""
    try:
        print(f"Fetching from: {url}")
        
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        
        try:
            json_data = response.json()
            return json_data
        except json.JSONDecodeError:
            return response.text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    
    # Get handle from environment variable
    handle = os.getenv('CODEFORCES_HANDLE')
    
    if not handle:
        print("Error: CODEFORCES_HANDLE environment variable is not set")
        print("Usage: export CODEFORCES_HANDLE=your_username")
        sys.exit(1)
    
    url = f"https://codeforces.com/api/user.status?handle={handle}"
        
    result = fetch_url(url, timeout=30)
    
    if isinstance(result, dict) and result.get('status') == 'OK':
        submissions = result.get('result', [])
        print(f"Fetched {len(submissions)} submissions")
        
        if submissions:
            solved_problems = set()
            problem_info = []
            for submission in submissions:
                if submission.get('verdict') == 'OK':
                    problem = submission.get('problem', {})
                    problem_id = f"{problem.get('contestId')}{problem.get('index')}"
                    if problem_id not in solved_problems:
                        solved_problems.add(problem_id)
                        contest_id = problem.get('contestId')
                        problem_index = problem.get('index')
                        problem_name = problem.get('name')
                        rating = problem.get('rating', 'N/A')
                        tags = ', '.join(problem.get('tags', []))
                        solution_link = f"https://codeforces.com/contest/{contest_id}/submission/{submission.get('id')}"
                        problem_info.append([contest_id, problem_index, problem_name, rating, tags, solution_link])
            
            # Reverse problem submissions so that the latest submitted is at the top
            reversed(problem_info)

            # Read current README
            with open('README.md', 'r') as f:
                lines = f.readlines()
            
            # Find the ## Solutions line
            solutions_idx = -1
            for i, line in enumerate(lines):
                if line.strip() == '## Solutions':
                    solutions_idx = i
                    break
            
            if solutions_idx != -1:
                # Keep everything up to ## Solutions
                new_lines = lines[:solutions_idx + 1]
                
                # Add total count
                new_lines.append(f"\nTotal problems solved: **{len(problem_info)}**\n\n")
                
                # Add table header
                new_lines.append("| # | Problem Name | Rating | Tags | Solution |\n")
                new_lines.append("|--------|--------------|--------|------|----------|\n")
                
                # Add problem rows
                for idx, (contest_id, problem_index, name, rating, tags, solution) in enumerate(problem_info, 1):
                    problem_num = f"{contest_id}{problem_index}"
                    solution_md = f"[Link]({solution})"
                    new_lines.append(f"| {problem_num} | {name} | {rating} | {tags} | {solution_md} |\n")
                
                # Write back to README
                with open('README.md', 'w') as f:
                    f.writelines(new_lines)
                
                print(f"\nUpdated README.md with {len(problem_info)} problems")
            else:
                print("Could not find ## Solutions in README.md")
    elif result:
        print(f"\n✓ Successfully fetched data from URL")
