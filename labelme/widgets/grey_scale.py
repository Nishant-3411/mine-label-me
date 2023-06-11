from PIL import Image
from qtpy.QtGui import QPixmap, QImage, QColor
from app import MainWindow

class ToGrey():
     def convert_to_grayscale(pixmap):
    
        pixmap = canvas.pixmap()

        # Convert the pixmap to a QImage
        image = pixmap.toImage()

        # Convert the image to 16-bit grayscale
        image = image.convertToFormat(QImage.Format_Grayscale16)

        # Convert the image back to a pixmap
        pixmap = QPixmap.fromImage(image)

        # Load the pixmap back to the canvas
        canvas.loadPixmap(pixmap)
        return pixmap