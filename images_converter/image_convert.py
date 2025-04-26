import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def convert_folder_to_pdf(input_folder, output_folder):
    # Kreiraj output folder ako ne postoji
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Prođi kroz sve slike u input folderu
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".pdf"
            output_path = os.path.join(output_folder, output_filename)

            # Učitaj sliku
            img = mpimg.imread(input_path)
            
            dpi = 300
            height, width = img.shape[:2]
            figsize = width / dpi, height / dpi

            fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
            ax.imshow(img)
            ax.axis('off')
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

            fig.savefig(output_path, format='pdf', dpi=dpi, bbox_inches='tight', pad_inches=0)
            plt.close(fig)

            print(f"Saved: {output_path}")

    print("Conversion completed for all images!")

# Primjer korištenja:
convert_folder_to_pdf("C:/Users/Korisnik/Desktop/images_converter/paper_images", "converted")
