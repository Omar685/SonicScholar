from src.ui.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import ( QMainWindow )
from src.utils.server import check_server_work
from src.modules.database import DatabaseManegar
import requests
import os

BASE_URL = "http://127.0.0.1:3000"

class SonicScholar(QMainWindow):
  def __init__(self):
    super(SonicScholar, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # connect database
    self.connect = DatabaseManegar.Data_Pers(os.path.join("data", "info.db"))
    # self.connect.create_table_userinfo()
    # self.connect.insert_or_update_user(table_name="user_info", username="...", email="...", password="...")

    username, password = self.connect.get_data("user_info")
    if username == "..." or password == "...":
      self.switch(self.ui.main_loginPage)
    else:
      self.switch(self.ui.main_mainPage)
    
    # check server work
    self.check = check_server_work(BASE_URL)
    if self.check:
      self.work = True
    else:
      self.work = False
    
    # siwtch page from login to register
    self.ui.registerBtn.clicked.connect(lambda: self.ui.loginStackedWidget.setCurrentWidget(self.ui.register_page_widget))
    # siwtch page from register to login
    self.ui.alreadyloginBtn.clicked.connect(lambda: self.ui.loginStackedWidget.setCurrentWidget(self.ui.login_page_widget))
    # Create Button clicked
    self.ui.createBtn.clicked.connect(self.create_account)
    # Login Button clicked
    self.ui.loginBtn.clicked.connect(self.login)

  def switch(self, widget_page):
    self.ui.stackedWidget.setCurrentWidget(widget_page)
  
  def passw_confirm(self):
    password = self.ui.input_password_register.text()
    password_confirm = self.ui.conf_password_register.text()

    if password == password_confirm: return True
    else: return False

  def create_account(self):
    global BASE_URL
    username = self.ui.input_username_register.text()
    email = self.ui.input_email_register.text()
    password = self.ui.input_password_register.text()

    if self.passw_confirm():
      data = {"username": username,"email": email, "password": password}
      if self.work == True:
        try:
          response = requests.post(f"{BASE_URL}/add_user", json=data)
          if response.status_code == 200:
            self.connect.insert_or_update_user(table_name="user_info", username=username, email=email, password=password)
            self.switch(self.ui.main_mainPage)
          elif response.status_code == 400:
            response_data = response.json()
            self.ui.errorLabel_register.setText(f"Error: {response_data['message']}")
            self.ui.errorLabel_register.setStyleSheet("color: red;")
          else:
            self.ui.errorLabel_register.setText("Error")
            self.ui.errorLabel_register.setStyleSheet("color: red;")
        except requests.exceptions.RequestException as e:
          self.ui.errorLabel_register.setText("try later!")
          self.ui.errorLabel_register.setStyleSheet("color: red;")
      else:
        self.ui.errorLabel_register.setText("The server stoped. try later!")
        self.ui.errorLabel_register.setStyleSheet("color: red;")
    else:
      self.ui.errorLabel_register.setText("The password does not match")
      self.ui.errorLabel_register.setStyleSheet("color: red;")

  def login(self):
    global BASE_URL
    email = self.ui.input_email.text()
    password = self.ui.input_password.text()
    data = {"email": email, "password": password}
    if self.work == True:
      try:
        response = requests.post(f"{BASE_URL}/check_user", json=data)
        if response.status_code == 200:
          self.connect.insert_or_update_user(table_name="user_info", email=email, password=password)
          self.switch(self.ui.main_mainPage)
        elif response.status_code == 400:
          response_data = response.json()
          self.ui.errorLabel.setText(f"Error: {response_data['message']}")
          self.ui.errorLabel.setStyleSheet("color: red;")
        else:
          self.ui.errorLabel_register.setText("Error")
          self.ui.errorLabel_register.setStyleSheet("color: red;")
      except requests.exceptions.RequestException as e:
        self.ui.errorLabel.setText("try later!")
        self.ui.errorLabel.setStyleSheet("color: red;")
    else:
      self.ui.errorLabel.setText("The server stoped. try later!")
      self.ui.errorLabel.setStyleSheet("color: red;")