# Taks 01
##### Gerando imagem
#
#

Para gerar imagem a partir de um de container
`docker commit php php-apache-gb`

Rodar imagem gerada de uma modificação no container
`docker run -d --name container_task_gb php-apache-gb`

Para gerar uma imagem a partir desse Dockerfile:
De posse de um arquivo "Dockerfile" assim como o anexado, podemos criar uma nova imagem. Neste caso esta sendo instalado pacotes para o servidor apache ter compatibilidade com o banco de dados postgres

Execute o seguinte comando para gerar a imagem:
`docker build -t nome_da_imagem:tag`
