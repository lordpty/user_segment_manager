# Snapchat Ad Platform User Segment Management

This Python program allows you to manage user segments in Snapchat's ad platform. You can push a list of user information to custom segments, store randomly generated user information, update existing segments, and display the segments.

## Features

- Add user information to custom segments.
- Update or refresh information in existing segments.
- Display all segments and their users.
- Easily extendable to push more segments by defining them.

## Requirements

- Python 3.x
- Access to the local file system

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Run the program:

    ```bash
    python main.py
    ```

## Usage

1. Upon running the program, you will be presented with a menu.
2. Choose options to add user information, update segments, display segments, or exit.
3. Follow the prompts to add or update user information.
4. Segments and user information will be saved to `user_data.txt`.

## Example

```bash
$ python main.py

1. Add User Information
2. Update User Information
3. Display Segments
4. Exit
Enter your choice: 1
Enter segment name: Segment1
User information added successfully!

1. Add User Information
2. Update User Information
3. Display Segments
4. Exit
Enter your choice: 3
Segment: Segment1
    {'Name': 'User1234', 'Age': 30, 'Gender': 'Male', 'Interests': ['Technology', 'Travel']}

