from behave import *

from features.pages.homePage import HomePage


@given(u'I goto navigated to home page')
def step_impl(context):
    context.homePage = HomePage(context.driver)
    expected_title = "Your Store"


@when(u'I entered valid product say "{product}" into the search box')
def step_impl(context, product):
    context.homePage.search_product_by_name(product)


@when(u'I click on Search button')
def step_impl(context):
    context.homePage.click_on_search_button()


@then(u'Valid product should get displayed in the search result')
def step_impl(context):
    context.homePage.valid_product_displayed()


@when(u'I entered invalid product say "{product}" into the search box')
def step_impl(context, product):
    context.homePage.search_product_by_name(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    context.homePage.proper_error_msg_displayed()


@when(u'I dont enter anything into the search box')
def step_impl(context):
    context.homePage.search_product_by_name("")
