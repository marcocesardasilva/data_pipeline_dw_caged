
def create_dimensions(df_final):
    print("--------------------------------------------------------------------------")
    print("Criando dataframes para as tabelas fato e dimensões...")

    # Criar df_dim_veiculos
    df_dim_veiculos =  df_final[[
        'sk_veiculo',
        'ano_fabricacao_veiculo',
        'cd_veiculo',
        'de_tipo_veiculo',
        'nm_marca_veiculo',
        'nm_modelo_veiculo'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_veiculos.name = 'df_dim_veiculos'
    print(f"Dataframe {df_dim_veiculos.name} criado.")

    # Criar df_dim_pessoa
    df_dim_pessoa =  df_final[[
        'sk_pessoa',
        'cd_pessoa',
        'de_estado_fisico',
        'de_faixa_etaria',
        'de_genero',
        'de_tipo_envolvido'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_pessoa.name = 'df_dim_pessoa'
    print(f"Dataframe {df_dim_pessoa.name} criado.")

    # Criar df_dim_informacoes
    df_dim_informacoes =  df_final[[
        'sk_informacoes',
        'cd_acidente',
        'de_causa_acidente',
        'de_classificacao_acidente',
        'de_condicao_metereologica',
        'de_fase_dia',
        'de_sentido_via',
        'de_tipo_acidente'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_informacoes.name = 'df_dim_informacoes'
    print(f"Dataframe {df_dim_informacoes.name} criado.")

    # Criar df_dim_calendario
    df_dim_calendario =  df_final[[
        'sk_calendario',
        'mes',
        'trimestre',
        'semestre',
        'ano',
        'dia_da_semana',
        'dt_acidente',
        'fl_dia_util',
        'fl_feriado'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_calendario.name = 'df_dim_calendario'
    print(f"Dataframe {df_dim_calendario.name} criado.")

    # Criar df_dim_pista
    df_dim_pista =  df_final[[
        'sk_pista',
        'ano_investimento',
        'de_sentido_praca_pedagio',
        'de_tipo_pista',
        'de_tracado_via',
        'fl_situacao',
        'fl_uso_solo',
        'latitude_praca_pedagio',
        'longitude_praca_pedagio',
        'nm_br',
        'nm_concessionaria',
        'nm_praca_de_pedagio',
        'fl_pista_sem_pedagio',
        'num_km_praca_pedagio',
        'vl_investimento'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_pista.name = 'df_dim_pista'
    print(f"Dataframe {df_dim_pista.name} criado.")

    # Criar df_dim_localizacao
    df_dim_localizacao =  df_final[[
        'sk_localizacao',
        'cd_grande_regiao',
        'cd_mesorregiao',
        'cd_microregiao',
        'cd_municipio',
        'cd_unidade_federativa',
        'de_tipo_concentracao_urbana',
        'fl_amazonia_legal',
        'fl_regiao_cidade_sao_paulo',
        'fl_semiarido',
        'nm_grande_regiao',
        'nm_mesorregiao',
        'nm_microrregiao',
        'nm_municipio',
        'nm_regiao_metropolitana',
        'nm_unidade_federativa',
        'qtd_populacao',
        'sg_unidade_federativa',
        'vl_pib',
        'vl_pib_per_capita'
        ]].drop_duplicates().reset_index(drop=True)
    df_dim_localizacao.name = 'df_dim_localizacao'
    print(f"Dataframe {df_dim_localizacao.name} criado.")

    # Criar df_fato_acidentes
    df_fato_acidentes = df_final[[
        'sk_informacoes',
        'sk_calendario',
        'sk_localizacao',
        'sk_pessoa',
        'sk_pista',
        'sk_veiculo',
        'dt_acidente',
        'hr_acidente',
        'num_km_acidente',
        'fl_feridos_graves',
        'fl_feridos_leves',
        'fl_ilesos',
        'fl_mortos',
        'latitude_acidente',
        'longitude_acidente',
        'qtd_pessoas_envolvidas',
        'qtd_veiculos_envolvidos',
        'qtd_acidentes',
        'perc_pessoas_envolvidas',
        'perc_fatalidade_acidentes'
        ]]
    df_fato_acidentes.name = 'df_fato_acidentes'
    print(f"Dataframe {df_fato_acidentes.name} criado.")
    print("--------------------------------------------------------------------------")

    return df_dim_veiculos, df_dim_pessoa, df_dim_informacoes, df_dim_calendario, df_dim_pista, df_dim_localizacao, df_fato_acidentes
