
# Detailed Specification for Creating a Proof of Concept (PoC) for Reading Comprehension Skill Fine-Tuning Using AgentInstruct with WikiText-103

---

### **Introduction: What is AgentInstruct?**

**AgentInstruct** is an agentic framework designed to generate large, diverse, and high-quality synthetic datasets for fine-tuning language models (LLMs). This framework automates the process of creating instruction-response pairs from raw data sources like text documents or code files. The primary goal is to train models for specific skills, such as text comprehension, reasoning, and other complex tasks. The dataset creation process is automated using agentic flows, where specialized agents perform tasks like data transformation, question generation, and refinement.

The three key flows within AgentInstruct include:
1. **Content Transformation Flow**: Converts raw, unstructured data into structured formats, preparing it for question generation.
2. **Seed Instruction Generation Flow**: Produces diverse instructions (e.g., questions) based on the structured data.
3. **Instruction Refinement Flow**: Refines and increases the complexity and quality of generated instructions.

This PoC will use **WikiText-103**, a smaller and high-quality text corpus, to source raw seeds and apply these three flows to generate a dataset for fine-tuning reading comprehension tasks.

---

### **Goal**

The PoC will generate a fine-tuning dataset for reading comprehension using the **WikiText-103** dataset as the seed source. The project will employ multiple agents to transform raw text into structured forms, generate reading comprehension questions, and refine these questions for enhanced quality and complexity.

---

### **Components and Architecture Overview**

The system will consist of three primary flows:
1. **Content Transformation Flow**: This flow transforms raw text from WikiText-103 into structured formats using 9 agents.
2. **Seed Instruction Generation Flow**: Agents generate diverse reading comprehension questions from the structured data.
3. **Instruction Refinement Flow**: A suggester-editor pair increases the complexity and challenge of the generated questions.

---

### **Dataset: WikiText-103**

**WikiText-103** is a publicly available dataset derived from verified Wikipedia articles. It contains high-quality, clean text with a wide range of topics, making it ideal for generating diverse reading comprehension seeds.

- **Size**: Approximately **500 MB** (100 million tokens).
- **Content**: The text is already well-structured, including informative paragraphs, which simplifies the transformation process.
- **Access**: You can download WikiText-103 from [Hugging Face](https://huggingface.co/datasets/wikitext) or [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/wikitext).

#### Why Use WikiText-103?
- Smaller size compared to larger datasets like BookCorpus, making it easier to work with.
- High-quality content with a wide range of topics from Wikipedia, suitable for generating varied reading comprehension tasks.

---

### **Steps for Implementation**

#### 1. **Raw Seed Collection from WikiText-103**
- **Input**: Extract text paragraphs from WikiText-103. Each paragraph can serve as a "seed" for question generation.
- **Goal**: Prepare text data from WikiText-103 for transformation.
- **Preprocessing**: Minimal preprocessing like sentence splitting, paragraph segmentation, and tokenization may be necessary. Ensure text passages are clean and formatted for downstream agents.

---

#### 2. **Content Transformation Flow (9 Agents)**

- **Description**: This flow transforms raw text seeds into structured formats, such as argument passages, conversations, or transcripts. Structured content is easier to generate high-quality questions from.
- **Agents**:
   1. **Argument Passage Generator**: Converts text into structured arguments with claims and evidence.
   2. **Debate Generator**: Presents content in a debate format, highlighting opposing viewpoints.
   3. **Long Passage Generator**: Expands text into long, narrative-driven passages suitable for comprehension questions.
   4. **Meeting Transcript Generator**: Converts text into a multi-party discussion.
   5. **Poetry Generator**: Converts text into poems, adding a layer of abstract comprehension.
   6. **Satirical Content Generator**: Adds humor or sarcasm, enhancing inference-based comprehension tasks.
   7. **News Article Generator**: Formats text like a factual news article.
   8. **API List Generator**: Converts technical or factual data into a structured API-like list.
   9. **Conversation Generator**: Converts the text into a conversation format, simulating casual dialogue.

- **Output**: Structured content from the extracted text that can be used to generate reading comprehension instructions.

---

#### 3. **Seed Instruction Generation Flow (Agents for Reading Comprehension)**

- **Description**: This flow generates a variety of reading comprehension questions based on the structured text from the previous flow. These questions will evaluate different skills such as literal comprehension, inference, and reasoning.
- **Key Objective**: Implement 5 agents that generate different question types:
   1. **Literal Comprehension Agent**: Generates questions that ask for explicit information from the text.
   2. **Inference Agent**: Produces questions requiring readers to infer meaning beyond the given text.
   3. **Strengthen/Weaken Agent**: Evaluates a reader's ability to assess or modify the strength of arguments.
   4. **Summarization Agent**: Asks readers to summarize the passage.
   5. **Reasoning Agent**: Generates questions testing logical flow and critical thinking within the passage.

- **Output**: A set of (passage, question, answer) tuples that form the initial dataset.

---

#### 4. **Instruction Refinement Flow (Suggester-Editor Pair)**

- **Description**: This flow refines the generated instructions by increasing complexity or adding additional challenges. This involves suggesting distractors or introducing hypothetical conditions.
- **Agents**:
   - **Suggester Agent**: Proposes changes to increase the complexity of questions (e.g., misleading answer choices).
   - **Editor Agent**: Incorporates suggestions and refines the questions for higher complexity and challenge.
  
- **Example**:
   ```
   Original Question: What is hyperuricemia?
   Suggester Suggestion: Add a lifestyle-based distractor.
   Edited Question: What is hyperuricemia? 
   Answer Choices:
   A) A condition caused by low uric acid levels.
   B) A condition caused by high uric acid levels, often linked to poor lifestyle choices.
   C) A disease affecting only the joints.
   D) A condition unrelated to uric acid levels.
   Correct Answer: B) A condition caused by high uric acid levels, often linked to poor lifestyle choices.
   ```

- **Output**: Refined (passage, question, answer) pairs with increased complexity.

---

### **Technical Specifications for Developers**

#### 1. **Languages & Frameworks**
   - **Primary Language**: Python
   - **Frameworks**: OpenAI API or similar LLM tools for agent implementation.

#### 2. **Agents**
   - **Content Transformation Agents**: Implement 3 agents from the 9 available (Argument Passage Generator, Long Passage Generator, Debate Generator).
   - **Instruction Generation Agents**: Implement 5 key instruction generation agents for question diversity (Literal Comprehension, Inference, Strengthen/Weaken, Summarization, and Reasoning).
   - **Refinement Agents**: Implement a suggester-editor pair for instruction refinement.

#### 3. **Orchestration**
   - Develop an orchestrator to pass raw text seeds through the three flows (Transformation, Instruction Generation, Refinement).
   - Chain agents so that the output from one flow serves as input for the next.

#### 4. **Data Output**
   - **Output Format**: (Passage, Question, Answer) tuples in JSON or CSV format.
   ```json
   {
     "passage": "High uric acid levels are linked to cardiovascular diseases.",
     "question": "What condition is linked to high uric acid?",
     "answer": "Cardiovascular diseases."
   }
   ```

#### 5. **Testing**
   - Develop unit tests for each agent to ensure the correctness of outputs.
   - Implement evaluation metrics to assess the diversity and quality of the final dataset.

---

### **Deliverables**
1. Python scripts or notebooks implementing the PoC.
2. Generated fine-tuning dataset (JSON or CSV format).
3. Documentation detailing the agent interactions and system extensions.

---

This updated specification incorporates the use of **WikiText-103** as the primary data source, ensuring a manageable dataset size while maintaining high quality and variety for reading comprehension tasks.
