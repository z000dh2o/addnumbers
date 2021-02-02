from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from add_two_numbers import sum_two_numbers
import uvicorn

title="REST API methods for performing addition of two numbers"
version="1.0"
description="Interface Specification for adding two numbers"

app = FastAPI(title=title,description=description,version=version)

if __name__ == "__main__":
	uvicorn.run(app,
					host="0.0.0.0",
					port=8080)

class SumNumbers(BaseModel):
    first_number: int = Field(None)
    second_number: int = Field(None)

@app.post("/api/v1/operations/sum_numbers")
def sum_numbers(post_request_data: SumNumbers):
    print("Entered sum_numbers")
    return JSONResponse(status_code=200, content=sum_two_numbers(SumNumbers.first_number, SumNumbers.second_number))