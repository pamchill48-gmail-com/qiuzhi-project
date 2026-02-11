# Monitoring & Maintenance
- **Service Checks**: Monitor Xray (software/v2rayN/bin/xray/xray) every 5 mins. Restart if down.
- **Auto-repair**: If services stop, restart them automatically.
- **Commands**:
  - `del`: Clean temporary files to free space.
  - `mem`: Add new content to memory system.

# Content Handling Rules
## YouTube Links
- **Batch Processing** (Multiple links):
  - **Filter**: Only keep Tech-related content (AI, 3C: Phone/PC/GPU/CPU/Chips, Tech News, Reviews).
  - **Output**: Summary only. **NO timestamps**.
- **Single Processing** (One link):
  - **Action**: Detailed analysis.
  - **Output**: Include timestamps and song identification (if applicable).

# Clawdbot/OpenClaw Knowledge Base
## Core Logic (Software)
- **Long-term Memory**: Uses `.md` text files for structured, human-readable storage. Solves LLM forgetfulness via 70% semantic + 30% keyword hybrid search.
- **Proactivity**: "Heartbeat" mechanism triggers tasks even when silent. Agent anticipates needs based on context (e.g., auto-pushing suggestions).
- **Automation**: Capable of browser automation (bypassing API limits) and budget self-management.

## Hardware & Deployment
- **Ideal Host**: Mac mini (2026 era) due to high performance/watt and I/O capabilities.
- **Physical Isolation**: Running agents on dedicated hardware protects main machine privacy and security from high-permission AI operations.
- **Hardware Shift**: Focus moves from screens to I/O status indicators and large RAM/storage for context/memory.

## Business & Organization
- **One-Person Company**: AI Agents enable individuals with domain expertise ("General") to command a digital workforce.
- **Business Model**: Potential shift from ad-based traffic to "pay-per-crawl" or agent-service models.
- **Data Format**: `.md` (Markdown) becoming the new "compiled code" for natural language processing eras.

# Project Management & Deployment
## GitHub Repositories (The "4 Machines" Rule)
- **genmini61-gmail-com** (Standard):
  - Repo: `qiuzhi-project`
  - Path: `qiuzhi-project/`
- **pamchill48-gmail-com** (Standard):
  - Repo: `qiuzhi-project`
  - Path: `qiuzhi-project/`
- **chillrnb559-cpu** (Standard):
  - Repo: `qiuzhi-project`
  - Path: `qiuzhi-project/`
- **junelieat941-sys** (**Special** - Restaurant):
  - Repo: `qiuzhi-restaurant`
  - Path: `qiuzhi-project/qiuzhi-restaurant/` (Nested structure)
  - Note: This is the dedicated restaurant project branch.
