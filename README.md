# Airbnb
T2 - INF1407 - Programação para a Web 2023.2

Michel Anísio ALmeida - 1521767
Wallace de Freitas    - 1621612

Este projeto consiste em um site de avaliação de hospedagens, onde um usuário pode dar uma nota e escrever um depoimento sobre o local em que se hospedou.

# Models e Endpoints

@User
user_nickname = String(100), PK
user_email =    String(100)
user_password = String(100)

GET - /api/user/all - Lista todos os usuários cadastrados
Parâmetros: Não requer

POST - /api/user/manager/
{"user_nickname" : "user1",
"user_email" : "user1@gmail.com",
"user_password" : "1234"}

GET - /api/user/manager/
{"user_nickname" : "user2"}


@UserComments
airbnb_name =   String(100),        PK
user_nickname = FK pra Users        PK
user_note =     Int
user_comment =  String(1000)


GET - /api/comments/all - Lista todos os comentários de todos os usuários
Parâmetros: Não requer

POST/PUT - /api/comments/manager/
{"airbnb_name" : "Casa da Maria",
"user_nickname" : "user1",
"user_note" : 4,
"user_comment" : "Bela casa, bem espaçosa"}

GET/DEL - /api/comments/manager/ 
{"airbnb_name" : "Casa da Maria",
"user_nickname" : "user1"}