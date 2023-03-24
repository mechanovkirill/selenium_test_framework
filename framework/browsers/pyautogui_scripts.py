import pyautogui
import pyperclip


class PyautoguiActions:

    @staticmethod
    def paste_text_into_active_window_field_and_enter(text: str) -> None:
        """Keyboard layout must be En!"""
        pyautogui.PAUSE = 1
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v", interval=0.25)
        pyautogui.press("enter", interval=0.25)
