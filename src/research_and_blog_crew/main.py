"""
Research and Blog AI Agent - Main Entry Point

This module serves as the primary entry point for running the AI crew.
The crew generates comprehensive research reports and converts them into
engaging blog posts on any specified topic.

Usage:
    python -m research_and_blog_crew.main
    
    Or use the installed command:
    run_crew
"""

from research_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the research and blog generation crew.
    
    The crew operates in two sequential steps:
    1. Research Agent generates a detailed report on the topic
    2. Blog Writer transforms the report into an engaging blog post
    
    The output is saved to the blogs/ directory.
    """
    inputs = {
        'topic': 'AI agents in coding',
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


