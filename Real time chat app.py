class ChatRoom:
    def __init__(self, room_id):
        self.room_id = room_id
        self.messages = []
        self.active_users = []

    def send_message(self, user, message):
        self.messages.append(f"{user}: {message}")

    def add_user(self, user):
        self.active_users.append(user)
    def display_messages(self):
        for message in self.messages:
            print(message)

    def display_active_users(self):
        for user in self.active_users:
            print(user)
    def main (self):
        # Get user input
        room_id = input("Enter Chat Room ID (e.g., Room123): ")
        messages_input = input("Enter Messages (e.g., 'Hello, everyone!', 'How's it going?', 'Goodbye!'): ")
        active_users_input = input("Enter Active Users (e.g., ['Alice', 'Bob', 'Charlie']): ")

        # Parse user input
        messages = messages_input.split(', ')
        active_users = active_users_input.strip('][').split(', ')

        # Create a chat room with the specified ID
        chat_room = ChatRoom(room_id)

        # Add active users to the chat room
        for user in active_users:
            chat_room.add_user(user.strip("'"))

        # Send messages in the chat room
        for message in messages:
            user, message = message.split(': ')
            chat_room.send_message(user.strip("'"), message.strip("'"))

        # Display messages and active users
        print("Chat Messages:")
        chat_room.display_messages()
        print("Active Users:")
        chat_room.display_active_users()

    if __name__ == "__main__":
        main()
