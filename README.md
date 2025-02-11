# Running the code

## Requirements
- python
- mysql

## Steps
- Clone repo
- In mysql workbench go to "File" → "Run SQL Script..." select the .sql file in the project
- Create venv in root of project
```bash
python -m venv venv
```
- run venv
```bash
venv\Scripts\activate
```
- install libraries
```bash
pip install -r requirements.txt
```
- Run
```bash
python management_inventory/interface.py 
```
