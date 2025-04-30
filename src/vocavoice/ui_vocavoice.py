import os
from pathlib import Path
import shutil
import sys
import yaml
from vocavoice.crew import Vocavoice

def run_vocavoice(
    language,
    topic,
    vocabulary_list,
    language_level,
    voice_style,
    llm_model,
    tts_model,
    tts_voice,
    api_key
):
    """
    Executes the Vocavoice crew with the specified inputs and returns file paths.
    """
    try:
        PROJECT_ROOT = Path(__file__).resolve().parents[2]  # vocavoice/

        output_dir = PROJECT_ROOT / "outputs"
        script_dir = output_dir / "scripts"
        audio_dir = output_dir / "audio"
        
        settings_config = PROJECT_ROOT /"src"/ "vocavoice"/ "config" / "settings.yaml"

        # Prepare new booster config
        booster_config = {
            "language": language,
            "topic": topic,
            "vocabulary_list": vocabulary_list,
            "language_level": language_level,
            "voice_style": voice_style,
            "llm_model": llm_model,
            "tts_model": tts_model,
            "tts_voice": tts_voice
        }
        output_config = {
            "audio_path": str(audio_dir.resolve().as_posix()),
            "script_path": str(script_dir.resolve().as_posix()),
            "file_naming": topic,
            "path_config": str(output_dir.resolve().as_posix())
        }


        # Load existing settings or create new
        if settings_config.exists():
            with open(settings_config, "r", encoding="utf-8") as file:
                config = yaml.safe_load(file) or {}
        else:
            config = {}

        config["app"] = booster_config
        config["output"] = output_config

        with open(settings_config, "w", encoding="utf-8") as file:
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True)

        # Clear previous outputs
        if output_dir.exists():
            shutil.rmtree(output_dir)
        
        # Create fresh output folders
        os.makedirs(audio_dir)
        os.makedirs(script_dir)

        # Set environment variables
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["MODEL"] = llm_model

        # Inputs for Vocavoice
        inputs = {
            "language": language,
            "vocabulary_list": vocabulary_list,
            "topic": topic,
            "language_level": language_level,
            "voice_style": voice_style,
            "tts_model": tts_model,
            "tts_voice": tts_voice,
            "audio_path": config["output"]["audio_path"],
            "script_path": config["output"]["script_path"],
            "path_config": config["output"]["path_config"]
        }

        # Start Vocavoice
        Vocavoice().crew().kickoff(inputs=inputs)

        # Define output file paths
        _output = Path(config["output"]["path_config"]) / "paths_config.yaml"
        # Load the  file
        with open(_output, "r", encoding="utf-8") as file:
            _output_config = yaml.safe_load(file)


        return {
            "generated_script_file": _output_config["generated_script_file_full_path"],
            "generated_audio_file": _output_config["generated_audio_file_full_path"]
        }

    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
