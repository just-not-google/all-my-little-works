import telebot
import requests
import json
from typing import Dict, Tuple, Optional

TOKEN = "7737702051:AAFWt_2pJTVys6DIZRmQcIJoY6WpeRCGnD0"
bot = telebot.TeleBot(TOKEN)

keys = {
    "биткоин": "BTC", "биток": "BTC", "btc": "BTC",
    "эфириум": "ETH", "эфир": "ETH", "eth": "ETH",
    "рипл": "XRP", "xrp": "XRP",
    "лайткоин": "LTC", "лайт": "LTC", "ltc": "LTC",
    "кардано": "ADA", "ada": "ADA",
    "солана": "SOL", "sol": "SOL",
    "доллар": "USD", "доллары": "USD", "usd": "USD",
    "евро": "EUR", "eur": "EUR",
    "фунт": "GBP", "фунты": "GBP", "gbp": "GBP",
    "иена": "JPY", "йена": "JPY", "jpy": "JPY",
    "франк": "CHF", "chf": "CHF",
    "рубль": "RUB", "рубли": "RUB", "ruble": "RUB", "rub": "RUB"
}

class CurrencyConverter:
    def __init__(self):
        self.cache = {}
        self.cache_timeout = 300
    
    def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        cache_key = f"{from_currency}_{to_currency}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            response = requests.get(
                f"https://min-api.cryptocompare.com/data/price?fsym={from_currency}&tsyms={to_currency}",
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            if to_currency in data and data[to_currency]:
                rate = data[to_currency]
                self.cache[cache_key] = rate
                return rate
                
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
        except json.JSONDecodeError as e:
            print(f"JSON Error: {e}")
        
        return None

converter = CurrencyConverter()

@bot.message_handler(commands=['start', 'help'])
def welcome_command(message):
    welcome_text = """
💰 *BROTHER_42_FOUNDATION - Конвертер валют и криптовалют* 💰

*Доступные команды:*
/start - Начало работы
/help - Помощь
/values - Список валют
/convert - Быстрая конвертация

*Форматы ввода:*
1. Через команду /convert
2. Текст: Биткоин Доллар 1.5
3. Текст: BTC USD 0.5

*Примеры:*
• `/convert BTC USD 1`
• `Эфириум Рубль 2`
• `SOL EUR 10`
    """
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['values'])
def all_values(message):
    crypto_currencies = {
        "Биткоин": ["BTC", "биткоин", "биток"],
        "Эфириум": ["ETH", "эфириум", "эфир"],
        "Рипл": ["XRP", "рипл"],
        "Лайткоин": ["LTC", "лайткоин", "лайт"],
        "Кардано": ["ADA", "кардано"],
        "Солана": ["SOL", "солана"]
    }
    
    fiat_currencies = {
        "Доллар": ["USD", "доллар"],
        "Евро": ["EUR", "евро"],
        "Фунт": ["GBP", "фунт"],
        "Иена": ["JPY", "иена"],
        "Франк": ["CHF", "франк"],
        "Рубль": ["RUB", "рубль"]
    }
    
    response = "*💎 Криптовалюты:*\n"
    for name, variants in crypto_currencies.items():
        response += f"• {name} ({', '.join(variants)})\n"
    
    response += "\n*💵 Фиатные валюты:*\n"
    for name, variants in fiat_currencies.items():
        response += f"• {name} ({', '.join(variants)})\n"
    
    response += "\n*💡 Подсказка:* Можно использовать как русские названия, так и международные коды!"
    
    bot.send_message(message.chat.id, response, parse_mode='Markdown')

@bot.message_handler(commands=['convert'])
def convert_command(message):
    try:
        args = message.text.split()[1:]
        if len(args) != 3:
            bot.reply_to(message, "❌ *Использование:* /convert <из валюты> <в валюту> <количество>", parse_mode='Markdown')
            return
        
        process_conversion(message, args[0], args[1], args[2])
        
    except Exception as e:
        bot.reply_to(message, "❌ Произошла ошибка при обработке команды. Проверьте правильность ввода.")

def process_conversion(message, from_curr: str, to_curr: str, amount_str: str):
    try:
        amount = float(amount_str.replace(',', '.'))
    except ValueError:
        bot.reply_to(message, f"❌ '{amount_str}' - неверный формат количества. Используйте числа.")
        return
    
    if amount <= 0:
        bot.reply_to(message, "❌ Количество должно быть положительным числом.")
        return
    
    from_curr_lower = from_curr.lower()
    to_curr_lower = to_curr.lower()
    
    if from_curr_lower not in keys:
        bot.reply_to(message, f"❌ Валюта '{from_curr}' не найдена. Используйте /values для списка валют.")
        return
    
    if to_curr_lower not in keys:
        bot.reply_to(message, f"❌ Валюта '{to_curr}' не найдена. Используйте /values для списка валют.")
        return
    
    from_code = keys[from_curr_lower]
    to_code = keys[to_curr_lower]
    
    if from_code == to_code:
        bot.reply_to(message, f"✅ {amount} {from_curr} = {amount} {to_curr} (одинаковые валюты)")
        return
    
    rate = converter.get_exchange_rate(from_code, to_code)
    
    if rate is None:
        bot.reply_to(message, "❌ Не удалось получить курс валют. Попробуйте позже.")
        return
    
    result = rate * amount
    
    response = f"""
💱 *Результат конвертации:*

*{amount:.8f} {from_curr.upper()} → {result:.2f} {to_curr.upper()}*

📊 *Курс:* 1 {from_code} = {rate:.6f} {to_code}
🕒 *Обновлено:* в реальном времени
    """
    
    bot.reply_to(message, response, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    try:
        parts = message.text.strip().split()
        
        if len(parts) == 3:
            from_curr, to_curr, amount = parts
            process_conversion(message, from_curr, to_curr, amount)
        else:
            bot.reply_to(message, 
                        "❌ *Неверный формат!*\n\n"
                        "✅ *Правильные форматы:*\n"
                        "• `Биткоин Доллар 1`\n"
                        "• `BTC RUB 0.5`\n"
                        "• `/convert ETH EUR 2`", 
                        parse_mode='Markdown')
                        
    except Exception as e:
        bot.reply_to(message, "❌ Произошла непредвиденная ошибка. Попробуйте еще раз.")

if __name__ == "__main__":
    print("Бот запущен...")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
