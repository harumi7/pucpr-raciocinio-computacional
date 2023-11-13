# Autora: harumi7
# Tecnólogo em Análise e Desenvolvimento de Sistemas - Raciocínio Computacional
# Início em: 09/05/2023 | Concluído em: 26/06/2023, 15:52

import json


# INÍCIO - PARTE FUNÇÕES

# SALVAR E LER ARQUIVO
def salvar_arquivo(lista: list, nome_arquivo: str):
    """
    Salva uma lista em determinado arquivo.

    :param lista: Lista com informações.
    :param nome_arquivo: Nome do arquivo onde será salvo a lista de informações.
    """
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)


def ler_arquivo(nome_arquivo: str):
    """
    Realiza a leitura de um determinado arquivo.

    :param nome_arquivo: Nome do arquivo que será realizada a leitura.
    :return: Retorna o conteúdo do arquivo se o código entrar no try. Caso contrário, se o código entrar
        em except ValueError/FileNotFoundError, retorna colchetes.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except ValueError:
        return []
    # FileNotFoundError ocorre quando se tenta ler um arquivo que não existe
    # Dessa forma, quando abre o programa pela primeira vez e tenta ler um arquivo inexistente,
    # retorna colchetes e cria o arquivo automaticamente.
    except FileNotFoundError:
        return []


# GERAL
def mostrar_linha(quantidade: int):
    """
    Mostra uma determinada quantidade de hífens.

    :param quantidade: Quantidade de hífens a ser mostrado na tela.
    """
    print('-' * quantidade)


def mostrar_linha_dupla(quantidade: int):
    """
    Mostra uma determinada quantidade de sinais de igual(=).

    :param quantidade: Quantidade de hífens a ser mostrado na tela.
    """
    linha_dupla = "=" * quantidade
    return linha_dupla


def mostrar_menu_principal():
    """
    Mostra o menu principal, respectivamente, com seis opções: Estudante, Disciplina, Turma, Matrícula,
    Professor e Sair.

    :return: Solicita que o usuário digite uma opção.
    """
    print(f'{mostrar_linha_dupla(7)} BEM-VINDO AO MENU PRINCIPAL! {mostrar_linha_dupla(7)}')
    mostrar_linha(44)
    print('[1] Estudante')
    print('[2] Disciplina')
    print('[3] Turma')
    print('[4] Matrícula')
    print('[5] Professor')
    print('[X] Sair')

    return input('—> Digite a opção que deseja gerenciar: ')


def mostrar_menu_operacoes():
    """
    Mostra o menu de operações, respectivamente, com cinco opções: Incluir, Listar, Alterar, Excluir e
    Voltar ao menu principal.

    :return: Solicita que o usuário digite uma operação.
    """
    print(f'{mostrar_linha_dupla(7)} MENU DE OPERAÇÕES | OPÇÃO [{opcao1.upper()}] {mostrar_linha_dupla(7)}')
    mostrar_linha(53)
    print('[1] Incluir')
    print('[2] Listar')
    print('[3] Alterar')
    print('[4] Excluir')
    print('[Z] Voltar ao menu principal')

    return input('—> Digite a operação desejada: ')


def mostrar_opcao_escolhida(opcao: str):
    """
    Mostra a opção escolhida pelo usuário.

    :param opcao: Opção digitada pelo usuário.
    """
    print(f'Você escolheu a opção "{opcao}".\n')


def mostrar_mensagem_voltar_menu_operacoes():
    """Mostra uma mensagem informando ao usuário a escolha realizada de voltar ao menu de operações."""
    print('Você escolheu voltar ao menu de operações.\n')


def verificar_digitou_voltar(lista_voltar: list, resposta_digitada):
    """
    Verifica se o usuário digitou a opção para voltar.

    :param lista_voltar: Lista de respostas válidas para que a ação de voltar seja realizada.
    :param resposta_digitada: Informação digitada pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    if resposta_digitada in lista_voltar:
        return True
    return False


def mostrar_mensagem_resposta_invalida(palavra: str):
    """
    Mostra uma mensagem informando ao usuário que a resposta digitada é inválida.

    :param palavra: Palavra correspondente à informação requerida que está inválida.
    :return: Mensagem informando que a resposta digitada pelo usuário é inválida.
    """
    # Necessário usar return aqui, porque já existe um print() quando a função é chamada.
    # Se usar print aqui e na hora de chamar, na saída vai aparecer "None"
    return f'<!> {palavra} INVÁLIDO, TENTE NOVAMENTE.'


def filtrar_respostas_validas(lista_respostas_entrada: list, indices: tuple):
    """
    Armazena em uma variável os dados da lista que se encontram nos índices informados.

    :param lista_respostas_entrada: Lista com as respostas válidas.
    :param indices: Tupla de índices necessários para entrar em cada opção/operação.
    :return: Retorna a variável em que foram armazenados os dados.
    """
    indices_desejados = [indices[0], indices[1], indices[2]]
    indices = [lista_respostas_entrada[indice] for indice in indices_desejados]
    return indices


def transformar_opcao_numero_em_opcao_palavra(
        numero_range: int, respostas_entrada: list, opcao: str, indice_inicio: int, indice_final: int
):
    """
    Se a opção digitada pelo usuário for um número válido, transforma esse número na palavra correspondente.
    Exemplo: Entrada é "1". Saída é "estudante".

    :param numero_range: Quantidade de vezes que o loop percorrerá.
    :param respostas_entrada: Lista de respostas válidas.
    :param opcao: Opção digitada pelo usuário no menu principal ou no menu de operações/secundário.
    :param indice_inicio: Índice onde deve começar a percorrer.
    :param indice_final: Índice onde deve terminar de percorrer.
    :return: Opção digitada pelo usuário em formato de palavra.
    """
    for indice in range(numero_range):
        if respostas_entrada[indice] == opcao:
            opcao = respostas_entrada[indice_inicio:indice_final]
            opcao = opcao[indice]
    return opcao


# VERIFICAÇÕES
# NOME
def verificar_em_nome_existe_numero(nome: str):
    """
    Percorre pelo nome digitado para verificar se há ocorrência de número.

    :param nome: Nome digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    for letra in nome:
        if letra.isnumeric():
            return True
    return False


def verificar_nome_comprimento_e_repeticao_letra(nome: str):
    """
    Verifica se o comprimento do nome digitado é menor que dois e se é apenas a repetição da mesma letra.

    :param nome: Nome digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    nome = nome.lower()  # <- Transforma todas as letras em minúsculas para possibilitar a verificação a seguir
    if 2 <= len(nome) != nome.count(nome[0]):
        return True
    return False


# CÓDIGO
def verificar_codigo_comprimento(codigo: int):
    """
    Verifica se o comprimento do código é igual a sete.

    :param codigo: Código digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    if len(str(codigo)) == 7:  # <- Transforma em string para poder usar o len()
        return True
    return False


def verificar_codigo_existe_no_arquivo(arquivo_lido: list, arquivo_codigo_chave: str, dado_incluir: int):
    """
    Verifica se o código digitado pelo usuário existe em determinado arquivo.

    :param arquivo_lido: Lista de informações.
    :param arquivo_codigo_chave: Chave existente nos dicionários da lista.
    :param dado_incluir: Código digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    for dicionario in arquivo_lido:
        if dicionario[arquivo_codigo_chave] == dado_incluir:
            return True
    return False


# CPF
def verificar_cpf_condicoes(cpf: str, lista_caracteres_validos: list):
    """
    Verifica se é apenas repetição de um mesmo número, ou se há caracteres digitados que não fazem parte da lista de
    caracteres permitidos, ou se o comprimento do CPF digitado é diferente de onze e de quatorze caracteres, ou se o
    método cpf.isalpha() retorna o valor booleano True.

    :param cpf: CPF digitado pelo usuário.
    :param lista_caracteres_validos: Lista de caracteres permitidos no CPF digitado.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    if len(cpf) == cpf.count(cpf[0]) or any(_ not in lista_caracteres_validos for _ in cpf) or len(cpf) != 11 and \
            len(cpf) != 14 or cpf.isalpha() is True:
        return True
    return False


def adicionar_caracteres_especiais_cpf(cpf: str):
    """
    Verifica a existência dos caracteres especiais "-" e "." no CPF digitado pelo usuário. Se não existirem, são
    adicionados neste mesmo CPF.

    :param cpf: CPF digitado pelo usuário.
    :return: Se a condição for realizada, retorna o CPF com os caracteres especiais adicionados. Caso contrário,
        retorna com o mesmo formato da entrada.
    """
    if '-' not in cpf and '.' not in cpf:
        cpf = f'{cpf[:3]}.{cpf[3:]}'
        cpf = f'{cpf[:7]}.{cpf[7:]}'
        cpf = f'{cpf[:11]}-{cpf[11:]}'
        return cpf
    return cpf


def verificar_cpf_ou_codigo_repetido(lista: list, chave: str, dado_incluir):
    """
    Verifica se o código ou CPF digitado pelo usuário já existe dentro de uma lista de dicionários.

    :param lista: Lista de dicionários com informações.
    :param chave: Chave de determinado dicionário a ser acessado.
    :param dado_incluir: Código ou CPF digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    for dicionario in lista:
        if dicionario[chave] == dado_incluir:
            return True
    return False


# VERIFICAÇÕES - REPETIÇÃO DE INFORMAÇÕES
def verificar_existencia_codigo(lista: list, codigo: int, chave: str):
    """
    Verifica se o código digitado pelo usuário existe na lista de dicionários.

    :param lista: Lista de dicionários, sendo que em cada dicionário é armazenado informações de um indivíduo diferente.
    :param codigo: Código digitado pelo usuário.
    :param chave: Chave de determinado dicionário a ser acessado.
    :return: Se a condição for realizada, retorna o dicionário em que o código se encontra. Caso contrário, retorna uma
        variável vazia (None).
    """
    dicionario_informacoes_estudante = None
    for dicionario in lista:
        if dicionario[chave] == codigo:
            dicionario_informacoes_estudante = dicionario
            break
    return dicionario_informacoes_estudante


def verificar_codigo_existe_algum_dicionario(lista: list, dados_para_alterar: dict, chave: str, dado_alterar):
    """
    Verifica se o código digitado pelo usuário existe na lista de dicionários e se determinado dicionário é diferente
    do que contém as informações do estudante/disciplina/turma/matrícula/professor, dados estes obtidos no início da
    operação "alterar".

    :param lista: Lista de dicionários com informações.
    :param dados_para_alterar: Dicionário com informações de determinado estudante/disciplina/turma/matrícula/professor.
    :param chave: Chave de determinado dicionário a ser acessado.
    :param dado_alterar: Código digitado pelo usuário.
    :return: Retorna o valor booleano True se a condição for realizada. Caso contrário, retorna o valor booleano False.
    """
    for indice in range(len(lista)):
        if lista[indice][chave] == dado_alterar and lista[indice] != dados_para_alterar:
            return True
    return False


# INCLUIR
# Como a função de incluir estava muito grande, foi dividido em três funções: Nome, código e CPF

# BLOCO NOME
def incluir_cadastro_bloco_nome(lista_voltar: list, dicionario: dict, chave: str):
    """
    Solicita que o usuário digite um nome e guarda essa informação em um dicionário.

    :param lista_voltar: Lista de respostas válidas para que a ação de voltar seja realizada.
    :param dicionario: Dicionário em que será guardado o nome digitado pelo usuário.
    :param chave: Chave de determinado dicionário a ser armazenado o nome digitado pelo usuário. Nessa função, também
    tem o propósito de nomear o campo de resposta.
    :return: Retorna o dicionário em que a informação foi armazenada. Se o usuário selecionar a opção de voltar ao menu
        de operações, retorna o valor booleano False.
    """
    while True:
        nome_incluir = ' '  # <- Variável declarada aqui apenas para usar o if
        if nome_incluir:
            nome_incluir = input(f'—> {chave}: ')

            if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=nome_incluir):
                mostrar_mensagem_voltar_menu_operacoes()
                continuar_funcao = False
                return continuar_funcao
            elif not nome_incluir:
                print('<!> PREENCHA O CAMPO DE RESPOSTA.')
                continue
            else:
                # Verificar se não há números no nome digitado
                # Não deixar cadastrar números, porém permitir nome composto e nome completo
                if verificar_em_nome_existe_numero(nome_incluir):
                    print(f'{mostrar_mensagem_resposta_invalida("NOME")}\n'
                          'O nome não deve conter números.')
                    continue

                # Verificar se é maior ou igual a dois e se não é apenas repetição da mesma letra
                elif verificar_nome_comprimento_e_repeticao_letra(nome_incluir):
                    dicionario[chave] = nome_incluir.title()
                    return dicionario
                    # Continua no bloco "CÓDIGO" logo abaixo
                else:
                    print(f'{mostrar_mensagem_resposta_invalida("NOME")}')
                    continue


# BLOCO CÓDIGO
# Parâmetros com ='': '' foi definido como valor-padrão, dessa forma, se não for informado o valor ao chamar a função,
# o '' ficará no lugar.
def incluir_cadastro_bloco_codigo(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, dicionario: dict, chave: str, sinal: str,
        arquivo_adicional='', arquivo_adicional_chave=''
):
    """
    Solicita que o usuário digite um código e guarda essa informação em um dicionário.

    :param lista_voltar: Lista de respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo em que as informações digitadas pelo usuário serão salvas.
    :param dicionario: Dicionário em que será armazenado o código digitado pelo usuário.
    :param chave: Chave de determinado dicionário a ser armazenado o código digitado pelo usuário. Nessa função, também
        tem o propósito de nomear o campo de resposta.
    :param sinal: Sinal enviado à função para que uma parte dela seja executada ou não.
    :param arquivo_adicional: Arquivo de outras opções (Estudante, Disciplina, Turma, Matrícula e Professor) sem ser a
        opção escolhida. É usada para verificar se o código digitado pelo usuário existe nesse arquivo adicional, para
        assim ser possível realizar certos cadastros.
    :param arquivo_adicional_chave: Chave de determinado dicionário.
    :return: Retorna uma variável com o valor booleano False armazenado se o usuário selecionar a opção de voltar ao
        menu de operações. Caso a informação seja validada e incluida em determinado dicionário, retorna o mesmo
        dicionário.
    """
    codigo_incluir = 1  # <- Variável declarada aqui apenas para usar o if
    if codigo_incluir:
        while True:
            try:
                codigo_incluir = int(input(f'—> {chave}: '))

                if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=codigo_incluir):
                    mostrar_mensagem_voltar_menu_operacoes()
                    continuar_funcao = False
                    return continuar_funcao
                elif verificar_codigo_comprimento(codigo_incluir):

                    # ENTRA NO BLOCO APENAS SE FOR ENVIADO O SINAL "executar1"
                    # Bloco verifica se o código digitado existe em algum dicionário da lista
                    if sinal == 'executar1':
                        # É necessário ler o arquivo e armazenar na variável para obter a versão mais atualizada dele
                        lista = ler_arquivo(nome_arquivo_dados)
                        if verificar_cpf_ou_codigo_repetido(lista=lista, chave=chave, dado_incluir=codigo_incluir):
                            print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                                  f'Este código já está cadastrado no sistema para outro(a) {opcao_digitada1}.')
                        else:
                            dicionario[chave] = codigo_incluir
                            return dicionario
                            # Continua no bloco "CPF" logo abaixo

                    # ENTRA NO BLOCO APENAS SE FOR ENVIADO O SINAL "executar2"
                    # Bloco verifica se o código digitado está presente em outro dicionário,
                    # em casos como incluir matrícula/turma, em que é necessário o código do professor, estudante etc.
                    elif sinal == 'executar2':
                        lista_arquivo = ler_arquivo(arquivo_adicional)
                        if verificar_codigo_existe_no_arquivo(
                                arquivo_lido=lista_arquivo, arquivo_codigo_chave=arquivo_adicional_chave,
                                dado_incluir=codigo_incluir
                        ):
                            dicionario[chave] = codigo_incluir
                            return dicionario
                            # Continua no bloco "CPF" logo abaixo
                        else:
                            print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                                  'O código digitado não está cadastrado no sistema.')

                else:
                    print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                          'Verifique a sequência numérica digitada.')
                    continue
            except ValueError:
                print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                      'O código deve conter apenas números.')
                continue


# BLOCO CPF
def incluir_cadastro_bloco_cpf(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, dicionario: dict, chave: str
):
    """
    Solicita que o usuário digite um CPF e guarda essa informação em um dicionário.

    :param lista_voltar: Lista de respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo em que as informações digitadas pelo usuário serão salvas.
    :param dicionario: Dicionário em que será armazenado o CPF digitado pelo usuário.
    :param chave: Chave de determinado dicionário a ser armazenado o CPF digitado pelo usuário. Nessa função, também
        tem o propósito de nomear o campo de resposta.
    :return: Retorna uma variável com o valor booleano False armazenado se o usuário selecionar a opção de voltar ao
        menu de operações.
    """
    cpf_incluir = ' '  # <- Variável declarada aqui apenas para usar o if
    if cpf_incluir:
        while True:
            caracteres_validos = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '.', '-'
            ]
            cpf_incluir = input(f'—> {chave}: ')

            if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=cpf_incluir):
                mostrar_mensagem_voltar_menu_operacoes()
                continuar_funcao = False
                return continuar_funcao
            elif not cpf_incluir:
                print('<!> PREENCHA O CAMPO DE RESPOSTA.')
                continue
            elif verificar_cpf_condicoes(cpf=cpf_incluir, lista_caracteres_validos=caracteres_validos):
                print(f'{mostrar_mensagem_resposta_invalida("CPF")}')
                continue
            # Adiciona no CPF digitado os caracteres especiais "." e "-"
            cpf_incluir = adicionar_caracteres_especiais_cpf(cpf_incluir)

            # É necessário ler o arquivo e armazenar na variável para obter a versão mais atualizada dele
            lista = ler_arquivo(nome_arquivo_dados)

            # Verifica se o CPF que o usuário digitou já está cadastrado para outro
            if verificar_cpf_ou_codigo_repetido(lista=lista, chave=chave, dado_incluir=cpf_incluir):
                print(f'{mostrar_mensagem_resposta_invalida("CPF")}\n'
                      f'Este CPF já está cadastrado no sistema para outro {opcao_digitada1}.')
                continue
            else:
                dicionario[chave] = cpf_incluir

                lista.append(dicionario)  # <- Adiciona o dicionário modificado na lista
                salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)  # <- Salva o arquivo
                print(f'<{opcao_digitada1.title()} cadastrado com sucesso!>')
                break
                # Volta para o começo do loop principal


# INCLUIR ESTUDANTES E PROFESSORES
def incluir_estudantes_e_professores(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, dicionario: dict, chaves: tuple
):
    """
    Realiza a operação de incluir para estudantes e professores.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param dicionario: Dicionário vazio de estudantes ou professores e que serão armazenadas as informações digitadas
        pelo usuário.
    :param chaves: Tupla de chaves de dicionários.
    """
    while True:
        # INCLUIR NOME DO ESTUDANTE/PROFESSOR
        retorno = incluir_cadastro_bloco_nome(lista_voltar=lista_voltar, dicionario=dicionario, chave=chaves[0])
        if retorno is False:  # <- Se selecionar voltar ao menu de operações, essa condição é realizada
            break

        # INCLUIR CÓDIGO DO ESTUDANTE/PROFESSOR
        retorno = incluir_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=retorno, chave=chaves[1], sinal='executar1'
        )
        if retorno is False:
            break

        # INCLUIR CPF DO ESTUDANTE/PROFESSOR
        retorno = incluir_cadastro_bloco_cpf(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=retorno, chave=chaves[2]
        )
        if retorno is False:
            break


# INCLUIR DISCIPLINAS
def incluir_disciplinas(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, dicionario: dict, chaves: tuple
):
    """
    Realiza a operação de incluir para disciplinas.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param dicionario: Dicionário vazio de disciplinas e que serão armazenadas as informações digitadas pelo usuário.
    :param chaves: Tupla de chaves de dicionários.
    """
    while True:
        # INCLUIR NOME DA DISCIPLINA
        retorno = incluir_cadastro_bloco_nome(lista_voltar=lista_voltar, dicionario=dicionario, chave=chaves[0])
        if retorno is False:  # <- Se selecionar voltar ao menu de operações, essa condição é realizada
            break

        # INCLUIR CÓDIGO DA DISCIPLINA
        retorno = incluir_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=retorno, chave=chaves[1], sinal='executar1'
        )
        if retorno is False:
            break

        # Salva aqui, pois o bloco código não salva as informações
        lista = ler_arquivo(nome_arquivo_dados)
        lista.append(retorno)
        salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)
        print('<Disciplina cadastrada com sucesso!>')


# INCLUIR TURMAS E MATRÍCULAS
def incluir_turmas_e_matriculas(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, dicionario: dict, chaves: tuple,
        arquivos_adicionais: tuple, arquivos_adicionais_chaves: tuple
):
    """
    Realiza a operação de incluir para turmas e matrículas.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param dicionario: Dicionário vazio de turmas ou matrículas e que serão armazenadas as informações digitadas pelo
        usuário.
    :param chaves: Tupla de chaves de um dicionário.
    :param arquivos_adicionais: Tupla de arquivos de outras opções (Estudante, Disciplina, Turma, Matrícula e Professor)
        sem ser a opção escolhida. É usada para verificar se o código digitado pelo usuário existe nesse arquivo
        adicional, para assim ser possível realizar certos cadastros.
    :param arquivos_adicionais_chaves: Chave do dicionário do primeiro arquivo adicional.
    """
    while True:
        # INCLUIR CÓDIGO DO PROFESSOR/TURMA
        retorno = incluir_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=dicionario, arquivo_adicional=arquivos_adicionais[0],
            arquivo_adicional_chave=arquivos_adicionais_chaves[0], chave=chaves[0], sinal='executar2'
        )
        if retorno is False:  # <- Se selecionar voltar ao menu de operações, essa condição é realizada
            break

        # INCLUIR CÓDIGO DA TURMA/MATRÍCULA
        retorno = incluir_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=retorno, chave=chaves[1], sinal='executar1'
        )
        if retorno is False:
            break

        # INCLUIR CÓDIGO DA DISCIPLINA/ESTUDANTE
        retorno = incluir_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            dicionario=retorno, chave=chaves[2], arquivo_adicional=arquivos_adicionais[1],
            arquivo_adicional_chave=arquivos_adicionais_chaves[1], sinal='executar2'
        )
        if retorno is False:
            break

        # Salva aqui, pois o bloco código não salva as informações
        lista = ler_arquivo(nome_arquivo_dados)
        lista.append(retorno)
        salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)
        print(f'<{opcao_digitada1.title()} cadastrada com sucesso!>')


# LISTAR
def listar_cadastros(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, chaves: tuple
):
    """
    Lista as informações cadastradas no sistema.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chaves: Tupla de chaves de um dicionário.
    :return: Sai da função.
    """
    lista = ler_arquivo(nome_arquivo_dados)
    if lista:
        print(f'{opcao_digitada1.upper()}: LISTAR')
        for indice in lista:
            # Poderia incluir a opção disciplina nesse bloco de if através de um try/except no print da chave3
            # para resolver o KeyError: '', porém a listagem de disciplinas ficaria tudo na mesma linha
            # Assim, a forma da resolução abaixo é por uma questão de organização das informações
            if opcao_digitada1 != 'disciplina':
                print(f'({chaves[1]}: #{indice[chaves[1]]}). ', end='')
                print(f'{chaves[0]}: {indice[chaves[0]]:.<35}, ', end='')
                print(f'{chaves[2]}: {indice[chaves[2]]}')
            else:
                print(f'({chaves[1]}: #{indice[chaves[1]]}). '
                      f'{chaves[0]}: {indice[chaves[0]]:.<35} ')
        print()
    else:
        print(f'Não há nenhum(a) {opcao_digitada1} cadastrado(a) para listar.\n')
        return

    # Esperar o usuário digitar "0" para voltar ao menu de operações
    while True:
        voltar1 = input('—> [Voltar ao menu de operações: Digite "0"]: ')
        if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=voltar1):
            mostrar_mensagem_voltar_menu_operacoes()
            break
        else:
            print('<!> RESPOSTA INVÁLIDA, TENTE NOVAMENTE.')


# ALTERAR
# Assim como para a função incluir, a função alterar ficaria muito grande, por isso, foi dividido em
# quatro funções: Bloco inicial, nome, código e CPF.

# BLOCO INICIAL
def alterar_cadastro_bloco_inicial(lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, chave: str):
    """
    Solicita um código para alterar as informações.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chave: Chave de determinado dicionário a ser acessado.
    :return: Retorna dois valores se não existir informações cadastradas ou se o usuário solicitar voltar ao menu de
        operações, e retorna outros dois valores se a operação de alterar for inicializada.
    """
    lista = ler_arquivo(nome_arquivo_dados)

    if lista:
        print(f'{opcao_digitada1.upper()}: ALTERAR\n'
              '[Voltar ao menu de operações: Digite "0"]')
    else:
        print(f'Não há nenhum(a) {opcao_digitada1} cadastrado(a) para alterar.\n')
        continuar_funcao = False
        # No return abaixo, o segundo valor serve para preencher a variável, uma vez que no outro return
        # dessa mesma função, são retornados dois valores.
        return continuar_funcao, ''

    while True:
        codigo_alterar = ' '  # <- Variável declarada aqui apenas para usar o if
        if codigo_alterar:
            try:
                codigo_para_alterar = int(input(f'—> Digite o código do(a) {opcao_digitada1} que deseja alterar: '))

                # Retorna o dicionário com as informações do estudante
                dados_para_alterar = verificar_existencia_codigo(lista=lista, codigo=codigo_para_alterar, chave=chave)

                if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=codigo_para_alterar):
                    mostrar_mensagem_voltar_menu_operacoes()
                    continuar_funcao = False
                    return continuar_funcao, ''
                elif dados_para_alterar is None:
                    print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                          'O código digitado não foi encontrado no sistema.')
                    continue
                else:
                    print('Código encontrado no sistema.\n')

                    # Mostra os dados do estudante selecionado
                    for chave, valor in dados_para_alterar.items():
                        print(f'{chave:.<8}: {valor:.<35}')

                    print('\nPara alterar, digite os novos dados nos campos de resposta.')
                    return dados_para_alterar, lista
                    # Continua no bloco "NOME" logo abaixo
            except ValueError:
                print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                      'O código deve conter apenas números.')
                continue


# BLOCO NOME
def alterar_cadastro_bloco_nome(lista_voltar: list, dados_para_alterar: dict, lista: list, chave: str):
    """
    Solicita que o usuário digite um novo nome e guarda essa informação em um dicionário. Conforme a alteração é
    realizada no dicionário, a lista também irá sendo modificada em conjunto.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param dados_para_alterar: Dicionário com informações de determinado estudante/disciplina/turma/matrícula/professor.
    :param lista: Lista de dicionários com informações.
    :param chave: Chave do dicionário a ser acessado.
    :return: Retorna dois valores se o usuário selecionar voltar ao menu de operações. Se o nome for alterado, retorna
        outros dois valores.
    """
    nome_alterar = ' '
    if nome_alterar:
        while True:
            nome_alterar = input(f'—> {chave}: ')

            if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=nome_alterar):
                mostrar_mensagem_voltar_menu_operacoes()
                continuar_funcao = False
                # No return abaixo, o segundo valor serve para preencher a variável, uma vez que no outro return
                # dessa mesma função, são retornados dois valores.
                return continuar_funcao, ''
            elif not nome_alterar:
                print('<!> PREENCHA O CAMPO DE RESPOSTA.')
                continue
            else:
                # Verificar se não há números no nome digitado
                # Não deixar cadastrar números, porém permitir nome composto e nome completo
                if verificar_em_nome_existe_numero(nome_alterar):
                    print(f'{mostrar_mensagem_resposta_invalida("NOME")}\n'
                          'O nome não deve conter números.')
                    continue

                # Verificar se é maior ou igual a 2 e se não é apenas repetição da mesma letra
                elif verificar_nome_comprimento_e_repeticao_letra(nome_alterar):
                    dados_para_alterar[chave] = nome_alterar.title()
                    return dados_para_alterar, lista
                    # Continua no bloco "CÓDIGO" logo abaixo
                else:
                    print(f'{mostrar_mensagem_resposta_invalida("NOME")}')
                    continue


# BLOCO CÓDIGO
# Parâmetros com ='': '' foi definido como valor-padrão, dessa forma, se não for informado o valor ao chamar a função,
# o '' ficará no lugar.
def alterar_cadastro_bloco_codigo(
        lista_voltar: list, dados_para_alterar: dict, lista: list, chave: str, sinal: str, arquivo_adicional='',
        arquivo_adicional_chave=''
):
    """
    Solicita que o usuário digite um novo código e guarda essa informação em um dicionário. Conforme a alteração é
    realizada no dicionário, a lista também irá sendo modificada em conjunto.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param dados_para_alterar: Dicionário com informações de determinado estudante/disciplina/turma/matrícula/professor.
    :param lista: Lista de dicionários com informações.
    :param chave: Chave do dicionário a ser acessado.
    :param sinal: Sinal enviado à função para que uma parte dela seja executada ou não.
    :param arquivo_adicional: Arquivo de outras opções (Estudante, Disciplina, Turma, Matrícula e Professor) sem ser a
        opção escolhida. É usada para verificar se o código digitado pelo usuário existe nesse arquivo adicional, para
        assim ser possível realizar certos cadastros.
    :param arquivo_adicional_chave: Tupla de chaves dos dicionários dos arquivos adicionais.
    :return: Retorna dois valores se o usuário selecionar voltar ao menu de operações. Se o nome for alterado, retorna
        outros dois valores.
    """
    codigo_alterar = 1
    if codigo_alterar:
        while True:
            try:
                codigo_alterar = int(input(f'—> {chave}: '))

                if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=codigo_alterar):
                    mostrar_mensagem_voltar_menu_operacoes()
                    continuar_funcao = False
                    # No return abaixo, o segundo valor serve para preencher a variável, uma vez que no outro return
                    # dessa mesma função, são retornados dois valores.
                    return continuar_funcao, ''
                elif verificar_codigo_comprimento(codigo_alterar):

                    # ENTRA NO BLOCO APENAS SE FOR ENVIADO O SINAL "executar1"
                    # Bloco verifica se o código digitado existe em algum dicionário da lista
                    if sinal == 'executar1':
                        if dados_para_alterar[chave] == codigo_alterar:
                            pass
                        elif dados_para_alterar[chave] != codigo_alterar:
                            if verificar_codigo_existe_algum_dicionario(
                                    lista=lista, dados_para_alterar=dados_para_alterar, chave=chave,
                                    dado_alterar=codigo_alterar
                            ):
                                print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                                      f'Este código já está cadastrado no sistema.')
                                continue

                        dados_para_alterar[chave] = codigo_alterar
                        return dados_para_alterar, lista
                        # Continua no bloco "CPF" logo abaixo

                    # ENTRA NO BLOCO APENAS SE FOR ENVIADO O SINAL "executar2"
                    # Bloco verifica se o código digitado está presente em outro dicionário,
                    # em casos como incluir matrícula/turma, em que é necessário o código do professor, estudante etc.
                    elif sinal == 'executar2':
                        lista_arquivo = ler_arquivo(arquivo_adicional)
                        if verificar_codigo_existe_no_arquivo(
                                arquivo_lido=lista_arquivo, arquivo_codigo_chave=arquivo_adicional_chave,
                                dado_incluir=codigo_alterar
                        ):
                            dados_para_alterar[chave] = codigo_alterar
                            return dados_para_alterar, lista
                            # Continua no bloco "CPF" logo abaixo
                        else:
                            print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                                  'O código digitado não está cadastrado no sistema.')

                else:
                    print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                          'Verifique a sequência numérica digitada.')
                    continue
            except ValueError:
                print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                      'O código deve conter apenas números.')


# BLOCO CPF
def alterar_cadastro_bloco_cpf(
        lista_voltar: list, opcao_digitada1: str, lista: list, dados_para_alterar: dict, nome_arquivo_dados: str,
        chave: str
):
    """
    Solicita que o usuário digite um novo CPF e guarda essa informação em um dicionário. Conforme a alteração é
    realizada no dicionário, a lista também irá sendo modificada em conjunto.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param lista: Lista de dicionários com informações.
    :param dados_para_alterar: Dicionário com informações de determinado estudante/disciplina/turma/matrícula/professor.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chave: Chave do dicionário a ser acessado.
    :return: Se o usuário solicitar voltar ao menu de operações, retorna o valor booleano False.
    """
    cpf_alterar = ' '
    if cpf_alterar:
        while True:
            caracteres_validos = [
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '.', '-'
            ]
            cpf_alterar = input(f'—> {chave}: ')

            if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=cpf_alterar):
                mostrar_mensagem_voltar_menu_operacoes()
                return False
            elif not cpf_alterar:
                print('<!> PREENCHA O CAMPO DE RESPOSTA.')
                continue
            elif verificar_cpf_condicoes(cpf=cpf_alterar, lista_caracteres_validos=caracteres_validos):
                print(f'{mostrar_mensagem_resposta_invalida("CPF")}')
                continue
            cpf_alterar = adicionar_caracteres_especiais_cpf(cpf_alterar)

            # Se o CPF é o mesmo das informações que estão sendo alteradas
            if dados_para_alterar[chave] == cpf_alterar:
                pass

            # Se o CPF é diferente das informações que estão sendo alteradas
            elif dados_para_alterar[chave] != cpf_alterar:
                # a) Código digitado é igual ao de outro dicionário
                if verificar_codigo_existe_algum_dicionario(
                        lista=lista, dados_para_alterar=dados_para_alterar, chave=chave, dado_alterar=cpf_alterar
                ):
                    print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                          f'Este código já está cadastrado no sistema.')
                    continue
                # b) Código não existe no sistema
                else:
                    dados_para_alterar[chave] = cpf_alterar

            salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)
            print(f'<Dados do(a) {opcao_digitada1} alterados com sucesso!>\n')
            return
            # Volta para o loop principal


# ALTERAR ESTUDANTES E PROFESSORES
def alterar_estudantes_e_professores(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, chaves: tuple
):
    """
    Realiza a operação de alterar para estudantes ou professores. Solicita ao usuário, respectivamente, o código das
    informações que deseja alterar, o novo nome, novo código e novo CPF.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chaves: Tupla de chaves de um dicionário.
    """
    while True:
        # ENCONTRAR CÓDIGO DO ESTUDANTE/PROFESSOR NA LISTA
        continuar_funcao, lista_dados = alterar_cadastro_bloco_inicial(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            chave=chaves[1]
        )
        # Se não existir informações para alterar ou o usuário selecionar voltar ao menu de operações,
        # essa condição é realizada
        if continuar_funcao is False:
            break

        # ALTERAR NOME DO ESTUDANTE/PROFESSOR
        dados_alterar, lista_dados = alterar_cadastro_bloco_nome(
            lista_voltar=lista_voltar, dados_para_alterar=continuar_funcao, lista=lista_dados, chave=chaves[0]
        )
        if dados_alterar is False:
            break

        # ALTERAR CÓDIGO DO ESTUDANTE/PROFESSOR
        dados_alterar, lista_dados = alterar_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, dados_para_alterar=dados_alterar, lista=lista_dados, chave=chaves[1],
            sinal='executar1'
        )
        if dados_alterar is False:
            break

        # ALTERAR CPF DO ESTUDANTE/PROFESSOR
        if alterar_cadastro_bloco_cpf(
                lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, lista=lista_dados,
                dados_para_alterar=dados_alterar, nome_arquivo_dados=nome_arquivo_dados, chave=chaves[2]
        ) is False:
            break


# ALTERAR DISCIPLINAS
def alterar_disciplinas(lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, chaves: tuple):
    """
    Realiza a operação de alterar para disciplinas. Solicita ao usuário, respectivamente, o código das informações que
    deseja alterar, o novo nome e novo código da disciplina.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chaves: Tupla de chaves de um dicionário.
    """
    while True:
        # ENCONTRAR CÓDIGO DA DISCIPLINA NA LISTA
        continuar_funcao, lista_dados = alterar_cadastro_bloco_inicial(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            chave=chaves[1]
        )
        # Se não existir informações para alterar ou o usuário selecionar voltar ao menu de operações,
        # essa condição é realizada
        if continuar_funcao is False:
            break

        # ALTERAR NOME DA DISCIPLINA
        dados_alterar, lista_dados = alterar_cadastro_bloco_nome(
            lista_voltar=lista_voltar, dados_para_alterar=continuar_funcao, lista=lista_dados, chave=chaves[0]
        )
        if dados_alterar is False:
            break

        # ALTERAR CÓDIGO DA DISCIPLINA
        dados_alterar, lista_dados = alterar_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, dados_para_alterar=dados_alterar, lista=lista_dados, chave=chaves[1],
            sinal='executar1'
        )
        if dados_alterar is False:
            break

        # Salva aqui, pois o bloco código não salva as informações
        salvar_arquivo(lista=lista_dados, nome_arquivo=nome_arquivo_dados)
        print(f'<Dados do(a) {opcao_digitada1} alterados com sucesso!>\n')


# ALTERAR TURMAS E MATRÍCULAS
def alterar_turmas_e_matriculas(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, arquivos_adicionais: tuple,
        arquivos_adicionais_chaves: tuple, chaves: tuple
):
    """
    Realiza a operação de alterar para turmas ou matrículas. Solicita ao usuário, respectivamente, o código das
    informações que deseja alterar, e três códigos, sendo que dois já devem existir em outra lista para que o cadastro
    seja feito.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param arquivos_adicionais: Tupla de arquivos de outras opções (Estudante, Disciplina, Turma, Matrícula e Professor)
        sem ser a opção escolhida. É usada para verificar se o código digitado pelo usuário existe nesse arquivo
        adicional, para assim ser possível realizar certos cadastros.
    :param arquivos_adicionais_chaves: Tupla de chaves dos dicionários dos arquivos adicionais.
    :param chaves: Tupla de chaves de um dicionário.
    """
    # ENCONTRAR CÓDIGO DA TURMA/MATRÍCULA NA LISTA
    while True:
        continuar_funcao, lista_dados = alterar_cadastro_bloco_inicial(
            lista_voltar=lista_voltar, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            chave=chaves[1]
        )
        if continuar_funcao is False:
            break

        # ALTERAR CÓDIGO DO PROFESSOR/TURMA
        retorno, lista = alterar_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, dados_para_alterar=continuar_funcao, lista=lista_dados, chave=chaves[0],
            arquivo_adicional=arquivos_adicionais[0], arquivo_adicional_chave=arquivos_adicionais_chaves[0],
            sinal='executar2'
        )
        if retorno is False:
            break

        # ALTERAR CÓDIGO DA TURMA/MATRÍCULA
        retorno, lista = alterar_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, dados_para_alterar=retorno, lista=lista_dados, chave=chaves[1],
            sinal='executar1'
        )
        if retorno is False:
            break

        # ALTERAR CÓDIGO DA DISCIPLINA/ESTUDANTE
        retorno, lista = alterar_cadastro_bloco_codigo(
            lista_voltar=lista_voltar, dados_para_alterar=retorno, lista=lista_dados, chave=chaves[2],
            arquivo_adicional=arquivos_adicionais[1], arquivo_adicional_chave=arquivos_adicionais_chaves[1],
            sinal='executar2'
        )
        if retorno is False:
            break

        # Salva aqui, pois o bloco código não salva as informações
        salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)
        print(f'<Dados do(a) {opcao_digitada1} alterados com sucesso!>\n')


# EXCLUIR
def excluir_cadastro(
        lista_voltar: list, opcao_digitada1: str, nome_arquivo_dados: str, chave: tuple
):
    """
    Solicita o código das informações que deseja excluir e, em seguida, realiza a exclusão dessas dados do sistema.

    :param lista_voltar: Lista com as respostas válidas para que a ação de voltar seja realizada.
    :param opcao_digitada1: Opção digitada pelo usuário no menu principal.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param chave: Tupla de chaves de um dicionário.
    :return: Sai da função.
    """
    lista = ler_arquivo(nome_arquivo_dados)

    if lista:
        print(f'{opcao_digitada1.upper()}: EXCLUIR\n'
              '[Voltar ao menu de operações: Digite "0"]')
    else:
        print(f'Não há nenhum(a) {opcao_digitada1} cadastrado(a) para excluir.\n')
        return

    while lista:
        try:
            codigo_excluir = int(input(f'—> Digite o código do(a) {opcao_digitada1} que deseja excluir: '))

            verificar_codigo = verificar_existencia_codigo(lista=lista, codigo=codigo_excluir, chave=chave[1])

            if verificar_digitou_voltar(lista_voltar=lista_voltar, resposta_digitada=codigo_excluir):
                mostrar_mensagem_voltar_menu_operacoes()
                return
            elif verificar_codigo is None:
                print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                      'O código digitado não foi encontrado no sistema.')
            else:
                lista.remove(verificar_codigo)
                salvar_arquivo(lista=lista, nome_arquivo=nome_arquivo_dados)
                print(f'<{opcao_digitada1.title()} excluído(a)!>')

        except ValueError:
            print(f'{mostrar_mensagem_resposta_invalida("CÓDIGO")}\n'
                  'O código deve conter apenas números.')
    print(f'Não há mais {opcao_digitada1} para excluir. Voltando ao menu de operações...\n')


# Confirmar saída do sistema
def confirmar_saida_sistema():
    """
    Pergunta ao usuário se deseja realmente sair do sistema e, caso a resposta for sim, o sistema finaliza. Caso
    contrário, volta ao menu principal.

    :return: Se o usuário confirmar a saída do sistema, retorna True.
    """
    sair_sistema_confirmar = ['X', 'x']
    voltar_sistema_confirmar = ['Z', 'z']
    print('\n<?> Tem certeza que deseja sair do Sistema PUC?')
    while True:
        confirmar_saida = input('—> [Sim: Digite "X"| Não: Digite "Z"]: ')

        if confirmar_saida in voltar_sistema_confirmar:
            print('Você escolheu voltar.\n')
            break
        elif confirmar_saida in sair_sistema_confirmar:
            print('Você escolheu sair.')
            return True
        else:
            print('<!> RESPOSTA INVÁLIDA, TENTE NOVAMENTE.')


# PROCESSAR MENU DE OPERAÇÕES
# Parâmetros com ='': '' foi definido como valor-padrão, dessa forma, se não for informado o valor ao chamar a função,
# o '' ficará no lugar.
def processar_menu_operacoes(
        opcao_digitada1: str, opcao_digitada2: str, nome_arquivo_dados: str, dicionario: dict, chaves: tuple,
        arquivos_adicionais: tuple = '', arquivos_adicionais_chaves: tuple = ''
):
    """
    Realiza as operações de incluir, listar, alterar e excluir informações.

    :param opcao_digitada1: Opção digitada pelo usuário no menu principal
    :param opcao_digitada2: Opção digitada pelo usuário no menu de operações.
    :param nome_arquivo_dados: Nome do arquivo que contém a lista de dicionários.
    :param dicionario: Dicionário vazio que serão armazenadas as informações digitadas pelo usuário.
    :param chaves: Tupla de chaves de dicionários.
    :param arquivos_adicionais: Tupla de arquivos de outras opções (Estudante, Disciplina, Turma, Matrícula e Professor)
        sem ser a opção escolhida. É usada para verificar se o código digitado pelo usuário existe nesse arquivo
        adicional, para assim ser possível realizar certos cadastros.
    :param arquivos_adicionais_chaves: Tupla de chaves do dicionário dos arquivos adicionais.
    :return: Retorna o valor booleano False, se o usuário selecionar voltar ao menu principal. Caso, contrário, retorna
        o valor booleano True.
    """
    # Respostas possíveis
    respostas_entrada2 = [
        '1', '2', '3', '4',
        'Incluir', 'Listar', 'Alterar', 'Excluir',
        'incluir', 'listar', 'alterar', 'excluir'
    ]
    respostas_voltar = [
        'Z', 'Voltar', 'Voltar ao menu principal',
        'z', 'voltar', 'voltar ao menu principal'
    ]

    # Se o usuário digitar a opção em formato de número, transforma em palavra
    opcao_digitada2 = transformar_opcao_numero_em_opcao_palavra(
        numero_range=4, respostas_entrada=respostas_entrada2, opcao=opcao_digitada2, indice_inicio=8, indice_final=12
    )

    voltar_operacao = [0, '0']
    # Necessário elif logo depois do if, ou o Python não vai deixar colocar o elif (vai dar erro)
    # INCLUIR
    if opcao_digitada2 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada2, indices=(0, 4, 8)
    ):
        mostrar_opcao_escolhida(opcao_digitada2)
        print(f'{opcao_digitada1.upper()}: INCLUIR\n'
              f'[Voltar ao menu de operações: Digite "0"]')

        # Estudantes e professores
        if opcao_digitada1 == 'estudante' or opcao_digitada1 == 'professor':
            incluir_estudantes_e_professores(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
                dicionario=dicionario, chaves=chaves
            )

        # Disciplinas
        elif opcao_digitada1 == 'disciplina':
            incluir_disciplinas(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao1, nome_arquivo_dados=nome_arquivo_dados,
                dicionario=dicionario, chaves=chaves
            )

        # Turmas e matrículas
        elif opcao_digitada1 == 'turma' or opcao_digitada1 == 'matrícula':
            incluir_turmas_e_matriculas(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao1, nome_arquivo_dados=nome_arquivo_dados,
                dicionario=dicionario, chaves=chaves, arquivos_adicionais=arquivos_adicionais,
                arquivos_adicionais_chaves=arquivos_adicionais_chaves
            )

    # LISTAR
    elif opcao_digitada2 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada2, indices=(1, 5, 9)
    ):
        mostrar_opcao_escolhida(opcao_digitada2)

        listar_cadastros(
            lista_voltar=voltar_operacao, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            chaves=chaves
        )

    # ALTERAR
    elif opcao_digitada2 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada2, indices=(2, 6, 10)
    ):
        mostrar_opcao_escolhida(opcao_digitada2)

        # Estudantes e professores
        if opcao_digitada1 == 'estudante' or opcao_digitada1 == 'professor':
            alterar_estudantes_e_professores(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
                chaves=chaves
            )

        # Disciplinas
        elif opcao_digitada1 == 'disciplina':
            alterar_disciplinas(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
                chaves=chaves
            )

        # Turmas e matrículas
        elif opcao_digitada1 == 'turma' or opcao_digitada1 == 'matrícula':
            alterar_turmas_e_matriculas(
                lista_voltar=voltar_operacao, opcao_digitada1=opcao1, nome_arquivo_dados=nome_arquivo_dados,
                arquivos_adicionais=arquivos_adicionais, arquivos_adicionais_chaves=arquivos_adicionais_chaves,
                chaves=chaves
            )

    # EXCLUIR
    elif opcao_digitada2 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada2, indices=(3, 7, 11)
    ):
        mostrar_opcao_escolhida(opcao_digitada2)

        excluir_cadastro(
            lista_voltar=voltar_operacao, opcao_digitada1=opcao_digitada1, nome_arquivo_dados=nome_arquivo_dados,
            chave=chaves
        )

    # Voltar ao menu principal
    elif opcao_digitada2 in respostas_voltar:
        print('Você escolheu voltar ao menu principal.\n')
        return False
    # Resposta digitada pelo usuário é inválida
    elif opcao_digitada2 not in respostas_entrada2 and opcao_digitada2 not in respostas_voltar:
        print('<!> OPERAÇÃO INVÁLIDA, TENTE NOVAMENTE.\n')

    return True
# FIM - PARTE FUNÇÕES


# INÍCIO
sair_sistema = False

# ARQUIVOS JSON
arquivo_estudantes = 'estudantes.json'
arquivo_disciplinas = 'disciplinas.json'
arquivo_turmas = 'turmas.json'
arquivo_matriculas = 'matriculas.json'
arquivo_professores = 'professores.json'

while sair_sistema is False:
    # MENU PRINCIPAL
    opcao1 = mostrar_menu_principal()

    # Respostas possíveis
    respostas_entrada1 = [
        '1', '2', '3', '4', '5',
        'Estudante', 'Disciplina', 'Turma', 'Matrícula', 'Professor',
        'estudante', 'disciplina', 'turma', 'matrícula', 'professor'
    ]
    respostas_sair = [
        'X', 'Sair',
        'x', 'sair'
    ]

    # Para melhorar a visualização da opção escolhida ao mostrar na tela, em caso da opção digitada ser número
    opcao1 = transformar_opcao_numero_em_opcao_palavra(
        numero_range=5, respostas_entrada=respostas_entrada1, opcao=opcao1, indice_inicio=10, indice_final=15
    )

    # Selecionar os índices das respostas desejadas na lista respostas_entrada1
    respostas_estudantes = filtrar_respostas_validas(
        lista_respostas_entrada=respostas_entrada1, indices=(0, 5, 10)
    )
    if opcao1 in respostas_estudantes:
        mostrar_opcao_escolhida(opcao1)

        # MENU SECUNDÁRIO - ESTUDANTES
        while True:
            opcao2 = mostrar_menu_operacoes()

            dicionario_estudantes = {}
            if not processar_menu_operacoes(
                    opcao_digitada1=opcao1, opcao_digitada2=opcao2, nome_arquivo_dados=arquivo_estudantes,
                    dicionario=dicionario_estudantes, chaves=('Nome', 'Código', 'CPF')
            ):
                break

    elif opcao1 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada1, indices=(1, 6, 11)
    ):
        mostrar_opcao_escolhida(opcao1)

        # MENU SECUNDÁRIO - DISCIPLINAS
        while True:
            opcao2 = mostrar_menu_operacoes()

            dicionario_disciplinas = {}
            if not processar_menu_operacoes(
                    opcao_digitada1=opcao1, opcao_digitada2=opcao2, nome_arquivo_dados=arquivo_disciplinas,
                    dicionario=dicionario_disciplinas, chaves=('Nome', 'Código')
            ):
                break

    elif opcao1 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada1, indices=(2, 7, 12)
    ):
        mostrar_opcao_escolhida(opcao1)

        # MENU SECUNDÁRIO - TURMAS
        while True:
            opcao2 = mostrar_menu_operacoes()

            dicionario_turmas = {}
            if not processar_menu_operacoes(
                    opcao_digitada1=opcao1, opcao_digitada2=opcao2, nome_arquivo_dados=arquivo_turmas,
                    dicionario=dicionario_turmas, chaves=(
                            'Código do professor', 'Código da turma', 'Código da disciplina'
                    ),
                    arquivos_adicionais=(arquivo_professores, arquivo_disciplinas),
                    arquivos_adicionais_chaves=('Código', 'Código')
            ):
                break

    elif opcao1 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada1, indices=(3, 8, 13)
    ):
        mostrar_opcao_escolhida(opcao1)

        # MENU SECUNDÁRIO - MATRÍCULAS
        while True:
            opcao2 = mostrar_menu_operacoes()

            dicionario_matriculas = {}
            if not processar_menu_operacoes(
                    opcao_digitada1=opcao1, opcao_digitada2=opcao2, nome_arquivo_dados=arquivo_matriculas,
                    dicionario=dicionario_matriculas, chaves=(
                            'Código da turma', 'Código da matrícula', 'Código do estudante'
                    ),
                    arquivos_adicionais=(arquivo_turmas, arquivo_estudantes),
                    arquivos_adicionais_chaves=('Código da turma', 'Código')
            ):
                break

    elif opcao1 in filtrar_respostas_validas(
            lista_respostas_entrada=respostas_entrada1, indices=(4, 9, 14)
    ):
        mostrar_opcao_escolhida(opcao1)

        # MENU SECUNDÁRIO - PROFESSORES
        while True:
            opcao2 = mostrar_menu_operacoes()

            dicionario_professores = {}
            if not processar_menu_operacoes(
                    opcao_digitada1=opcao1, opcao_digitada2=opcao2, nome_arquivo_dados=arquivo_professores,
                    dicionario=dicionario_professores, chaves=('Nome', 'Código', 'CPF')
            ):
                break

    # Confirmar se deseja realmente sair e, enquanto não digitar uma resposta válida, permanecer em loop
    elif opcao1 in respostas_sair:
        if confirmar_saida_sistema():
            break
        continue
    else:
        print('<!> OPÇÃO INVÁLIDA, TENTE NOVAMENTE.\n')

    # FIM
