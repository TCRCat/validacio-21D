import pandas as pd

anc_meses = pd.read_csv('input/current.csv')
parlament = pd.ExcelFile('input/09detall.xlsx')
parlament_meses = parlament.parse('Meses_2017', header=2)
parlament_meses['CodiMesa'] = parlament_meses.apply(lambda x: str(x['Codi circumscripció']).zfill(2) + str(x['Codi municipi']).zfill(3) + str(x['Districte']).zfill(2) + str(x['Secció']).zfill(3) + x['Mesa'], axis=1)
parlament_meses = parlament_meses.set_index('CodiMesa')
anc_meses = anc_meses.set_index('CodiMesa')
joined = parlament_meses.join(anc_meses).fillna(0)
matchings = [
    ['VNULS', 'Vots nuls'],
    ['VBLANCS', 'Vots en blanc'],
    ['VCS', 'Vots'],
    ['VJXC', 'Vots.1'],
    ['VERC', 'Vots.2'],
    ['VPSC', 'Vots.3'],
    ['VCOM', 'Vots.4'],
    ['VCUP', 'Vots.5'],
    ['VPPC', 'Vots.6'],
    ['VPACMA', 'Vots.7'],
    ['VRECORTES', 'Vots.8'],
    ['VPUMJUST', 'Vots.9'],
    ['VDIALEG', 'Vots.10']
    ]
joined['matches'] = joined.apply(lambda x: all(map(lambda c: x[c[0]] == x[c[1]], matchings)), axis=1)
vots_meses = joined[['MesaTancada', 'matches'] + [item for sublist in matchings for item in sublist]]
nomatch_mesatancada = vots_meses[(vots_meses['matches'] == False) & (vots_meses['MesaTancada'] == 1)]
nomatch_nomesatancada = vots_meses[(vots_meses['matches'] == False) & (vots_meses['MesaTancada'] == 0)]

print('Meses tancades que no quadren:', len(nomatch_mesatancada))
print('Meses no tancades que no quadren', len(nomatch_nomesatancada))

nomatch_mesatancada.to_csv('output/nomatch_mesatancada.csv', columns=[item for sublist in matchings for item in sublist])
nomatch_nomesatancada.to_csv('output/nomatch_nomesatancada.csv', columns=[item for sublist in matchings for item in sublist])

# Desquadrament en vots:
#nomatch_mesatancada.apply(lambda x: sum(map(lambda c: abs(x[c[0]] - x[c[1]]), matchings)), axis=1).sort_values(ascending=False)
