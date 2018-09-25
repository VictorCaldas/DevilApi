# DevilApi
Mother Fucker Post Offices!!

Essa API pega as informaçoes do site do correios.

através do endpoint https://lilithamor.herokuapp.com/rastreamento
Faça um POST nessa URL passando o header como Content-Type":"application/json"
e passando como body {"cod":"SEU CODIGO"}

ele retorna para voce uma resposta desse jeito.

{  
   "eventos":[  
      {  
         "data":"13/09/2013  14:23        ITAPERUNA / RJ ",
         "evento":" Objeto entregue ao destinatário  "
      },
      {  
         "data":"11/09/2013  13:24        SAO PAULO / SP ",
         "evento":" Objeto postado  "
      }
   ],
   "status":{  
      "cidade":"RIO DE JANEIRO",
      "data":"13/09/2013",
      "hora":"14:25",
      "status":"Objeto entregue ao destinatário",
      "uf":"RJ"
   }
}

Primeira versão finalizada mas ainda será criada novas features e melhorada ao longo do tempo!
desculpa pela documentacao feia mas sera ajustada tambem
