
#!/usr/bin/python3
import base64
def inicio():
  print("Iniciando a execucao")
  print("Vou continuar")
  hello()

def hello():
  valores = ["sol","chuva","vento","noite","lua"]
  print("Oi")
  loop(valores)
  wFile('resultado.txt')

def loop(var):
  for i in var:
    print(i)

def wFile(fname):
  content = 'TWVuc2FnZW0gc2VjcmV0YSwgdm9jZSBjb25zZWd1aXUuIE8gY29kaWdvIMOpIDIwMjIuCg==\n'
  texto_codificado = content.strip()
  texto_decodificado = base64.b64decode(texto_codificado).decode("utf-8")
  print("")  
  print("")
  print(texto_decodificado)
  f = open(fname, 'w')
  f.write(content)
  f.close()


inicio()

