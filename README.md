<p align="center">
  <h1 align="center">VocaVoice</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/serkanyasr/vocavoice?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
  <img src="https://img.shields.io/github/last-commit/serkanyasr/vocavoice?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/serkanyasr/vocavoice?style=default&color=0080ff" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/serkanyasr/vocavoice?style=default&color=0080ff" alt="repo-language-count">
</p>

---

## 📍 Overview

**VocaVoice** is an AI-powered vocabulary learning tool that generates podcast-style episodes tailored to your language level, voice preference, and chosen topic. Built with [CrewAI](https://docs.crewai.com), [OpenAI](https://openai.com/), and [Streamlit](https://streamlit.io/).

## 🎧 Demo

![UI Screenshot](path/to/screenshot.png)

[Listen to a sample podcast](link-to-audio.mp3)

## 🎯 Example Use Case

- You are an A2-level English learner and select English as your language.
- You choose the topic "Technology", pick a calm voice, and provide your personal vocabulary list.
- VocaVoice generates a podcast script, simplifies it based on your level, and produces an audio version for listening practice.


## ✨ Features

- 🧠 AI-generated scripts based on your selected topic and level
- 📜 Simplified vocabulary explanations
- 🎤 Text-to-speech podcast creation
- 📂 Auto-organized outputs (scripts + audio)
- 🌐 Web UI via Streamlit for non-technical users

---

---

## 🧱 Project Structure

```bash
vocavoice/
├── src/
│   └── vocavoice/
│       ├── config/           # Configuration files
│       ├── tools/            # Assistant tools
│       ├── ui/               # User interface components
│       ├── crew.py           # CrewAI configuration
│       ├── main.py           # Main application
│       └── ui_vocavoice.py   # Streamlit interface
├── tests/                    # Test files
├── pyproject.toml           # Project dependencies
└── README.md
```

---

## 🚀 Getting Started

### ☑️ Prerequisites

- Python >=3.10 <3.13
- UV (Dependency Management)

### ⚙️ Installation

First, install UV:

```bash
pip install uv
```

Navigate to your project directory and install dependencies:

```bash
# Clone the repository
❯ git clone https://github.com/serkanyasr/vocavoice
❯ cd vocavoice

# Install dependencies
❯ crewai install
```

### 🔧 Customization

**Add your `OPENAI_API_KEY` to the `.env` file**

- Modify `src/vocavoice/config/agents.yaml` to define your agents
- Modify `src/vocavoice/config/tasks.yaml` to define your tasks
- Modify `src/vocavoice/crew.py` to add your own logic, tools and specific args
- Modify `src/vocavoice/main.py` to add custom inputs for your agents and tasks



## 🤖 Running the Project

To start your VocaVoice agents and begin task execution, run this from the root folder:

```bash
❯ crewai run
```

This command initializes the VocaVoice crew, assembling the agents and assigning them tasks as defined in your configuration.

### Running with Streamlit Interface:
```bash
❯ streamlit run src/vocavoice/ui/streamlit_ui.py
```

## 🧠 Understanding Your Crew

The VocaVoice crew consists of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

---

## 🧪 Development / Contributing

- Fork the repo and create feature branches
- Submit a PR with a description of your changes
- Tag @serkanyasr in issues or PRs

---

## 🎗 License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENCE) file.

---
