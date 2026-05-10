# Usage Guide for Tell AI About Yourself

## Getting Started

### Step 1: Create Your Profile

Choose one of three approaches:

#### **Method A: Interactive (Simplest)**
```bash
# Run the setup script:
python3 setup-profile.py
```
Answer the guided questions and your profile saves automatically to `/memories/user-profile.md`.

#### **Method B: YAML Configuration**
1. Copy [preferences-template.yaml](./preferences-template.yaml)
2. Fill in your information
3. Save as `/memories/user-profile.yaml`

#### **Method C: Manual Markdown**
Create `/memories/user-profile.md` with sections like:
```markdown
# My Profile

## About Me
- Name: John Doe
- Background: 5 years as a Full Stack Engineer

## Current Work
- Project: Migration to microservices
- Tech: Node.js, Docker, Kubernetes
- Goal: Complete by Q3 2026

## Preferences
- Code style: Airbnb ESLint
- Detail level: Balanced (not too verbose)
- Learning style: Hands-on with examples
```

### Step 2: Verify It Works

Ask the AI:
```
"Based on my profile, what's the best next step?"
```

The AI should reference information from your profile in its response.

### Step 3: Update As Needed

Use `/tell-ai-about-yourself edit` to update sections or create a new profile.

## File Locations

Your profile is stored **locally** (not synced):
- Markdown: `/memories/user-profile.md`
- YAML: `/memories/user-profile.yaml`
- Both can coexist; AI reads whichever format is available

## What Information to Include

### Essential (Start Here)
- [ ] Your role/job title
- [ ] What you're currently working on
- [ ] Your main goal for this project/quarter
- [ ] One key preference (e.g., code style, explanation depth)

### Important (Add Next)
- [ ] Your experience level
- [ ] Tech stack you use
- [ ] Team size/structure
- [ ] Communication preferences

### Nice to Have
- [ ] Languages you know
- [ ] Learning targets
- [ ] Specific constraints
- [ ] Things you like/dislike about code

## Privacy & Security

✅ **Your profile stays on your machine**  
✅ **Not synced to cloud by default**  
✅ **Only readable by you and AI in your session**  
✅ **You control what information is included**  

## Troubleshooting

### Profile Not Being Used?
1. Check file exists: `ls ~/.memories/user-profile.*`
2. Verify filename: Must be `user-profile.md` or `user-profile.yaml`
3. Try asking: "What do you know about my profile?"

### Want to Start Over?
Delete your profile file and run the skill again:
```bash
rm ~/.memories/user-profile.md
```

### Profile Too Long?
It's okay! Focus on key sections. AI will reference the most relevant parts.

## Examples of How AI Uses Your Profile

### Before Profile
> "How should I structure my database?"

**Generic response** about relational vs NoSQL

### After Profile (with role = "Startup CTO", constraint = "small team")
> "Given your startup context and small team, I'd recommend PostgreSQL with Prisma ORM because it requires minimal setup but scales well..."

### Before Profile
> "Review this code"

**Generic code review** with standard checklist

### After Profile (with preference = "Airbnb style", care about = "performance")
> "Review against Airbnb style guide and performance concerns:
> - Line 12: This N+1 query can be optimized with a join
> - Lines 5-8: Consider extracting this to a custom hook (Airbnb pattern)"

## Advanced: Custom Sections

You can add domain-specific information:

```yaml
# For ML Engineers
ml_preferences:
  frameworks: ["PyTorch", "Hugging Face"]
  gpu: true
  experiment_tracking: "Weights & Biases"

# For DevOps Engineers
infrastructure:
  cloud_provider: "AWS"
  container_orchestration: "ECS"
  iac_tool: "Terraform"

# For Product Managers
product_context:
  market: "B2B SaaS"
  team_size: 50
  stage: "Growth"
```

## Next Steps

1. ✅ Create your profile with this skill
2. ✅ Ask AI a question related to your work
3. ✅ Notice how the response includes your context
4. ✅ Update your profile as your situation changes
5. ✅ Enjoy more personalized AI assistance!

---

**Questions?** Edit this guide or your profile at any time. Changes take effect immediately in the next chat message.
