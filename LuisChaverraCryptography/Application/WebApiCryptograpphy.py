#Creación de la WebApi

from fastapi import FastAPI
from LuisChaverraCryptography.Core.Security.Decrypt.DESDecode import DESDecode
from LuisChaverraCryptography.Core.Security.Encrypt.DESEncode import DESEncode

app: FastAPI = FastAPI(title='SOAP Python Cryptography', description='USBSI 2023-02')

@app.get("/DESEncode", summary="DES Encrypt", description="Codificado en DES", tags=["DES"])
async def DESEncode(Data: str | None = None, user_key: str | None = None):
    encrypted_data: str | None = None
    try:
        ##desencode = DESEncode()
        ##encrypted_data = desencode.encrypt(Data, key)
        if len(user_key) != 8:
            encrypted_data = "Codificación interrumpida, la clave debe tener 8 bytes"
        else:
            key = user_key.encode()
            desencode = DESEncode()
            encrypted_data = desencode.encrypt_data(Data, key)

    except:
        encrypted_data = "Codificación no exitosa"

    return encrypted_data


@app.get("/DESDecode", summary="DES Decrypt", description="Decodificado en DES",tags=["DES"])
async def DESDecode(encrypted_data: str | None = None, key: str | None = None):
    plaint_data: str | None = None
    try:
        desdecode = DESDecode()
        plaint_data = desdecode.decrypt(encrypted_data, key)
    except:
        plaint_data = "Decodificación fallida"
    return plaint_data
