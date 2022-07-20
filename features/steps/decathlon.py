from behave import step

from pageobjects.pesas_mancuernas import DecathPesasMancuernas


@step('I navigate to "{url}" URL for "{resource}" web page')
def navigate_to_url(context, url, resource):
    context.url = url
    context.driver.get(url)

    # Set up correct PageObject depending on the resource accessed by the user
    context.current_page = globals()[resource](context.driver)

    # Avoid certificate checking if necessary
    if context.driver.title in ['Certificate Error: Navigation Blocked', 'This site isn’t secure',
                                'Error de certificado: navegación bloqueada', 'Este sitio no es seguro.']:
        context.driver.execute_script("document.getElementById('overridelink').click();")

@step('I wait for page "{page_name}" completely loaded')
def wait_for_page_loaded(context, page_name):
    """
    Waiting for page is completely loaded
    """
    context.current_page = globals()[page_name](context.driver)
    context.current_page.wait_until_loaded(timeout=5)

@step('the item is available to purchase')
def wait_for_page_loaded(context):
    """

    :param context:
    :return:
    """
    DecathPesasMancuernas(context.driver).accept_cookies()
    verify = DecathPesasMancuernas(context.driver).element_add_to_cart_is_enabled()
    if verify:
        print("Parece que ya hay stock del elemento que buscas, revisalo ¡corre!")
    else:
        assert False, "No es posible añadir el producto a la cesta. El elemento que buscas sigue sin estar disponible"

@step('the price is "{number}"')
def get_price(context, number):
    """

    :param context:
    :return:
    """
    DecathPesasMancuernas(context.driver).accept_cookies()
    price = DecathPesasMancuernas(context.driver).get_price()
    print(f"El precio del producto es actualmente: {price}")
    assert price == number, "Los precios difieren, echalé un ojo"
