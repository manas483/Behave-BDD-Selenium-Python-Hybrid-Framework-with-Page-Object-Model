from behave import *

from features.pages.homePage import HomePage
from features.pages.login import Login
from utilities import emailGenerator


@given(u'I navigated to Login page')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    context.homePage.click_on_my_account()
    context.myAccount = context.homePage.click_on_login()


@when(u'I enter valid email as "{email}" and valid password as "{password}"into the fields')
def step_impl(context, email, password):
    context.myAccount.enter_email(email)
    context.myAccount.enter_password(password)


@when(u'I click on Login Button')
def step_impl(context):
    context.myAccount.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    context.myAccount.login_msg()


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    invalid_email = emailGenerator.get_new_email()
    context.myAccount.enter_email(invalid_email)
    context.myAccount.enter_password("Manas@123")


@then(u'I should get a proper warning message')
def step_impl(context):
    context.myAccount.warning_msg()


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.myAccount.enter_email("manas@gmail.com")
    context.myAccount.enter_password("1Manas@123")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.myAccount.enter_email("1manas@gmail.com")
    context.myAccount.enter_password("1Manas@123")


@when(u'I dont enter anything into email and password the fields')
def step_impl(context):
    context.myAccount.enter_email("")
    context.myAccount.enter_password("")
