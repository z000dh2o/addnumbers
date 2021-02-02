
import uvicorn
from api import app

if __name__ == "__main__":

    print("Entering Main Method")
	uvicorn.run(app,
					host="0.0.0.0",
					port=8080)