#!/usr/bin/env python
import sys
import warnings
from pathlib import Path
import yaml



# Import your crew definition
from vocavoice.crew import Vocavoice

# Ignore specific warnings from pysbd (sentence boundary detection library)
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is designed for local running of your CrewAI project.
# Try to keep this file clean, only for execution purposes.

def run():
    """
    Run the Vocavoice crew with configuration inputs.
    """
    # Define the base directory (the folder where this file is located)
    BASE_DIR = Path(__file__).resolve().parent

    # Construct the full path to the settings.yaml file
    settings_config = BASE_DIR / "config" / "settings.yaml"    
    # Safely load the YAML configuration
    with open(settings_config, "r", encoding="utf-8") as file: 
        config = yaml.safe_load(file)

    # Prepare the inputs dictionary for the crew
    inputs = {
        "language": config["app"]["language"],
        "vocabulary_list": config["app"]["vocabulary_list"],
        "topic": config["app"]["topic"],
        "language_level": config["app"]["language_level"],
        "voice_style": config["app"]["voice_style"],
        "tts_model": config["app"]["tts_model"],
        "tts_voice": config["app"]["tts_voice"],
        "audio_path": config["output"]["audio_path"],
        "script_path": config["output"]["script_path"],
        "path_config": config["output"]["path_config"]
    }
    
    
    try:
        # Initialize and start the Vocavoice crew with the prepared inputs
        Vocavoice().crew().kickoff(inputs=inputs)
        
    except Exception as e:
        # Raise a clear exception if anything goes wrong
        raise Exception(f"An error occurred while running the crew: {e}")
