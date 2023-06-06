from rembg import remove
from PIL import Image

class removeBG:
    def __init__(self ,origem="",destino=""):
        self.origem = origem
        self.destino = destino
        # self.formato = formato

    def ExecultaRemocao(self):
        input_path = self.origem
        output_path = self.destino
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)