import os
import re
import requests
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QScrollArea
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
class EmailScraperGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Email-Scraper")
        self.setGeometry(100, 100, 750, 550)
        self.setStyleSheet("background-color:#03001C;")

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(30, 30, 30, 30)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        scroll_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(scroll_content)

        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)  

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Enter URL:")
        self.entry.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.entry.setStyleSheet("color: white;")

        self.scrape_btn = QPushButton("Scrape Email")
        self.set_button_style(self.scrape_btn)
        self.scrape_btn.clicked.connect(self.scrape_emails)

        self.save_btn = QPushButton("Save Email")
        self.set_button_style(self.save_btn)
        self.save_btn.clicked.connect(self.save_email)
        self.save_btn.setVisible(False)

        self.go_back_btn = QPushButton("Go Back")
        self.set_button_style(self.go_back_btn)
        self.go_back_btn.clicked.connect(self.go_back)
        self.go_back_btn.setVisible(False)

        layout.addWidget(self.entry)
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.scrape_btn)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.go_back_btn)
        scroll_content.setLayout(scroll_layout)
        list_box_style = "color:white;padding-left:5px; padding-top:10px;font-size:14px"
        scroll_content.setStyleSheet(list_box_style)
    def set_button_style(self, button):
        button_style = "color: white; background-color: #3E76EC; border: 1px solid #3E76EC; "
        button.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        button.setStyleSheet(button_style)


    def run(self):
        self.scroll_area.verticalScrollBar().setValue(0)  
        self.show()

    def scrape_emails(self):
        url = self.entry.text()
        scroll_layout = self.scroll_area.widget().layout()  

        if url:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
                    page_source = soup.get_text()
                    list_of_emails = re.findall(regex, page_source)

                    if not list_of_emails:
                        label = QLabel("Email Not Found.")
                        label.setFont(QFont("Arial", 14))
                        scroll_layout.addWidget(label)
                        self.save_btn.setVisible(False)
                        self.go_back_btn.setVisible(True)
                    else:
                        for i, email in enumerate(list_of_emails):
                            label = QLabel(f"{i + 1}: {email}")
                            label.setFont(QFont("Arial", 14))
                            scroll_layout.addWidget(label)

                        self.save_btn.setVisible(True)

                    self.scrape_btn.setVisible(False)
                    self.scroll_area.verticalScrollBar().setValue(0)

            except Exception as e:
                label = QLabel("Invalid URL")
                label.setFont(QFont("Arial", 14))
                scroll_layout.addWidget(label)
                self.go_back_btn.setVisible(True)
                self.scrape_btn.setVisible(False)

    def save_email(self):
        save_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        file_path = os.path.join(save_directory, "scraped_emails.txt")
        with open(file_path, "a") as file:
            scroll_layout = self.scroll_area.widget().layout()
            for i in range(scroll_layout.count()):
                widget = scroll_layout.itemAt(i).widget()
                if isinstance(widget, QLabel):
                    email_parts = widget.text().split(": ")
                    if len(email_parts) > 1:
                        email = email_parts[1]
                        file.write(email + "\n")

        QMessageBox.information(self, "Emails Saved", "Emails have been saved in the Downloads")
        self.save_btn.setVisible(False)
        self.go_back_btn.setVisible(True)

    def go_back(self):
        scroll_layout = self.scroll_area.widget().layout()
        while scroll_layout.count() > 0:
            item = scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.entry.setText("")
        self.scrape_btn.setVisible(True)
        self.save_btn.setVisible(False)
        self.go_back_btn.setVisible(False)
       
    def run(self):
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    email_scraper = EmailScraperGUI()
    email_scraper.run()
    app.exec()