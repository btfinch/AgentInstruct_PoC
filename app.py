from flask import Flask, render_template, request, jsonify
from src.utils.data_utils import get_preprocessed_paragraphs
from src.agents.transformation import ArgumentPassageGenerator, LongPassageGenerator, DebateGenerator
from src.agents.instruction_generation import (
    LiteralComprehensionAgent, InferenceAgent, StrengthenWeakenAgent,
    SummarizationAgent, ReasoningAgent
)
from src.agents.refinement import SuggesterAgent, EditorAgent
import random
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Initialize agents
transformation_agents = {
    "ArgumentPassageGenerator": ArgumentPassageGenerator(api_key),
    "LongPassageGenerator": LongPassageGenerator(api_key),
    "DebateGenerator": DebateGenerator(api_key)
}

instruction_agents = {
    "LiteralComprehensionAgent": LiteralComprehensionAgent(api_key),
    "InferenceAgent": InferenceAgent(api_key),
    "StrengthenWeakenAgent": StrengthenWeakenAgent(api_key),
    "SummarizationAgent": SummarizationAgent(api_key),
    "ReasoningAgent": ReasoningAgent(api_key)
}

suggester_agent = SuggesterAgent(api_key)
editor_agent = EditorAgent(api_key)

# Load paragraphs
paragraphs = get_preprocessed_paragraphs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_paragraph')
def get_random_paragraph():
    return jsonify({"paragraph": random.choice(paragraphs)})

@app.route('/transform', methods=['POST'])
def transform():
    data = request.json
    paragraph = data['paragraph']
    agent_name = data['agent']
    agent = transformation_agents[agent_name]
    transformed = agent.generate_response(f"Transform this text: {paragraph}")
    return jsonify({"transformed": transformed})

@app.route('/generate_instruction', methods=['POST'])
def generate_instruction():
    data = request.json
    paragraph = data['paragraph']
    agent_name = data['agent']
    agent = instruction_agents[agent_name]
    instruction = agent.generate_response(f"Generate a question for this text: {paragraph}")
    return jsonify(instruction)

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    suggestion = suggester_agent.generate_response(data['passage'], data['question'], data['answer'])
    return jsonify({"suggestion": suggestion})

@app.route('/edit', methods=['POST'])
def edit():
    data = request.json
    edited = editor_agent.generate_response(data['passage'], data['question'], data['answer'], data['suggestion'])
    return jsonify(edited)

if __name__ == '__main__':
    app.run(debug=True)