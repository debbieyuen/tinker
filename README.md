# tinker

## Setup
In Windows Powershell: 

Install `uv` for package management
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Then restart PowerShell and verify
```bash
uv --version
```
Create a virtual environment
```bash
uv venv
```
Activate the folder
```bash
.\.venv\Scripts\Activate.ps1
```
Install Tinker
```bash
uv pip install tinker
```
Then create a Tinker API key from the Tinker Console
```bash
$env:TINKER_API_KEY="your_actual_api_key_here"
```
