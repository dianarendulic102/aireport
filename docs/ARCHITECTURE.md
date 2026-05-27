# 🏗️ AI Report Agent - Technical Architecture

## System Overview

```
┌─────────────────────────────────────────────────────┐
│                 User/CLI Interface                   │
│            (agents/main.py - Click CLI)              │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│              Report Agent Core                       │
│         (agents/report_agent.py)                     │
│  - Load Reports (CSV, Excel, JSON, TXT)             │
│  - Process & Parse Data                             │
│  - Manage Conversations                             │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│           Prompt Management System                  │
│          (agents/prompts.py)                        │
│  - Load Prompts from prompts/ folder                │
│  - Customize System Prompts                         │
│  - Template Management                              │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│            OpenAI API Integration                    │
│     (OpenAI GPT-4 Chat Completions)                 │
│  - Model: gpt-4 (or gpt-3.5-turbo)                  │
│  - Temperature: 0.7 (configurable)                  │
│  - Max Tokens: 2000 (configurable)                  │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│           Response Processing                       │
│  - Format Output (Text, JSON, HTML)                 │
│  - Error Handling                                   │
│  - Logging                                          │
└─────────────────────────────────────────────────────┘
```

## Component Architecture

### 1. **CLI Interface** (`agents/main.py`)
- Entry point for the application
- Command-line argument parsing (Click)
- User input validation
- Output formatting and display

**Actions:**
- `analyze` - Full report analysis
- `summarize` - Quick summary
- `ask` - Answer specific questions
- `compare` - Compare two reports
- `insights` - Extract key insights

### 2. **Report Agent** (`agents/report_agent.py`)
- Core business logic
- File loading and parsing
- Interaction with OpenAI API
- Conversation management

**Key Methods:**
- `load_report()` - Load various file formats
- `analyze()` - Analyze report
- `summarize()` - Summarize report
- `answer_question()` - Answer specific question
- `compare()` - Compare two reports
- `extract_insights()` - Extract insights

### 3. **Prompt Management** (`agents/prompts.py`)
- Dynamic prompt loading
- Prompt customization
- Caching system
- Default prompts fallback

**Features:**
- Loads prompts from `prompts/` folder
- Caches prompts for performance
- Provides defaults if file missing

### 4. **Configuration** (`config/settings.json`)
- Application settings
- Model configuration
- Path management
- Feature flags

### 5. **Prompts** (`prompts/`)
Customizable system prompts:
- `analyze.txt` - Analysis prompt
- `summarize.txt` - Summary prompt
- `questions.txt` - Q&A prompt
- `compare.txt` - Comparison prompt
- `insights.txt` - Insights prompt

### 6. **Sample Reports** (`reports/`)
Test data:
- `sample_sales_report.csv`
- `sample_marketing_report.csv`
- `sample_analytics_report.csv`

## Data Flow

```
1. User Input
   └─> CLI parses arguments
   
2. File Loading
   └─> ReportAgent.load_report()
       └─> Parse CSV/Excel/JSON/TXT
       └─> Convert to text format
   
3. Prompt Loading
   └─> PromptManager.get_prompt()
       └─> Check cache
       └─> Load from file
       └─> Use default if missing
   
4. API Call
   └─> ReportAgent._call_gpt()
       └─> OpenAI ChatCompletion API
       └─> Model: gpt-4
       └─> System + User prompts
   
5. Response Processing
   └─> Format output (text/JSON/HTML)
   └─> Error handling
   └─> Return to user
```

## File Format Support

### CSV
```python
df = pd.read_csv(file)
text = df.to_string()
```

### Excel
```python
df = pd.read_excel(file)
text = df.to_string()
```

### JSON
```python
data = json.load(file)
text = json.dumps(data, indent=2)
```

### TXT
```python
with open(file) as f:
    text = f.read()
```

## Configuration System

### Environment Variables (.env)
```env
OPENAI_API_KEY=sk-...
AGENT_MODEL=gpt-4
TEMPERATURE=0.7
MAX_TOKENS=2000
TIMEOUT=30
DEBUG=false
```

### Settings File (config/settings.json)
```json
{
  "ai": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000
  },
  "features": {
    "analyze": true,
    "summarize": true,
    "ask": true,
    "compare": true,
    "insights": true
  }
}
```

## Error Handling

### File Errors
- FileNotFoundError - Report not found
- ValueError - Unsupported file format

### API Errors
- RuntimeError - OpenAI API failure
- Timeout - Request timeout

### Validation Errors
- Missing API key
- Invalid arguments
- Missing required options

## Performance Optimization

1. **Prompt Caching** - Avoid reloading prompts
2. **File Size Limiting** - Truncate large reports (5000 chars)
3. **Token Optimization** - Configure max_tokens
4. **Timeout Management** - Configurable timeout

## Future Enhancements

- [ ] Web UI (Flask/FastAPI)
- [ ] Database storage for history
- [ ] Real-time streaming responses
- [ ] Multi-file batch processing
- [ ] Custom model fine-tuning
- [ ] Slack bot integration
- [ ] Tableau/Power BI integration
- [ ] Advanced caching with Redis
- [ ] Load balancing for high volume
- [ ] Multi-language support
