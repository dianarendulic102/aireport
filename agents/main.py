#!/usr/bin/env python3
"""AI Report Agent - Main CLI Application."""

import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import click
from colorama import Fore, Style

from .report_agent import ReportAgent

# Load environment variables
load_dotenv()


class Config:
    """Configuration class."""
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    AGENT_MODEL = os.getenv('AGENT_MODEL', 'gpt-4')
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 2000))
    TIMEOUT = int(os.getenv('TIMEOUT', 30))
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'


def validate_report_path(ctx, param, value):
    """Validate that report file exists."""
    if value:
        path = Path(value)
        if not path.exists():
            raise click.BadParameter(f"Report file not found: {value}")
    return value


def validate_api_key():
    """Validate OpenAI API key is set."""
    if not Config.OPENAI_API_KEY:
        click.echo(
            f"{Fore.RED}Error: OPENAI_API_KEY not found in .env file{Style.RESET_ALL}"
        )
        click.echo(f"{Fore.YELLOW}Please set your OpenAI API key in .env file{Style.RESET_ALL}")
        sys.exit(1)


@click.command()
@click.option(
    '--report',
    type=click.Path(exists=True),
    required=True,
    help='Path to report file (CSV, Excel, JSON, TXT)'
)
@click.option(
    '--action',
    type=click.Choice(['analyze', 'summarize', 'ask', 'compare', 'insights']),
    required=True,
    help='Action to perform on report'
)
@click.option(
    '--question',
    type=str,
    default=None,
    help='Question to ask (required for "ask" action)'
)
@click.option(
    '--compare',
    type=click.Path(exists=True),
    default=None,
    help='Second report for comparison (required for "compare" action)'
)
@click.option(
    '--output',
    type=click.Choice(['text', 'json', 'html']),
    default='text',
    help='Output format'
)
@click.option(
    '--verbose',
    is_flag=True,
    help='Enable verbose output'
)
def main(report, action, question, compare, output, verbose):
    """AI Report Agent - Intelligent Analytics Assistant.
    
    Examples:
        # Analyze report
        python agents/main.py --report reports/sales.csv --action analyze
        
        # Ask a question
        python agents/main.py --report reports/sales.csv --action ask --question "What was total revenue?"
        
        # Compare two reports
        python agents/main.py --report reports/april.csv --compare reports/may.csv --action compare
    """
    
    # Validate API key
    validate_api_key()
    
    try:
        if verbose:
            click.echo(f"{Fore.CYAN}🤖 AI Report Agent v1.0.0{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}Model: {Config.AGENT_MODEL}{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}Temperature: {Config.TEMPERATURE}{Style.RESET_ALL}")
            click.echo()
        
        # Initialize agent
        agent = ReportAgent(
            api_key=Config.OPENAI_API_KEY,
            model=Config.AGENT_MODEL,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS,
            timeout=Config.TIMEOUT,
            debug=verbose
        )
        
        if verbose:
            click.echo(f"{Fore.GREEN}✅ Agent initialized{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}📖 Loading report: {report}{Style.RESET_ALL}")
        
        # Perform action
        result = None
        
        if action == 'analyze':
            result = agent.analyze(report)
            if verbose:
                click.echo(f"{Fore.CYAN}📊 Analysis complete{Style.RESET_ALL}")
        
        elif action == 'summarize':
            result = agent.summarize(report)
            if verbose:
                click.echo(f"{Fore.CYAN}📝 Summarization complete{Style.RESET_ALL}")
        
        elif action == 'ask':
            if not question:
                click.echo(f"{Fore.RED}Error: --question is required for 'ask' action{Style.RESET_ALL}")
                sys.exit(1)
            result = agent.answer_question(report, question)
            if verbose:
                click.echo(f"{Fore.CYAN}❓ Question answered{Style.RESET_ALL}")
        
        elif action == 'compare':
            if not compare:
                click.echo(f"{Fore.RED}Error: --compare is required for 'compare' action{Style.RESET_ALL}")
                sys.exit(1)
            result = agent.compare(report, compare)
            if verbose:
                click.echo(f"{Fore.CYAN}🔍 Comparison complete{Style.RESET_ALL}")
        
        elif action == 'insights':
            result = agent.extract_insights(report)
            if verbose:
                click.echo(f"{Fore.CYAN}💡 Insights extracted{Style.RESET_ALL}")
        
        # Output result
        click.echo()
        click.echo(f"{Fore.GREEN}{'='*80}{Style.RESET_ALL}")
        
        if output == 'json':
            click.echo(json.dumps(result, indent=2))
        elif output == 'html':
            click.echo(f"<pre>{result}</pre>")
        else:
            click.echo(result)
        
        click.echo(f"{Fore.GREEN}{'='*80}{Style.RESET_ALL}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}", err=True)
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
