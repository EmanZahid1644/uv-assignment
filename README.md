# Assignment 02 - Python UV Projects Collection

This repository contains multiple Python projects developed using **uv** and modern Python development practices. The projects demonstrate package creation, application execution, simple Python functionality, and AI agent integration using Google's Gemini model.

## 📂 Projects Included

### 1. Packaged App

A packaged Python application created using **uv** with the **src layout** structure.

#### Features

- Displays student information:
  - Name: Eman Zahid
  - PIAIC Registration Number: PIAIC259328
- Defines two numbers
- Displays both numbers
- Checks whether the numbers are equal

#### Run the Application

```bash
uv run main
```

---

### 2. Simple App

A basic Python application created using **uv**.

#### Features

- Displays student information:
  - Name: Eman Zahid
  - PIAIC Registration Number: PIAIC259328
- Takes two numbers
- Calculates and displays the difference between them

#### Run the Application

```bash
uv run python main.py
```

---

### 3. Gemini Agent Example

A conversational AI agent built using the **OpenAI Agents Framework** and **Google Gemini 2.5 Flash** through an OpenAI-compatible API.

#### Features

- Loads API keys securely using `.env`
- Uses `AsyncOpenAI`
- Connects to Gemini 2.5 Flash
- Demonstrates AI agent interaction
- Restricts responses to a single line
- Uses asynchronous execution

#### Requirements

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

#### Run the Agent

```bash
uv run python main.py
```

---

## 🛠️ Technologies Used

- Python
- uv Package Manager
- OpenAI Agents Framework
- Google Gemini 2.5 Flash
- AsyncOpenAI
- python-dotenv

---

## 📁 Repository Structure

```text
Assignment-02/
│
├── packaged-app/
│   ├── src/
│   ├── pyproject.toml
│   └── README.md
│
├── simple-app/
│   ├── main.py
│   ├── pyproject.toml
│   └── README.md
│
├── gemini-agent-example/
│   ├── main.py
│   ├── .env
│   ├── pyproject.toml
│   └── README.md
│
└── README.md
```

---

## 🎯 Learning Objectives

This assignment demonstrates:

- Python project management using uv
- Packaging applications with src layout
- Running Python applications through uv
- Environment variable management with dotenv
- Building AI agents using modern frameworks
- Integrating Google Gemini models with OpenAI-compatible APIs
- Working with asynchronous Python programming

---

## 👨‍💻 Author

**Eman Zahid**  
PIAIC Registration Number: **PIAIC259328**

---

## 📜 License

This project is created for educational purposes as part of the PIAIC coursework.
