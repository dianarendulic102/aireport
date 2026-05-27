"""ReportAgent - AI-powered report analysis agent."""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any
import pandas as pd
from openai import OpenAI

from .prompts import PromptManager


class ReportAgent:
    """AI-powered agent for analyzing reports."""
    
    def __init__(
        self,
        api_key: str,
        model: str = 'gpt-4',
        temperature: float = 0.7,
        max_tokens: int = 2000,
        timeout: int = 30,
        debug: bool = False
    ):
        """Initialize ReportAgent.
        
        Args:
            api_key: OpenAI API key
            model: Model to use (gpt-4, gpt-3.5-turbo)
            temperature: Temperature for generation (0-1)
            max_tokens: Maximum tokens in response
            timeout: Request timeout in seconds
            debug: Enable debug logging
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.debug = debug
        self.prompt_manager = PromptManager()
    
    def load_report(self, file_path: str) -> str:
        """Load report from file.
        
        Args:
            file_path: Path to report file
            
        Returns:
            Report content as string
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"Report not found: {file_path}")
        
        if path.suffix == '.csv':
            df = pd.read_csv(file_path)
            return df.to_string()
        elif path.suffix in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
            return df.to_string()
        elif path.suffix == '.json':
            with open(file_path, 'r') as f:
                data = json.load(f)
            return json.dumps(data, indent=2)
        elif path.suffix == '.txt':
            with open(file_path, 'r') as f:
                return f.read()
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")
    
    def _call_gpt(
        self,
        system_prompt: str,
        user_message: str
    ) -> str:
        """Call GPT API.
        
        Args:
            system_prompt: System prompt for GPT
            user_message: User message
            
        Returns:
            GPT response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Error calling GPT API: {str(e)}")
    
    def analyze(self, report_path: str) -> str:
        """Analyze report.
        
        Args:
            report_path: Path to report file
            
        Returns:
            Analysis result
        """
        report_content = self.load_report(report_path)
        system_prompt = self.prompt_manager.get_prompt('analyze')
        
        user_message = f"""Please analyze this report and provide key insights:
        
{report_content[:5000]}  # Limit to first 5000 chars
"""
        
        return self._call_gpt(system_prompt, user_message)
    
    def summarize(self, report_path: str) -> str:
        """Summarize report.
        
        Args:
            report_path: Path to report file
            
        Returns:
            Summary result
        """
        report_content = self.load_report(report_path)
        system_prompt = self.prompt_manager.get_prompt('summarize')
        
        user_message = f"""Please summarize this report in 3-5 sentences:
        
{report_content[:5000]}
"""
        
        return self._call_gpt(system_prompt, user_message)
    
    def answer_question(self, report_path: str, question: str) -> str:
        """Answer a question about the report.
        
        Args:
            report_path: Path to report file
            question: Question to answer
            
        Returns:
            Answer
        """
        report_content = self.load_report(report_path)
        system_prompt = self.prompt_manager.get_prompt('questions')
        
        user_message = f"""Based on this report, please answer the question:
        
Report:
{report_content[:5000]}

Question: {question}
"""
        
        return self._call_gpt(system_prompt, user_message)
    
    def compare(self, report1_path: str, report2_path: str) -> str:
        """Compare two reports.
        
        Args:
            report1_path: Path to first report
            report2_path: Path to second report
            
        Returns:
            Comparison result
        """
        content1 = self.load_report(report1_path)
        content2 = self.load_report(report2_path)
        system_prompt = self.prompt_manager.get_prompt('compare')
        
        user_message = f"""Please compare these two reports:
        
Report 1:
{content1[:3000]}

Report 2:
{content2[:3000]}
"""
        
        return self._call_gpt(system_prompt, user_message)
    
    def extract_insights(self, report_path: str) -> str:
        """Extract key insights from report.
        
        Args:
            report_path: Path to report file
            
        Returns:
            Insights
        """
        report_content = self.load_report(report_path)
        system_prompt = self.prompt_manager.get_prompt('insights')
        
        user_message = f"""Please extract the key insights and opportunities from this report:
        
{report_content[:5000]}
"""
        
        return self._call_gpt(system_prompt, user_message)
