# Import necessary libraries
import os
from pathlib import Path
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from openai import OpenAI
import yaml

# Define the base directory and load the configuration file (settings.yaml)
BASE_DIR = Path(__file__).resolve().parent.parent
settings_config = BASE_DIR / "config" / "settings.yaml"

# Read and load the settings.yaml file
with open(settings_config, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Define the input schema for the TTS Tool using Pydantic
class TTSToolInput(BaseModel):
    """Input schema for the TTS Tool."""
    simplified_script: str = Field(..., description="Simplified English script to convert into speech.")
    audio_path: str = Field(..., description="Directory path to save the generated audio file.")
    file_naming: str = Field(..., description="Filename without extension, e.g., 'Tech_Talk_Podcast'.")

# Define the TTS Tool class that extends BaseTool
class TTSTool(BaseTool):
    """
    A tool to convert a given text into speech and save it as an audio file using OpenAI's TTS model.

    Attributes:
        name (str): The name of the tool.
        description (str): A brief description of what the tool does.
        args_schema (Type[BaseModel]): The schema defining expected input parameters.
    """

    name: str = "convert text to audio file"
    description: str = "Convert the given text into a TTS audio file using OpenAI's speech API."
    args_schema: Type[BaseModel] = TTSToolInput

    # Main function that executes the tool logic
    def _run(self, simplified_script: str, audio_path: str, file_naming: str) -> str:
        # Initialize OpenAI client
        client = OpenAI()

        # Ensure the audio_path exists (create it if it doesn't)
        os.makedirs(audio_path, exist_ok=True)

        # Define the full filename with '.mp3' extension
        filename = f"{file_naming}.mp3"
        full_path = os.path.join(audio_path, filename)

        # Generate the speech audio using OpenAI's API
        response = client.audio.speech.create(
            model=config["app"]["tts_model"],  # Model is taken from the config file
            voice=config["app"]["tts_voice"],  # Voice is taken from the config file
            input=simplified_script,
            response_format="mp3",
            instructions="Speak in a clear, natural, podcast-like tone with slight emphasis on vocabulary."
        )

        # Save the generated audio content to the specified file
        with open(full_path, "wb") as f:
            f.write(response.content)

        # Return a success message with the path to the saved file
        return f"Audio successfully saved at: {full_path}"
