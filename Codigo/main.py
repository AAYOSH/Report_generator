# -*- coding: utf-8 -*-

from jinja2 import FileSystemLoader, Environment
import pdfkit
import os



def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """

    ################ precisamos obter o numero de revisoes
    nREVS = 5 # -> REV0 ... REV4



    jinja_var  = {
        'content' : 'a',
        'imagem1': 'figuras/figureREV1SIN.png',
        'imagem2':'figuras/diffsREV1.png',
        'imagem3':'figuras/TabelasRev1.png'
    }

    env = Environment(
        loader=FileSystemLoader(searchpath="./")
    )

    template = env.get_template("report2.html")

    with open("outer.html", "w") as f:
         f.write(template.render(jinja_var))
    #print(template.render(jinja_var))
    print('IN')
   # pdfkit.from_file('outer.html', 'outer.pdf')

if __name__ == "__main__":
    main()