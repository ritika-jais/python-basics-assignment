import datetime

def log_chat():
    
    with open('chat_log.txt', 'a') as log_file:
        print("Chat Logger started! Type 'exit' to end the chat.")
        
        while True:
            user_message = input("You: ")
            if user_message.lower() == 'exit':
                print("Chat ended. The conversation is saved.")
                break
            
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"{timestamp} - You: {user_message}\n")
            print(f"{timestamp} - You: {user_message}")

if __name__ == "__main__":
    log_chat()
