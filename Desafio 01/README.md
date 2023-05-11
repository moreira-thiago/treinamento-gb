
# Instalação e Configuração
## Pré-requisitos

Antes de começar, você precisará das seguintes credenciais da AWS:

 - Access Key ID 
 - Secret Access Key

`Referencia: https://www.youtube.com/watch?v=SteXxricweA`

## Instalação das ferramentas

 1. Abra um terminal e execute o seguinte comando para instalar a AWS
    CLI e pip3:

	`sudo apt-get install awscli pip3`
    
 2. Instale as bibliotecas Python boto e boto3 usando o pip3:

	`pip3 install boto boto3`

 3. Instale o Ansible e o Ansible Core:

	`sudo apt install ansible ansible-core`

## Configuração da AWS CLI

 1. Execute o seguinte comando para configurar a AWS CLI:

	`aws configure`

 2. Insira as suas credenciais da AWS quando solicitado. Você também
    pode configurar a região padrão e o formato de saída.

 3. Verifique se a configuração está correta executando o seguinte
    comando:

	`aws sts get-caller-identity`

 4. Se você tiver várias contas ou papéis da AWS, poderá usar o seguinte
    comando para alternar entre eles:

	`aws configure --profile <profile-name>`
	
## Configuração do Ansible

 1. Verifique se o Ansible foi instalado corretamente executando o
    seguinte comando:

	`ansible --version`

 2. Instale a coleção Amazon AWS executando o seguinte comando:

	`ansible-galaxy collection install amazon.aws`

 3. Verifique se a coleção foi instalada corretamente executando o
    seguinte comando:

	`ansible-galaxy collection list`
	
## Verificação

1.  Verifique se o Ansible está configurado corretamente para se comunicar com a AWS executando o seguinte comando:
    
    `aws ec2 describe-instances`
    
2.  Verifique se você pode se conectar às instâncias da EC2 usando o Ansible executando o seguinte comando:
    
    `ansible -i <path-to-inventory-file> -m ping <ec2-instance-name>`
    
# Criação da instância EC2 usando o Ansible
Agora que você tem o Ansible e a AWS CLI instalados e configurados, você pode usar o Ansible para criar uma instância EC2.

## Crie um playbook

Abra um terminal e navegue até o diretório onde você deseja criar o arquivo do playbook.

 1. Crie um arquivo chamado nome_desejado.yml usando o comando touch nome_desejado.yml.
    
	`touch nome_desejado.yml`
 2. Edite o arquivo create-ec2-instance.yml. No arquivo create-ec2-instance.yml, adicione o seguinte código:

```ansible
---
- name: Criar uma instância EC2
  hosts: localhost
  connection: local
  gather_facts: false
  vars:
    instance_type: t2.micro
    ami_id: ami-0c94855ba95c71c99
    key_name: your_key_pair_name
    subnet_id: your_subnet_id
    security_group_id: your_security_group_id
    region: us-east-1
    tag_name: your_tag_name
  tasks:
  - name: Criar a instância
    ec2:
      key_name: "{{ key_name }}"
      instance_type: "{{ instance_type }}"
      image: "{{ ami_id }}"
      region: "{{ region }}"
      vpc_subnet_id: "{{ subnet_id }}"
      assign_public_ip: true
      group_id: "{{ security_group_id }}"
      instance_tags:
        Name: "{{ tag_name }}"
    register: ec2
  - name: Mostrar informações da instância criada
    debug:
      var: ec2 
```
 3. Substitua os valores your_key_pair_name, your_subnet_id, your_security_group_id e your_tag_name pelos valores correspondentes à sua conta AWS. O valor ami-0c94855ba95c71c99 é a AMI do Amazon Linux 2 para a região US East (N. Virginia), mas você pode usar outra AMI, se preferir.


 4. Você criou com sucesso um playbook para criar uma instância EC2 usando o Ansible. Agora você pode executar o playbook usando o comando:
	`ansible-playbook nome_desejado.yml`

Ele criará uma nova instância EC2 na sua conta AWS com as especificações fornecidas no playbook. A partir daqui, você pode personalizar ainda mais o playbook para atender às suas necessidades, como a instalação de software na instância ou a configuração de regras de firewall.

## Breve explicação do playbook
Essas são as principais configurações definidas no playbook que ajudam a definir o escopo da execução do playbook e configurar as conexões e fatos do host.

-   `name`: Nome do playbook ou da tarefa que está sendo executada. Neste caso, é definido como `Criar uma instância EC2`.
    
-   `hosts`: Define qual ou quais hosts serão afetados pela execução do playbook. Neste caso, é definido como `localhost`, o que significa que a tarefa será executada na máquina local.
    
-   `connection`: Define o tipo de conexão que será usada para acessar o host. Neste caso, é definido como `local`, o que significa que a conexão será feita localmente.
    
-   `gather_facts`: Indica se os fatos sobre o host devem ser coletados antes de executar o playbook. Neste caso, é definido como `false`, o que significa que não serão coletados fatos sobre o host antes da execução do playbook.

-   `instance_type`: O tipo de instância que será criado. Neste caso, é definido como `t2.micro`, que é um tipo de instância de baixo custo que é adequado para muitos casos de uso.
    
-   `ami_id`: O ID da imagem da máquina virtual que será usada para criar a instância. Neste caso, é definido como `ami-0c94855ba95c71c99`, que é uma imagem do Amazon Linux 2.
    
-   `key_name`: O nome da chave SSH que será usada para acessar a instância. Neste caso, é definido como `your_key_pair_name`, que deverá ser substituído pelo nome da sua chave SSH.
    
-   `subnet_id`: O ID da sub-rede na qual a instância será criada. Neste caso, é definido como `your_subnet_id`, que deverá ser substituído pelo ID da sua sub-rede.
    
-   `security_group_id`: O ID do grupo de segurança que será associado com a instância. Um grupo de segurança é um firewall virtual que controla o tráfego de entrada e saída da instância. Neste caso, é definido como `your_security_group_id`, que deverá ser substituído pelo ID do seu grupo de segurança.
    
-   `region`: A região da AWS onde a instância será criada. Neste caso, é definido como `us-east-1`, que é a região leste dos EUA.
    
-   `tag_name`: O nome que será dado à instância. Neste caso, é definido como `your_tag_name`, que deverá ser substituído pelo nome que você deseja dar à sua instância.

-   `ec2`: Um módulo do Ansible que permite criar, gerenciar e deletar instâncias EC2 na AWS. Neste caso, ele é usado para criar uma nova instância.
    
-   `key_name`: Nome da chave SSH que será usada para acessar a instância. É definido como `{{ key_name }}`, que se refere ao valor da variável `key_name` definida na seção `vars` do playbook.
    
-   `instance_type`: O tipo de instância que será criada. É definido como `{{ instance_type }}`, que se refere ao valor da variável `instance_type` definida na seção `vars` do playbook.
    
-   `image`: A imagem que será usada para criar a instância. É definida como `{{ ami_id }}`, que se refere ao valor da variável `ami_id` definida na seção `vars` do playbook.
    
-   `region`: A região da AWS onde a instância será criada. É definida como `{{ region }}`, que se refere ao valor da variável `region` definida na seção `vars` do playbook.
    
-   `vpc_subnet_id`: O ID da sub-rede na qual a instância será criada. É definido como `{{ subnet_id }}`, que se refere ao valor da variável `subnet_id` definida na seção `vars` do playbook.
    
-   `assign_public_ip`: Define se um endereço IP público deve ser atribuído à instância. É definido como `true`, o que significa que um endereço IP público será atribuído à instância.
    
-   `group_id`: O ID do grupo de segurança que será associado com a instância. É definido como `{{ security_group_id }}`, que se refere ao valor da variável `security_group_id` definida na seção `vars` do playbook.
    
-   `instance_tags`: As tags que serão atribuídas à instância. Neste caso, é definido como `Name: "{{ tag_name }}"`, que define uma tag chamada `Name` com o valor da variável `tag_name` definida na seção `vars` do playbook.
    
-   `register`: Permite armazenar a saída da tarefa em uma variável. Neste caso, é definido como `ec2`, o que significa que a saída da tarefa será armazenada na variável `ec2`.
    
   
-   `debug`: Uma tarefa do Ansible que permite imprimir informações durante a execução do playbook. Neste caso, é usado para imprimir informações sobre a instância criada.
    
-   `var`: Uma opção da tarefa `debug` que permite definir qual variável deve ser impressa na saída. Neste caso, é definido como `ec2`, que se refere à variável `ec2` armazenada na tarefa anterior.
