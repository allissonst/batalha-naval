<html>
  <body>
    <h1>:arrow_forward: Jogo de batalha naval feito em Python</h1>

   <p> <a href="https://replit.com/@allissont/batalha-naval-1#main.py">Clique aqui para jogar on-line</a></p>
    
  <p><h2>Regras do jogo:</h2></p>

O tabuleiro de cada jogador deverá ser representado por uma matriz quadrada de ordem 10, sendo as linhas identificadas por letras (A a J) e as colunas por números (1 a 10).

A frota de cada jogador será composta por navios, onde cada um deles ocupará uma célula da matriz. 

A quantidade de navios da frota será igual para ambos jogadores e deverá ser definida pelo usuário no início de jogo (máximo de 10). 

Ao ser iniciado um novo jogo, a frota de cada jogador deverá ser posicionada no respectivo tabuleiro de forma aleatória pelo computador. Essa alocação deverá ser feita colocando-se a letra “N” na célula onde ele estiver posicionado. Obs: um navio não pode ficar encostado em outro (nem adjacente e nem diagonal). 

Após os navios terem sido posicionados, o jogo continua numa série de tiros, que consiste no jogador escolher uma coordenada (linha x coluna) para tentar atingir algum navio do oponente. 

Se o tiro for certeiro deverá aparecer a palavra “FOGO” e na posição do tiro ser exibida a letra “F”. Esse mesmo jogador continuará atirando até errar.

Caso contrário, deverá aparecer a palavra “ÁGUA” e na posição do tiro ser exibido a letra “A”. Nesse caso, a vez de jogar passará para o outro jogador. 

Os dois tabuleiros devem ficar sempre visíveis na tela. Vale ressaltar que, inicialmente, as frotas não devem aparecer nos tabuleiros, irão aparecer gradativamente à medida que os navios forem sendo atingidos. 

O jogo é encerrado quando um jogador afundar todos os navios do seu oponente. 

ATENÇÃO: para fins de teste, o programa deverá permitir tornar visível as frotas. 
  </body>
</html>
