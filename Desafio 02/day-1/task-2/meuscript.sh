#!/bin/bash

# Bem vindo!
echo "Bem vindo!"

# Obtem o endereco IP usando o site http://ifconfig.me
ip_address=$(curl -s ifconfig.me)

# Exibe o endereco IP
echo "Endereco IP: ${ip_address}"

# Verifica se o endereco IP responde ao protocolo ping
ping -c 1 ${ip_address}