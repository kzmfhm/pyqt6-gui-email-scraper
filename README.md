## Email-Scraper 🐬

- An email scraper application built using the PyQt6 and beautifulsoup library in Python. 
- It allows users to enter a URL, scrape emails from the webpage's source code, and save the scraped emails to a file.
## Dependencies 🐋

- pyqt6: A custom module that provides  enhanced functionality for gui widgets.
- messagebox: A module from the pyqt6 library used to display messages and prompts to the user.
- os: A module for interacting with the operating system, used for file operations.
- re: A module for regular expressions, used for email pattern matching.
- requests: A library for making HTTP requests to retrieve the webpage source code.
- BeautifulSoup: A library for parsing HTML and XML documents, used for extracting information from the webpage source code.

## How to Run 🪼

- Clone the repository: git clone https://github.com/kzmfhm/pyqt6-gui-email-scraper
- Navigate to the project directory: cd gui-email-scraper
- Create a virtual environment (optional): python3 -m venv venv
- Activate the virtual environment:
        For Linux/Mac: source venv/bin/activate
        For Windows: venv\Scripts\activate.bat
- Install the required dependencies: pip install -r requirements.txt
- Run command in root directory: python3 main.py

## Usage 🦢

- Run the script in a Python environment.
- The GUI window titled "Email-Scraper" will appear.
- Enter a URL in the provided entry field "Enter Url"
- Click the "Scrape Email" button to start scraping emails from the webpage.
- If emails are found, they will be displayed in the scrollable frame.
- Click the "Save Email" button to save the scraped emails to a file named "scraped_emails.txt" in the Downloads.
- A message box will appear, confirming that the emails have been saved.
- Click the "Go Back" button to reset the application and enter a new URL.
- If email is not found on website page then a message is appear "Email not Found" on window scrollable frame and Go Back button will also appear that allow user to enter another url to continue process.
- if user enter invalid url accidently then "Invalid Url" message will also appear on scrollable window frame.

## ⭐️ Support

Give a ⭐️ if this project helped you!

## License ©

[The MIT License](LICENSE)
