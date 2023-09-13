# main

import uvicorn

###########################################################################################

if __name__ == "__main__":
    uvicorn.run("LuisChaverraCryptography.Application.WebApiCryptograpphy:app",
                host="127.0.0.1",
                port=8070,
                reload=True)
