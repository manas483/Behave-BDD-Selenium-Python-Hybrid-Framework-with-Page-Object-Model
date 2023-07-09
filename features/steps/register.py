from behave import *
from features.pages.homePage import HomePage
from features.pages.login import Login
from features.pages.register import RegisterPage
from utilities import emailGenerator


@given(u'I navigated to Register Page')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    context.homePage.click_on_my_account()
    context.registerPage = RegisterPage(context.driver)
    context.registerPage.click_on_register_option()
    context.myAccount = Login(context.driver)


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.registerPage.enter_first_name("row[first_name]")
        context.registerPage.enter_last_name("row[last_name]")
        valid_email = emailGenerator.get_new_email()
        context.registerPage.enter_telephone("row[telephone]")
        context.myAccount.enter_password("row[password]")
        context.registerPage.enter_confirm_password("row[password]")


@when(u'I click on Continue button')
def step_impl(context):
    context.registerPage.click_on_check_box()
    context.registerPage.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    context.registerPage.account_created_successfully_msg()


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.registerPage.enter_first_name("row[first_name]")
        context.registerPage.enter_last_name("row[last_name]")
        valid_email = emailGenerator.get_new_email()
        context.registerPage.enter_telephone("row[telephone]")
        context.myAccount.enter_password("row[password]")
        context.registerPage.enter_confirm_password("row[password]")


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.registerPage.enter_first_name("Manas Ranjan")
    context.registerPage.enter_last_name("Singdev sachan")
    context.registerPage.enter_telephone("12345")
    context.myAccount.enter_password("Manas@123")
    context.registerPage.enter_confirm_password("Manas@483")


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.registerPage.enter_first_name("Manas Ranjan")
    context.registerPage.enter_last_name("Singdev sachan")
    context.myAccount.enter_email("manaas@gmail.com")
    context.registerPage.enter_telephone("12345")
    context.myAccount.enter_password("Manas@123")
    context.registerPage.enter_confirm_password("Manas@483")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    context.registerPage.warning_msg()


@when(u'I dont enter anything into the field')
def step_impl(context):
    context.registerPage.enter_first_name("")
    context.registerPage.enter_last_name("")
    context.myAccount.enter_email("")
    context.registerPage.enter_telephone("")
    context.myAccount.enter_password("")
    context.registerPage.enter_confirm_password("")
