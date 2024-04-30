import random
import os

class UserSegment:
    def __init__(self):
        self.segments = {}

    def add_segment(self, segment_name, user_info):
        if segment_name not in self.segments:
            self.segments[segment_name] = [user_info]
        else:
            self.segments[segment_name].append(user_info)

    def update_segment(self, segment_name, user_info):
        if segment_name in self.segments:
            self.segments[segment_name].append(user_info)

    def display_segments(self):
        for segment_name, users in self.segments.items():
            print(f"Segment: {segment_name}")
            for user in users:
                print(f"\t{user}")

def generate_user_info():
    # Generate random user information
    name = f"User{random.randint(1000, 9999)}"
    age = random.randint(18, 65)
    gender = random.choice(['Male', 'Female', 'Other'])
    interests = random.sample(['Technology', 'Music', 'Sports', 'Travel', 'Food'], random.randint(1, 3))
    return {'Name': name, 'Age': age, 'Gender': gender, 'Interests': interests}

def main():
    user_segment = UserSegment()

    # Check if the data file exists and load the segments
    if os.path.exists('user_data.txt'):
        with open('user_data.txt', 'r') as file:
            for line in file:
                segment_name, user_info = line.strip().split(':')
                user_info = eval(user_info)  # Convert string representation to dictionary
                user_segment.add_segment(segment_name, user_info)

    while True:
        print("\n1. Add User Information\n2. Update User Information\n3. Display Segments\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            segment_name = input("Enter segment name: ")
            user_info = generate_user_info()
            user_segment.add_segment(segment_name, user_info)
            print("User information added successfully!")

        elif choice == '2':
            segment_name = input("Enter segment name to update: ")
            user_info = generate_user_info()
            user_segment.update_segment(segment_name, user_info)
            print("User information updated successfully!")

        elif choice == '3':
            user_segment.display_segments()

        elif choice == '4':
            # Save segments to file before exiting
            with open('user_data.txt', 'w') as file:
                for segment_name, users in user_segment.segments.items():
                    for user_info in users:
                        file.write(f"{segment_name}:{user_info}\n")
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

