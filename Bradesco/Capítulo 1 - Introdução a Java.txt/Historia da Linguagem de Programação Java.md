# História do Java

Cada linguagem de programação tem suas próprias história e finalidade, que justificam sua criação e disseminação.

Você conhece a história do Java? Sabe dizer desde quando essa linguagem existe e o porquê de seu nome?

Vamos, então, conhecer a história da linguagem de programação Java.

* Java é uma lingaugem de programação Orientada a Objetos
* Criada pela Sun Microsystem - 1990
* J. Gosling
* Compialada pela conversão da linguagem para ByteCode. 
* Projetada para ser implementada em vários dispositivos
* A plataforma foi lançada em 1995
* A linguagem mais executada na história 

***

# Contexto Atual

Em 2015, a linguagem Java completou 20 anos em pleno vigor. Para compreender os motivos que contribuíram para a conquista de tamanha importância no cenário atual, é preciso entender como o Java funciona e como se deu a evolução tecnológica do mundo nas últimas duas décadas.

Entre tantas linguagens de programação existentes, o Java deve ser visto como uma linguagem de programação moderna que se adaptou muito bem à internet e aos chamados dispositivos móveis (tablets e smartphones).

Na atualidade, a maior parte dos aplicativos desenvolvidos para dispositivos móveis é desenvolvido em Java, o que faz com que os programadores que dominam essa linguagem sejam profissionais bastante procurados e valorizados no mercado de trabalho atual.

* **9 bilhoes de Programadores**
* **7 bilhoes de Dispositivos**

***
# Processo de Compilação

Tal como foi tratado no vídeo a que você acabou de assistir, para executar um programa, precisamos transformá-lo em uma linguagem de máquina ou linguagem de baixo nível. A linguagem de máquina é a linguagem que os computadores entendem.

A transformação de linguagens é chamada de compilação. Nesse sentido, a compilação acontece quando um código é convertido de uma linguagem natural (linguagem de programação, código-fonte ou, ainda, linguagem humana) para uma linguagem de máquina (linguagem de baixo nível).

No Java, o código-fonte é transformado em bytecode, que é a linguagem entendida e executada pela Máquina Virtual Java (Java Virtual Machine – JVM).

* Compilação na maioria dos programas
Codigo fonte (ling. Alto Nivel) --> Compilador --> Cod. executavel (Ling. de Maquina) 

* Compilação no Java
Codigo fonte (ling. Alto Nivel) --> JavaC (Compilador Java) --> ByteCode --> JVM --> Cod. executavel (Ling. de Maquina) 

***
# Maquina Virtual Java

Para desenvolver e processar programas escritos em Java, temos de compreender o que é uma JVM – Java Virtual Machine (Máquina Virtual Java).
* A JVM é fundamental para o pleno funcionamento dos códigos feitos na linguagem de programação Java.
Lembre-se de que os **bytecodes** (códigos compilados em Java) são interpretados e executados pela JVM. Isso significa que, sem a JVM, os programas em Java simplesmente não funcionam.

* A JVM é composta por:
    * Instruções;
    * Registradores;
    * Pilha;
    * Garbage-collected heap
    * Área de Memória (armazenamento de métodos).

* Composição da JVM
    * As funções da Java Virtual Machine (Máquina Virtual Java) são: 

        - [ ] Acompanhar e proteger todas as classes do programa.
        - [ ] Verificar as especificações da Java Virtual Machine para gerar os bytecodes sem transgredir a integridade e a segurança da plataforma.
        - [ ] Interpretar os códigos compilados para as Máquinas Virtuais (bytecode).

No instante do processamento, os bytecodes são carregados para o sistema e verificados por meio de um recurso identificado como Bytecode Verifier para serem processados.

* Fluxo de Acesso a JVM

Eição e compilação          --->    Programa Compilado            
(javac <programafonte.java>)        java <programafonte.class>          

__JVM__ |                                                               
:---:|
Bytecode Verifier
Runtime

* Estutura da JVM

Edição Comp. de Prog. Java | Programa Fonte | Prog no Frmt BCode |                                                              
:---: | :---: | :---: | :---:
Estrutura da JVM | Class Loader (carregador de classe) | Bytecode Verifier (verificador de código) | Runtime (execução)
Sistemas Operacionais | Windows, Linix, MAC OS | | |

***
* Características Da Linguagem Java

O objetivo inicial da criação da plataforma Java era sua utilização em pequenos dispositivos.
No início do desenvolvimento da linguagem, ocorreram algumas dificuldades ao se elaborarem os códigos.

* Algumas das dificuldades encontradas no início do desenvolvimento dos códigos foram:

    * Definição dos ponteiros
    * Controle de memória
    * Administração/organização
    * Ausência de bibliotecas
    * Adaptação do código em função do sistema operacional.

Apesar dos entraves detectados durante a criação da linguagem Java, as principais dificuldades encontradas puderam ser resolvidas. Isso porque muitas delas já haviam sido enfrentadas e solucionadas em outras linguagens de programação.
    - Ponteiros
    - Organização
    - Bibliotecas
    - Memoria
    - SO

* As principais características que destacaram a linguagem Java entre as linguagens mais utilizadas pelos desenvolvedores nos ajudam a entender a projeção significativa dessa linguagem. Vejamos essas características a seguir:

    *   Apresentação de tipagem estática forte – detectando os tipos de variáveis quando declaradas.
    *   Orientação a objetos.
    *   Possibilidade de ser interpretada (execução dos bytecodes do Java por meio de qualquer máquina).
    *   Baseada no modelo de Simula 67.
    *   Portabilidade – recursos de rede e extensa biblioteca de rotinas, facilitando a cooperação com protocolos TCP/IP, como HTTP e FTP.
    *   Segurança – permite a execução de programas via rede com restrições de execução.
    *   Gerenciamento automático de memória (Garbage Collection).
    *   Sintaxe similar a C/C++.
    *   Facilidades de internacionalização – suporta, naturalmente, caracteres Unicode.
    *   Simplicidade na especificação da linguagem e do "ambiente" de execução (JVM).
    *   Distribuição de um vasto conjunto de bibliotecas (ou APIs).
    *   Facilidades para desenvolvimento de programas distribuídos e multitarefas (múltiplas linhas de execução em um mesmo programa).
    *   Carga dinâmica de código.

***
* O que é Orientação a Objetos
    *   Orientação a objetos é um modelo de programação direcionado a um elemento real e concreto.
    *   Na programação orientada a objetos, a estrutura básica está definida por um conjunto de classes que definem os objetos presentes no sistema de software.
    *   Além da definição do relacionamento com outros objetos, cada classe estabelece o comportamento e os estados possíveis de seus objetos (atributos) por meio dos métodos. 

    * Programas em Java são formados por uma coleção de classes armazenadas de modo independente e que podem ser carregadas no momento de utilização.

***
* Portabilidade - Idenpendencia da Plataforma
A linguagem Java é independente da plataforma.
Dessa forma, como não existe a preocupação com particularidades do sistema operacional ou do hardware, o desenvolvedor pode dedicar-se ao desenvolvimento do código de programação com exclusividade.
Uma vez desenvolvido o código, é possível executá-lo em diversas plataformas.
Desse modo, podemos compilar um programa em qualquer sistema e executar o arquivo binário no mesmo sistema operacional.
    * Esse modo de funcionamento é chamado de **_Portabilidade_**

Programa | Public Class HelloWorld{}
:---: | ---: 
Compilação | > javac HelloWorld.java
Execução | > java HelloWorld
Plataformas | Linux, Windows, MAC OS

