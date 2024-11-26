# aleandro
trabalho de micros 2
Pratica 5

A pratica 5 consistiu em reutilizar um programa de alguma pratica feita anteriormente e fazer com que ele seja executado junto com a inicializaçào do sistema operacional.
Utilizamos o programa que faz um led piscar, o blink.py, porém ele foi modificado para que acendam dois leds, um branco e um verde, sendo que eles piscam de forma alternada. (blink2.py)
Para excecuta-lo ao ligar a raspberry pi foi necessario criar um arquivo com a extensão .service (extensão que o systemd lê), este arquivo (blink2.service) contem uma descrição breve para identificar o blink2.py, 
ele também contém o diretorio em que o blink2.py e o diretorio em que o python são escontrados.
Também foi necessario criar um programa que fosse executado quando o blink2.service é interrompido, o programa criado (blink3.py) fazia com que um led vermelho começasse a piscar. Este programa foi inserido no blink2.servide 
da mesma forma que o blink2.py foi.
O blink2.service pode ser executado e interrompido manualmente. Para fazer-lo iniciar junto do OS é necessario utilizar um comando especifico.
Tudo ocorreu sem maiores problemas. O unico detalhe é que quando é inputada uma parada manual o blink2.py fica sendo executado por alguns minutos antes de parar por completo. 
