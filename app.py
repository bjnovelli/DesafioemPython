window=sg.Window('Login',layout=layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
     break
    
    elif event == 'login':

     senha_correta = '123456'
     usuario_correto ='bruna'
     usuario = values['usuário']
     senha = values['senha']
     if senha == senha_correta and usuario == usuario_correto:
       window['mensagem'].update('Login feito com sucesso')
     else:
       window['mensagem'].update('senha ou usuário incorreto')
