from pathlib import Path

from organizador.categorias import categorizar


def test_categoriza_imagem():
    assert categorizar(Path("foto.JPG")) == "Imagens"


def test_extensao_desconhecida_vai_para_outros():
    assert categorizar(Path("arquivo.xyz")) == "Outros"