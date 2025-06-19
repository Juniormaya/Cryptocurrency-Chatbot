class Cryptocurrencychatbot: 
    def __init__(self):
        self.name = "Cryptosage"
        self.description = "A chatbot that provides information about cryptocurrencies."
        self.rules = {
            "hi there": "Hello! I'm Cryptosage, your professional yet approachable AI assistant for cryptocurrency investment insights. How can I help you today?",
            "hello": "Hi! I'm Cryptosage, your go-to AI assistant for all things cryptocurrency. What would you like to know?",
            "bye": "Goodbye! If you have more questions in the future, feel free to ask. Please note, I provide general advice based on the information you provide and my pre-programmed rules. Always do your own research before investing! Have a great day!",
            "help": "I'm here to assist you with any questions about cryptocurrencies. You can ask me about Bitcoin, Ethereum, how to buy cryptocurrencies, and more. Just type your question!",
        }

    def respond(self, user_input):
            user_input = user_input.lower()
            for key in self.rules:
                if key in user_input:
                    return self.rules[key]
            return "I'm sorry, I don't have information on that topic."

# Example of a simple cryptocurrency database
crypto_db = {
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}  
# Profitability logic
def calculate_profitability(crypto_name):
    if crypto_name in crypto_db:
        crypto = crypto_db[crypto_name]
        if crypto["price_trend"] == "rising":
            if crypto["market_cap"] == "high":
                return f"Investing in {crypto_name} is likely to be profitable. Your investment could grow significantly."
            elif crypto["market_cap"] == "medium":
                return f"Investing in {crypto_name} could be profitable, but with moderate growth potential."
            else:
                return f"{crypto_name} is rising but has a low market cap. Consider the risks before investing."
        elif crypto["price_trend"] == "stable":
            return f"{crypto_name} is stable. Your investment is likely to maintain its value."
        else:
            return f"{crypto_name} is not currently a profitable investment. Consider other options."
    else:
        return "Cryptocurrency not found in the database."

# Sustainability logic
def evaluate_sustainability(crypto_name):
    if crypto_name in crypto_db:
        crypto = crypto_db[crypto_name]
        score = crypto["sustainability_score"]
        if score > 7/10 and crypto["energy_use"] == "low":
            return f"{crypto_name} is a sustainable choice with a score of {score}"
        elif score > 4/10:
            return f"{crypto_name} has moderate sustainability with a score of {score}"
        else:
            return f"{crypto_name} has low sustainability with a score of {score}. Consider alternatives."
    else:
        return "Cryptocurrency not found in the database." 

# Helper to map user input to the correct crypto name
def get_crypto_key(user_input):
    user_input = user_input.strip().lower()
    for key in crypto_db.keys():
        if user_input == key.lower():
            return key
    return None

# Example usage
chatbot = Cryptocurrencychatbot()
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Cryptosage: Goodbye! If you have more questions in the future, feel free to ask.")
        break

    available_cryptos = ", ".join(crypto_db.keys())

    # Check if user wants profitability or sustainability info
    if "profit" in user_input.lower():
        crypto_name = input(f"Which cryptocurrency? ({available_cryptos}): ")
        crypto_key = get_crypto_key(crypto_name)
        if crypto_key:
            print("Cryptosage:", calculate_profitability(crypto_key))
        else:
            print("Cryptosage: Cryptocurrency not found in the database.")
    elif "sustainability" in user_input.lower():
        crypto_name = input(f"Which cryptocurrency? ({available_cryptos}): ")
        crypto_key = get_crypto_key(crypto_name)
        if crypto_key:
            print("Cryptosage:", evaluate_sustainability(crypto_key))
        else:
            print("Cryptosage: Cryptocurrency not found in the database.")
    else:
        # Try to match direct crypto name input
        crypto_key = get_crypto_key(user_input)
        if crypto_key:
            print("Cryptosage:", calculate_profitability(crypto_key))
            print("Cryptosage:", evaluate_sustainability(crypto_key))
        else:
            print("Cryptosage:", chatbot.respond(user_input))
