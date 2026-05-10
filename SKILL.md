---
name: tell-ai-about-yourself
description: 'Build a comprehensive user profile to personalize all AI responses. Use when: setting up new workspace, updating personal context, or refreshing preferences. Collects info about who you are, profession, current goals, challenges, preferences, and work style. Stores securely in /memories/ for persistent cross-session reference.'
argument-hint: 'Optional: setup | view | edit'
user-invocable: true
---

# Tell AI About Yourself

Create a comprehensive personal profile that guides all AI responses. This skill enables any AI assistant to provide tailored advice based on your background, goals, challenges, and preferences.

## When to Use

- **Session start**: First time in a new workspace
- **Onboarding**: Getting the AI to understand your context
- **Updates**: Refreshing preferences or adding new information
- **Troubleshooting**: When responses don't match your needs

## What Gets Collected

Your profile includes:

| Category | Examples |
|----------|----------|
| **Who You Are** | Name, background, expertise level, experience years |
| **Profession & Role** | Job title, industry, team size, responsibilities |
| **Current Work** | Project name, tech stack, deliverables, timeline |
| **Challenges** | Technical obstacles, time constraints, knowledge gaps |
| **Goals** | Short-term objectives, learning targets, career goals |
| **Preferences** | Communication style, code style, documentation preference |
| **Context** | Team environment, constraints, best practices |

## Workflow

### Option 1: Interactive Setup (Recommended)

1. Run the skill (invoke `/tell-ai-about-yourself` command or run the setup script)
2. Answer guided questions
3. Review and confirm your profile
4. Profile saves to `/memories/user-profile.md`

### Option 2: YAML Configuration

1. Copy the [template](./references/preferences-template.yaml)
2. Edit manually with your information
3. Save to `/memories/user-profile.yaml`
4. AI will parse and apply it automatically

### Option 3: View/Edit Existing Profile

- **View**: Use `/tell-ai-about-yourself view` to see current profile
- **Edit**: Use `/tell-ai-about-yourself edit` to update specific sections

## How AI Uses Your Profile

Once your profile exists in `/memories/`:

- **Every response** is filtered through your preferences
- **Code examples** match your preferred style and language
- **Explanations** adjust to your experience level
- **Recommendations** consider your constraints and goals
- **Communication** adapts to your stated preferences

## Key Benefits

✅ **Consistent context** across sessions  
✅ **Personalized advice** aligned with your role  
✅ **Better problem-solving** with goal awareness  
✅ **Time savings** by avoiding context re-explanation  
✅ **Privacy first** - stored locally in your workspace  

## Technical Details

- **Storage**: `/memories/user-profile.md` (Markdown) or `/memories/user-profile.yaml` (YAML)
- **Privacy**: Files only readable by you on your machine
- **Format**: Plain text, version-control friendly
- **Frequency**: Read once per session, can be updated anytime

## Troubleshooting

| Issue | Solution |
|-------|----------|
| AI not using my profile | Check file exists at `/memories/user-profile.md` or `.yaml` |
| Need to add more info | Run `/tell-ai-about-yourself edit` to add sections |
| Want to reset | Delete `/memories/user-profile.md` and run skill again |
| Conflicts between profile settings | Edit the file directly to resolve |

## Examples

### Try This

After creating your profile, ask:
- "What's the best next step for my [project name]?"
- "Review this code with my preferences in mind"
- "Suggest learning resources for my skill gap: [gap]"
- "Help me plan my [goal], considering my constraints"

The AI will reference your profile automatically to give better responses.
