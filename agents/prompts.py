"""Prompt management for AI Report Agent."""

import os
from pathlib import Path
from typing import Dict


class PromptManager:
    """Manages prompts for the agent."""
    
    def __init__(self, prompts_dir: str = 'prompts'):
        """Initialize PromptManager.
        
        Args:
            prompts_dir: Directory containing prompt files
        """
        self.prompts_dir = Path(prompts_dir)
        self.cache: Dict[str, str] = {}
    
    def get_prompt(self, prompt_type: str) -> str:
        """Get prompt by type.
        
        Args:
            prompt_type: Type of prompt (analyze, summarize, etc.)
            
        Returns:
            Prompt content
        """
        # Check cache first
        if prompt_type in self.cache:
            return self.cache[prompt_type]
        
        # Load from file
        prompt_file = self.prompts_dir / f"{prompt_type}.txt"
        
        if not prompt_file.exists():
            # Return default prompt if file not found
            return self._get_default_prompt(prompt_type)
        
        with open(prompt_file, 'r') as f:
            prompt = f.read().strip()
        
        # Cache it
        self.cache[prompt_type] = prompt
        return prompt
    
    def _get_default_prompt(self, prompt_type: str) -> str:
        """Get default prompt.
        
        Args:
            prompt_type: Type of prompt
            
        Returns:
            Default prompt
        """
        defaults = {
            'analyze': """You are an expert business analyst. 
Analyze the provided report and provide:
1. Key findings and metrics
2. Trends and patterns
3. Anomalies or concerns
4. Actionable recommendations

Be concise, data-driven, and professional.""",
            
            'summarize': """You are a professional report writer.
Summarize the provided report in 3-5 sentences.
Focus on the most important metrics and findings.
Be clear and concise.""",
            
            'questions': """You are a business intelligence expert.
Answer questions about the provided report accurately.
Always cite specific data from the report.
If you cannot find the answer, say so clearly.""",
            
            'compare': """You are a comparative analyst.
Compare the two provided reports and highlight:
1. Key differences
2. Metrics that improved or declined
3. Trends
4. Recommendations based on changes

Be specific and data-driven.""",
            
            'insights': """You are a business strategist.
Extract key insights from the report:
1. Opportunities for growth
2. Risk areas
3. Strategic recommendations
4. Metrics to monitor

Be insightful and forward-looking."""
        }
        
        return defaults.get(prompt_type, "You are a helpful assistant analyzing reports.")
