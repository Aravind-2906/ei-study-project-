class ConsoleObserver:
    """Observer to print conflict or info notifications."""
    def notify(self, message: str) -> None:
        print("[NOTIFY]", message)
