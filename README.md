# IMDB BackEnd
**Desenvolvedor:** Wallace de Freitas - 1621612

Este projeto tem como objetivo ser um clone do IMDB com funcionalidades reduzidas. Um usuário não autenticado pode consultar filmes/atores e usuários autenticados podem realizar operações de Update, Delete e Post de novos filmes.

## Endpoints e JSON

### Ator
- `ator/all`: Retorna uma lista com todos os atores. Não precisa de parâmetro.
- `ator/get`: Busca um ator pelo nome e retorna o objeto. Parâmetro:
```json
{
    "nome": "maria"
}
```
- `ator/post`: Insere um ator na base de dados. Parâmetro:
```json
{
    "nome": "joao"
}
```

### Diretor
- `diretor/all`: Retorna uma lista com todos os diretores. Não precisa de parâmetro.
- `diretor/get`: Busca um diretor pelo nome e retorna o objeto. Parâmetro:
```json
{
    "nome": "maria"
}
```
- `diretor/post`: Insere um diretor na base de dados. Parâmetro:
```json
{
    "nome": "joao"
}
```

### Filme
- `filme/all`: Retorna uma lista com todos os filmes. Não precisa de parâmetro.
- `filme/get`: Busca um filme pelo nome e retorna o objeto. Parâmetro:
```json
{
     "titulo": "shazam"
}
```
- `filme/post`: Insere um novo filme na base de dados. Precisa de um token de autenticação. Parâmetro:
```json
{
    "token": "29387a04e3958bc54a5f8c7ac475284bfc7fbc01",
    "titulo": "Nome do Filme",
    "ano": 2023,
    "sinopse": "Sinopse do Filme",
    "atores": ["Ator1","Ator2"],
    "diretor": "Diretor"
}
```

- `filme/del`: Deleta um filme da base de dados. Precisa de um token de autenticação. Parâmetro: 
```json
{
	"token": "29387a04e3958bc54a5f8c7ac475284bfc7fbc01", 
	"titulo": "Nome do filme"}
```

- `filme/post`: Insere um novo filme na base de dados. Precisa de um token de autenticação. Parâmetro:

```json
{
    "token": "29387a04e3958bc54a5f8c7ac475284bfc7fbc01",
    "titulo": "nome original",
    "ano": 2030,
    "sinopse": "Nova Sinopse",
    "atores": ["novo ator","nova atriz"],
    "diretor": "novo diretor"
}
```

- `filme/films_by_actor`: Retorna todos os filmes que o ator já participou. Parâmetro:

```json
{
	"nome": "joão"
}
```

### Usuário
- `user/register`: Registra um novo usuário no banco e retorna seu token. Parâmetro:
```json
{
	"username": "nome do usuário",
    "password": "senha do usuário"
}
```
- `user/login`: Retorna o token de um usuário já cadastrado. Parâmetro:
```json
{
	"username": "nome do usuário",
    "password": "senha do usuário"
}
```
- `user/logout`:Deleta o token passado, assim fazendo logout. Parâmetro:
```json
{
	"token": "ba047b4504d20a87f5f5af6f2864c948b87ff3dc"
}
```