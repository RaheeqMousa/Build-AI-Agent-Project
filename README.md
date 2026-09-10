# Build AI Agent
This project is a Command-Line AI agent with Python and OpenRouter
The program takes a prompt user wrote in the terminal, sends it to an AI model through OpenRouter, 
and finally prints the response

## Requirements
- Python 3
- uv
- OpenRouter API Key

## How it works
The program requires a user prompt:
Example: uv run main.py "Talk about Mount Everest, no more than one paragraph"
Then, the AI response will be printed in the terminal

The agent follows a feedback loop as follow:

The agents uses Four tools:
- get_files_info which lists files and dictionaries
- get_file_content which reads file contents
- write_file which overwrites contents or creates of a file
- run_python_file which runs python file ans return the result
All tools' results are added back to the conservation "messages variable" so the LLM can use them in the next iteration
Also, the agent is limited to 20 iterations to prevent an infinite loops.

```mermaid
flowchart LR
  A["User Prompt"]
  B["main.py"]
  C["LLM using OpenRouter"]
  D{"Tool needed?"}
  E["Finished"]
  F["call_function.py"]
  G["get_file_info.py"]
  H["get_file_content.py"]
  I["write_file.py"]
  J["run_python_file.py"]
  K["Tool result"]

  A --> B
  B --> C
  C --> D

  D --"no?"--> E
  D --"yes?"--> F

  F --> G
  F --> H
  F --> I
  F --> J

  G --> K
  H --> K
  I --> K
  J --> K

  K --> C
```

## Example of Fixing a Bug
Suppose the user gives the agent:
Fix the bug: 3 + 7 * 2 shouldn't be 20.
The agent can reason through the project using its tools.

```mermaid
flowchart LR
    A["Task<br/>3+7*2 should not be 20"]
    B["get_files_info"]
    C["get_file_content"]
    D["Identity bug<br>+ precedence set to 3"]
    E["write_file"]
    F["run_python_file"]
    G["verify result is 17"]
    H["Final response"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
```

## Configuration
Create a .env file and put inside it you OpenRouter API Key as
OPENROUTER_API_KEY=your_api_key_here
And be sure to be included in .gitignore file.
