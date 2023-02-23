



print("Hello! How can I help you today?")
while True:
        user_input = input("You: ")
        
        if user_input.lower() == "hello" or user_input.lower() == "hi":
            print("Bot: Hello. Hope you’re having a good day. How can I help you?")
            
            
        elif user_input.lower() == "i want to order some flower?" or user_input.lower() == "order some flower?":
            print("Bot: What kind of flowers are you looking for?")
        
        
        elif user_input.lower() == "i am looking for white colored daisies" or user_input.lower() == "i am looking for yellow colored daisies" or user_input.lower() == "i am looking for lightpink colored daisies" or user_input.lower() == "i am looking for white colored roses" or user_input.lower() == "i am looking for yellow colored roses" or user_input.lower() == "i am looking for red colored roses" or user_input.lower() == "i am looking for white colored tulips" or user_input.lower() == "i am looking for red colored tulips" or user_input.lower() == "i am looking for yellow colored tulips"  or user_input.lower() == "i am looking for gold colored sunflower" or user_input.lower() == "i am looking for yellow colored sunflower" or user_input.lower() == "i am looking for orange colored sunflower":
            print("Bot:How many white Roses would you like to order? 4, 6 or 12?")
            
        
        elif user_input.lower() == "i do like 4 please" or user_input.lower() == "i do like 6 please" or user_input.lower() == "i do like 12 please" :
            print("Bot:Great! Just to confirm, your order is for 6 white Roses?")
            
             
        elif user_input.lower() == "yes this is correct":
            print("Bot: Thanks. Your order has been placed and will be shipped to you shortly. Have a great day.")
            
        
        elif user_input.lower() == "thank you":
            print("Bot: You’re welcome!")
            
            
        elif user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm sorry, I don't understand. Could you please rephrase your question?")
