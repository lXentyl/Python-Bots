from binance.client import Client
import time

# Tus claves de API de Binance
API_KEY = 'tu_api_key'
API_SECRET = 'tu_api_secret'

# Conexión con la API de Binance
client = Client(API_KEY, API_SECRET)

# Función para obtener el precio actual de un par de criptomonedas
def get_price(symbol):
    ticker = client.get_ticker(symbol=symbol)
    return float(ticker['lastPrice'])

# Función para realizar una compra
def buy(symbol, quantity):
    try:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print(f"Compra realizada: {order}")
    except Exception as e:
        print(f"Error al realizar la compra: {e}")

# Función para realizar una venta
def sell(symbol, quantity):
    try:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print(f"Venta realizada: {order}")
    except Exception as e:
        print(f"Error al realizar la venta: {e}")

# Estrategia de trading: compra si el precio baja un X% y vende si sube un Y%
def trading_bot(symbol, quantity, buy_price_threshold, sell_price_threshold):
    initial_price = get_price(symbol)
    print(f"Precio inicial para {symbol}: {initial_price}")
    
    while True:
        current_price = get_price(symbol)
        price_change = (current_price - initial_price) / initial_price * 100
        
        print(f"Precio actual: {current_price}, Cambio: {price_change:.2f}%")
        
        if price_change <= -buy_price_threshold:
            print(f"Precio ha bajado un {buy_price_threshold}%, comprando...")
            buy(symbol, quantity)
            initial_price = current_price  # Actualizamos el precio de referencia después de la compra
        elif price_change >= sell_price_threshold:
            print(f"Precio ha subido un {sell_price_threshold}%, vendiendo...")
            sell(symbol, quantity)
            initial_price = current_price  # Actualizamos el precio de referencia después de la venta
        
        time.sleep(60)  # Esperamos un minuto antes de comprobar de nuevo

# Parámetros del bot
symbol = 'BTCUSDT'  # Par de criptomonedas a operar
quantity = 0.001  # Cantidad a comprar/vender (en BTC, por ejemplo)
buy_price_threshold = 1.0  # Comprar si el precio baja un 1%
sell_price_threshold = 1.5  # Vender si el precio sube un 1.5%

# Ejecutamos el bot
if __name__ == "__main__":
    trading_bot(symbol, quantity, buy_price_threshold, sell_price_threshold)
