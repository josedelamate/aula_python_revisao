from fastapi import FastAPI
app = FastAPI()
orders = [
    { "codigo":1, "total": 150.00, "pagamento":"PIX" },
    { "codigo":2, "total": 150.00, "pagamento":"PIX" },

]

@app.get('/orders')
def getOrders():
    return orders

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

'''Para testes utilizar a Extensão 
   { REST Client for Visual Studio Code }
   criar o arquivo 'client.http'
   colocar o comando : GET http://localhost:8000/orders
   e clicar no link Send Request
'''