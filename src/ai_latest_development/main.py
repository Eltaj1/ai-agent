import sys
import warnings
from datetime import datetime
from ai_latest_development.crew import AiLatestDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Transformers and Large Language Models in Arxiv',
        'current_year': str(datetime.now().year),
        'date': datetime.now().strftime("%Y-%m-%d")
    }
    
    try:
        AiLatestDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
else:
    run()