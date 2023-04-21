import boto3
import random
import datetime
import json

# Cria conexão com AWS Dynamodb
boto3.setup_default_session(profile_name="default")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('purchases_arthur_vinicius_santos_silva')

opcoes_pagamento = ["pix", "debito", "credito", "boleto"]

perifericos = [
    "Mouse Logitech MX Master 3",
    "Teclado Mecânico HyperX Alloy FPS Pro",
    "Fone de Ouvido Sony WH-1000XM4",
    "Caixa de Som Bluetooth JBL Charge 4",
    "Monitor Gamer Asus TUF Gaming VG249Q",
    "Placa de Vídeo Nvidia GeForce RTX 3070",
    "Webcam Logitech C920s HD Pro",
    "Impressora HP DeskJet Ink Advantage 2776",
    "Headset Gamer Razer Kraken",
    "Tablet Samsung Galaxy Tab A7",
    "HD Externo Western Digital My Passport",
    "Gabinete Gamer Cooler Master MasterBox MB511 RGB",
    "Fonte de Alimentação Corsair CX750M",
    "SSD Samsung 970 EVO Plus",
    "Roteador TP-Link Archer C6",
    "Hub USB 3.0 Orico 10 Portas",
    "No-Break APC Back-UPS BZ1200-BR",
    "Switch TP-Link TL-SG108",
    "Câmera de Segurança Intelbras VMD 1120 IR",
    "Microfone Blue Yeti",
    "Projetor Epson PowerLite X41+",
    "HD Interno Seagate Barracuda",
    "Cooler para Processador Cooler Master Hyper 212",
    "Placa-mãe Asus Prime B450M Gaming/BR",
    "Nobreak SMS Net 4+ Expert 700VA",
    "Leitor de Cartão Multilaser MC146",
    "Kit Teclado e Mouse Sem Fio Logitech MK270",
    "Estabilizador SMS Revolution Speedy 300VA",
    "Placa de Som Asus Xonar DGX",
    "Adaptador Wi-Fi TP-Link Archer T3U",
]

purchases = [
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Periferico de Hardware",
        "nome_produto": random.choice(perifericos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
]

# exemplo de estrutura do item:
'''
{
    'tipo_produto': 'Periferico de Hardware', 
    'nome_produto': 'Fone de Ouvido Sony WH-1000XM4', 
    'preco': 'R$7.73', 'data_hora': '21/04 - 11:44:30', 
    'ano': '2023', 
    'forma_pagamento': 'pix'}
'''
for purchase in purchases:
    print(purchase)
    table.put_item(Item=purchase)
