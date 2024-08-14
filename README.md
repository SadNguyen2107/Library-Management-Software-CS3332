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
4. <a href="#step-4">Create folder instance/</a>
5. <a href="#step-5">Create file .env</a>
6. <a href="#step-6">Setup the database to run</a>
7. <a href="#step-7">Run the program</a>


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

<details>
    <summary>
        <h3 id="step-4"><strong>Step 4: Create folder instance/</strong></h3>
    </summary>
    <p>Create a folder named <b>instance/</b> this directory (same as this README.md file) or type the following command:</p>
    <pre><code>$ mkdir instance</code></pre>
</details>

<details>
    <summary>
        <h3 id="step-5"><strong>Step 5: Create file .env </strong></h3>
    </summary>
    <p>Step 1: Create a file named <b>.env</b> in folder <b>instance/</b> you just created</p>
    <pre><code>$ flask --app src init-db</code></pre>
    <br>
    <p>Insert some data of your own in the { } curly brackets</p>
    <pre><code>SECRET_KEY="{ your_own_random_key }"
DATABASE="{ absolute path to the database file }"
SQLALCHEMY_DATABASE_URI = "sqlite:///{ absolute path to the database file }"
SQLALCHEMY_TRACK_MODIFICATION="False"</code></pre>
</details>

<details>
    <summary>
        <h3 id="step-6"><strong>Step 6: Setup database to run</strong></h3>
    </summary>
    <p>Step 1: Use this command to initialize the database:</p>
    <pre><code>$ flask --app src init-db</code></pre>
    <br>
    <p>Step 2: Use this command to insert some fake data into the database:</p>
    <pre><code>$ flask --app src insert-db</code></pre>
    <br>
    <p><strong>Note*:<strong> Use this command to drop all the tables (included all the data) in the database:</p>
    <pre><code>$ flask --app src drop-db</code></pre>
    <br>
</details>


<details>
    <summary>
        <h3 id="step-7"><strong>Step 7: Run the program</strong></h3>
    </summary>
    <p>Step 1: Use this command to run the program:</p>
    <pre><code>$ flask --app src run --debug</code></pre>
    <br>
    <p>Step 2: Open your web browser and type in the url:</p>
    <pre><code>http://127.0.0.1:5000</code></pre>
</details>