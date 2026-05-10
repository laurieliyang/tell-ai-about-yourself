# Tell AI About Yourself

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Skill](https://img.shields.io/badge/AI-Skill-blue)](https://github.com/laurieliyang/tell-ai-about-yourself)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-brightgreen)](https://github.com/laurieliyang/tell-ai-about-yourself)

> 🤖 **Personalize your AI assistant by building a comprehensive user profile** — Tell your AI about yourself once, and get context-aware, tailored responses for every question.

## 🎯 What Is This?

A portable AI personalization skill that creates and maintains your personal profile, enabling:

- **Contextual Responses**: AI understands your role, projects, and goals
- **Tailored Advice**: Recommendations fit your experience level, constraints, and preferences
- **Privacy-First**: Your data stays local on your machine
- **One-Time Setup**: Create your profile once, use it across all sessions

## ✨ Key Features

✅ **Interactive Profile Setup** — Answer guided questions  
✅ **YAML Configuration** — Manual template-based setup  
✅ **Multiple Formats** — Markdown or YAML storage  
✅ **Cross-Session Persistence** — Profile follows you across workspaces  
✅ **Easy Updates** — Modify your profile anytime  
✅ **Privacy Focused** — Local storage, no cloud sync  
✅ **Fully Documented** — Usage guide, templates, and examples included  

## 📊 What Gets Stored?

Your profile includes:

| Category | Examples |
|----------|----------|
| **Who You Are** | Name, background, expertise level |
| **Your Role** | Job title, industry, team size |
| **Current Work** | Projects, tech stack, timeline |
| **Goals** | Short/medium/long-term objectives |
| **Challenges** | Technical obstacles, constraints |
| **Preferences** | Communication style, code preferences, detail level |
| **Likes/Dislikes** | What you value in code and work |

## 🚀 Quick Start

### Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/laurieliyang/tell-ai-about-yourself.git
   cd tell-ai-about-yourself
   ```

2. **For local AI tools** (e.g., Claude, VS Code):
   ```bash
   cp -r tell-ai-about-yourself ~/.claude/skills/
   # or for VS Code
   cp -r tell-ai-about-yourself ~/.vscode/extensions/
   ```

3. **For project-level use** (`.github/skills/`):
   ```bash
   cp -r tell-ai-about-yourself .github/skills/
   ```

### Create Your Profile

Choose one method:

#### Option 1: Interactive Setup (Recommended)
```bash
python3 scripts/setup-profile.py
```
Answer guided questions → Profile auto-saves to `/memories/user-profile.md`

#### Option 2: YAML Template
1. Copy `references/preferences-template.yaml`
2. Fill in your information
3. Save as `/memories/user-profile.yaml`

#### Option 3: Manual Markdown
Create `/memories/user-profile.md` with freeform information.

### Verify It Works

Ask your AI assistant:
```
"Based on my profile, what's the next step for my project?"
```

AI should reference your profile information in the response. ✨

## 📖 Documentation

| File | Purpose |
|------|---------|
| [SKILL.md](./SKILL.md) | Skill definition and overview |
| [USAGE.md](./references/USAGE.md) | Step-by-step usage guide |
| [preferences-template.yaml](./references/preferences-template.yaml) | Complete YAML template |
| [EXAMPLE-PROFILE.md](./references/EXAMPLE-PROFILE.md) | Example profile reference |

## 📁 Project Structure

```
tell-ai-about-yourself/
├── README.md                                    # This file
├── SKILL.md                                     # Skill definition
├── LICENSE                                      # MIT License
├── scripts/
│   └── setup-profile.py                         # Interactive setup script
└── references/
    ├── USAGE.md                                 # Detailed usage guide
    ├── preferences-template.yaml                # YAML configuration template
    └── EXAMPLE-PROFILE.md                       # Example profile
```

## 💡 How It Works

### Before Profile
```
You: "How should I structure my codebase?"
AI:  "You can organize it with src/, tests/, docs/ folders..."
```

### After Profile
```
You: "How should I structure my codebase?"
AI:  "Given that you're building a microservices system with your 
      3-person team, I'd recommend using a monorepo structure with 
      individual service folders, using the Airbnb style guide you prefer..."
```

## 🎓 Use Cases

### For Individual Developers
- Get personalized coding advice matching your style
- Save time explaining your project context
- Consistent guidance across sessions

### For Teams
- Each team member can create their profile
- AI adapts to different experience levels
- Shared preferences ensure consistency

### For Learning
- AI adjusts explanation depth to your level
- Recommendations match your learning goals
- Examples use your preferred technologies

## 🔒 Privacy & Security

✅ **Local Storage Only** — Files stored in `/memories/` on your machine  
✅ **No Cloud Sync** — Data never leaves your computer by default  
✅ **Full Control** — You decide what information to include  
✅ **Easy Deletion** — Delete your profile anytime  

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Profile not being used | Verify file exists at `/memories/user-profile.md` or `.yaml` |
| Need to update profile | Run setup script again or edit file directly |
| Want to reset | Delete profile file and run setup script |
| File location unclear | See [USAGE.md](.github/skills/tell-ai-about-yourself/references/USAGE.md#file-locations) |

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report issues or suggest improvements
- Improve documentation
- Add new profile templates or examples
- Translate to other languages

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

- **Python** 3.7+ (for interactive setup script)
- Access to store profile files locally
- An AI assistant tool (Claude, ChatGPT, VS Code Copilot, etc.)

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Designed for cross-platform AI personalization
- Inspired by developer productivity workflows
- Thanks to the open source community

## 📧 Contact

Questions? Suggestions? Issues?
- Create a [GitHub Issue](https://github.com/laurieliyang/tell-ai-about-yourself/issues)
- Start a [Discussion](https://github.com/laurieliyang/tell-ai-about-yourself/discussions)

## 🗺️ Roadmap

- [ ] Web UI for profile creation
- [ ] Profile templates for different roles (DevOps, DataScientist, PM, etc.)
- [ ] Profile sharing/export feature
- [ ] Integration with other AI platforms (Claude, ChatGPT, etc.)
- [ ] Multi-language support

---

**Ready to get started?** See [Quick Start](#-quick-start) above or read [USAGE.md](./references/USAGE.md) for detailed instructions.

**Questions?** Check [Troubleshooting](#-troubleshooting) or open an [issue](https://github.com/laurieliyang/tell-ai-about-yourself/issues).

---

Made with ❤️ for developers who want AI that understands them.
