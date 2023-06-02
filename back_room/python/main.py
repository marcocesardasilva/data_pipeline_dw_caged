# importar de outro arquivo
from extract import *
# from caged_transform import *
from load import *

##########################################################################
#                            Definir variáveis                           #
##########################################################################
file_key = "keys\dw-caged-e843b4e16870.json"
dataset_name = "caged"
data_folder = "dados"

##########################################################################
#               Criar conexão com o GCP, dataset e tabelas               #
##########################################################################
# Conexão com GCP
client, credentials = gcp_connection(file_key)
# Verificar se o dataset já existe, se não existe, cria
dataset_fonte = dataset_exist(client,dataset_name)
# Verifica se as tabelas já existem, se não existe, cria
table_movimentacao, table_localidade, table_trabalhador, table_periodo, table_empregador, table_fato_caged = table_exist(client,dataset_fonte)

##########################################################################
#                            Executar extrações                          #
##########################################################################
# Verificar próximo ano e mês a baixar dados
proximo_ano, proximo_mes = update_date(client,credentials,dataset_fonte,table_periodo)
# Baixar arquivos
download_files(proximo_ano,proximo_mes,data_folder)

'''
##########################################################################
#                         Executar transformações                        #
##########################################################################
# Ler todos os arquivos, tratar e agrupar em um único dataframe
df_group = group_files(data_folder)
# Criar dfs da fato e das dimensões
df_movimentacao, df_localidade, df_trabalhador, df_periodo, df_empregador, df_fato_caged = create_dfs(df_group)

##########################################################################
#                              Executar Carga                            #
##########################################################################
# Incluir tabelas e dfs em uma biblioteca
tables_dfs = {
    table_movimentacao:df_movimentacao,
    table_localidade:df_localidade,
    table_trabalhador:df_trabalhador,
    table_periodo:df_periodo,
    table_empregador:df_empregador,
    table_fato_caged:df_fato_caged}
# Carregar os dados no GCP
load_data(tables_dfs,client,dataset_fonte)
'''
