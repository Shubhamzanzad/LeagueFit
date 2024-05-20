from fastapi import FastAPI, File, UploadFile, HTTPException,Response
import pandas as pd
from fastapi.responses import JSONResponse
import uvicorn
import logging
import os

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'app.log'),
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
app = FastAPI()

@app.get("/getDf")
def _getDf():
    path = "./data.csv"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    logging.info("Sending dataframe")
    with open(path, 'r') as file:
        csv =  file.read()
        return Response(content=csv, media_type="text/csv")

@app.post("/addPlayer")
def _addPlayer(file: UploadFile = File(...)):
    logging.info("adding player to dataframe")
    try:
        file_location = f"/app/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

@app.get("/check")
def _test():
    df = pd.read_csv("./data.csv")
    return df.iloc[-1]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)