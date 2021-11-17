# bibliotecas


#definições/ definitions
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Novo_Cadastro_Webdriver():
    # Método de Inicialização do Teste
    def setup_method(self, method):
        self.driver = webdriver.Chrome('driver/chrome/95/chromedriver.exe')
        # Qualquer elemento do teste espera três minutos
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.vars = {}



    # Método Finalização do Teste

    def teardow_method(self, method):
        # encerra o objeto do Selenium WebDriver
        self.driver.quit()

    # Método de Teste - Cadastrar um Novo Contato

    def test_novo_cadastro(self):

     self.driver.get('https://iterasys.com.br/cadastro/')

     self.driver.find_element(By.ID, 'cadastro_sucesso').text.count('Não é Aluno? Matricule-se já!')
     self.driver.find_element(By.ID,'nome').send_keys('Fulano')
     self.driver.find_element(By.ID,'telefone').send_keys('(31) 9000-7009')
     self.driver.find_element(By.ID,'email').send_keys('rjr33866@cuoly.com')
     self.driver.find_element(By.ID,'senha').send_keys('tESTE@2570')
     self.driver.set_page_load_timeout(5)
     self.driver.find_element(By.ID,' e - captcha').send_keys('')
     self.driver.find_element(By.ID,'btn_cadastro').click()
     











   #  self.driver.get_cookie('cookieconsent:desc').clear()
   #  self.driver.find_element(By.LINK_TEXT, 'cc-btn cc-dismiss').click()



