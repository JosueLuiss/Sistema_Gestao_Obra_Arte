from flask import Flask, render_template
from artista import Artistas
from categoria import Categoria
from obra_arte import Obra_arte
from comentarios import Comentario
from exibicoes import Exibicao
from leiloes import Leilao

app = Flask(__name__)

artistas_list = [
    Artistas(1, ' Leonardo da Vinci', 'https://p2.trrsf.com/image/fget/cf/1200/1200/middle/images.terra.com/2019/06/24/leo.jpg', 'Leonardo da Vinci (1452-1519) foi um dos maiores gênios da história, conhecido por sua vasta produção intelectual e artística. Nascido em Vinci, na Itália, ele foi pintor, escultor, arquiteto, cientista, engenheiro, inventor e anatomista, entre outras coisas. Seu trabalho abrangeu diversas áreas do conhecimento humano, e sua curiosidade insaciável o levou a explorar temas que iam desde a anatomia humana até a engenharia militar e a física.'),
    Artistas(2, 'Michelangelo', 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJOWc6Ipehuf3tL2dGfmbtkTxzHenqw1Rq57DhKxf6j0l_r41FZ4sikaNuxqUGINOidUkw-k-ZUieF1b4290K1fD3JrwvrUp8sPL2lrLuifj8-3yXwNiOKl9H7ovSywNMxuNg5jad_4aU/s1600/michelangelo.jpg', 'Michelangelo Buonarroti (1475-1564) foi um dos maiores artistas do Renascimento italiano, conhecido por sua genialidade em escultura, pintura, arquitetura e poesia. Ele nasceu em Caprese, na Itália, e sua obra é marcada pela busca pela perfeição técnica e pela expressão emocional intensa. Entre suas criações mais notáveis estão a escultura David, que exemplifica a idealização do corpo humano, e o teto da Capela Sistina, onde pintou cenas bíblicas, como a Criação de Adão, em uma obra monumental que se tornou um ícone da arte ocidental. Michelangelo também teve um papel importante na arquitetura da Basílica de São Pedro, no Vaticano. Sua habilidade em representar a anatomia humana com realismo, seu uso inovador da luz e sombra e sua capacidade de capturar a emoção humana fizeram dele uma figura central no desenvolvimento da arte renascentista. Ele é frequentemente considerado um dos maiores artistas de todos os tempos, com uma influência duradoura em várias gerações de artistas.'),
    Artistas(3, 'Ansel Adams', 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgw3XJFYaqEREj1mAOAq3hv3uegYTwLlMTA-9Xt5dTBrCpOi1ocXUO8Odtg2RWWV1kOIbSANS34h52w5UvlrEJG2N-0EYiNTL-CjxECFU9tWIXEweo6D_8NvXAck39UiLdY-OSryYKyEa0/s1600/ansel_adams.jpg', 'Ansel Adams (1902-1984) foi um renomado fotógrafo e ambientalista americano, conhecido por suas impressionantes imagens em preto e branco da natureza, especialmente do Parque Nacional de Yosemite, na Califórnia. Considerado um mestre da fotografia de paisagens, Adams utilizou técnicas inovadoras de exposição e impressão para capturar a grandiosidade e a beleza da natureza americana. Ele foi um defensor ardente da preservação ambiental e suas fotografias ajudaram a sensibilizar o público sobre a importância da conservação dos parques nacionais e das terras selvagens. Adams também desenvolveu o famoso "Sistema de Exposição de Zona", uma técnica que lhe permitiu controlar de forma precisa os tons e o contraste em suas imagens. Seu trabalho continua a ser uma referência para fotógrafos e amantes da natureza, e sua contribuição para a arte e a conservação é amplamente reconhecida.'),
    Artistas(4, 'Albrecht Dürer', 'https://uploads6.wikiart.org/images/albrecht-durer.jpg!Portrait.jpg', 'Albrecht Dürer (1471-1528) foi um dos artistas mais importantes da Renascença do Norte e é amplamente reconhecido por suas inovações na gravura, pintura e desenho. Nascido em Nuremberg, na Alemanha, Dürer se destacou por sua habilidade técnica e por sua capacidade de combinar o detalhamento da tradição medieval com as influências do Renascimento italiano, especialmente em sua abordagem à perspectiva e à proporção. Ele é particularmente famoso por suas gravuras e xilogravuras, como Melancolia I, O Cavaleiro, a Morte e o Diabo e O Rinoceronte, que demonstram seu talento na criação de imagens complexas e simbólicas. Além de suas obras gráficas, Dürer também produziu pinturas notáveis, como o Autorretrato e o Adão e Eva, que exploram tanto a técnica refinada quanto o simbolismo. Sua contribuição para a arte, especialmente no campo da gravura, teve um impacto duradouro, influenciando gerações de artistas em toda a Europa.'),
]

categoria_list = [
    Categoria(1, 'Pintura'),
    Categoria(2, 'Escultura'),
    Categoria(3, 'Fotografia'),
    Categoria(4, 'Gravura')
]

obra_arte_list = [
    Obra_arte(1, 'Mona Lisa', 'Leonardo da Vinci',  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_x9lYphCQoGyOXWoASL2sLh0ZOLE9vKL_Gg&s', 1503, 'A Mona Lisa, também conhecida como La Gioconda, é uma das obras mais famosas do pintor italiano Leonardo da Vinci. Pintada entre 1503 e 1506, provavelmente continuada até 1517, é uma pintura a óleo sobre madeira, com 77 x 53 cm de dimensões. A obra retrata uma mulher com um sorriso enigmático e um olhar penetrante que parece seguir o espectador, o que lhe confere uma aura de mistério e fascinante realismo.', 1, 1, 1),
    Obra_arte(2, 'A Última Ceia', 'Leonardo da Vinci', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Leonardo_da_Vinci_%281452-1519%29_-_The_Last_Supper_%281495-1498%29.jpg/300px-Leonardo_da_Vinci_%281452-1519%29_-_The_Last_Supper_%281495-1498%29.jpg', 1495, 'A Última Ceia é uma das pinturas mais icônicas de Leonardo da Vinci, criada entre 1495 e 1498. Esta obra foi pintada a fresco na parede do refeitório do Convento de Santa Maria delle Grazie, em Milão, e retrata o momento em que Jesus Cristo compartilha a última refeição com seus apóstolos antes de sua crucificação.', 1, 1, 2),
    Obra_arte(3, 'Dama com Arminho', 'Leonardo da Vinci','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Leonardo_da_Vinci_046.jpg/250px-Leonardo_da_Vinci_046.jpg', 1489, 'Dama com Arminho é uma pintura do renascentista italiano Leonardo da Vinci, criada entre 1489 e 1490. A obra retrata Cecilia Gallerani, uma jovem da corte milanesa, que era amante de Ludovico Sforza, o Duque de Milão e patrono de Da Vinci. O arminho, animal que ela segura, simboliza pureza, mas também é associado a Ludovico, que tinha o apelido de "Ermellino" (arminho, em italiano). A pintura é famosa por sua inovação no retrato, pois Cecilia é representada em uma posição de perfil virado, transmitindo uma sensação de movimento e profundidade psicológica. Esta obra é admirada pela técnica detalhada e pelo uso sutil de luz e sombra, refletindo o estilo característico de Da Vinci e seu domínio do sfumato, que dá ao retrato uma qualidade de realismo e suavidade.', 1, 1, 3),
    Obra_arte(4, 'A Virgem dos Rochedos', 'Leonardo da Vinci', 'https://www.historiadasartes.com/wp-content/uploads/2017/10/m_DetalheLeonardoDaVinciVirgemRochedosNationalGallery.jpg', 1483, 'Virgem dos Rochedos é uma obra emblemática de Leonardo da Vinci, com duas versões, uma criada entre 1483 e 1486 e outra por volta de 1495 a 1508. As pinturas foram encomendadas para uma capela em Milão e apresentam a Virgem Maria com o Menino Jesus, o anjo Uriel e o jovem São João Batista, em um cenário de cavernas e formações rochosas.', 1, 1, 4), 
    Obra_arte(5, 'São João Batista', 'Leonardo da Vinci', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Anton_Raphael_Mengs_-_St._John_the_Baptist_Preaching_in_the_Wilderness_-_Google_Art_Project.jpg/250px-Anton_Raphael_Mengs_-_St._John_the_Baptist_Preaching_in_the_Wilderness_-_Google_Art_Project.jpg', 1513, 'A obra João Batista, atribuída a diversos artistas ao longo da história, geralmente retrata o profeta João Batista, figura central no cristianismo, conhecido por pregar sobre o arrependimento e batizar Jesus no rio Jordão. Em suas representações artísticas, ele é frequentemente mostrado com uma pele de camelo, como descrito na Bíblia, e segurando um bastão ou uma cruz, símbolos de sua missão profética.', 1, 1, 5),
    Obra_arte(6, 'Davi', 'Michelangelo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/David_SM_Maggiore.jpg/220px-David_SM_Maggiore.jpg', 1501, 'David é uma das esculturas mais famosas de Michelangelo, esculpida entre 1501 e 1504 durante o Renascimento italiano. A obra representa o herói bíblico Davi em uma pose de tensão contida, momentos antes de enfrentar o gigante Golias. A escultura, com mais de cinco metros de altura, é feita em mármore e mostra o impressionante domínio de Michelangelo sobre a anatomia humana, com músculos e veias detalhados que conferem uma sensação de vida e força ao personagem.', 2, 2, 1),
    Obra_arte(7, 'Teto da Capela Sistina', 'Michelangelo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Sistine_chapel.jpg/300px-Sistine_chapel.jpg', 1508, 'O Teto da Capela Sistina é uma das mais grandiosas obras de Michelangelo, pintada entre 1508 e 1512 a pedido do Papa Júlio II. O teto cobre uma área extensa da capela no Vaticano e apresenta cenas do Gênesis, incluindo a famosa criação de Adão, onde a mão de Deus quase toca a mão de Adão, simbolizando o ato de dar vida à humanidade.', 2, 2, 2),
    Obra_arte(8, 'A Pietà', 'Michelangelo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Michelangelo%27s_Pieta_5450_cropncleaned_edit.jpg/320px-Michelangelo%27s_Pieta_5450_cropncleaned_edit.jpg', 1498, 'A Pietà é uma escultura em mármore de Michelangelo, criada entre 1498 e 1499 e localizada na Basílica de São Pedro, no Vaticano. A obra retrata a Virgem Maria segurando o corpo de Jesus após a crucificação, capturando um momento de dor e serenidade. Michelangelo representa Maria como uma figura jovem e serena, em contraste com o sofrimento de Jesus, transmitindo uma imagem idealizada da pureza e do amor materno.', 2, 2, 3),
    Obra_arte(9, 'Moisés', 'Michelangelo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/%27Moses%27_by_Michelangelo_JBU140.jpg/250px-%27Moses%27_by_Michelangelo_JBU140.jpg', 1513, 'Moisés é uma das esculturas mais impressionantes de Michelangelo, esculpida entre 1513 e 1515 como parte do túmulo do Papa Júlio II, que está localizado na Igreja de San Pietro in Vincoli, em Roma. A obra retrata o profeta bíblico Moisés em uma posição imponente e expressiva, segurando as Tábuas da Lei. Michelangelo escolheu representar Moisés com um olhar intenso e vigilante, em um momento de profunda concentração e força interior.', 2, 2, 3),
    Obra_arte(10, 'Juízo Final', 'Michelangelo', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Last_Judgement_%28Michelangelo%29.jpg/250px-Last_Judgement_%28Michelangelo%29.jpg', 1536, 'Juízo Final é uma pintura monumental de Michelangelo, executada entre 1536 e 1541 no altar da Capela Sistina, no Vaticano. A obra representa o fim dos tempos, com Cristo no centro, julgando as almas da humanidade, separando os bem-aventurados dos condenados. Cristo aparece em uma postura dinâmica, enquanto figuras de santos e mártires o cercam, exibindo os instrumentos de seu martírio.', 2, 2, 4),
    Obra_arte(11, 'Moonrise, Hernandez, New Mexico', 'Ansel Adams', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Moonrise%2C_Hernandez%2C_New_Mexico.jpg/350px-Moonrise%2C_Hernandez%2C_New_Mexico.jpg', 1941, '"Moonrise, Hernandez, New Mexico" é uma famosa fotografia de Ansel Adams, tirada em 1941. A imagem captura uma cena noturna impressionante na pequena cidade de Hernandez, no Novo México. No centro da foto, vemos a lua cheia surgindo sobre uma paisagem montanhosa, com as sombras dramáticas projetadas nas montanhas e no campo. O céu é iluminado por um tom suave de azul e laranja, enquanto as tradicionais cruzes de madeira no campo acrescentam um elemento humano e simbólico à composição.', 3, 3, 5),
    Obra_arte(12, 'Clearing Winter Storm, Yosemite National Park', 'Ansel Adams', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Clearing_Winter_Storm%2C_Yosemite_Valley.jpg/350px-Clearing_Winter_Storm%2C_Yosemite_Valley.jpg', 1944, 'Clearing Winter Storm, Yosemite National Park é uma icônica fotografia de Ansel Adams, capturada no parque nacional de Yosemite, Califórnia. A obra, feita em preto e branco, retrata um momento de transição após uma tempestade de inverno, quando a neblina começa a se dissipar, revelando a impressionante paisagem de Yosemite, com seus majestosos penhascos e árvores cobertas de neve. A foto destaca a profundidade e a força da natureza, com uma composição de contraste dramático entre as nuvens, as rochas e as árvores, criando um efeito quase etéreo. Adams, conhecido por seu trabalho em defesa da natureza e pelo uso de técnicas precisas de fotografia, criou uma obra que transmite o poder e a serenidade do ambiente natural.', 3, 3, 1),
    Obra_arte(13, 'The Tetons and the Snake River, Grand Teton National Park', 'Ansel Adams', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Adams_The_Tetons_and_the_Snake_River.jpg/350px-Adams_The_Tetons_and_the_Snake_River.jpg', 1942, 'The Tetons and the Snake River, Grand Teton National Park é uma célebre fotografia de Ansel Adams, capturada em 1942, que mostra o Parque Nacional de Grand Teton, em Wyoming. Na imagem, o rio Snake forma curvas elegantes em primeiro plano, levando o olhar do espectador até as montanhas Tetons ao fundo, que se erguem dramaticamente contra o céu. A fotografia, em preto e branco, utiliza contrastes fortes para acentuar as texturas e a profundidade da paisagem, transmitindo uma sensação de vastidão e serenidade. Essa imagem, encomendada pelo Departamento de Interior dos EUA, não só destaca a beleza natural do parque, como também reforça a visão de Adams sobre a importância da preservação ambiental.', 3, 3, 2),
    Obra_arte(14, 'Monolith, the Face of Half Dome, Yosemite National Park', 'Ansel Adams', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Ansel-adams-monolith-the-face-of-half-dome.jpg/250px-Ansel-adams-monolith-the-face-of-half-dome.jpg', 1927, 'Monolith, the Face of Half Dome, Yosemite National Park é uma das fotografias mais icônicas de Ansel Adams, tirada em 1927. A imagem mostra a face imponente do Half Dome, uma formação rochosa em Yosemite, capturada com um contraste intenso e uma precisão que realça as texturas da rocha e a vastidão da paisagem. Adams usou um filtro vermelho para escurecer o céu e intensificar o contraste, o que resultou em um efeito dramático, com o Half Dome parecendo quase um monumento sagrado. Essa obra marcou um momento significativo na carreira de Adams, pois ele passou a explorar novas técnicas de controle de exposição para capturar a essência da natureza e suas dimensões monumentais.', 3, 3, 3),
    Obra_arte(15, 'Aspens, Northern New Mexico', 'Ansel Adams', 'https://ids.si.edu/ids/deliveryService?id=NMAH-2007-8450-000001&max=600', 1958, 'Aspens, Northern New Mexico é uma fotografia de Ansel Adams que retrata um bosque de álamos na região norte do Novo México. A imagem, feita em preto e branco, apresenta os troncos claros e esguios das árvores, alinhados em harmonia, destacando suas texturas e contrastes contra o chão escuro e a vegetação ao fundo. Adams captura a simplicidade e a elegância da natureza, revelando os padrões rítmicos e repetitivos das árvores. A composição transmite uma sensação de tranquilidade e ordem natural, refletindo a capacidade do fotógrafo de encontrar beleza na estrutura e simetria dos elementos naturais.', 3, 3, 4),
    Obra_arte(16, 'Melancolia I', 'Albrecht Dürer', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Melencolia_I_%28Durero%29.jpg/300px-Melencolia_I_%28Durero%29.jpg', 1514, 'Melancolia I é uma gravura em metal criada pelo artista renascentista Albrecht Dürer em 1514. A obra é rica em simbolismo e é considerada uma meditação sobre a criatividade, o conhecimento e as limitações humanas. No centro da imagem, uma figura feminina alada, que representa a personificação da melancolia, está sentada pensativa, cercada por diversos objetos científicos e artísticos, como uma balança, um compasso, uma ampulheta e um poliedro. Ao fundo, há uma misteriosa paisagem sob um céu escuro, simbolizando a introspecção e o mistério do conhecimento incompleto. A obra é complexa, e os elementos matemáticos e geométricos sugerem uma busca incessante por entendimento e perfeição, temas que eram centrais no Renascimento.', 4, 4, 5),
    Obra_arte(17, 'O Cavaleiro, a Morte e o Diabo', 'Albrecht Dürer', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Knight-Death-and-the-Devil.jpg/280px-Knight-Death-and-the-Devil.jpg', 1513, 'O Cavaleiro, a Morte e o Diabo é uma gravura em metal criada pelo artista alemão Albrecht Dürer em 1513. A imagem retrata um cavaleiro medieval montado em seu cavalo, que avança em meio a um cenário sombrio e ameaçador. Ao seu lado, aparecem figuras simbólicas da Morte, que segura uma ampulheta como lembrança da finitude, e do Diabo, representado com traços grotescos. Apesar dessas presenças sinistras, o cavaleiro segue impassível e determinado, simbolizando virtudes como a coragem e a firmeza diante das adversidades. A gravura, com seus ricos detalhes e domínio técnico, é frequentemente interpretada como uma alegoria da perseverança moral e da força de espírito perante a inevitabilidade da morte e o perigo da tentação.', 4, 4, 1),
    Obra_arte(18, 'São Jerônimo em sua Cela', 'Albrecht Dürer', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/D%C3%BCrer-Hieronymus-im-Geh%C3%A4us.jpg/280px-D%C3%BCrer-Hieronymus-im-Geh%C3%A4us.jpg', 1514, 'São Jerônimo em sua Cela é uma obra do pintor renascentista italiano Caravaggio, criada em 1606. A pintura retrata São Jerônimo, o teólogo e tradutor da Bíblia, em sua cela de estudo, imerso em um momento de introspecção e arrependimento. Ele é representado em uma postura pensativa, com uma expressão grave, olhando para um crânio, símbolo da transitoriedade da vida e da morte. Ao seu lado, estão os livros e instrumentos de seu trabalho como tradutor, incluindo a Bíblia, e uma janela que permite que a luz entre na cena, iluminando o santo e conferindo uma atmosfera contemplativa. A obra é caracterizada pelo uso dramático de luz e sombra, técnica que Caravaggio dominava, criando uma sensação de realismo intenso e emocional. A imagem de São Jerônimo, com seu aspecto humano e vulnerável, é um exemplo do estilo de Caravaggio, que misturava temas religiosos com um forte foco na psicologia e na expressão emocional dos personagens.', 4, 4, 2),
    Obra_arte(19, 'Adão e Eva', 'Albrecht Dürer', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Expulsion_of_Adam_and_Eve_%28Alexandre_Cabanel%29.jpg/198px-Expulsion_of_Adam_and_Eve_%28Alexandre_Cabanel%29.jpg', 1504, 'Adão e Eva é uma famosa pintura de Albrecht Dürer, criada em 1507, que ilustra o momento bíblico da Criação, quando Deus criou Adão e Eva no Jardim do Éden. A obra é notável por sua técnica detalhada e pela representação refinada dos corpos humanos, em um estilo renascentista que busca a perfeição nas proporções e na anatomia. Adão e Eva estão nus, com expressões serenas, e estão rodeados por uma flora exuberante e uma série de animais simbólicos que representam as virtudes e os vícios humanos. A obra é rica em simbolismo, com a árvore do conhecimento e a serpente representando o pecado original e a queda da humanidade. Dürer, influenciado pela perspectiva e pelos ideais clássicos, criou uma cena de grande complexidade e harmonia visual, enquanto explora temas como a inocência, a tentação e a redenção.', 4, 4, 3),
    Obra_arte(20, 'O Rinoceronte', 'Albrecht Dürer', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/D%C3%BCrer%27s_Rhinoceros%2C_1515.jpg/260px-D%C3%BCrer%27s_Rhinoceros%2C_1515.jpg', 1515, 'A obra "O Rinoceronte" é uma gravura de Albrecht Dürer, criada em 1515, que retrata um rinoceronte de forma detalhada, embora o artista nunca tenha visto o animal pessoalmente. A imagem foi baseada em descrições e esboços de um rinoceronte que havia sido enviado como presente ao rei Manuel I de Portugal. Dürer, conhecido por seu talento em representar animais e natureza, criou uma obra extraordinariamente precisa em termos de composição, mas com algumas liberdades estilísticas, como a adição de placas de armadura ao animal, o que não correspondia à aparência real do rinoceronte. A gravura se tornou uma das imagens mais icônicas de Dürer e um marco na história da arte, simbolizando tanto a curiosidade do Renascimento sobre o mundo natural quanto as limitações do conhecimento da época.', 4, 4,4)
]

exibicoes_list = [
    Exibicao(1, "Luzes do Infinito", "Centro Cultural Horizonte Aberto - São Paulo, Brasil", "15/01/2025", "30/04/2025", "Mariana Velasco"),
    Exibicao(2, "Fragmentos do Passado: Ecos da Memória", "Museu das Artes Eternas - Lisboa, Portugal", "03/03/2025", "28/06/2025", "João Carvalho"),
    Exibicao(3, "Sintonia Urbana: Arte e Movimento", "Galeria do Horizonte Moderno - Nova York, EUA", "10/02/2025", "20/05/2025", "Charlotte Nguyen"),
    Exibicao(4, "As Cores do Silêncio", "Espaço Cultural Aurora Boreal - Tóquio, Japão", "05/04/2025", "15/07/2025", "Akira Matsumoto")
]

leiloes_list = [
    Leilao(1, 50, "11/05/2026"),
    Leilao(2, 100, "16/06/2026"),
    Leilao(5, 150, "03/07/2026"),
    Leilao(6, 200, "22/08/2026"),
    Leilao(9, 250, "07/09/2026"),
    Leilao(10, 300, "15/10/2026"),
    Leilao(13, 350, "21/11/2026"),
    Leilao(14, 400, "14/12/2026")
]

comentarios_list = [
    Comentario(1, "Josué Luis", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "09/10/2024"),
    Comentario(2, "Anna Clara", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "05/04/2024"),
    Comentario(3, "Pedro Henrique", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "13/05/2024"),
    Comentario(4, "Eloísa Fernanda", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "21/06/2024"),
    Comentario(5, "Denilson Fernando", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "26/09/2024"),
    Comentario(6, "Regiene Maria", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "12/02/2024"),
    Comentario(7, "Leonardo Araújo", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "28/03/2024"),
    Comentario(8, "Paola Marques", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "07/05/2024"),
    Comentario(9, "Lavínia Marques", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "19/06/2024"),
    Comentario(10, "Marcia Marques", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "03/08/2024"),
    Comentario(11, "Lucas Diego", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "15/09/2024"),
    Comentario(12, "Carlos Henrique", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "23/10/2024"),
    Comentario(13, "Manuel Alves", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "04/11/2024"),
    Comentario(14, "Sâmea Letícia", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "16/04/2024"),
    Comentario(15, "Rigana Célia", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "29/01/2024"),
    Comentario(16, "Flávio Ventura", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam a dicta adipisci quidem, eveniet architecto aut expedita odio libero, cum fugiat explicabo iure beatae tempore accusamus! Neque debitis repellat esse?", "09/05/2024")
]

@app.route('/')
def home():
    seis_recentes = sorted(obra_arte_list, key=lambda obra: obra.ano, reverse=True)[:6]

    obras_invertidas = sorted(obra_arte_list, key=lambda obra: obra.get_id(), reverse=True)
    ultimas_obras_pintura = []
    ultimas_obras_escultura = []
    ultimas_obras_fotografia = []
    ultimas_obras_gravura = []

    for categoria in categoria_list:
        for obra in obras_invertidas:
            if obra.get_categoria() == 1 and categoria.get_id() and len(ultimas_obras_pintura) < 3:
                ultimas_obras_pintura.append(obra)
        
            if obra.get_categoria() == 2 and categoria.get_id() and len(ultimas_obras_escultura) < 3:
                ultimas_obras_escultura.append(obra)

            if obra.get_categoria() == 3 and categoria.get_id() and len(ultimas_obras_fotografia) < 3:
                ultimas_obras_fotografia.append(obra)

            if obra.get_categoria() == 4 and categoria.get_id() and len(ultimas_obras_gravura) < 3:
                ultimas_obras_gravura.append(obra)

    ultimas_obras = [ultimas_obras_pintura, ultimas_obras_escultura, ultimas_obras_fotografia, ultimas_obras_gravura]

    return render_template('index.html', obra_arte_list=obra_arte_list, seis_recentes=seis_recentes, artistas_list=artistas_list, categoria_list=categoria_list, ultimas_obras=ultimas_obras)

@app.route('/detalhes_artista/<int:id>')
def detalhes_artistas(id):
    obra_artista_list = []
    for artista in artistas_list:
        if artista.get_id() == id:
            for obra in obra_arte_list:
                if obra.get_autor() == artista.get_id():
                    obra_artista_list.append(obra)
            return render_template('detalhes-artistas.html', artista=artista, obra_artista_list=obra_artista_list)
        
@app.route("/obra/<int:id>")
def detalhes_obra(id):
    for obra in obra_arte_list:
        for categoria in categoria_list:
            if categoria.get_id() == obra.get_categoria():
                categoria_obra = categoria
        
        if obra.get_id() == id:
            return render_template("detalhes-obras.html", obra=obra, categoria_obra=categoria_obra)
        
@app.route("/exibicoes")
def exibicoes():
    return render_template("exibicoes.html", exibicoes_list=exibicoes_list)

@app.route("/exibicao/<int:id>")
def detalhes_exibicao(id):
    obras_exibicao = []          
    for exibicao in exibicoes_list:
        if exibicao.get_id() == id:
            for obra in obra_arte_list:
                if obra.get_id_exibicao() == exibicao.get_id():
                    obras_exibicao.append(obra)
            
            return render_template("detalhes-exibicao.html", exibicao=exibicao, obras_exibicao=obras_exibicao)

@app.route("/leiloes")
def leiloes():
    obra_leilao = []
    dados_leilao = []
    for leilao in leiloes_list:
        for obra in obra_arte_list:
            if obra.get_id() == leilao.get_id_obra():
                dados_leilao.append(leilao)
                obra_leilao.append(obra)
    
    return render_template("leiloes.html", dados_leilao=dados_leilao, obra_leilao=obra_leilao)

@app.route("/comentario/<int:id>")
def detalhes_comentario(id):
    for comentario in comentarios_list:
        if comentario.get_id() == id:
            comentario_obra = comentario
            return render_template("detalhes-comentario.html", comentario_obra=comentario_obra)