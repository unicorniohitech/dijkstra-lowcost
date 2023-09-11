import pandas as pd
table = pd.read_excel("Ligacoes_entre_Cidades.xlsx")
states = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'RJ',
          'PA', 'PB', 'PR', 'PE', 'PI', 'SP', 'RN', 'RS', 'RO', 'RR', 'SC', 'SE', 'TO', 'DF']
column = ['id_reg', 'cod_ori', 'coduf_ori', 'nivel_ori', 'classe_ori', 'cod_dest', 'coduf_dest', 'nivel_dest', 'classe_des', 'vinculo', 'multi_metr', 'metr_simb', 'nome_metr', 'multi_cap', 'cap_reg_si', 'nome_cap_r', 'entre_met', 'gp_metr', 'ge_metr',
          'ligrod_met', 'aero_metr', 'quest', 'quest_1', 'quest_2', 'quest_3', 'quest_4', 'quest_5', 'quest_6', 'quest_7', 'quest_8', 'quest_9', 'quest_10', 'lig_c_tv', 'aero_pax', 'agro', 'agro_q1', 'agro_q2', 'agro_q3', 'agro_q4']
table.drop


def delete_column(name):
    table.drop(name, axis=1, inplace=True)


def delete_row(column):
    table.drop(table[table[column]].index, inplace=True)


for col in column:
    delete_column(col)
for state in states:
    table.drop(table[table['uf_ori'] == state].index, inplace=True)
    table.drop(table[table['uf_dest'] == state].index, inplace=True)
table['nome_ori'] = table['nome_ori'].str.replace(
    'Arranjo Populacional de ', '', regex=False)
table['nome_ori'] = table['nome_ori'].str.replace(
    '/MG', '', regex=False)
table['nome_dest'] = table['nome_dest'].str.replace(
    'Arranjo Populacional de ', '', regex=False)
table['nome_dest'] = table['nome_dest'].str.replace(
    '/MG', '', regex=False)

table.drop('uf_ori', axis=1, inplace=True)
table.drop('uf_dest', axis=1, inplace=True)

table.to_excel("REGIC2018_Ligacoes_entre_Cidades.xlsx", index=False)
table.to_csv('InterMunicipal_MG.txt', ',')

with open('InterMunicipal_MG.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()[1:]
with open('InterMunicipal_MG.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        values = line.strip().split(',')
        new_value = ','.join(values[1:])
        file.write(new_value + '\n')
