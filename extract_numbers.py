import re

data = """17/09/2020 11:31 - As mensagens e as chamadas são protegidas com a criptografia de ponta a ponta e ficam somente entre você e os participantes desta conversa. Nem mesmo o WhatsApp pode ler ou ouvi-las. Toque para saber mais.
17/09/2020 11:31 - ‎+55 51 9963-4149 criou o grupo "Avisos SETRA"
17/09/2020 11:31 - ‎+55 51 9963-4149 adicionou você
17/09/2020 11:31 - +55 51 9161-4414: 👍
17/09/2020 11:31 - +55 51 8453-5246: Bom dia!!
17/09/2020 11:31 - ‎+55 51 9688-8125 saiu
17/09/2020 11:31 - +55 51 8431-3676: Tô dentro!
17/09/2020 11:32 - +55 51 9300-7783: 👍
17/09/2020 11:32 - +55 51 9982-2461: Ok
17/09/2020 11:32 - Dimas: 🤙🏾
17/09/2020 11:32 - Fulber: Ok
17/09/2020 11:32 - +55 51 8405-4339: 👍🏿
17/09/2020 11:33 - ‎+55 51 9963-4149 mudou as configurações desse grupo para permitir que somente admins possam editar os dados do grupo
17/09/2020 11:33 - ‎+55 51 9963-4149 mudou as configurações desse grupo para permitir que somente admins possam enviar mensagens ao grupo
17/09/2020 11:41 - +55 51 9963-4149: Olá pessoal, este grupo foi criado para enviar avisos aos operadores e supervisores. Aqui ressalto que o mesmo servirá como somente consulta, como assim? Somente os supervisores poderão escrever no grupo. Os operadores somente poderão ler as mensagens. Portanto, caso o supervisor necessite de uma confirmação do operador sobre algo específico, deverá enviar a mensagem individualmente. 
Peço a todos que deixem este grupo sem o silenciamento sonoro, pois só deverá ser usado em mensagens importantes de ciência a todos. Do mesmo modo, peço a todos que não apaguem o histórico do grupo, já que somente deverá ter mensagens pertinentes ao nosso trabalho.
17/09/2020 11:51 - ‎+55 51 9963-4149 adicionou +55 51 9134-8725
17/09/2020 11:58 - ‎+55 51 9963-4149 adicionou +55 51 9959-7930
17/09/2020 12:33 - +55 51 9943-0482: Ciente!
17/09/2020 12:35 - Claiton: ATENÇÃO AO PONTO DE PARADA NAS EXTREMIDADES:
Ao chegar em NH na V2 ou entrando direto na V1 o ponto de parada é sempre na EXTREMIDADE norte, mesmo sendo TUE S100 simples ou S200.
17/09/2020 13:00 - ‎+55 51 9287-1880 saiu
17/09/2020 13:26 - Claiton: <Arquivo de mídia oculto>
17/09/2020 13:55 - +55 51 9293-6783: Ok
17/09/2020 14:04 - Barcelos: Lembrando que em manobras em NH com trens simples (S100 ou S200), além da parada na extremidade norte da V1, o operador que assumira o trem deverá puxá-lo para a extremidade sul depois de prestar servico ao norte, e prestar servico so sul da plataforma, mesmo que o trem esteja atrasado.
17/09/2020 14:06 - ‎Dimas saiu
17/09/2020 14:07 - Barcelos: Nas manobras de chegada em MR2 também se aplica a regra, entrando direto na extremidade sul e o operador que vai assumir deve posicionar o trem na extremidade norte, prestando serviço novamente, mesmo em atraso.
17/09/2020 14:11 - ‎Ana Carolina saiu
17/09/2020 14:12 - ‎+55 51 9118-0942 saiu
17/09/2020 14:18 - ‎+55 51 9272-4227 saiu
17/09/2020 16:15 - +55 51 9154-7572: Eliezer solicitou algumas mudanças na Rmop do Tavares, será  abonado dias 7 e 8 pelo Sepes por este motivo tirei uma troca dia 23, favor avisar para ele.
17/09/2020 16:25 - +55 51 9154-7572: Jonathas favor avisar amanhã
17/09/2020 16:28 - ‎+55 51 9237-9118 saiu
17/09/2020 16:29 - ‎+55 51 8463-9806 saiu
17/09/2020 16:31 - ‎+55 51 9249-1388 saiu
17/09/2020 16:53 - ‎+55 51 9740-7599 saiu
17/09/2020 17:09 - ‎+55 51 9252-2401 saiu
17/09/2020 17:09 - ‎+55 51 9688-9043 saiu
17/09/2020 23:27 - ‎+55 51 9340-5451 saiu
18/09/2020 04:46 - +55 51 9152-6011: <Arquivo de mídia oculto>
18/09/2020 04:47 - +55 51 9152-6011: Seleção de P.A ou Intercom no pedal esquerdo do série 100 ☝🏼
18/09/2020 08:22 - ‎+55 51 9287-1880 entrou usando o link de convite deste grupo
18/09/2020 11:17 - ‎Dimas entrou usando o link de convite deste grupo
18/09/2020 17:33 - Patrícia: <Arquivo de mídia oculto>
20/09/2020 10:09 - +55 51 9698-0812: Todos operadores que recolherem ao pt de  amanhã  dia 21/09 devem aguardar pois terão  instrução sobre o rádio(quem ainda não teve).
21/09/2020 10:16 - ‎Patrícia adicionou +55 51 9152-2572
21/09/2020 10:32 - ‎+55 51 9963-4149 adicionou +55 51 9297-5910
21/09/2020 16:21 - +55 51 9152-2572: <Arquivo de mídia oculto>
21/09/2020 20:11 - +55 51 9152-6011: <Arquivo de mídia oculto>
21/09/2020 20:12 - +55 51 9152-6011: Demonstração rádio digital 239 👆🏼
21/09/2020 20:15 - ‎Mauro Mello saiu
21/09/2020 20:17 - +55 51 8463-9860: Bom .
21/09/2020 21:55 - 🐸: <Arquivo de mídia oculto>
22/09/2020 09:56 - +55 51 8463-9860: Atenção. Tue com radio digital quando apresentar alguma dificuldade de comunicação na via informar o local para o cco.
22/09/2020 13:37 - +55 51 9152-6011: <Arquivo de mídia oculto>
23/09/2020 13:33 - +55 51 9152-2572: <Arquivo de mídia oculto>
23/09/2020 13:33 - +55 51 9152-2572: <Arquivo de mídia oculto>
23/09/2020 13:33 - +55 51 9152-2572: Eleições CIPA 👆🏼! Votação até 27/09. Participe!
24/09/2020 08:07 - +55 51 9152-2572: Bom dia!
Colegas, reservem 5 min para participar da votação da CIPA, é simples e rápido.
É necessário 50%+1 de votos do total de empregados para a validação da eleição. A Geinf nos informou que o SETRA teve até o momento apenas 14%. 
Caso haja alguma dúvida para acessar liguem para o ramal 8257 e falem com a Neida ela estará a disposição para auxiliar.
25/09/2020 14:06 - +55 51 9152-2572: Boa tarde colegas!
Quem ainda não votou para a CIPA e está com alguma dificuldade, a Neida está hoje só a disposição para auxiliar nisso... ramal 8257!
Participem para que a eleição seja validada!
25/09/2020 14:20 - +55 51 9260-2396: Tá difícil? Esqueceu a senha ? Ligue para a Neida no ramal 8257...
Além da votação para a CIPA, existem diversas informações de seu interesse...
Participe...
25/09/2020 15:52 - +55 51 9152-2572: http://corporerm.trensurb.gov.br/corpore.net/Login.aspx
25/09/2020 15:52 - +55 51 9152-2572: Quem preferir pode acessar esse link para votar
25/09/2020 16:55 - +55 51 9669-5756: Boa tarde, eleições prorrogadas até quarta-feira, dia 30/09/2020. Vide REP-0350/2020.
28/09/2020 09:47 - +55 51 9152-2572: Bom dia!
Lembrando que as eleições  para a CIPA foram prorrogadas até quarta-feira, dia 30/09. Então quem ainda não votou, participe! As eleições  precisam de um número mínimo de votos para que seja validada e a participação do SETRA ainda está baixa...
Dúvidas em relação a senha entre em contato com o Help 8200 ou Neida no 8257. Se tiver a senha mas está com dificuldade e dúvidas no acesso, tbm posso auxiliar!
28/09/2020 10:38 - +55 51 9152-2572: Essa mensagem foi apagada
28/09/2020 10:38 - +55 51 9152-2572: Essa mensagem foi apagada
28/09/2020 10:38 - +55 51 9152-2572: Essa mensagem foi apagada
28/09/2020 10:38 - +55 51 9152-2572: Essa mensagem foi apagada
28/09/2020 10:38 - +55 51 9152-2572: <Arquivo de mídia oculto>
28/09/2020 10:38 - +55 51 9152-2572: <Arquivo de mídia oculto>
28/09/2020 10:38 - +55 51 9152-2572: <Arquivo de mídia oculto>
28/09/2020 10:38 - +55 51 9152-2572: <Arquivo de mídia oculto>
28/09/2020 10:38 - +55 51 9152-2572: Passo a passo 👆🏼
29/09/2020 14:10 - +55 51 9152-2572: Boa tarde colegas!
29/09/2020 14:10 - +55 51 9152-2572: 👆🏼
30/09/2020 10:13 - +55 51 9152-2572: <Arquivo de mídia oculto>
30/09/2020 10:13 - +55 51 9152-2572: Último dia para votação na CIPA 👆🏼
03/10/2020 23:18 - ‎+55 51 9963-4149 removeu +55 51 8255-1136
05/10/2020 17:45 - +55 51 9152-6011: LISTA de PRESENÇA do curso de RADIO digital - Deixei em MR as listas de presença por dia do curso de rádio digital dado no trem. Favor assinarem. Podem avaliar o curso na outra folha. Lembrando que o material do curso são os guias rápidos e os vídeos que postei aqui.
05/10/2020 17:52 - +55 51 9152-6011: Essa mensagem foi apagada
05/10/2020 17:53 - +55 51 9152-6011: <Arquivo de mídia oculto>
05/10/2020 19:03 - +55 51 9152-6011: <Arquivo de mídia oculto>
05/10/2020 19:07 - +55 51 9152-6011: Quando entrar na cauda do trem série 100 o rádio vai estar em stand by. Segure o botão vermelho do canto direito de baixo por dois segundos o rádio liga (ambas as séries) . A cauda ouve a outra cabine mesmo com o rádio em stand by. Pode dar P.A ou falar com o CCO mesmo em cauda.
05/10/2020 19:36 - +55 51 9152-6011: <Arquivo de mídia oculto>
06/10/2020 15:34 - +55 51 9152-6011: <Arquivo de mídia oculto>
06/10/2020 21:26 - Claiton: A partir do dia 8/10 o operação comercial irá ser estendida novamente até as 23:25. Em função disto pedimos que verifiquem as alterações nos horários/locais de entrada de suas missões bem como horários das respectivas voltas. 
O Turno manhã não teve nenhuma implicação em função desta alteração. Os turnos tarde e noite foram os mais afetados (turno tarde terá algumas viagens a mais e turno noite não entrará mais tão cedo como vinha ocorrendo). 
Principais mudanças, PORÉM NÃO AS ÚNICAS:
Missão 01N volta a injetar direto a MV e retornando em Marcha a Vista até FR1 de onde parte para MR. 
Missão 12N irá de carona do PT até o MR para fazer a viagem 05:22.
Missão 33T e missão 28T devem ficar de reserva até a chegada do reserva do turno noite, quando não houver OT reserva até a chegada do OT da missão 08N.
Somente 2 missões (27T e 29T darão uma volta em MR e deverão retornar ao PT para injeção);
Missões 04T, 09T, 14T e 19T permanecem com seus horários de entrada 12:00 PT devendo se apresentar no PT no máximo até as 12:40. Esta tolerância não se aplica aos demais turnos ou missões que deverão se apresentar sempre no horário previsto de entrada. Além disto haverá a tolerância de 40 minutos na entrada para as missões 28T e 33T porém estas entram mais tarde no PT. OTs "100% Reservas" sempre devem registrar a entrada no horário previsto no PÁTIO (não há tolerância de deslocamento).
Missões de sábados e domingos a tarde também sofreram pequenos ajustes. VERIFIQUEM.

Caso percebam alguma discrepância em relação aos horários/locais de entrada ou intervalo peço a gentileza que me avisem que tentarei ajustar com a maior brevidade possível.
06/10/2020 21:31 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:32 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:35 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:36 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:42 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:43 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:44 - Claiton: <Arquivo de mídia oculto>
06/10/2020 21:45 - Claiton: <Arquivo de mídia oculto>
06/10/2020 22:24 - Claiton: <Arquivo de mídia oculto>
06/10/2020 22:24 - Claiton: <Arquivo de mídia oculto>
07/10/2020 08:57 - +55 51 9152-2572: <Arquivo de mídia oculto>
08/10/2020 23:14 - +55 51 9963-4149: OLÁ PESSOAL, FORAM CRIADAS 2 MISSÕES PELA MANHÃ E 2 MISSÕES PELA TARDE PARA O AEROMÓVEL. AS MESMAS APARECERÃO NO EFETIVO DIÁRIO. OS OPERADORES QUE ESTIVEREM ALOCADOS, DEVERÃO COMPARECER NO AEROMÓVEL PARA OPERÁ-LO. AM1 E AM2 (AEROMOVEL MANHÃ) E AT1 E AT2 (AEROMOVEL TARDE). 
PS: CASO SEJA UM OPERADOR E NÃO ESTEJA NO QUADRO DO AEROMÓVEL, E ESTEJA ALOCADO INDEVIDAMENTE NESTAS MISSÕES, AVISE A MESA DE MR.
08/10/2020 23:24 - +55 51 8232-4223: 👍
09/10/2020 10:30 - 🐸: <Arquivo de mídia oculto>
15/10/2020 12:55 - +55 51 9152-2572: Boa tarde colegas! A Gecin está solicitando uma colaboração dos operadores com fotos usando máscara (selfies) na cabine ou perto do trem para divulgação em uma campanha de "dia do maquinista" da ANPTrilhos.
Quem puder participar encaminha por e-mail para kaue.menezes@trensurb.gov.br autorizando a divulgação. Se possível ainda hoje, mais tardar amanhã. Obrigada!
19/10/2020 11:15 - Claiton: Atenção quem for mesário nas próximas eleições: favor me avisar no privado para que eu já faça o lançamento devido nos seus RMOPs antes de liberar o arquivo de novembro. Para o segundo turno, quem for mesário novamente, favor avisar diretamente a mesa de MR porque o arquivo já estará em uso até lá.
20/10/2020 05:07 - Claiton: SEGUR ENTRANDO NA VIA AO SUL DE NT 05:05
26/10/2020 09:26 - +55 51 9698-0812: Relembrando a pedido do David:  O rádio digital não é necessário falar muito próximo do microfone.
26/10/2020 21:13 - +55 51 9154-7572: Mello não  informou sobre atestado para próximos  dias, considerei sua presença.
29/10/2020 05:17 - Claiton: RÁDIO INOPERANTE NA VIA PRINCIPAL:
Devido à falha no sistema de rádio na via principal que teve início ontem 28/10 às 18:30 e que ainda não possui previsão de normalização. Ficou definido o que segue:
a) todos os TUEs deverão portar um aparelho celular corporativo. Os aparelhos deverão permanecer nas cabines e não mais ficar com os OTs durante o turno. Favor OTs que possuírem algum aparelho em sua posse devolvam o mesmo ao SGT de MR ou PT assim que possível.
b) no TM de MR o OT que estiver se deslocando na cabine MA ao TM deverá alcançar o aparelho ao OT que deverá estar aguardando a chegada do TUE já no TM a fim de agilizar a troca de cabine. Caso o OT da cabine MA não alcance o celular ao OT que vier a assumir o TUE na cabine MB o mesmo deverá se dirigira até a cabine MB para entregar o celular ao OT que assumir o TUE. O OT da cabine MB não deverá partir da plataforma de MR sem ter em sua posse o celular correspondente aquele TUE/composição;
c) os celulares deverão ser fixos dos TUEs já que o CCO utilizará os contatos (Cel/TUE) previamente informados ao CCO para realizar contato telefônico sempre que o contato via rádio não for possível (até a falha do sistema de rádio ser sanada);
d) em SC os TUEs S100 que injetarem direto PT/SC poderão parar junto ao OT que estiver aguardando na fila e já alcançar o celular ao OT assumirá a cabine MA, TUEs S200 injetados do PT deverão parar no ponto de parada normal em SC e na VD trocar de cabine levando o celular até o colega na MA. TUEs que estiverem prestando serviço não poderão parar junto ao OT da fila, devendo sempre parar na extremidade norte da V2 e no retorno na V1 trazer o celular até a cabine MA. O OT da cabine MA não deverá partir sem estar em posse do celular correspondente ao TUE;
e) em NH o TUE sempre deverá parar na extremidade norte V2 e a troca do aparelho celular deverá ser feita quando o TUE retornar para a plataforma 1, o OT da cabine MA não deverá partir enquanto não estiver na posse do celular corporativo correspondente aquele TUE/composição;
f) os celulares deverão permanecer sempre ligados com volume de toque máximo e ao final do turno devem ser entregues no PT para recarga. Caso notem baixa carga da bateria deverão solicitar ao SGT de MR a substituição do mesmo e este deverá informar o novo número correspondente aquele TUE/composição ao CCO.

REFORÇANDO: O CELULAR NÃO DEVERÁ SER LEVADO CONSIGO, DEVERÁ PERMANECER SEMPRE NA CABINE QUE FOR LÍDER. Evite de colocar o mesmo no bolso, mantenha o mesmo sempre em local visível para lembrar de entregar ao colega seguinte na troca de cabine. 

Contamos com a colaboração de todos.
29/10/2020 18:00 - +55 51 9152-2572: 👆🏼 Situação normalizada, porém continuem fazendo o procedimento até segunda ordem!
30/10/2020 14:33 - Barcelos: Esclarecimento: a declaração de rotina de monitoramento de sinais e sintomas Civid-19 deve ser entregue preenchida a cada final de mês. Uma ficha para cada mês. Não é necessário o preenchimento total da ficha, mas somente os dias trabalhados em cada mês. Esta havendo confusão e alguns entregaram a ficha só agora, pois aguardaram o preenchimento de todos os campos.
30/10/2020 19:46 - Barcelos: Boa noite.
Deve ser atendido o determinado na RED 0018/2020 
Portanto, todos empregados  devem retornar ao serviço em suas escalas a partir do dia 03/11
30/10/2020 19:49 - Barcelos: Para esclarecimento, acaba a PRONTIDÃO e o ponto volta ao normal com marcação de entrada e saída nos horários normais de cada missao, sem abono das horas não trabalhadas.
31/10/2020 19:02 - Barcelos: Alerto aos colegas que hoje é dia de devolução de todas as folhas da Declaração de rotina de monitoramento de sinais e sintomas Covid-19.
02/11/2020 18:09 - Barcelos: Reforçando a todos, a partir do dia 03/11 todos deverão retornar aos postos de trabalho, realizando suas marcações de ponto normais, como faziam antes da Pandemia. Os abonos de ponto serão considerados esquecimentos e os horários a menos na marcação serão descontados, com a tolerância de até 60 minutos ao mês.
02/11/2020 18:25 - ‎+55 51 9129-0092 saiu
03/11/2020 15:24 - +55 51 9154-7572: Boa tarde! Colegas, nos rádios novos não há necessidade de falar muito próximo ao microfone, ele é bastante sensível e isso acaba prejudicando a comunicação. Att Marcelo
03/11/2020 19:15 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/11/2020 20:05 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/11/2020 20:07 - +55 51 9152-6011: ☝🏼 atualização de comutação automática: TUEs 117, 120, 231, 234 e 238
03/11/2020 20:49 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/11/2020 20:49 - +55 51 9152-6011: Todos os trens em laranja e verde já possuem balizamento automático, ou seja, entrada  do pátio muda automático grupo trens para torre e saída do pátio muda automático grupo torre para trens.
03/11/2020 20:49 - +55 51 9152-6011: Demais vão sendo programados
03/11/2020 21:59 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/11/2020 22:02 - +55 51 9152-6011: ☝🏼"Distância do microfone" reiterando que se deve manter uma distância de 60 centímetros do microfone (dois palmos) para que a transmissão se torne audível. Foi aumentada a sensibilidade do microfone e se falarmos de mais perto a comunicação sai abafada e inaudível.
03/11/2020 23:17 - ‎+55 51 9134-8725 saiu
05/11/2020 14:04 - +55 51 9152-6011: Lista de presença de CURSO DE RÁDIO DIGITAL -  quem não assinou a lista de presença do curso de rádio que teve nos trens, por favor assine. Está em uma pasta azul de treinamento em MR. Preciso entregar. Grato!
06/11/2020 09:28 - +55 51 9963-4149: Novo procedimento de recolhimento dos trens.
Olá pessoal, conforme a orientação da gerência, quando recolher do terminal de MR, o operador que estiver na cabine MA do trem deverá verificar a existência de usuários em seu interior. E, o operador que recolherá o trem, deverá esperar a verificação do colega antes de ir ao pátio.
Caso exista um usuário dentro do TUE o CCO deverá ser acionado.
06/11/2020 13:44 - Barcelos: Pessoal! Estamos iniciando a arrecadação dos valores para encomendar os 'parka'. Na encomenda devemos pagar 50% e os demais 50% na entrega. Assim estamos recolhendo R$ 70,00 ficando  R$ 69,90 para a entrega. Precisamos que seja urgente pois caso contrario não garante o preço, pois houve alta dos insumos. Vamos aproveitar e encomendar logo, pois aqueles que atrasarem podem ter que pagar mais caro.
06/11/2020 13:48 - Barcelos: <Arquivo de mídia oculto>
06/11/2020 13:48 - Barcelos: Depósitos na conta da Jubira acima, enviando o comprovante para a mesma. Quem quiser pagar total antecipado também pode.
06/11/2020 13:57 - Barcelos: Só precisa CPF se for de outro banco.
06/11/2020 15:13 - Barcelos: Segunda feira possivelmente teremos amostras em MR para a escolha de tamanhos.
06/11/2020 16:49 - +55 51 9293-6783: Conforme Ambulatório Gil afastado até dia 19  devido a suspeita de sua esposa estar com COVID
06/11/2020 18:49 - Barcelos: Penso que quando tínhamos SC a tarde, havia seguranças psra fazer esse serviço. Porque não fazem o mesmo em NH, já que não temos SC?
06/11/2020 19:57 - ‎+55 51 9993-0514 saiu
07/11/2020 10:06 - +55 51 9963-4149: <Arquivo de mídia oculto>
07/11/2020 16:57 - Barcelos: Pessoal! Após uma conversacao com a outra cabine através do intercomunicador, deve retornar para TA-PA para poder emitir PA, caso contrário continua conversando com a cabine cauda.
08/11/2020 23:10 - Claiton: <Arquivo de mídia oculto>
08/11/2020 23:11 - Claiton: <Arquivo de mídia oculto>
09/11/2020 00:08 - ‎+55 51 9972-6595 saiu
13/11/2020 10:01 - Claiton: PRONTIDÃO E REGISTRO DE PONTO:

Ficou definido que retorna o sistema de PRONTIDÕES como vinha sendo feito anteriormente. Reforçando que PRONTIDÃO é diferente de FOLGA. 

REGISTRO DE PONTO: NÃO é mais necessário completar as 8:30 horas, mas devem SER REALIZADOS SEMPRE OS DOIS REGISTROS de ponto. O adicional noturno e hora suplementar serão pagos somente sobre o horário registrado.
16/11/2020 06:44 - Claiton: ATENÇÃO MESÁRIOS: Os operadores que serão mesários nas cidades onde houver segundo turno deverão avisar NOVAMENTE a mesa de MR para serem realizados os ajustes nos respectivos RMOPs.
16/11/2020 18:34 - Claiton: Prezados.
A partir de amanhã, 17/11, a Segurança fará a vistoria nos trens que recolhem de MR.
17/11/2020 08:07 - +55 51 9963-4149: Relembrando, a partir de hoje, os recolhimentos programados terão a evacuação na V1 de MR supervisionada pela SEGUR. Para facilitar o processo, solicito a todos os operadores que reposicionem o indicador de destino e emitam a mensagem de recolhimento para agilizar o processo. Desde já agradeço a colaboração.
17/11/2020 08:08 - +55 51 9963-4149: saindo da estação rodoviária
19/11/2020 07:53 - +55 51 9152-6011: Curso de Situação Degradada e Avarias - sala 1 do SETRE - Não precisa registrar ponto nem botina pela manhã. Na parte da tarde é no pátio de manobras. Tragam lanche para o café.
19/11/2020 11:24 - +55 51 9698-0812: Velocidade restrita 60km entre ES e PB via 1 frente da REFAP. Placas indicativas no local de início e fim.
20/11/2020 15:30 - Prado: *ATENÇÃO:* OT's que participaram de treinamento para mesário ou foram mesário, favor, encaminhar documentação ao SEPES para abono.
22/11/2020 21:27 - +55 51 9152-6011: Essa mensagem foi apagada
22/11/2020 21:30 - +55 51 9152-6011: Amanhã 8h - Curso de Situação Degradada e Avarias (rádio digital tb) - sala 1 do SETRE - Não precisa registrar ponto. Na parte da tarde é no pátio de manobras. Tragam lanche para o café.
23/11/2020 09:39 - Quintana/Trem: https://www.tse.jus.br/eleitor/mesario/declaracao-de-dias-trabalhados
23/11/2020 09:41 - Quintana/Trem: Segue o link para obter os comprovantes que deverão ser entregues no SEPES ou enviados por email (ponto@trensurb.gov.br)...abonos encerra quarta, dia 25/11
23/11/2020 14:15 - Quintana/Trem: <Arquivo de mídia oculto>
23/11/2020 16:00 - Patrícia: Atenção aos mesarios do primeiro turno, devem enviar o quanto antes os comprovantes. Amanhã encerra os abonos. 👆🏼👆🏼👆🏼👆🏼
23/11/2020 20:23 - +55 51 9152-2572: <Arquivo de mídia oculto>
23/11/2020 20:23 - +55 51 9152-2572: <Arquivo de mídia oculto>
23/11/2020 20:23 - +55 51 9152-2572: Segue para conhecimento e ampla divulgação,  Regulamento do TRENSURB PREV  e Termo de Adesão ao Plano.
Dúvidas ou outras informações com Andréia - SEPES - Ramal 8118.
24/11/2020 13:53 - ‎Claiton adicionou +55 51 9129-0092
24/11/2020 23:32 - Prado: <Arquivo de mídia oculto>
25/11/2020 17:00 - +55 51 9154-7572: Folha pra impressora mais rolo de papel no armário da supervisão  - Linck
25/11/2020 19:13 - +55 51 9154-7572: Essa mensagem foi apagada
25/11/2020 19:14 - +55 51 9154-7572: Essa mensagem foi apagada
26/11/2020 08:52 - +55 51 9963-4149: Olá pessoal, reforçando que, no novo sistema de radio digital, DEVE-SE FALAR AFASTADO DO MICROFONE. Peço também para esperar o delay de 2 segundos entre pisar no pedal e falar.
27/11/2020 06:26 - +55 51 9152-6011: <Arquivo de mídia oculto>
27/11/2020 06:26 - +55 51 9152-6011: <Arquivo de mídia oculto>
27/11/2020 13:40 - Claiton: Retificando local da reciclagem operação. A parte da manhã está sendo realizada no SETRE Sala 1 e não na sala de bem estar ao lado do refeitório como eu havia informado nas mensagens individuais que enviei a cada um agendando as turmas.
27/11/2020 13:42 - +55 51 9963-4149: Turma de NR10 dia 1/12 cancelada. Todos retornam ao efetivo.
28/11/2020 13:24 - +55 51 9152-6011: Levar caneta para a curso de reciclagem setra
01/12/2020 05:30 - Barcelos: https://youtu.be/i9dZdWDEXRo
01/12/2020 05:30 - Barcelos: Pipoqueira britania
01/12/2020 08:04 - +55 51 9152-6011: Curso reciclagem setra na sala 4 hj no setre
03/12/2020 15:43 - Prado: <Arquivo de mídia oculto>
03/12/2020 17:00 - Prado: <Arquivo de mídia oculto>
03/12/2020 18:53 - +55 51 9152-2572: Colegas, todas as turmas de treinamento que já estavam agendadas foram canceladas e temporariamente suspensas até nova orientação. Solicito que confiram seus RMOPS pois serão incluídos novamente no efetivo.
03/12/2020 18:54 - +55 51 9152-2572: NR10 e Reciclagens 👆🏼
04/12/2020 11:55 - +55 51 9152-6011: <Arquivo de mídia oculto>
04/12/2020 12:50 - +55 51 9152-6011: <Arquivo de mídia oculto>
04/12/2020 12:52 - +55 51 9152-6011: ☝🏼ponto de parada tue acoplado para recolhimento V1
04/12/2020 14:30 - +55 51 9152-6011: <Arquivo de mídia oculto>
04/12/2020 14:32 - +55 51 9152-6011: COVID - VALLERIUS - exame deu negativo. Seus dois filhos tiveram.
04/12/2020 15:08 - +55 51 9152-6011: <Arquivo de mídia oculto>
04/12/2020 15:56 - +55 51 9152-6011: <Arquivo de mídia oculto>
06/12/2020 10:57 - +55 51 9963-4149: Olá, pessoal.
Solicito a todos que, primeiramente, evitem vir no seu próprio trem, e também, ao juntar as voltas, evitar o bate-volta no mesmo, principalmente na grade de 20min de intervalo. Caso ocorra alguma ocorrência operacional há possibilidade real de perda de missão, e ao mesmo tempo, o benefício de se liberar antes ou chegar mais tarde para suas voltas.
Desde já agradeço a compreensão.
06/12/2020 18:59 - +55 51 9154-7572: Tavares fora efetivo, esposa testou Covid positivo. Ele está  bem
07/12/2020 04:06 - +55 51 9152-6011: <Arquivo de mídia oculto>
08/12/2020 11:46 - Quintana/Trem: <Arquivo de mídia oculto>
09/12/2020 14:22 - Barcelos: <Arquivo de mídia oculto>
09/12/2020 14:37 - +55 51 9152-6011: Rádio digital do trem - Começar a abrir falhas de rádio como P.I para ficar registrado e arrumarem.
09/12/2020 16:28 - +55 51 9669-5756: <Arquivo de mídia oculto>
09/12/2020 20:38 - +55 51 9152-6011: <Arquivo de mídia oculto>
09/12/2020 20:38 - +55 51 9152-6011: <Arquivo de mídia oculto>
09/12/2020 20:56 - +55 51 8463-9860: Muito bom Vagner .
09/12/2020 21:07 - +55 51 9152-6011: Legal né! Acredito que vai facilitar os acoplamentos. Mas só revisei e publiquei. Méritos do Jonas pelo esquema e do Guilherme Ribeiro Seofi) pelo procedimento.
09/12/2020 21:08 - Barcelos: Muito bom. Parabéns.
09/12/2020 21:21 - +55 51 9152-6011: Salientando: "Ligar a chave que energiza os pinos de acoplamento do freio microprocessado (acima da caixa laranja) SOMENTE após o acoplamento dos trens! ", para evitar curto ou arco-voltaico
11/12/2020 15:09 - +55 51 9152-6011: RADIO DIGITAL TRENS - A recomendação é deixar o rádio HT desligado e atualizar o do trem (grupo TRENS) na via. Ouço relatos da recepção estar ruim e intercortado. Abram falhas toda vez que estiver ruim e digam os pontos que está saindo intercortada a comunicação. Não podemos "mascarar" as falhas.
14/12/2020 12:38 - +55 51 9152-6011: <Arquivo de mídia oculto>
14/12/2020 12:38 - +55 51 9152-6011: CHAVES SETRA NH - Fica um conjunto de chaves S100+S200 na sala de controle de NH - Quem precisar de uma chave, se identifica e pega o conjunto inteiro e entrega na mesa do Setra MR. O supervisor manda de volta o conjunto para a estação NH
14/12/2020 12:40 - +55 51 9152-6011: Retificando aviso acima: Foi pensado em deixar a chave na estação para quando o colega perder/quebrar a chave, não precisar ir trocando com o da fila e caso a sala esteja chaveada. Melhor na estação pois eles tem controle no RDE de quem pegou visto que nem sempre tem supervisor do setra lá.
14/12/2020 13:16 - +55 51 9152-6011: O preenchimento da RDE é eletrônico. Por isso é só se identificar. Pede para o operador que chegou no trem retornar no mesmo e aí ganha mais tempo, evitando troca-troca de chaves
14/12/2020 13:31 - +55 51 9152-6011: <Arquivo de mídia oculto>
14/12/2020 17:08 - +55 51 9152-2572: Boa tarde!
Quem tiver interesse em realizar o teste de COVID me encaminhe o nome que vou deixar na fila de espera,  na medida que forem surgindo oportunidade eu comunico.
14/12/2020 17:09 - +55 51 8463-9860: Coloca- me na fila.
15/12/2020 15:27 - +55 51 9152-2572: <Arquivo de mídia oculto>
16/12/2020 15:23 - +55 51 9152-2572: Atenção!!!
Composições passar com velocidade acima de 20km/h pelo sinaleiro 10E-A na extremidade Sul de MRV1.
17/12/2020 11:23 - +55 51 9963-4149: Olá pessoal, informo que os dias 24/12 e 31/12 tiveram alteração da grade horária e missões. Peço atenção aos novos horários!
17/12/2020 11:25 - +55 51 9963-4149: <Arquivo de mídia oculto>
17/12/2020 11:31 - +55 51 9963-4149: Este arquivo é somente um exemplo de como ficarão distribuídas as missões. Solicito que verifiquem as alterações no posto de MR.
18/12/2020 02:33 - +55 51 9152-6011: Favor assinar lista de presença dos Rádios digitais (apresentação do rádio nos trens) Atualizei quem fez depois e encontra-se em MR.     Grato!
18/12/2020 02:42 - +55 51 9152-6011: Façam também, quando possível, a avaliação do curso (e do rádio no item 5) pois nosso conhecimento sobre ele deveria ser melhor e me relatam que a recepção do rádio piorou. Precisamos de um rádio de qualidade
22/12/2020 14:25 - Prado: BoA TARDE!!Não esqueçam de pegar HT. A comunicação com os TUE's está pessima.
23/12/2020 16:22 - Quintana/Trem: Atenção...
Para agilizar os abonos de ponto necessários, solicito ao colegas que informem ao supervisor de MR (relógios biométricos inoperantes ou outros problemas que não permitem registrar entrada ou saída), mesmo que os eventos sejam recorrentes. O importante é que as informações sejam lançadas nos RMPOs. Grato a todos.
23/12/2020 19:12 - +55 51 9152-6011: <Arquivo de mídia oculto>
24/12/2020 09:55 - +55 51 8463-9860: Bom dia. DESEJO UM FELIZ NATAL A TODOS E SUAS FAMILIAS.
24/12/2020 11:33 - +55 51 9669-5756: <Arquivo de mídia oculto>
03/01/2021 20:04 - ‎+55 51 9716-8936 saiu
07/01/2021 16:41 - +55 51 9154-7572: Boa tarde! Pessoal, só pra lembrar que se não tiver nenhum problema com o radio do TUE, o transceptor portátil deve permanecer desligado ou com volume baixo, para evitar interferências na comunicação com o CCO. Obrigado! Marcelo.
08/01/2021 11:16 - +55 51 9152-2572: Bom dia,
Reforçamos a necessidade de solicitar abertura de PI ao Supervisor a respeito dos rádios. De qualquer falha, inclusive trechos com sinal ruim. Temos ainda 6 meses de garantia e os problemas tem que aparecer agora para serem solucionados.
08/01/2021 23:07 - +55 51 9154-7572: Dornelles  informou as 22:56hs que sua sobrinha testou positivo, segunda orientei a fazer contato com ambulatório para ver qtos dias ficará  afastado
12/01/2021 11:22 - +55 51 8463-9860: Essa mensagem foi apagada
12/01/2021 11:22 - +55 51 8463-9860: Essa mensagem foi apagada
12/01/2021 11:24 - +55 51 8463-9860: <Arquivo de mídia oculto>
12/01/2021 15:24 - +55 51 8463-9860: Pessoal. Na reforma a sala dos armários, parte da cozinha e o sanitário masculino serão interditados para fazer a ampliação na área da sala dos armários e depois o restante será reformado. Como a antiga sala dos supervisores ficaria muito apertado para colocar os sofás , foi cedida para nós a sala de treinamento ao lado do restaurante. Esta sala é ampla e tem dois sanitários. colocaremos os sofás e  passará a ser usada principalmente a noite. Na sala antiga do supervisor usaremos como extensão da cozinha e alguns armários.
13/01/2021 12:02 - +55 51 8463-9860: Ola Marcos Costa. Entre hoje e amanhã pode retirar os armarios da cozinha.coloca na sala que era do supervisor.
13/01/2021 15:58 - +55 51 9152-6011: <Arquivo de mídia oculto>
13/01/2021 18:40 - +55 51 9152-6011: <Arquivo de mídia oculto>
13/01/2021 18:50 - +55 51 9152-6011: Aperte o asterisco para andar com o HT fora da cabine e na cabine deixe o HT desligado para evitar microfonia. Se a recepção do rádio do trem estiver inaudível, peça para abrir falha
13/01/2021 18:51 - +55 51 9152-6011: O botão vermelho de cima é emergência. Ele tranca todas as outras comunicações e demora para entrar a chamada. Então só utilize em Extrema urgência quando o sinal estiver ocupado constantemente
14/01/2021 06:02 - Claiton: Devido a falsa ocupação na V1 os trens estão chegando atrasados em MR. Tentem chegar ao menos em um trem antes.
14/01/2021 09:06 - Claiton: SEVIP LP/SC Marcha a vista no local
14/01/2021 13:57 - +55 51 9152-6011: <Arquivo de mídia oculto>
14/01/2021 15:28 - +55 51 9152-6011: <Arquivo de mídia oculto>
15/01/2021 11:08 - Claiton: CCO Acabou de informar que a SEVIP retirou a restrição de velocidade 30Km/h RD1/MR1. Velocidade Cab-Signal no trecho.
16/01/2021 04:58 - +55 51 9152-6011: <Arquivo de mídia oculto>
16/01/2021 05:01 - +55 51 9152-6011: ☝🏼aqui vai dizer somente porque o trem não anda. Entre elas:
16/01/2021 05:02 - +55 51 9152-6011: Essa mensagem foi apagada
16/01/2021 05:03 - +55 51 9152-6011: <Arquivo de mídia oculto>
16/01/2021 05:05 - +55 51 9152-6011: <Arquivo de mídia oculto>
16/01/2021 05:08 - +55 51 9152-6011: Falhas (IOS)  que aparecem no canto superior esquerdo da DDU. Laranja pode ser falha do operador ou o trem que não carregou totalmente, normalmente é resolvido. Verde, avisa o CCO e abre falha assim que ocorrer. Vermelho é grave. Falta melhorar mas estás falhas foi as que verifiquei de 2017 em diante que mais ocorreram
17/01/2021 13:27 - +55 51 9963-4149: Olá pessoal. Peço a gentileza que não alterem a posição 1 gelando do controle do ar condicionado da sala da tv de mr. O mesmo está com o termostato em falha.
18/01/2021 05:04 - Claiton: SEGUR e SESIN sul CN

Falsa ocupação V1 e V2 MV/CN. Informar CCO e aguardar liberação para desligar equipamento. Informar CCO quando religar equipamento.

Sinaleiros Norte PB/Norte ES com os 3 aspectos acesos. Não é necessário desligar equipamento, atentar ao cab-signal.

Tentar chegar ao menos um trem antes ao MR.
18/01/2021 05:05 - Claiton: <Arquivo de mídia oculto>
18/01/2021 18:08 - +55 51 8463-9860: <Arquivo de mídia oculto>
18/01/2021 18:10 - +55 51 8463-9860: <Arquivo de mídia oculto>
18/01/2021 18:26 - +55 51 9669-5756: A sala esta sem cortinas?
18/01/2021 18:30 - +55 51 8463-9860: Sim sem cortinas. Tem insulfime. Se ficar muito claro coloco papel pardo.
18/01/2021 18:31 - +55 51 9669-5756: Sim, vamos dar privacidade pro pessoal
18/01/2021 18:34 - +55 51 8463-9860: Ok.
18/01/2021 18:36 - +55 51 8463-9860: <Arquivo de mídia oculto>
18/01/2021 22:14 - +55 51 9154-7572: Ag hur afastado de  19/01 a 28/01 suspeita de Covid
18/01/2021 22:15 - +55 51 9154-7572: Já  tirei do efetivo
19/01/2021 18:32 - +55 51 9152-6011: <Arquivo de mídia oculto>
20/01/2021 14:53 - +55 51 9152-6011: <Arquivo de mídia oculto>
20/01/2021 14:56 - +55 51 9152-6011: Estamos colocando as capinhas nós HTs para evitar danos ☝🏼 Cada capa tem o número do HT. Utilize e entregue na mesa dos supervisores. Se estiver carregado, dá para largar com capa no armário. Se não, o supervisor da mesa retira a capinha, põe a carregar e recoloca a capinha.
20/01/2021 17:55 - +55 51 9152-6011: <Arquivo de mídia oculto>
20/01/2021 20:33 - +55 51 9152-6011: <Arquivo de mídia oculto>
22/01/2021 12:17 - Claiton: Encontram-se em MR os avisos de férias dos seguintes funcionários:
KAUE
FRAGA
VALDIR
MACEDO
PAIM
JUBIRA
MAURO
VENHOFEN
GEORGE
KELLY
ZULEIKA
TELES
MAURICIO
PATRICIA
ELOY
22/01/2021 14:06 - Claiton: <Arquivo de mídia oculto>
22/01/2021 14:06 - Claiton: Aos sábados a missão que recolherá por NH será a missão 14T e não mais a missão 12T
22/01/2021 14:06 - Claiton: Domingo não houve nenhuma alteração
23/01/2021 21:00 - Claiton: Ajustes citados anteriormente foram cancelados mantém se a POL sem alterações.
23/01/2021 21:01 - ‎+55 51 8131-4550 saiu
25/01/2021 13:45 - Claiton: Atenção PROPRIETÁRIOS dos veículos: 
Onix IUT 4565
Ka IYX4044
25/01/2021 13:45 - Claiton: Entrar em contato com a mesa de MR
26/01/2021 02:27 - +55 51 9152-6011: <Arquivo de mídia oculto>
27/01/2021 00:57 - Claiton: Boa noite pessoal, criei o grupo Avisos SETRA também no TELEGRAM este grupo foi criado com o mesmo propósito do grupo Avisos SETRA do WhatsApp. Somente os supervisores poderão postar e o grupo destina se a informar sobre procedimentos, alterações de POL, pequenas instruções que forem julgadas necessárias sobre os TUEs, Rádio digital... Enfim a ideia é que tudo que for postado no grupo do Whatsapp também seja postado no grupo do Telegram
27/01/2021 00:57 - Claiton: Já foram adicionados 46 OTs. E na medida que forem entrando no telegram peço que me avisem para que eu os inclua também no outro grupo
27/01/2021 01:13 - ‎+55 51 9224-8220 saiu
28/01/2021 22:12 - +55 51 9963-4149: Olá pessoal, no posto de MR está a lista para vacinação de gripe deste ano. Solicito aos interessados que preencham para que seja reservada sua dose. A vacinação está programada para abril, portanto, somente será validado o interesse até o dia 26/2. 
Desde já agradeço a atenção.
29/01/2021 15:21 - +55 51 9152-6011: <Arquivo de mídia oculto>
29/01/2021 16:00 - +55 51 9152-6011: <Arquivo de mídia oculto>
29/01/2021 17:27 - Prado: ATENÇÃO NO RECOLHIMENTO HOJE - Haverá algumas alterações
01/02/2021 12:28 - Claiton: <Arquivo de mídia oculto>
01/02/2021 12:30 - Claiton: <Arquivo de mídia oculto>
03/02/2021 18:30 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/02/2021 18:30 - +55 51 9152-6011: <Arquivo de mídia oculto>
03/02/2021 18:46 - +55 51 9152-6011: A chaves do acoplamento elétrico (figura 7) deve estar na posição normal ANTES de acoplar e somente ligá-las depois de acoplar (led "Acoplado acende no painel) para evitar danos elétricos no equipamento
04/02/2021 08:56 - +55 51 8463-9860: Ola.legal estas orientações.
08/02/2021 05:09 - Matheus: Segur e Sesin na via FT/CN V1 Falsa ocupação.
09/02/2021 17:57 - +55 51 9152-6011: <Arquivo de mídia oculto>
09/02/2021 18:00 - +55 51 9152-6011: <Arquivo de mídia oculto>
09/02/2021 18:15 - +55 51 9152-6011: <Arquivo de mídia oculto>
12/02/2021 14:53 - +55 51 9152-6011: <Arquivo de mídia oculto>
12/02/2021 15:50 - +55 51 9669-5756: <Arquivo de mídia oculto>
13/02/2021 20:44 - Claiton: <Arquivo de mídia oculto>
15/02/2021 12:23 - +55 51 8463-9860: Esta previsto a qualquer momento a interdição dos dois sanitários para iniciar a reforma.utolizar os da sala de descanso.
16/02/2021 15:06 - ‎+55 51 9297-5910 mudou para +55 51 9322-9145
18/02/2021 21:24 - +55 51 9963-4149: Olá, peço aos seguintes operadores que assinem amanhã a ciência da nova NPG de Marcha Ré, o documento estará na mesa de mr:
dimas, zozimo, klein, michael, benhur da silva, lino, jorge, paim, ines miranda, claudia, bolzan, nunes, vergara, soares, silvana, senair, andrade, shayene.
18/02/2021 21:35 - +55 51 9963-4149: Olá, peço aos seguintes operadores que assinem amanhã a ciência da nova NPG de Marcha Ré, o documento estará na mesa de mr: Pacheco, jorge filho, junior, gonzaga, silva
19/02/2021 23:55 - +55 51 9963-4149: Olá pessoal, 
como sabido por todos a partir do dia 20/2 teremos os encerramentos das atividades a partir das 22:00. Portanto, as grades de sábado, domingo e dia útil tiveram alterações nos turnos tarde e noite. Sendo assim peço a todos que confirmem seus postos de trabalho com a mesa de MR.
19/02/2021 23:56 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:57 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:57 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:58 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:58 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:59 - +55 51 9963-4149: <Arquivo de mídia oculto>
19/02/2021 23:59 - +55 51 9963-4149: <Arquivo de mídia oculto>
20/02/2021 00:00 - +55 51 9963-4149: <Arquivo de mídia oculto>
20/02/2021 00:01 - +55 51 9963-4149: <Arquivo de mídia oculto>
20/02/2021 14:00 - Prado: BOA TARDE!! *SUBESTAÇÃO LIBERTADE* em manutenção, tensão vai estar baixa ao passar no trecho alimentado por ela!!
20/02/2021 16:28 - Prado: ATENÇÃO: OPERAÇÃO COMERCIAL ATÉ AS 23H25. DUVIDAS LIGAR PARA MERCADO. ESTOU AVISANDO O PESSOAL DA NOITE SOBRE A ALTERAÇÃO
20/02/2021 18:30 - Prado: *ATENÇÃO: VELOCIDADE MÁXIMA DE 70KM/H NO TRECHO SC-NH/V1-V2*
21/02/2021 00:06 - +55 51 9698-0812: VELOCIDADE NORMAL SC/NH. V1 E V2.
22/02/2021 13:09 - Claiton: SEPES
ATENÇÃO
Atestados de matrícula - 1º Semestre/2021

Informamos a todos os empregados com dependentes estudantes de Ensino Médio ou Técnico com idade de 18 a 21 anos (incompletos), ou de Curso Superior com idade de 18 a 25 anos ( incompletos ), em ambos os casos matriculados em instituição de ensino regular, reconhecida pelo MEC e SEC-RS que, para permanência de seus dependentes nos planos de saúde UNIMED e SESI deverão entregar os comprovantes de matrícula do 1° semestre ou do ano letivo de 2021, impreterivelmente, até o dia 26/02/21,  no SEPES - SETOR DE PESSOAL , Prédio de apoio, ou através do e-mail  assistenciamedica@trensurb.gov.br.

Observação: Em caso de envio por e-mail, o documento deve ser digitalizado, não pode ser foto.

De acordo com a NPG-PES-509, " o titular deverá comunicar a TRENSURB quando quaisquer de seus dependentes deixarem de atender as condições que os caracterizam como beneficiário " ; sendo assim, na falta de comprovação da dependência será cobrado o valor integral da mensalidade do Plano de Saúde, a partir de 01/03/21.
 . 
Obs.: Não serão aceitos "solicitação" ou "requerimento" de matrícula, apenas comprovante ou atestado!!
 
Solicitamos aos supervisores, chefes e gerentes que repassem este aviso aos demais colegas que não possuem acesso ao Lotus Notes.
_________________________________________________________________________________________
Incluído por:  Rosita Ferreira Ramos em: 18/02/2021  10:13:17
23/02/2021 11:23 - +55 51 9698-0812: ATENÇÃO: Quem tem interesse na vacina da gripe,  preencher o cadastro em MR.    O prazo encerra sexta dia 26/02.
23/02/2021 11:41 - +55 51 9698-0812: Bom dia... Na sexta temos que enviar a relação dos que querem a vacina em Planilha de excel via CI para o SESET. Para facilitar vamos centralizar no Miguel as informações... As informações  que já tiver aí em MR enviar pra cá e os demais solicitar pelo Ramal 8194 ou ssetra@trensurb.gov.br.
24/02/2021 08:57 - +55 51 9963-4149: Ola pessoal, lista para vacinação da Gripe está com a chefia, caso queira inclusão ou alteração de dado ligar para o 8498, até o dia 26/2.
24/02/2021 13:03 - +55 51 9963-4149: Olá pessoal, a partir de hoje a noite as estações fecharão às 22:00. Portanto, peço a todos que confirmem seus horários, principalmente os turnos tarde e noite. Abaixo estarão os novos horários.
24/02/2021 13:03 - +55 51 9963-4149: noites 24, 25 e 26/2
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: dias 25 e 26 tarde
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: manhas 25 e 26
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 27/2 manha
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 27/2 tarde
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 27/2 noite
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 28/2 manha
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 28/2 tarde
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:03 - +55 51 9963-4149: 28/2 noite
24/02/2021 13:03 - +55 51 9963-4149: <Arquivo de mídia oculto>
24/02/2021 13:45 - Claiton: INFORMANDO QUE AS MISSÕES DE 01N A 07N ESTÃO COM A ENTRADA MAIS CEDO E AS RESPECTIVAS VOLTAS SÃO BEM MAIS CEDO TAMBÉM
24/02/2021 13:45 - Claiton: QUEM TIVER DÚVIDA FAVOR ENTRAR EM CONTATO COM MR
24/02/2021 23:18 - +55 51 9152-6011: <Arquivo de mídia oculto>
25/02/2021 03:43 - +55 51 9152-6011: Estamos sem sistema (rede e internet )
25/02/2021 03:44 - +55 51 9152-6011: Rede Aérea está quente
25/02/2021 05:27 - +55 51 9152-6011: <Arquivo de mídia oculto>
25/02/2021 08:14 - +55 51 9963-4149: Ola pessoal, hoje começou a operação dos TUEs S200, acoplados. Sendo assim a sua preparação tem uma peculiaridade, a sua energização deverá ser feita pelas cabinas intermediárias.
01/03/2021 14:40 - Prado: <Arquivo de mídia oculto>
01/03/2021 14:59 - Prado: <Arquivo de mídia oculto>
01/03/2021 15:21 - Prado: <Arquivo de mídia oculto>
02/03/2021 17:12 - Prado: 5. Ações a serem adotadas no SETRA

5.1 O acesso a cabine dos trens deverá ser restrito a duas pessoas (o operador e mais uma), respeitando a hierarquia determinada na NPG-OPE-107 Controle de Acesso às Áreas Operacionais.
5.2 Excepcionalmente poderão acessar a cabine em duplas (duas pessoas mais o operador), os empregados lotados no SEOPE Processo Segurança, SENERG e SEVIP, quando efetuando inspeção de via ou sistemas.
5.3 Os empregados que solicitarem acesso a cabine deverão estar, obrigatoriamente, utilizando máscara facial.
5.4 Excepcionalmente o acesso a cabine cauda durante a Operação será autorizado além das condições dispostas na NPG-OPE-107, desde que atendendo os seguintes requisitos:
5.5.1 A excepcionalidade se restringe aos operadores de trem;
5.5.2 O aceso será permitido para apenas um operador por vez;
5.5.3 O operador, antes de efetuar o acesso, deverá comunicar ao SGT de MR e ao CCO a estação de embarque;
5.5.4 O CCO informará ao operador do trem em que haverá o acesso a cabine cauda;
5.5.5 Após acessar a cabine cauda o operador informará ao operador titular sobre sua presença na cabine cauda;
5.5.6 Ao efetuar o acesso a cabine cauda, o operador deverá ter o máximo cuidado para que se evite acidentes;
5.5.7 O acesso a cabine cauda, em hipótese alguma poderá ser feito com o trem em movimento.
02/03/2021 17:12 - Prado: OSI-DIROP 0002/2021
02/03/2021
03/03/2021 06:00 - Claiton: <Arquivo de mídia oculto>
03/03/2021 12:27 - Claiton: A partir de hoje 3/3 houve a inversão dos recolhimentos das missões 09T x 01T e 19T x 11T. As missões 09T e 19T passam a encerrar em MR e as missões 01T e 11T passam a recolher de NH. Além disso a primeira volta da missão 24T passa a ser 17:00 e a missão 04T partirá de MR às 17:07.
03/03/2021 13:59 - 🐸: Óculos laranja 🍊 é do Roger..,
Esqueceu hoje na injeção!
03/03/2021 14:26 - Claiton: Já pegou
04/03/2021 16:33 - Matheus: <Arquivo de mídia oculto>
04/03/2021 21:18 - +55 51 9154-7572: <Arquivo de mídia oculto>
05/03/2021 15:06 - Matheus: <Arquivo de mídia oculto>
05/03/2021 15:25 - Claiton: Alteração Grades de Sábado e domingo:
A PARTIR DE AMANHÃ 6/3 os trens passarão a ter intervalos de 20 minutos aos sábados e 30 minutos aos domingos. A POL de sábado já está colada. Amanhã colarei a POL de domingo dia 7 e dos demais finais de semana.  Avisarei os OTs do domingo um a um.
06/03/2021 11:11 - +55 51 9963-4149: Ola pessoal, agora as chaves reservas de NH ficarão no cofre ao lado da porta de entrada da sala de pilotos de NH. Abaixo está o vídeo de como abrir o cofre. A senha está com o supervisor de MR. O mesmo deverá ser avisado sobre o uso das chaves e o seu retorno ao cofre.
06/03/2021 11:12 - +55 51 9963-4149: <Arquivo de mídia oculto>
10/03/2021 12:17 - +55 51 9152-6011: <Arquivo de mídia oculto>
11/03/2021 12:36 - +55 51 8260-0372: TUEs 108 e 235 já estão com a mudança manual do grupo de comunicação de rádio para entrada e saída do pátio.
11/03/2021 12:38 - +55 51 8260-0372: Conforme os TUEs forem atualizados o seitec vai repassando a relação para o Setra.
11/03/2021 12:40 - +55 51 8260-0372: Em breve toda frota voltará a ter a mudança manual dos grupos TRENS e TORRE.
12/03/2021 16:25 - Prado: <Arquivo de mídia oculto>
16/03/2021 14:13 - +55 51 9152-2572: <Arquivo de mídia oculto>
16/03/2021 17:39 - +55 51 9152-2572: <Arquivo de mídia oculto>
16/03/2021 17:40 - ‎Patrícia adicionou +55 51 9166-0683
17/03/2021 22:55 - +55 51 9152-6011: <Arquivo de mídia oculto>
17/03/2021 23:24 - Claiton: Essa mensagem foi apagada"""

phones = re.findall(r'\d{2}\s+\d{4}-\d{4}', data, flags=re.M)
for i in phones:
    print(i)

unique_list = list(set(phones))
for i in unique_list:
    print(*i)

print(len(phones), len(unique_list))
print(unique_list)






