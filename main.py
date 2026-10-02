from fastapi import FastAPI

app = FastAPI(title="eval_python_svc_1790929970")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "eval_python_svc_1790929970", "owner": "eval_team_1790929970"}
