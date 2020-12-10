# Brazil Chatbot-Rasa 2.0+
COVID-19 Chatbot utiliza perguntas e resposta do portal da Fiocruz (https://mooc.campusvirtual.fiocruz.br/rea/coronavirus/faq.html)

``` MIT License | Rasa 2 | MongoDB | Python | Open Source 💙  ```

1. Rodar este comando para iniciar:

```docker-compose up --build```

2. Pagina web do bot:

```http://localhost:3000```

Obs: esperar a mensagem no terminal *connected to socketIO endpoint.* do rasa_server.



**NOTE:** 
```
Rasa Version     : 2.1.3
Rasa SDK Version : 2.1.2
Rasa X Version   : 0.34.0
Python Version   : 3.7.9
Operating System : Linux-5.9.8-200.fc33.x86_64-x86_64-with-fedora-33-Thirty_Three
Docker version 19.03.13, build 4484c46
docker-compose version 1.27.4, build unknown


rasa : http://localhost:5005/
rasa action_server: http://localhost:5055/

frontend: http://localhost:3000/

mongodb: http://localhost:27017/
username: rasa
password: example

mongo-express: http://localhost:8081/
username: rasa
password: example


actions:

action_global_cases_covid
acionada pela intent: global_cases_covid
funcao:
fazer uma chamada do tipo "GET" na API "https://api.covid19api.com/summary" e retornar ao usuario as ultimas informacoes de 
Confirmados, Recuperados e Óbitos

```

## Virtual Env
```
pip3 install virtualenv
virtualenv env_rasa_chatbot
source env_rasa_chatbot/bin/activate
pip3 install -r requirements.txt --no-index

 
terminal $: docker-composer up nginx mongo mongo-express chatbot_ui -d 

dentro da pasta backend
(env_rasa_chatbot)terminal $: rasa run actions & rasa x -m models --enable-api --log-file rasa.log  --cors "*"
```
### ToDo:
- [ ] Implementar Telegram
- [ ] Implementar action_news_covid (Ultimas noticias de covid)
- [x] Corrigir action_server
