You can run this FastAPI app locally: **direct on your machine** 

---

1. **Run the `.env` file** with the minimum variables:
Note:- change the ENV to local 
```bash
TABLE_DESCRIPTOR=/Users/piyush.khadgi/PycharmProjects/chatbot_V2/tabledesc
ENV=local
LOG_LEVEL=DEBUG
ENABLE_PROFILER=false
AI_PROVIDER=openai
BOT_NAME=openai
BOT_SOURCE=slack
BOT_CHANNEL=C09330201G8
BOT_TOKEN=xoxb-426913680261-9076056573123-Ts9mL2iE3
BOT_SECRET_KEY=933ad09861725444e6d1b8c623195493
SELF_ID=U09281NGV3M
USER_ROLE="a growth analyst"
USER_CONTEXT="a fintech startup operating in retail lending in Phil"
AI_KEY=sk-proj-OBsEdyxt7bNAhlsiXhFJ9E2fyjUzpzk9qO3
OPENAI_API_KEY=sk-proj-OBsEdyxt7bNAhlsiXhFJ9E2fyjUzpzk9qO3
LLM_KEY=sk-proj-OBsEdyxt7bNAhlsiXhFJ9E2fyjUzpzk9qO3
```


2. **Create & activate a virtualenv**
```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -V
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install fastapi "uvicorn[standard]" python-dotenv pydantic
# plus anything your modules need (e.g., slack_sdk, httpx, openai, pyyaml, google-cloud-bigquery, etc.)
# or simply: pip install -r requirements.txt
```

4. **Create dependent folders**
```bash
mkdir -p /Users/piyush.khadgi/PycharmProjects/chatbot_V2/logs
touch /Users/piyush.khadgi/PycharmProjects/chatbot_V2/logs/slackbot.log
# plus anything your modules need (e.g., slack_sdk, httpx, openai, pyyaml, google-cloud-bigquery, etc.)
# or simply: pip install -r requirements.txt
```

5. **Run the app**
```bash
python main.py
# or explicitly:
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

6. **Test it**
```bash
curl -s http://127.0.0.1:8080/health
# -> {"status": "ok", "message": "Virtual Assistant API is healthy.\n"}

# Open the interactive docs:
# http://127.0.0.1:8080/docs
```

Note:- In case you get an error that something else is already listening on port 8080 use:-
```bash
kill -9 $(lsof -ti:8080)
```
