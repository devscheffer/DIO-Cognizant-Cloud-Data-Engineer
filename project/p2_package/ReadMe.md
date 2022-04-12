# Referência

https://pt.wikipedia.org/wiki/Codifica%C3%A7%C3%A3o_de_Huffman#Algoritmo
https://www.gatevidyalay.com/huffman-coding-huffman-encoding/

# Algoritmo de Huffman

- [x] Dicionário de frequência
- [x] Dicionário de lista de mesma frequência
- [x] Criação de arvore binaria
- [x] Dicionário dos path para cada leaf
- [x] Conversão da lista path para string
- [x] Função do cálculo da compressão

# huffman-sch

Description.
The package package_name is used to:
	- Text compression using Huffman algorithm.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install package_name
```

## Usage

```python
from huffman_sch.main import huffman_sch
text = 'hello world'
cls = huffman_sch(text)
print(cls.compression())
```

## Author
My_name

## License
[MIT](https://choosealicense.com/licenses/mit/)
