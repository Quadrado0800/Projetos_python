# ONLY imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import customtkinter as ct
from customtkinter import CTk
import threading
import win32api
import win32print
# Configura o navegador abrir com a opções desejadas
chrome_options = Options()
# ignora caixa de dialogo para imprimir
chrome_options.add_argument('--kiosk-printing')
#   Definindo caminho para a aplicação do chrome
driver_path = "Application//chrome.exe"
#  define variavel para utilizar na ultima checkbox 
def abrir_chrome_selenium():
    # Abre o link na guia selecionada do selenium
    driver.maximize_window()
    driver.get('https://desbravadorweb.com.br/acesso/6510')
# Coleta links de todos as confirmações de check-ins, e solicita a impressora
def reservas_dia_coiso():
    driver.get("https://desbravadorweb.com.br/#/reserva/")
    sleep(2)
    # check box check-ins do dia
    driver.find_element(By.XPATH,"//*[@id='grid']/div[1]/div/div[2]/div/label").click()
    sleep(1)
    reservas_lista_coiso()
# Coleta links de todos as confirmações de check-ins, e solicita a impressora
def reservas_lista_coiso():
    # busca todos os botões para emitir confirmações a partir da pagina "Painel-reservas"
    reservas_in_reservas_dia = driver.find_elements(By.XPATH, "//a[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeLarge css-1nn2l2u']") 
    sleep(1)
    # Define uma variavel para a check-box, e pre-define coom falsa
    global fichas
    fichas = ct.BooleanVar(value=False)
    a: list = []
    nums: list = []
    roomloc:list = []
    impressor = win32print.GetDefaultPrinter()
    # Find and storage all the links to get 
    for i in reservas_in_reservas_dia:
        print(i)
        cancel_conf = i.get_attribute('tabindex')
        if cancel_conf == "0":
            i_loc = i.get_attribute('href')
            sleep(2)
            a.append(i_loc)
        else:
            cancel_inf = i.get_attribute('href')
            print("Its not what you want (confirmation canceled) N = " + cancel_inf)
    driver.implicitly_wait(0.8)
    sleep(0.8)
    # click links that are stored in 'i_loc' (all the check-in that are needed, or all on the page...)
    for J in a:
        print(J)
        # Abre o link listado em 'a'
        driver.get(J)
        driver.implicitly_wait(1) 
         #coleta o numero dos uhs
        sleep(3)
        room_infs = driver.find_elements(By.XPATH, "//td[@style='width: 50%;']/p[@class='line-left']")
        # DONT FORGET TO REWORK THIS 
        for r in room_infs:
            sleep(3)
            text = r.__getattribute__('text')
            sleep(2)
            a_text = text.split(") - ")
            sleep(2)
            text = a_text[1]
            print(text)
            nums.append(text) 
        # utiliza o scroll para rolagem até o pé da guia
        sleep(4)
        driver.execute_script("window.scrollBy(0, 1000);")
        driver.implicitly_wait(3)
        sleep(1)
        # Click no botão para emitir confirmacao
        driver.find_element(By.XPATH,"//*[@id='imprimir-confirmacao-reserva']").click()
        sleep(1)
        try:
            driver.find_element(By.XPATH, "//*[@id='conteudo-total-sistema']/div[9]/div[3]/div/div[3]/button[1]").click()
        except:
            print("haven't appeard the noise popup " + J)
        # handles = abas do chrome aberto  
        sleep(1)
        handles = driver.window_handles
        sleep(1)
        #seleciona nova guia(ultima a ser aberta)
        driver.switch_to.window(handles[-1])
        sleep(0.8)
        # Imprimi o documento/site/pagina (comando simula "CONTROL + P")(nesse caso,impimi o documento de confirmação que esta selecionado)
        print(nums)
        #driver.execute_script(f'window.print();') # iniciando impressão da pagina aberta no chrome
        sleep(8)
        try:
            for n in nums:
                print(n)
                win32api.ShellExecute(0, "print", "C:\\Users\\PC\\Documents\\ISAAC_DOC\\python_testes\\python_on_VS\\Projeto02-criacao de inf\\inf" + n + "- OLD -.docx", None, ".", 0
                print("starting ficha File...")
                sleep(6)
                win32api.ShellExecute(0, "print", "C:\\Users\\PC\\Documents\\ISAAC_DOC\\python_testes\\python_on_VS\\projeto03\\Ficha-Hospedes.docx", None, ".", 0)
                print("starting inf File...")
                sleep(6) 
                driver.execute_script(f'window.print();') # iniciando impressão da pagina aberta no chrome
                sleep(8)
            print("Inf, confirm and Ficha done!")
            nums = []
        except:
            print("//////////////////  Cant print files from checkin!!!  ////////////////////////")
            nums = []
        # Fecha a nova guia (que foi anteriormente selecionada)
        driver.close()
        sleep(1)
        # seleciona novamente a guia principal (site do sistema)
        driver.switch_to.window(handles[0])
        sleep(1)      
    # entra no site do link abaixo, listado com aspas duplas
    driver.get("https://desbravadorweb.com.br/#/reserva/")
    print("Now, you should be good brother.")
#  passa em cada uh ocupado e ocupado com checkout para ser efetuada a conferencia
def conferencia_UHS():
    driver.get("https://desbravadorweb.com.br/#/mapaUh/")
    sleep(4)
    UHS: list = []
    uhs_ocupados = driver.find_elements(By.XPATH, "//*[@class='btn btn-popover-grande OCUPADA no-padding']")
    try:
        uhs_checkouts = driver.find_elements(By.XPATH, "//*[@class='btn btn-popover-grande OCUPADA_CHECKOUT no-padding']")
    except:
        print("theres no check-out room")
    try:
        uhs_checkoutcheckin = driver.find_elements(By.XPATH, "//*[@class='btn btn-popover-grande OCUPADA_CHECKIN_CHECKOUT no-padding']")
    except:
        print("Theres no check-out check-in room")
    sleep(2)
    for i in uhs_ocupados:
        sleep(1)
        aaa = i.get_attribute("onclick")
        sleep(1)
        b = aaa.split("'")
        sleep(1)
        z = b[1]
        print(z)
        UHS.append(z)
    sleep(1)
    try:
        for i in uhs_checkouts:
            sleep(1)
            aaa = i.get_attribute("onclick")
            sleep(1)
            b = aaa.split("'")
            sleep(1)
            z = b[1]
            print(z)
            UHS.append(z)
    except:
        print("dont have checkouts in this list!")
    sleep(1)
    try:
        for i in uhs_checkoutcheckin:
            sleep(1)
            aaa = i.get_attribute("onclick")
            sleep(1)
            b = aaa.split("'")
            sleep(1)
            z = b[1]
            print(z)
            UHS.append(z)
    except:
        print("dont have checkouts-checkins in this list!")
    for itemm in UHS:
        driver.get(f"https://desbravadorweb.com.br/#{itemm}")
        sleep(4)
        try:
            print("Particular room reserv")
            driver.find_element(By.XPATH, "//*[@id='extrato-contas']/div[6]/div[2]/div/div/div[2]/div/label[2]").click()
            sleep(2)
            sleep(34)
            item_on_room = driver.find_elements(By.XPATH, "//*[@style='display: block;']")
        except:
            print("Private room reserv")       
            sleep(2)
            sleep(34)
            item_on_room = driver.find_elements(By.XPATH, "//div[@class='well-sm row extrato-div-comandas extrato-div-lancamento-comandas']")
        # para cada item esperar o tempo de 16 segundos ou coisa do tipo // for comanda in room wait X amount of time 
        for iten in item_on_room:
            sleep(16)
    sleep(6)
    driver.get("https://desbravadorweb.com.br/#/mapaUh/")
#  passa em cada uh ocupado com checkout para ser efetuada a conferencia
def conferencia_UHS_checkouts():
    driver.get("https://desbravadorweb.com.br/#/mapaUh/")
    sleep(4)
    UHS: list = []
    uhs_checkouts = driver.find_elements(By.XPATH, "//*[@class='btn btn-popover-grande OCUPADA_CHECKOUT no-padding']")
    uhs_checkin_checkout = driver.find_elements(By.XPATH, "//*[@class='btn btn-popover-grande OCUPADA_CHECKIN_CHECKOUT no-padding']")
    sleep(2)
    #  cria um loop, e passa por todos os uhs ocupados_checkout, para conferencia de checkouts
    for i in uhs_checkin_checkout:
        sleep(1)
        aaaa = i.get_attribute('onclick')   
        sleep(1)
        bb = aaaa.split("'")
        zz = bb[1]
        print(zz)
        UHS.append(zz)
    for i in uhs_checkouts:
        sleep(1)
        aaa = i.get_attribute('onclick')   
        sleep(1)
        b = aaa.split("'")
        z = b[1]
        print(z)
        UHS.append(z)
    for itemm in UHS:
        driver.get(f"https://desbravadorweb.com.br/#{itemm}")
        sleep(4)
        try:
            driver.find_element(By.XPATH, "//*[@id='extrato-contas']/div[6]/div[2]/div/div/div[2]/div/label[2]").click()
        except:
            print("private room reserv")
        sleep(2)
        sleep(24)
        item_on_room = driver.find_elements(By.XPATH, "//*[@style='display: block;']")
        for iten in item_on_room:
            sleep(17)
    sleep(4)
    driver.get("https://desbravadorweb.com.br/#/mapaUh/")
def conferencia_UHS_tred():
    threading.Thread(target=conferencia_UHS, daemon=True).start()
def conferencia_UHS_checkouts_tred():
    threading.Thread(target=conferencia_UHS_checkouts, daemon=True).start()
# Função para executar o chrome e chama a função "abrir_chrome_selenium"
def lalala_webdriver():
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    abrir_chrome_selenium()
#abre a outra função com um "Thread" especifico(usado para funionar simultaneamente com a janela)
def rodar_chrome_selenium():
    threading.Thread(target=lalala_webdriver, daemon=True).start()
    # Criação de uma nova thread para executar o Selenium
#abre a outra função com um "Thread" especifico(usado para funionar simultaneamente com a janela)
def dodia():
    threading.Thread(target=reservas_dia_coiso, daemon=True).start()
#abre a outra função com um "Thread" especifico(usado para funionar simultaneamente com a janela)
def dalista():
    threading.Thread(target=reservas_lista_coiso, daemon=True).start()
#define uma função para executar e manter a janela 
def janela_customtkinter():
    app = CTk()  
    app.title("IMPRIMIR --confirmação -reserva")
    app.geometry("600x550")
    #Define um botão e adiciona a ação de executar a função "rodar_chrome_selenium" definida anteriormente
    button_abrir_chrome = ct.CTkButton(app, text="iniciar programa", command=rodar_chrome_selenium)
    button_abrir_chrome.pack(padx=60, pady=60)
    #define um botão para utilizar a verificação em todos os uhs listados no mapa como ocupados e ocupados-checkout
    button_conferencia = ct.CTkButton(app, text="conferir UHS ocupados", command=conferencia_UHS_tred)
    button_conferencia.pack(padx=20, pady=20)
    #define um botão para utilizar a verificação em todos os uhs listados no mapa como ocupados-checkout
    button_conferencia_checkout = ct.CTkButton(app, text="conferir UHS de checkout", command=conferencia_UHS_checkouts_tred)
    button_conferencia_checkout.pack(padx=20, pady=20)
    #define um botão e atribui a função "dodia" a ele
    button_confirms_dia = ct.CTkButton(app, text="imprimir do dia", command=dodia)
    button_confirms_dia.pack(padx=20, pady=20)
    #adiciona um botão e atribui a função "dalista" a ele
    button_confirms_lista = ct.CTkButton(app, text="imprimir da lista", command=dalista)
    button_confirms_lista.pack(padx=20, pady=20)
    #Inicia loop(mantem a janela viva)
    app.mainloop()
#abre a janela quando executar o codigo todo
if __name__ == "__main__":
    janela_customtkinter()
