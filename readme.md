## Dataset spotify

Repo para trabalharmos os datasets que encontramos, podendo adicionar mais musicas, melhoras os dados e etc
Esse projeto é basicamente um punhado de scripts python que visam juntar vários datasets encontrados no Kaggle (e outras fontes da internet) para alimentar um modelo de machine learning que recomenda músicas parecidas com músicas de uma playlist.

Nas pastas teremos vários arquivos CSV contendo milhares de linhas com dados sobre músicas. Esses arquivos são a base de dados para nosso dataset, não sendo o dataset final. Imagine como uma camada "silver" na arquitetura de medalhão da engenharia de dados.


### Dúvidas
1. Devemos remover músicas com nomes duplicados? (porém IDs diferentes). Isso não pode fazer o recomendador recomendar a mesma música, porém de artistas diferentes? 
 Acho que não é viavel remover as músicas com nomes duplicados, mas precisamos ficar atentos ao recomendador recomendar músicas repetidas.

### TODO
- [ ] Usar o dataset `data_w_genres.csv` pra criar um array de "possible_genres" que triangula os artistas envolvidos na música e seus respectivos gêneros com o gênero da música.
- [ ] Melhoria pro ponto acima: Criar um modelo capaz de inferir qual dos possíveis gêneros a música pertence, buscando qual dos gêneros tem "features" mais próximas das features da música. Acho que uma regressão linear multivariável é a melhor opção? Estudar mais sobre outras possíveis opções