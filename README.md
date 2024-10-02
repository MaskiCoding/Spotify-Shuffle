# Spotify Shuffle

## Overview

Spotify Shuffle is a Python application that allows you to easily shuffle your Spotify playlists, enhancing your listening experience.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.12.6** or higher
- **Spotify Developer Account**

## Setup

Follow these steps to set up the project:

### Step 1: Clone the Repository

```bash
git clone git@github.com:MaskiCoding/Spotify-Shuffle.git
cd spotify-shuffle
```

### Step 2: Create a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the `.env` File

Create a `.env` file in the root directory of the project and add the following environment variables:

```plaintext
CLIENT_ID="your_client_id_here"
CLIENT_SECRET="your_client_secret_here"
REDIRECT_URI="http://localhost:8888/callback"
```

### Step 5: Obtain Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on "Create an App".
4. Fill in the required details and click "Create".
5. After creating the app, note your `CLIENT_ID` and `CLIENT_SECRET`.
6. Set the `REDIRECT_URI` to `http://localhost:8888/callback` in the app settings.

### Step 6: Run the Program

To start the application, navigate to the folder containing the Python files and run the main script:

```bash
cd src 
python main.py
```
## Creating an Executable File

To create an executable file from the Python script, follow these steps:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Create the executable**:
   ```bash
   pyinstaller --onefile src/main.py
   ```

3. **Find the executable**: The executable file will be located in the `dist` directory.

This will generate an executable file in the `dist` directory, which you can distribute and run on other machines without requiring a Python interpreter.

## Usage

After running the program, follow the prompts to shuffle your playlists. Enjoy discovering your music in a new way!

## Troubleshooting

If you encounter any issues:

- Ensure that your environment variables are correctly set.
- Check your internet connection.
- Refer to the [Spotify API documentation](https://developer.spotify.com/documentation/web-api/) for additional guidance.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Contact

For any questions or feedback, please reach out to [MaximilianLin@vivaldi.net](mailto:MaximilianLin@vivaldi.net).

