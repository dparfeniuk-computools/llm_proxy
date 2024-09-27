# LLM Proxy Service

### Core idea

This service is going to handle HTTP requests which allow to get response from pre-trained LLM.

The application handles multiple types of **operations** :

1. research
2. finances
3. code-assistance

Each opeartion stands for separate 'domain' which means different operations used to resolve different problems.
Generally, each type of operation just adds additional prompt to the veriety

IMPORTANT: this proxy service is going to be used by other services at the same network. Which means that
each type of operation has its own strict type of response that includes LLM's output.

Technically the application workflow looks next:

1. request: `HTTP GET /research?q=how to learn vim`
2. response (not completed):

```json
{
    "result": {
        "tldr": "..."  // brief representation of output.
        "detailed": "..."  // rich representation of output.
        // ...
    }
}
```

### REST Resources

1. `HTTP GET /research` - specific prompts and data structures about research
2. `HTTP GET /finances` - specific prompts and data structures about **finantes**
   2.1 `HTTP GET /finances/analytics` - some sort of prompts that allows to get finances
   ...

### Backlog

- [ ] setup project (pip-tools, mypy, black, isort, flake8, pytest, pyproject.toml, pydantic, uvicorn, fastapi, gunicorn)
- [ ] create basic routes and data structures ...

Some details:

```sh
# files structure
├─ llm_proxy
    ├─ .env.example  # configurations
    ├─ .gitignore
    ├─ .dockerignore
    ├─ .flake8
    ├─ Makefile  # dev commands
    ├─ README.md
    ├─ pyproject.toml  # project metadata / dev-tools configuration
    ├─ Dockerfile
    ├─ docker-compose.yaml
    ├─ src
        ├─ main.py  # entrypoint
        ├─ config  # configuration proxy (pydantic-settings)
        ├─ rest
            ├─ research  # includes FastAPI routes and high-level business operations for each 'research' usecase
            ├─ finances  # ... 'finances' usecase
            └─ code_assistance  # ... 'code assistance' usecase
        ├─ domain
            ├─ research
            ├─ finances
            └─ code_assistance
        ├─ infrastructure
            ├─ application
                ├─ factory
                ├─ entities
                └─ ...
            └─ llm
                └─ service  # includes `LLMService` that allows make requests to the local LLM service
```
