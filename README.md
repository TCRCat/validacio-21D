Validació 21-D
==============

Aquest script compara els resultats oficials del 21-D amb els resultats del
recompte paral·lel de ANC, CUP i CDRs.

Requeriments **python3** i **pandas**.

Executar
--------
```
python validacio.py
```

Inputs
------

- **input/current.csv**. Fitxer del recompte paral·lel.
```
https://cataloniavotes.today/data/meses/current.csv
```
- **input/09detall.xlsx**. Fitxer amb les dades oficials
```
https://resultats.parlament2017.cat/09mesas/09detall.xlsx.zip
```

Outputs
-------

- **output/nomatch_mesatancada.csv**. Meses tancades que no quadren.
- **output/nomatch_nomesatancada.csv**. Meses no tancades que no quadren.
