# 📚 AI Report Agent - API Reference

## ReportAgent Class

The main class for interacting with reports.

### Initialization

```python
from agents.report_agent import ReportAgent

agent = ReportAgent(
    api_key="sk-your-api-key",
    model="gpt-4",
    temperature=0.7,
    max_tokens=2000,
    timeout=30,
    debug=False
)
```

**Parameters:**
- `api_key` (str, required): OpenAI API key
- `model` (str, default='gpt-4'): Model to use
  - Options: 'gpt-4', 'gpt-3.5-turbo'
- `temperature` (float, default=0.7): Creativity level (0-1)
  - 0 = focused/deterministic
  - 1 = creative/random
- `max_tokens` (int, default=2000): Maximum response length
- `timeout` (int, default=30): Request timeout in seconds
- `debug` (bool, default=False): Enable debug logging

### Methods

## 1. `analyze(report_path: str) -> str`

Perform comprehensive analysis of a report.

**Parameters:**
- `report_path` (str): Path to report file

**Returns:**
- str: Analysis result with key findings, trends, anomalies, and recommendations

**Example:**
```python
result = agent.analyze("reports/sales.csv")
print(result)
```

**Output:**
```
📊 ANALYSIS:

Key Findings:
- Total Revenue: €1.25M
- Growth: 15% vs April
- Top Region: EU (45%)

Anomalies:
- APAC drop of 8%
```

---

## 2. `summarize(report_path: str) -> str`

Generate a concise 3-5 sentence summary of the report.

**Parameters:**
- `report_path` (str): Path to report file

**Returns:**
- str: Summary of key metrics and findings

**Example:**
```python
summary = agent.summarize("reports/marketing.csv")
print(summary)
```

**Output:**
```
May marketing campaigns generated €2.89M in revenue with a 43% ROI.
Social media showed strongest engagement (5%), while email 
delivered highest conversion at 4.4%. Overall performance 
improved 35% vs April with all channels contributing positively.
```

---

## 3. `answer_question(report_path: str, question: str) -> str`

Answer a specific question about the report.

**Parameters:**
- `report_path` (str): Path to report file
- `question` (str): Question to answer

**Returns:**
- str: Answer based on report data

**Example:**
```python
question = "What was the top-performing product and why?"
answer = agent.answer_question("reports/sales.csv", question)
print(answer)
```

**Output:**
```
Product_A was the top performer with €1.05M in revenue 
(42% of total). Strong performance driven by:
- EU success (€450K, 15% growth)
- High customer satisfaction (250 customers)
- Consistent growth across all regions
```

---

## 4. `compare(report1_path: str, report2_path: str) -> str`

Compare two reports and highlight key differences.

**Parameters:**
- `report1_path` (str): Path to first report file
- `report2_path` (str): Path to second report file

**Returns:**
- str: Comparison with differences and trends

**Example:**
```python
comparison = agent.compare(
    "reports/april_sales.csv",
    "reports/may_sales.csv"
)
print(comparison)
```

**Output:**
```
May vs April Comparison:

📈 Improvements:
- EU Revenue: +15% (+€58K)
- Americas: +10% (+€29K)

📉 Declines:
- APAC Revenue: -8% (-€47K)
- Product_B: -5% overall

🎯 Key Trend:
Shift towards EU market success
```

---

## 5. `extract_insights(report_path: str) -> str`

Extract strategic insights and opportunities from the report.

**Parameters:**
- `report_path` (str): Path to report file

**Returns:**
- str: Strategic insights, opportunities, and risks

**Example:**
```python
insights = agent.extract_insights("reports/analytics.csv")
print(insights)
```

**Output:**
```
💡 Key Insights:

🚀 Opportunities:
1. Mobile market - 67% of traffic, growing 5%/month
2. Social media campaigns - Highest engagement
3. EU expansion - Strong growth potential

⚠️ Risk Areas:
1. APAC underperformance
2. Desktop traffic declining
3. Product_B needs attention

📊 Metrics to Monitor:
- Mobile conversion rate
- EU market share
- APAC recovery plan
```

---

## 6. `load_report(file_path: str) -> str`

Load and parse a report file (internal method).

**Parameters:**
- `file_path` (str): Path to report file

**Returns:**
- str: Report content as string

**Supported Formats:**
- CSV (.csv)
- Excel (.xlsx, .xls)
- JSON (.json)
- Text (.txt)

**Example:**
```python
content = agent.load_report("reports/sales.csv")
```

---

## PromptManager Class

Manages system prompts for different actions.

### Initialization

```python
from agents.prompts import PromptManager

pm = PromptManager(prompts_dir='prompts')
```

### Methods

## `get_prompt(prompt_type: str) -> str`

Get a prompt by type.

**Parameters:**
- `prompt_type` (str): Type of prompt
  - Options: 'analyze', 'summarize', 'questions', 'compare', 'insights'

**Returns:**
- str: Prompt content

**Example:**
```python
analyze_prompt = pm.get_prompt('analyze')
summarize_prompt = pm.get_prompt('summarize')
```

**Features:**
- Loads from `prompts/{type}.txt` files
- Caches prompts for performance
- Falls back to default if file missing

---

## Command-Line Interface

### CLI Command

```bash
python agents/main.py [OPTIONS]
```

### Options

```bash
--report PATH              Path to report file (REQUIRED)
--action ACTION            Action: analyze, summarize, ask, compare, insights (REQUIRED)
--question TEXT            Question to ask (required for 'ask' action)
--compare PATH             Second report (required for 'compare' action)
--output FORMAT            Output format: text, json, html (default: text)
--verbose                  Enable verbose output
--help                     Show help message
```

### Examples

**Analyze:**
```bash
python agents/main.py \
  --report reports/sales.csv \
  --action analyze \
  --verbose
```

**Summarize:**
```bash
python agents/main.py \
  --report reports/marketing.csv \
  --action summarize
```

**Ask Question:**
```bash
python agents/main.py \
  --report reports/sales.csv \
  --action ask \
  --question "What was the revenue?"
```

**Compare:**
```bash
python agents/main.py \
  --report reports/april.csv \
  --compare reports/may.csv \
  --action compare
```

**Extract Insights:**
```bash
python agents/main.py \
  --report reports/analytics.csv \
  --action insights \
  --output json
```

---

## Error Handling

### Exceptions

**FileNotFoundError**
```python
try:
    result = agent.analyze("nonexistent.csv")
except FileNotFoundError as e:
    print(f"File error: {e}")
```

**ValueError**
```python
try:
    result = agent.analyze("file.unsupported")
except ValueError as e:
    print(f"Format error: {e}")
```

**RuntimeError**
```python
try:
    result = agent.analyze("report.csv")
except RuntimeError as e:
    print(f"API error: {e}")
```

---

## Configuration

### Environment Variables

```bash
export OPENAI_API_KEY="sk-..."
export AGENT_MODEL="gpt-4"
export TEMPERATURE="0.7"
export MAX_TOKENS="2000"
export TIMEOUT="30"
export DEBUG="false"
```

### Settings File

```json
{
  "ai": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000,
    "timeout": 30
  }
}
```

---

## Performance Tips

1. **Model Selection**
   - Use `gpt-3.5-turbo` for faster/cheaper responses
   - Use `gpt-4` for better quality

2. **Token Management**
   - Reduce `max_tokens` to save costs
   - Increase for longer responses

3. **Temperature Settings**
   - Lower (0.3-0.5) for factual answers
   - Higher (0.8-1.0) for creative responses

4. **Batch Processing**
   - Process multiple reports efficiently
   - Implement queue system for scaling

5. **Caching**
   - Prompts are cached automatically
   - Consider implementing result caching
