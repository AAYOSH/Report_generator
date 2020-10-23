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
    out_dir = r'C:\Users\yoshidaa\OneDrive - Simple Energy\Documentos\Projetos\Report_generator\HTML'


    jinja_var  = {
        'hoje': '23/10',
        'ontem': '22/10',
        'ecmwf_hoje' : [1,2,3,4,5,6,7,8,9],
        'ecmwf_ontem': [10,2,3,4,5,6,7,8,9],
        'gefs_hoje':[1,5,3,4,5,6,7,8,9],
        'gefs_ontem':[162,2,3,4,5,6,7,8,9]
    }

    env = Environment(
        loader=FileSystemLoader(searchpath="./")
    )
    
    os.chdir(out_dir)
    template = env.get_template("template.html")

    with open("outer.html", "w") as f:
         f.write(template.render(jinja_var))
    #print(template.render(jinja_var))
    print('IN')
   # pdfkit.from_file('outer.html', 'outer.pdf')

if __name__ == "__main__":
    main()