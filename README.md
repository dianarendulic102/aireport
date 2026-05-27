# 🤖 AI Report Agent - Complete Installation & Usage Guide

[![GitHub](https://img.shields.io/badge/GitHub-dianarendulic102-blue?logo=github)](https://github.com/dianarendulic102/aireport)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green?logo=openai)](https://openai.com/)
[![License](https://img.shields.io/badge/License-Internal-red)](#)

**Intelligent AI-powered analytics assistant for instant answers to your monthly report questions.**

---

## 📚 Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Support](#-support)

---

## 🚀 Quick Start

Get AI Report Agent running in 5 minutes:

```bash
# 1. Clone repository
git clone https://github.com/dianarendulic102/aireport.git
cd aireport

# 2. Create virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 5. Run agent
python agents/main.py --report reports/sample_sales_report.csv --action analyze
```

---

## 💻 Installation

### Prerequisites
- **Python 3.10+** ([Download](https://www.python.org/))
- **OpenAI API Key** ([Get here](https://platform.openai.com/api-keys))
- **Git** ([Download](https://git-scm.com/))

### Step-by-Step Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/dianarendulic102/aireport.git
cd aireport
```

### 2️⃣ Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Configuration
```bash
cp .env.example .env
```

Edit `.env` file and add your credentials:
```env
OPENAI_API_KEY=sk-your-api-key-here
AGENT_MODEL=gpt-4
TEMPERATURE=0.7
MAX_TOKENS=2000
```

### 5️⃣ Verify Installation
```bash
python agents/main.py --help
```

You should see the help message with available options.

---

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Required
OPENAI_API_KEY=sk-your-api-key-here

# Optional (defaults provided)
AGENT_MODEL=gpt-4                    # Model to use (gpt-4, gpt-3.5-turbo)
TEMPERATURE=0.7                      # Creativity level (0-1)
MAX_TOKENS=2000                      # Max response length
TIMEOUT=30                           # Request timeout in seconds
DEBUG=false                          # Enable debug logging
```

### Report Formats Supported

✅ **CSV** - Comma-separated values  
✅ **Excel** - .xlsx, .xls files  
✅ **JSON** - Structured data  
✅ **TXT** - Plain text reports  

### Prompt Customization

Edit files in `prompts/` folder:

```
prompts/
├── analyze.txt       # Full report analysis
├── summarize.txt     # Quick summary (3-5 sentences)
├── questions.txt     # Answer specific questions
├── compare.txt       # Compare multiple reports
└── insights.txt      # Extract key insights
```

---

## 📖 Usage

### Basic Commands

#### 1. Analyze Report
```bash
python agents/main.py --report reports/monthly_sales.csv --action analyze
```

**Output:**
```
📊 ANALYSIS:

Key Findings:
- Total Revenue: €1,250,000 (↑ 15% vs last month)
- Top Region: EU with 45% of sales
- Growth Rate: 12% month-over-month

Anomalies Detected:
- Unexpected drop in APAC region (-8%)
- One product underperforming vs trend

Recommendations:
1. Investigate APAC region issues
2. Boost underperforming product marketing
3. Scale success in EU region
```

#### 2. Summarize Report
```bash
python agents/main.py --report reports/monthly_sales.csv --action summarize
```

#### 3. Ask Questions
```bash
python agents/main.py \
  --report reports/monthly_sales.csv \
  --action ask \
  --question "What was the top-performing region and why?"
```

#### 4. Compare Reports
```bash
python agents/main.py \
  --report reports/april_report.csv \
  --compare reports/may_report.csv \
  --action compare
```

#### 5. Extract Insights
```bash
python agents/main.py --report reports/monthly_sales.csv --action insights
```

---

## 📁 Project Structure

```
aireport/
├── README.md                 # This file
├── DESCRIPTION.md            # Project overview & business case
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
│
├── agents/
│   ├── __init__.py              # Python package init
│   ├── main.py              # Main CLI application
│   ├── report_agent.py      # ReportAgent class
│   └── prompts.py           # Prompt management
│
├── prompts/
│   ├── analyze.txt          # Analysis prompt
│   ├── summarize.txt        # Summary prompt
│   ├── questions.txt        # Q&A prompt
│   ├── compare.txt          # Comparison prompt
│   └── insights.txt         # Insights prompt
│
├── reports/
│   ├── sample_sales_report.csv
│   ├── sample_marketing_report.csv
│   └── sample_analytics_report.csv
│
├── config/
│   └── settings.json        # Configuration settings
│
└── docs/
    ├── ARCHITECTURE.md      # Technical architecture
    └── API_REFERENCE.md     # API documentation
```

---

## 🔧 API Reference

### ReportAgent Class

```python
from agents.report_agent import ReportAgent

# Initialize agent
agent = ReportAgent()

# Analyze report
analysis = agent.analyze("reports/report.csv")

# Summarize report
summary = agent.summarize("reports/report.csv")

# Answer question
answer = agent.answer_question("reports/report.csv", "What was the revenue?")

# Compare reports
comparison = agent.compare("reports/april.csv", "reports/may.csv")

# Extract insights
insights = agent.extract_insights("reports/report.csv")
```

### Command-Line Interface

```bash
python agents/main.py [OPTIONS]

Options:
  --report PATH              Path to report file (REQUIRED)
  --action ACTION            Action to perform (REQUIRED)
                            Options: analyze, summarize, ask, compare, insights
  --question TEXT            Question to ask (required for 'ask' action)
  --compare PATH             Second report for comparison (required for 'compare')
  --output FORMAT            Output format: text, json, html (default: text)
  --verbose                  Enable verbose output
  --help                     Show help message
```

---

## 📊 Examples

### Example 1: Analyze Sales Report
```bash
python agents/main.py \
  --report reports/sample_sales_report.csv \
  --action analyze \
  --verbose
```

### Example 2: Quick Summary
```bash
python agents/main.py \
  --report reports/sample_marketing_report.csv \
  --action summarize
```

### Example 3: Answer Questions
```bash
python agents/main.py \
  --report reports/sample_analytics_report.csv \
  --action ask \
  --question "What were the top 3 revenue drivers?"
```

### Example 4: Compare Two Reports
```bash
python agents/main.py \
  --report reports/sample_sales_report.csv \
  --compare reports/sample_marketing_report.csv \
  --action compare
```

---

## 🚨 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'openai'"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: "OpenAI API key not found"

**Solution:**
```bash
# 1. Check .env file exists
ls -la .env

# 2. Verify API key format
cat .env | grep OPENAI_API_KEY

# 3. Get new key from https://platform.openai.com/api-keys
# 4. Update .env file
```

### Problem: "File not found: reports/report.csv"

**Solution:**
```bash
# Check available reports
ls -la reports/

# Verify file path is correct
python agents/main.py --report reports/sample_sales_report.csv --action analyze
```

---

## 🤝 Contributing

This is an internal Porsche AG project. For contributions:

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
3. **Commit Changes**
   ```bash
   git commit -m "Add: description of changes"
   ```

4. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Submit Pull Request**

---

## 📞 Support

- **Product Owner**: Diana Rendulic
- **Technical Leads**: Josip Banjedvorac, Denis Čuljak
- **Team**: Jarvis Analytics Team
- **Email**: diana.rendulic@porsche.digital

---

**Version**: 1.0  
**Last Updated**: May 27, 2026  
**Status**: 🟢 Active Development