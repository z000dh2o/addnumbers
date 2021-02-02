from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from add_two_numbers import sum_two_numbers

title="REST API methods for performing addition of two numbers"
version="1.0"
description="Interface Specification for adding two numbers"

app = FastAPI(title=title,description=description,version=version)

class SumNumbers(BaseModel):
    first_number: int = Field(None)
    second_number: int = Field(None)

@app.post("/api/v1/operations/sum_numbers")
def sum_numbers(post_request_data: SumNumbers):
    print("Entered sum_numbers")
    return JSONResponse(status_code=200, content=sum_two_numbers(post_request_data.first_number, post_request_data.second_number))