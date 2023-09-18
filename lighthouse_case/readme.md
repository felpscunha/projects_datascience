# INDICIUM - DESAFIO CIENTISTA DE DADOS

- PROGRAMA LIGHTHOUSE

# DESAFIO 

Você foi alocado(a) em um time da Indicium que está trabalhando atualmente junto a um cliente que o core business é compra e venda de veículos usados. Essa empresa está com dificuldades na área de revenda dos automóveis usados em seu catálogo.

Para resolver esse problema, a empresa comprou uma base de dados de um marketplace de compra e venda para entender melhor o mercado nacional, de forma a conseguir precificar o seu catálogo de forma mais competitiva e assim recuperar o mau desempenho neste setor.

Seu objetivo é analisar os dados para responder às perguntas de negócios feitas pelo cliente e **criar um modelo preditivo que precifique os carros do cliente de forma que eles fiquem o mais próximos dos valores de mercado**. 

# DESCRIÇÃO DOS DADOS

**id**: Contém o identificador único dos veículos cadastrados na base de dados
**num_fotos**: contém a quantidade de fotos que o anuncio do veículo contém
**marca**: Contém a marca do veículo anunciado
**modelo**: Contém o modelo do veículo anunciado
**versao**: Contém as descrições da versão do veículo anunciando. Sua cilindrada, quantidade de válvulas, se é flex ou não, etc.
**ano_de_fabricacao**: Contém o ano de fabricação do veículo anunciado
**ano_modelo**: Contém o modelo do ano de fabricação do veículo anunciado
**hodometro**: Contém o valor registrado no hodômetro do veículo anunciado
**cambio**: Contém o tipo de câmbio do veículo anunciado
**num_portas**: Contém a quantidade de portas do veículo anunciado
**tipo**: Contém o tipo do veículo anunciado. Se ele é sedã, hatch, esportivo, etc.
**blindado**: Contém informação se o veículo anunciado é blindado ou não
**cor**: Contém a cor do veículo anunciado
**tipo_vendedor**: Contém informações sobre o tipo do vendedor do veículo anunciado. Se é pessoa física (PF) ou se é pessoa jurídica (PJ)
**cidade_vendedor**: Contém a cidade em que vendedor do veículo anunciado reside
**estado_vendedor**: Contém o estado em que vendedor do veículo anunciado reside
**anunciante**: Contém o tipo de anunciante do vendedor do veículo anunciado. Se ele é pessoa física, loja, concessionário, etc
**entrega_delivery**: Contém informações se o vendedor faz ou não delivery do veículo anunciado
**troca**: Contém informações o veículo anunciado já foi trocado anteriormente
**elegivel_revisao**: Contém informações se o veículo anunciado precisa ou não de revisão
**dono_aceita_troca**: Contém informações se o vendedor aceita ou não realizar uma troca com o veículo anunciado
**veiculo_único_dono**: Contém informações o veículo anunciado é de um único dono
**revisoes_concessionaria**: Contém informações se o veículo anunciado teve suas revisões feitas em concessionárias
**ipva_pago**: Contém informações se o veículo anunciado está com o IPVA pago ou não
**veiculo_licenciado**: Contém informações se o veículo anunciado está com o licenciamento pago ou não
**garantia_de_fábrica**: Contém informações o veículo anunciado possui garantia de fábrica ou não
**revisoes_dentro_agenda**: Contém informações se as revisões feitas do veículo anunciado foram realizadas dentro da agenda prevista
**veiculo_alienado**: Contém informações se o veículo anunciado está alienado ou não
**preco (target)**: Contém as informações do preço do veículo anunciado

# FERRAMENTAS UTILIZADAS

Este projeto foi concluído usando Python e algumas de suas bibliotecas associadas, como:

- NumPy;
- Pandas;
- Matplotlib;
- Seaborn;
- Scikit-learn;

# ORGANIZAÇÃO DO PROJETO

```sh
.
├── main
│   ├── datasets
│   │   ├── processed
│   │   └── raw
│   │       ├── cars_test.csv
│   │       └── cars_train.csv
│   ├── notebooks
│   │   ├── eda
│   │   │   ├── eda.ipynb
│   │   ├── model
│   │   │   ├── model.ipynb
│   └── outputs
│       └── predicted.csv
├── readme.md
└── utils
    ├── environment.yml
    └── requirements.txt
```

# INSTALAÇÃO

## Instalação
Foi utilizado o [Python](https://www.python.org/) v3.8.10.

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create -f environment.yml
```

- Ativar
```sh
conda activate ml_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requirements.txt para criar o ambiente virtual.

- Criar ambiente virtual
```sh
python -m venv ml_venv
```

- Ativar
```sh
source ./ml_venv/bin/activate
```

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```