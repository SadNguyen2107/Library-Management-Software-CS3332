# Library-Management-Software-CS3332

Sections:
1. <a href="#diagrams">Diagrams</a>
2. <a href="#diagrams">Diagrams</a>


## Diagrams:
**Database Diagram:**
1. <a href="./Diagrams/Database/EntityRelationshipDiagrams.md">Entity Relation Diagram</a>
2. <a href="./Diagrams/Database/mermaid-diagram-2024-08-10-235800.svg">PNG File</a>
3. <a href="./Diagrams/Database/mermaid-diagram-2024-08-10-235800.svg">SVG File</a>

**Model-View-Controller Diagrams:**
1. <a href="./Diagrams/Model-View-Controller/SequenceDiagrams.md">All the Features in the website</a>


## Steps to run project
Steps:
1. <a href="#step-1">Create Virtual Environment</a>
2. <a href="#step-2">Run the python virtual environment</a>
3. <a href="#step-3">Install the Project dependencies</a>


<details>
    <summary>
        <h3 id="step-1"><strong>Step 1: Create Virtual Environment</strong></h3>
    </summary>
    <p>Type the following in the command prompt, remember to navigate to where you want to create your project:</p>
    <p><strong>Windows:</strong></p>
    <pre><code>$ py -m venv .venv</code></pre>
    <p><strong>Unix/MacOS:</strong></p>
    <pre><code>$ python -m venv .venv</code></pre>
</details>

<details>
    <summary>
        <h3 id="step-2"><strong>Step 2: Run the python virtual environment</strong></h3>
    </summary>
    <p>Typing this command in the <code>Command Prompt</code>, <code>PowerShell</code> or <code>Bash</code></p>
    <p><strong>Command Prompt:</strong></p>
    <pre><code>$ .venv\Scripts\activate.bat</code></pre>
    <p><strong>PowerShell:</strong></p>
    <pre><code>$ .venv\Scripts\Activate.ps1</code></pre>
    <p><strong>Bash:</strong></p>
    <pre><code>$ source .venv/Scripts/activate</code></pre>
    <br>
    <p><strong>NOTE:</strong>To deactivate the python virtual environment in <code>Command Prompt</code>, type:</p>
    <pre><code>$ .venv\Scripts\deactivate.bat</code></pre>
</details>

<details>
    <summary>
        <h3 id="step-3"><strong>Step 3: Install the Project dependencies</strong></h3>
    </summary>
    <p>Use <code>pip</code> to install your project in the virtual environment:</p>
    <pre><code>$ pip install -e .</code></pre>
    <br>
    <p>This tells <code>pip</code> to find <i>pyproject.toml</i> in the current directory and install the project in editable or development mode</p>
</details>