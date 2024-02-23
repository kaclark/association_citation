import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import sys

def latex_to_png(latex_str, fname):
    fig = plt.figure()
    plt.axis("off")
    plt.text(0.5,0.5, f"${latex_str}$", size=50, ha="center", va="center")
    pdf_path = "./imgs/" + fname + ".pdf"
    png_path = "./imgs/" + fname + ".png"

    plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.4)
    plt.close(fig)

    images = convert_from_path(pdf_path)
    images[0].save(png_path, "PNG")

latex_to_png(sys.argv[1], sys.argv[2])
