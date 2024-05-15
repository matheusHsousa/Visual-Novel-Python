define e = Character("Narrador")
define marido = Character("???")
define c = Character("Cientista")
image cientista = "images/cientista.png"
image lanchonete = "images/lanchonete.png"
image narrador = "images/narrador.png"
image cidade = "images/cidade.png"
image jornal = "images/jornal.jpg"
image ligacao = "images/ligação.jpg"
image telefonema = "images/telefonema.png"
image falatelefo = "images/falatelefo.jpg"
image casaDetetive = "images/casaDetetive.jpg"
image final1 = "images/final1.jpg"
image quartos = "images/quartos.jpg"
image floresta = "images/floresta.png"
image florestaInterna = "images/florestaInterna.jpg"
image tomar = "images/tomar.jpg"
image pos = "images/posRemedio.jpg"
image final2 = "images/final2.jpg"
image lab = "images/lab.jpg"
image casaVitima = "images/casa.png"
image bater = "images/bater.jpg"
image abrir = "images/abrir.jpg"
image abriu = "images/abriu.jpg"
image dumbman = "images/final3.jpg"
image cozinha = "images/cozinha.png"
image quarto = "images/quarto.png"
image lendo = "images/lendo.png"
image riacho = "images/riacho.png"
image pegar = "images/pegar.jpg"
image sangue = "images/maoSangue.jpg"
image correndo = "images/correndo.jpg"
image final = "images/final.jpg"



transform shake:
    ease .1 xoffset 24 
    ease .1 xoffset -24
    ease .1 xoffset 20
    ease .1 xoffset -20
    ease .1 xoffset 16
    ease .1 xoffset -16
    ease .1 xoffset 12
    ease .1 xoffset -12
    ease .1 xoffset 8
    ease .1 xoffset -8
    ease .1 xoffset 4
    ease .1 xoffset -4
    ease .1 xoffset 0

init:
 python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)


define pov = Character("[povname]", image="detetive")
image define detetive idle = "images/detetive.png"
image define detetive sangue = "images/detetive.png"


define z = Character("???", image="semnome")
image define semnome idle = "images/semnome.png"


init:
    $ flash = Fade(.50, 0, .75, color="#fff")




label start:

    play music "audio/fundo.mp3" volume 0.5

    scene lanchonete
    show narrador:
        xpos 600
        ypos 1,0
        xanchor 0,9
        yanchor 1,0
    
    
    $renpy.sound.play("audio/pessoas.mp3", loop=True) 


    e "Olá meu querido jogador, antes de começarmos o jogo preciso saber que nome gostaria de usar durante a historia..."

    $ povname = renpy.input("Qual o seu nome?", length=32 )
    $ povname = povname.strip()

    pov "Meu nome é [povname]."

    e "Olá [povname], não poderei citar meu nome, porém pode me chamar de narrador, eu te conduzirei ao longo dessa historia..."

    e "Agora que fomos devidamente apresentados, acredito que podemos começar!"

    stop sound fadeout 1.0

    scene cidade
    with flash


    e "Nossa cidade de Nikolinos é muito tranquila e pacifica, ou na verdade era..."
    e "Na verdade nunca sabemos o que pode acontecer"
    show narrador:
        xpos 0,15
        ypos 1,0
        xanchor 0,5
        yanchor 1,0
    e "Em um momento tudo está certo mas do dia para noite, reviravoltas podem acontecer..."

    scene jornal
    with flash

    z idle "Já faz um tempo que ela está desaparecida..."

    z idle "Pelo visto não terei mais escolha..."

    z idle "Minha esposa já está desaparecida a 3 dias..."

    z idle "Vou ligar para o detetive [povname]"

    scene ligacao

    # play sound 
    $renpy.sound.play("audio/telefone.mp3", loop=True)

    "too..."
    "too...too..."
    "too...too...too..."
    "too..."
    "too...too..."
    "too...too...too..."
    "too..."
    "too...too..."
    "too...too...too..."

    stop sound
    
    scene telefonema
    with flash


    "."
    ".."
    "..."

    scene falatelefo
    with flash

    $renpy.sound.play("audio/conversa.mp3", loop=True)


    z idle "...alô?"
    
    pov idle "Olá?"

    z idle "..eh..eh..Meu nome é *******, gostaria de falar com o detetive [povname]?"
  
    pov idle "Pode falar. Sou ele!"

    z idle "Então, sou marido da mulher que desapareceu a alguns dias..."

    z idle "..gostaria de contratar seus serviços para encontrala..."

    z idle "Estou muito preocupado sabe..."

    z idle "Não queria pensar dessa forma..."

    z idle "Mas não acredito que verei ela com vida novamente..."

    "."
    ".."
    "..."

    pov idle "Entendo sua preocupação..."

    pov idle "Farei o meu melhor como detetive..."

    pov idle "Espero conseguir..."

    pov idle "Conseguir fazer você reencontra-lá da melhor maneira..."

    "(Barulho de choro)"

    "."
    ".."
    "..."

    z idle "Acredito em você..."

    pov idle "Poderia me dizer onde foi a ultima vez que a viu?"

    z idle "Bom... não sei exatamente, a policia achou algumas pistas..."

    z idle "...Da ultima vez que falaram comigo me disseram que acharam rastros na floresta..."

    z idle "...Rastros esses que coincidem com uma mulher..."

    pov idle "Entendi, vou começar minhas buscas. Até logo!"
    
    z idle "Até..."

    scene casaDetetive
    with flash

    show narrador:
        xpos 0,15
        ypos 1,0
        xanchor 0,5
        yanchor 1,0




    stop sound

    e "Olá de novo, [povname]!"

    e "Agora o jogo começa de verdade para você, meu querido detetive..."



    menu:
     "O que tú quer fazer?"

     "Desistir.":
         pov idle"vou não mano, to de boa..."
         e "voce é um cagão"
         jump cagao

     "Investigar.":
         $ Jogar = True
         jump investigar            
         "bora que bora, quero resolver logo esse misterio!"
                  
         
label cagao:
    window hide 
    stop music
    play music "audio/cagao.mp3" 
  

    show final1 with vpunch
    window hide 
    pause 5.0


    return


label investigar:

    play music "audio/fundo.mp3" volume 0.5

    e "Muito bem jogador, para onde deseja ir?"

    menu:
     "Pra onde tu que ir?"

     "Floresta.":
         pov idle"vou não mano, to de boa..."
         e "voce é um cagão"
         jump floresta

     "To de boa, vou ficar por aqui.":
         $ Jogar = True            
         "bora que bora, quero resolver logo esse misterio!"
         call screen narrador_screen


screen narrador_screen:
  add "images/casaDetetive.jpg"
  imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.3 
        ypos 0.28
        idle "images/narrador_idle.png"
        hover "images/narrador_houver.png"
        action Jump("floresta")  

  imagebutton:
        xanchor 0.5
        yanchor 0.3
        xpos 0.82 
        ypos 0.3
        idle "images/escada_idle.png"
        hover "images/escada_houver.png"
        action Jump("quartos") 


label quartos:
    play music "audio/fundo.mp3" volume 0.5
    scene quartos
    "Não tem nada aqui! bobinho..."
    call screen narrador_screen


label floresta:
    play music "audio/fundo.mp3" volume 0.5
    scene floresta
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pause 5.0
    pov idle"Hmm, essa floresta está muito calma"
    call screen telaFloresta
    stop sound
    
    
screen telaFloresta:

  add "images/floresta.png"
  imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.51 
        ypos 0.72
        idle "images/porta da floresta.png"
        hover "images/hover_PORTA.png"
        action Jump("florestaInterna")  

    
label florestaInterna:
    play music "audio/fundo.mp3" volume 0.5
    scene florestaInterna
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pov idle "Talvez eu ache alguma prova aqui"
    pause 3.0
    call screen florestaBusca

screen florestaBusca:
    add "images/florestaInterna.jpg"
    imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.83 
        ypos 0.73
        idle im.Scale("images/remedio_hover.png", 50, 50)
        hover "images/remedio.png"
        action Jump("remedio")  
    imagebutton:
        xanchor 0.1
        yanchor 0.2
        xpos 0.167
        ypos 0.75
        idle im.Scale("images/camiseta.png", 150, 150)
        hover "images/camiseta_hover.png"
        action Jump("iten1")

label iten1:
    play music "audio/fundo.mp3" volume 0.5
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pov idle "Eca sangue, vo mexer mais nisso não..."
    pov idle "..deve ter nada ver com o caso!"
    call screen florestaBusca
    stop sound

label remedio:
    play music "audio/fundo.mp3" volume 0.5
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pov idle"Esse remedio deve ser algo importante..."
    pov idle"o que devo fazer?"
    stop sound

    menu:
     "escolha:"

     "Levar para laboratorio":
         pov idle"Devo levar ao laboratorio"
         pov idle"eles devem saber com precisão se são remedios, drogas ou veneno"
         e "Muito bem detetive..."
         e "vamos até o laboratorio"
         jump lab

     "guardar comprimidos":            
         e "espero que tenha feito a escolha certa..."
         call screen guardar



screen guardar:
  add "images/casaDetetive.jpg"
  imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.3 
        ypos 0.28
        idle "images/narrador_idle.png"
        hover "images/narrador_houver.png"
        action Jump("fala2")  

  imagebutton:
        xanchor 0.5
        yanchor 0.3
        xpos 0.82 
        ypos 0.3
        idle "images/escada_idle.png"
        hover "images/escada_houver.png"
        action Jump("quartos") 

label fala2:
    scene casaDetetive
    with flash
    scene casaDetetive
    show narrador:
        xpos 0,15
        ypos 1,0
        xanchor 0,5
        yanchor 1,0



    e "Está é sua ultima chance, tome o remedio ou leve ao laboratorio"

    menu:
     "escolha:"

     "Levar para laboratorio":
         pov idle"Devo levar ao laboratorio"
         pov idle"eles devem saber com precisão se são remedios, drogas ou veneno"
         show narrador:
             xpos 0,15
             ypos 1,0
             xanchor 0,5
             yanchor 1,0
         e "Muito bem detetive..."
         e "vamos até o laboratorio"
         jump lab

     "Tomar":            
         e "espero que tenha feito a escolha certa..."
         jump Tomar

label Tomar:
    stop music

    scene tomar
    with flash
    pause 1.0
    scene pos
    with flash
    $renpy.sound.play("audio/engolir.mp3", loop=True)
    pause 3.0
    stop sound
    pause 2.0
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    pause 1.0
    scene final2
    play music "audio/amimir.mp3" 
    pause 6.8

return

label lab:
    scene lab
    with flash
    show cientista at center:
         zoom 1.7
        
    c "Olá [povname]..."
    c "Os resulatos devem sair em breve"
    c "Passe aqui, em aproximadamente uma hora e eles já devem estar prontos"
    pov idle "Ok ok..."
    
    hide cientista

    pov idle "Para onde sera que devo ir agora?"
    pov idle "Poderia ir até a casa do meu contratante..."
    pov idle "É isso mesmo, vou ver se acho algo na casa..."

    jump casaVitima
    
label casaVitima:
   
   $renpy.sound.play("audio/bater.mp3", loop=True)
   scene bater
   with vpunch
   with vpunch
   with vpunch
   with vpunch
   stop sound

 
   pause 2.0 
   scene abrir 
   pause 2.0 
   scene abriu 
   pause 2.0 


   scene casaVitima
   with flash
      
   pov idle "Parece que não tem ninguem em casa..."
   pov idle "Mas tudo parece normal por aqui..."
   pov idle "Será que devo invadir?..."


   menu:
     "escolha:"

     "Ir embora":
         pov idle"Não devo encontrar nada por aqui..."
         e "Você é meio burro né?"
         jump dumb

     "investigar":            
         pov idle "Devo averiguar todas as possibilidades!"
         call screen casaVitimaTela

label dumb:
    stop music
    play music "audio/burro.mp3" 

    scene dumbman
    with flash
    pause 5
return



screen casaVitimaTela:
  add "images/casa.png"
  imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.297 
        ypos 0.512
        idle "images/cozinha_idle.png"
        hover "images/cozinha_hover.png"
        action Jump("cozinha")  

  imagebutton:
        xanchor 0.5
        yanchor 0.3
        xpos 0.53 
        ypos 0.516
        idle "images/subir_idle.jpg"
        hover "images/subir_hover.jpg"
        action Jump("quarto") 


label cozinha:

    scene cozinha
    pov idle "parece não ter nada por aqui..."
    call screen casaVitimaTela


label quarto:

    scene quarto
    pov idle "Será que tem algo por aqui?"
    call screen quartoBusca

screen quartoBusca:
    add "images/quarto.png"
    imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.817 
        ypos 0.54    
        idle  im.Scale("images/carta.png", 70,70)
        hover "images/carta_hover.png"
        action Jump("lendo")
  
label lendo:

    scene lendo
    e "Não estava aguentando mais...."
    e "As vozes falavam comigo todos os dias..."
    e "'Queima! Mata! Destroi!' dizim elas..."
    e "se eu continuasse..."
    e "Talvez todos ao meu redor não estariam mais aqui..."
    e "Então esse é o meu adeus..."
    e "Para todos que um dia me amaram..."

    pov idle "devo ir até o laboratorio" 
    jump lab2 


label lab2:
    scene lab
    with flash
    show cientista at center:
         zoom 1.7
        
    c "Olá [povname]..."
    c "sairam os resultados do sobre a amostra que deixou aqui..."
    c "era tioridazina, um medicamento aplamente usado para esquizofrenia..."
    c "e sindrome de multiplas personalidades..."

    hide cientista

    pov idle "Certo... já entendi tudo o que aconteceu..."
    pov idle "Tenho que ir agora para a floresta"

    jump floresta2

label floresta2:
    play music "audio/fundo.mp3" volume 0.5
    scene floresta
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pause 5.0
    pov idle"Hmm, calma como sempre"
    call screen telaFloresta2
    stop sound
    
    
screen telaFloresta2:

  add "images/floresta.png"
  imagebutton:
        xanchor 0.5
        yanchor 0.2
        xpos 0.51 
        ypos 0.72
        idle "images/porta da floresta.png"
        hover "images/hover_PORTA.png"
        action Jump("florestaInterna2")  

    
label florestaInterna2:
    play music "audio/riacho.mp3" volume 0.5
    play music "audio/fundo.mp3" volume 0.5
    scene florestaInterna
    $renpy.sound.play("audio/floresta.mp3", loop=True)
    pov idle "Onde será que ela pode estar..."
    pov idle "Estou ouvindo um barulho de agua..."
    pov idle "Vou seguir em direção a ele..."

    jump riacho

label riacho:
    play music "audio/riacho.mp3" volume 1
    scene riacho
    pov idle "O que é aquilo?"
    call screen faca

screen faca:

  add "images/riacho.png"
  imagebutton:
        xanchor 0.53
        yanchor 0.2
        xpos 0.243 
        ypos 0.8
        idle im.Scale("images/faca_idle.png", 90,90)
        hover im.Scale("images/faca.png", 190,190)
        action Jump("final4")

label final4:
    scene pegar
    pause 1
    scene sangue
    with Shake((0, 0, 0, 0), 1.0, dist=30)
    pause 1
    scene pegar
    pause 0.8
    scene sangue
    pause 0.8
    scene pegar
    pause 0.4
    scene sangue
    pause 0.4
    scene pegar
    pause 0.2
    scene sangue
    pause 0.2
    scene pegar
    pause 0.2
    scene sangue
    pause 0.2
    scene pegar
    pause 0.1
    scene sangue
    pause 0.1
    scene pegar
    pause 0.1
    scene sangue
    pause 0.1

    pov sangue "O que está acontecendo..."
    pov sangue "eu... eu... não me lembro de nada"
    e "Você finalmente descobriu quem é o assassino?"


    pov "Não... não... não acredito..."
    e "Não fuja de você mesmo"
    pov "AHHHHHH"

    scene correndo
    with flash 
    pause 3.0

    jump final

label final:
    stop music
    play music "audio/louco.mp3" 
    scene final
    with flash
    pause 3.0
return