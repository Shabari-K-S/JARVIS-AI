import sys
import threading
from PyQt5.QtWidgets import QApplication
from jarvis.speech.recognizer import SpeechRecognizer
from jarvis.ui.layered_image_widget import LayeredImageWidget
from jarvis.ai.ai_interface import AI

def main():
    app = QApplication([])
    main_widget = LayeredImageWidget()
    main_widget.show()

    ai = AI()
    model = ai.connect()
    
    recognizer = SpeechRecognizer(main_widget, app, model, ai)

    thread = threading.Thread(target=recognizer.listen_and_update)
    thread.daemon = True
    thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()