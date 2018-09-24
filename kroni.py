# coding=utf-8
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from flask import json


def seek_and_destroy(code):
    global json_rastreamento
    print("Rodando Seek And Destroy")
    url = "https://www2.correios.com.br/sistemas/rastreamento/"

    chrome_exec_shim = os.environ.get("GOOGLE_CHROME_BIN", "chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_exec_shim
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(executable_path='/app/development/chromedriver', chrome_options=chrome_options)


    print("Chrome pronto!")
    # versao sem headless
    driver_visible = webdriver.Chrome('/Users/victorcaldas/PycharmProjects/devilApi/chromedriver')

    # redenrizando tela
    driver.get(url)


    # acao na pagina
    print("buscando elementos")
    driver.find_element_by_id("objetos").clear()
    driver.find_element_by_id("objetos").send_keys(code)
    driver.find_element_by_id("btnPesq").click()

    # pegando html
    html = driver.page_source

    print("Pegando Elementos")
    # pegando titulo inicial
    element = driver.find_element_by_class_name("highlightSRO")
    element_table = driver.find_element_by_css_selector("[class='listEvent sro']")

    # pegando o html das tag desejadas
    status_raw = element.get_attribute('innerHTML')
    table_raw = element_table.get_attribute('innerHTML')

    # parse das informacoes do titulo
    soup = BeautifulSoup(status_raw, "lxml")
    soup_table = BeautifulSoup(table_raw, "lxml")

    # pegando as strings
    value = soup.get_text()
    value.split()
    value_table = soup_table.get_text()

    # limpando informacoes
    status = value.split('\n')
    status_filtered = [x for x in status if len(x.strip()) > 0]

    print("Quase lá!")
    print("---------")
    print("---------")
    print("---------")
    # colocando nas variaveis
    data_status, hora_status, cidade_status, d, uf_status, f = status_filtered[1].split(" ")

    # print
    print(status_filtered[0])
    print(data_status)
    print(hora_status)
    print(cidade_status)
    print(uf_status)
    print("---------")

    # pegando valores da minha linha
    for tr in soup_table:
        td = tr.find_all('td')
        row = [i.text for i in td]

    # limpando cagadas!
    lista = [el.replace('\xa0', ' ') for el in row]
    lista = [el.replace('\n', ' ') for el in lista]
    lista = [el.replace('\t', ' ') for el in lista]

    m = []

    # Obrigado lira!
    for i in range(0, int(len(lista[::-1]) / 2)):
        m.append(lista[i * 2: i * 2 + 2])

    print("Agora sim!")

    #Magica baby
    j = {'status': {'status': status_filtered[0],
                                    'data': data_status, 'hora': hora_status,
                                    'cidade': cidade_status, 'uf': uf_status},
                         'eventos': [{"data": ip[0], "evento": ip[1]} for ip in m]}

    json_rastreamento = json.dumps(j, ensure_ascii=False)

    print(json_rastreamento)

    time.sleep(4)

    #yes mother fucker!!!!!!
    driver.close()

    return json_rastreamento
