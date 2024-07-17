from behave import given,when,then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given(u'que estou na pagina do Instituto Joga Junto')
def step_enter_on_ijj_page(context):
    title = context.browser.title

    assert 'Instituto Jogffffa Junto' in title, "Titulo não encontrado"


@when(u'preencho o furmulario')
def step_preencher_form(context):
    input_name = context.browser.find_element(By.NAME, 'nome').send_keys('Matheus Munhoz')
    input_email = context.browser.find_element(By.NAME, 'email').send_keys('matheusmunhoz35@gmail.com')
    input_descp = context.browser.find_element(By.NAME, 'body').send_keys('Automação final')
    
    subject = context.browser.find_element(By.NAME, 'assunto')

    select_subject = Select(subject)
    
    select_subject.select_by_visible_text('Ser facilitador')

@when(u'aperto o botão para enviar')
def step_submit(context):
    submit_button = context.browser.find_element(By.XPATH,"/html/body/div/div[2]/section[8]/div[1]/form/button").submit()

@then(u'o dado é recebodo com sucesso')
def step_rec(context):
    #import ipdb; ipdb.sset_trace()

    wait = WebDriverWait(context.brouser, 10)

    alert = wait.until(EC.alert_is_present())
    assert 'Dados recebidos!' in alert.text, "dados não recebidos"