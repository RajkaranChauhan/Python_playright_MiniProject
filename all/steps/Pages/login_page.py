import time

from playwright.sync_api import Page

from all.utils.data_read import DataRead


class login_page():

    def __init__(self, page:Page):
        self.page = page
        print(self.page)
        print("in login const")

    @property
    def txt_box_user_name(self):
        return self.page.get_by_placeholder("email@example.com")
    @property
    def txt_box_pass(self):
        return self.page.get_by_placeholder("enter your passsword")
    @property
    def dashboardPage(self):
        return self.page.get_by_text("Automation Practice")
    @property
    def btn_login(self):
        return self.page.get_by_role('button', name='Login')


    def navigate_to_application(self):
        self.page.goto("https://rahulshettyacademy.com/client")
        print("user in application")

    def enter_user(self, user):
        email=DataRead.data_from_file(user)
        print("****"+email)
        self.user = email
        self.txt_box_user_name.fill(self.user)


    def enter_pass(self, pas):
        pas = DataRead.data_from_file(pas)
        print("****" + pas)
        self.pas=pas
        self.txt_box_pass.fill(self.pas)


    def btn_login_clicked(self):
        # self.btn_login.click()
        self.btn_login.click()

    def app_login_success(self):
        print(self.dashboardPage.text_content())




