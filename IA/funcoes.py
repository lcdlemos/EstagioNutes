from pptx.util import Inches
import os

def contar_slides(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        num_slides = texto.count("Slide")
    return num_slides

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
    return texto

def criar_capa(auto_apresentacao, texto):
    modelo_slide = auto_apresentacao.slide_layouts[0]
    slide = auto_apresentacao.slides.add_slide(modelo_slide)
    titulo = slide.shapes.title
    subtitulo = slide.placeholders[1]
    titulo.text = texto[1].lstrip("- Título: ").rstrip("\n")
    subtitulo.text = texto[2].strip("\n")
    return slide

def coletar_titulos(texto):
    titulos = []
    for linha in texto:
        if "Título" in linha:
            titulos.append(linha)
    return titulos

def coletar_topicos(texto):
    topicos = []
    for topico in texto:
        if "- " in topico and "Título" not in topico and "Autor:" not in topico or "\n" == topico:
            topicos.append(topico)
    topicos.append("\n")
    return topicos

def adicionar_slides(auto_apresentacao, texto, titulos, topicos, num_slides):
    slides = []
    j = 1
    for i in range(num_slides - 1):
        modelo_slide = auto_apresentacao.slide_layouts[1]
        slide = auto_apresentacao.slides.add_slide(modelo_slide)
        titulo = slide.shapes.title
        titulo.text = titulos[i+1].lstrip("- Título: ").rstrip("\n")
        caixa_topicos = slide.shapes
        caixa_topico = caixa_topicos.placeholders[1]
        caixa_topico.text = topicos[j].strip("- ""\n")
        j += 1
        while topicos[j] != "\n":
            if "    -" in topicos[j]:
                topico = caixa_topico.text_frame.add_paragraph()
                topico.text = topicos[j].strip("    -""\n")
                topico.level = 1
            elif "Imagem" in topicos[j]:
                # imagem = r"C:\Users\Luiz Carlos\Documents\UEPB\Estágio\Slides\ia.jpg"
                # if os.path.isfile(imagem):
                img1 = "ia.jpg"
                esquerda = Inches(3)
                topo = Inches(4.5)
                adiciona_imagem = slide.shapes.add_picture(img1, esquerda, topo)
            else:
                topico = caixa_topico.text_frame.add_paragraph()
                topico.text = topicos[j].strip("- ""\n")
            j += 1
        j += 1
        slides.append(slide)
    return slides