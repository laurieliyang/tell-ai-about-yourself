#!/usr/bin/env python3
"""
Interactive user profile setup for Tell AI About Yourself
Guides users through questions and generates user-profile.md
"""

import os
import json
from datetime import datetime
from pathlib import Path


def get_memories_path():
    """Get the /memories/ directory path"""
    # Try common locations
    possible_paths = [
        Path.home() / ".memories",
        Path.home() / ".ai" / "memories",
        Path.home() / ".claude" / "memories",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    # Create .memories in home directory as default
    default_path = Path.home() / ".memories"
    default_path.mkdir(parents=True, exist_ok=True)
    return default_path


def get_answer(question, options=None, default=None):
    """Get user input with optional list of choices"""
    if options:
        print(f"\n{question}")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        while True:
            try:
                choice = int(input("Your choice (number): ").strip())
                if 1 <= choice <= len(options):
                    return options[choice - 1]
            except ValueError:
                pass
            print("Invalid choice, try again.")
    else:
        hint = f" [default: {default}]" if default else ""
        answer = input(f"\n{question}{hint}\n> ").strip()
        return answer or default


def get_list_input(prompt):
    """Get multiple items from user"""
    print(f"\n{prompt}")
    print("(Enter items one per line, empty line to finish)")
    items = []
    while True:
        item = input("> ").strip()
        if not item:
            break
        items.append(item)
    return items


def generate_markdown_profile(answers):
    """Generate Markdown format profile"""
    content = f"""# My AI Profile

*Created: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

## About Me

- **Name**: {answers.get('name', 'Not specified')}
- **Background**: {answers.get('background', 'Not specified')}
- **Experience Level**: {answers.get('experience_level', 'Not specified')} years in field

## Current Role

- **Job Title**: {answers.get('job_title', 'Not specified')}
- **Industry**: {answers.get('industry', 'Not specified')}
- **Team Size**: {answers.get('team_size', 'Not specified')}

## What I'm Working On

- **Project**: {answers.get('project_name', 'Not specified')}
- **Description**: {answers.get('project_description', 'Not specified')}
- **Tech Stack**: {', '.join(answers.get('tech_stack', []))}
- **Timeline**: {answers.get('timeline', 'Not specified')}

## My Goals

### Short-term
{chr(10).join(f"- {goal}" for goal in answers.get('short_term_goals', []))}

### Medium-term
{chr(10).join(f"- {goal}" for goal in answers.get('medium_term_goals', []))}

### Learning Targets
{chr(10).join(f"- {goal}" for goal in answers.get('learning_targets', []))}

## Current Challenges

{chr(10).join(f"- {challenge}" for challenge in answers.get('challenges', []))}

## My Preferences

- **Communication Style**: {answers.get('communication_style', 'balanced')}
  - Direct and concise
  - Detailed explanations
  - Conversational tone
  
- **Code Examples**: {answers.get('code_examples', 'Include examples')}

- **Detail Level**: {answers.get('detail_level', 'balanced')}
  - High-level overview
  - Balanced mix
  - Deep technical dive
  
- **Primary Language**: {answers.get('primary_language', 'JavaScript')}

- **Code Style**: {answers.get('code_style', 'Clean and readable')}

## Things I Like

{chr(10).join(f"- {item}" for item in answers.get('likes', []))}

## Things I Dislike

{chr(10).join(f"- {item}" for item in answers.get('dislikes', []))}

## Additional Notes

{answers.get('additional_notes', 'None')}

---
*This profile helps AI provide personalized, contextual assistance. Update it anytime using `/tell-ai-about-yourself edit`*
"""
    return content


def main():
    print("=" * 60)
    print("Tell AI About Yourself - Interactive Setup")
    print("=" * 60)
    print("\nI'll ask you some questions to build your AI profile.")
    print("(Skip any question by pressing Enter)\n")
    
    answers = {}
    
    # Personal Info
    print("\n--- Personal Information ---")
    answers['name'] = get_answer("What's your name?")
    answers['background'] = get_answer("Brief background about yourself?")
    answers['experience_level'] = get_answer("Years of professional experience?")
    
    # Professional
    print("\n--- Professional Info ---")
    answers['job_title'] = get_answer("Your job title?")
    answers['industry'] = get_answer("Industry you work in?")
    answers['team_size'] = get_answer("Your team size?")
    
    # Current Work
    print("\n--- Current Work ---")
    answers['project_name'] = get_answer("What project are you working on?")
    answers['project_description'] = get_answer("Brief project description?")
    answers['tech_stack'] = get_list_input("What technologies do you use? (list each)")
    answers['timeline'] = get_answer("Project timeline/deadline?")
    
    # Goals
    print("\n--- Your Goals ---")
    answers['short_term_goals'] = get_list_input("Short-term goals (this month/quarter)?")
    answers['medium_term_goals'] = get_list_input("Medium-term goals (next 6-12 months)?")
    answers['learning_targets'] = get_list_input("What do you want to learn?")
    
    # Challenges
    answers['challenges'] = get_list_input("What challenges are you facing?")
    
    # Preferences
    print("\n--- Your Preferences ---")
    answers['communication_style'] = get_answer(
        "How do you prefer responses?",
        options=["Direct and concise", "Detailed explanations", "Conversational"]
    )
    answers['code_examples'] = get_answer(
        "Do you want code examples?",
        options=["Yes, include examples", "Minimal code", "Comprehensive walkthroughs"]
    )
    answers['detail_level'] = get_answer(
        "Preferred detail level?",
        options=["High-level overview", "Balanced", "Deep technical dive"]
    )
    answers['primary_language'] = get_answer("Primary programming language?")
    answers['code_style'] = get_answer("Your preferred code style?")
    
    # Likes/Dislikes
    print("\n--- What You Like/Dislike ---")
    answers['likes'] = get_list_input("Things you like (in code, work style, etc)?")
    answers['dislikes'] = get_list_input("Things you dislike?")
    
    # Additional
    answers['additional_notes'] = get_answer("Any other context for the AI?")
    
    # Generate and save
    profile_content = generate_markdown_profile(answers)
    
    memories_path = get_memories_path()
    profile_file = memories_path / "user-profile.md"
    
    try:
        with open(profile_file, 'w') as f:
            f.write(profile_content)
        
        print("\n" + "=" * 60)
        print("✅ Profile Created Successfully!")
        print("=" * 60)
        print(f"\nSaved to: {profile_file}")
        print("\nYour profile is ready! Try asking the AI:")
        print('  "Based on my profile, what should I do next?"')
        print('  "Review this code with my preferences in mind"')
        print("\nTo edit: /tell-ai-about-yourself edit")
        print("To view: /tell-ai-about-yourself view")
        
    except Exception as e:
        print(f"\n❌ Error saving profile: {e}")
        print("Profile content (save manually):")
        print(profile_content)


if __name__ == "__main__":
    main()
