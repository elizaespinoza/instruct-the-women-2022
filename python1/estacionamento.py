#!/usr/bin/python
# # -*- coding: utf-8 -*-

import sys

if sys.version_info[0] < 3:
    raise Exception("This script must run in Python 3.9.10.")

"""
- Estacionamento:
    - O estacionamento tem 50 vagas
    - É preciso saber o numero de vagas livres de carro e de moto
    para que o estacionamento saiba se pode colocar carros e motos
- Vagas:
    - 5 para carros
    - 5 para motos
    - Cada vaga é identificada por um número identificador único
- Carros:
    - Indentificados por suas placas
    - Só podem estar estacionados em vagas específicas para carros
    - É preciso ter controle sobre qual carro está em qual vaga
    agilizar a saida quando o dono vem buscar
- Motos:
    - Indentificados por suas placas
    - Podem ser estacionados em vagas para carros, caso terminar as
    vagas específica para motos
"""
