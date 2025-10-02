# Adapter Pattern demo: Legacy printer adapted
class LegacyPrinter:
    def old_print(self, text):
        print(f"Legacy: {text}")

class PrinterAdapter:
    def __init__(self, legacy):
        self.legacy = legacy

    def print(self, text):
        self.legacy.old_print(text)


legacy = LegacyPrinter()
printer = PrinterAdapter(legacy)
printer.print("Hello Adapter!")
