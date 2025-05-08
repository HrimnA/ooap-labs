import tkinter as tk
from tkinter import simpledialog, messagebox

# ==== VISITOR PATTERN ====

class DocumentElement:
    def accept(self, visitor):
        pass

class Paragraph(DocumentElement):
    def __init__(self, text):
        self.text = text
        self.style = None  # InlineStyle or ColumnStyle

    def accept(self, visitor):
        visitor.visit_paragraph(self)

class Text(DocumentElement):
    def __init__(self, content):
        self.content = content

    def accept(self, visitor):
        visitor.visit_text(self)

# ==== VISITOR ====

class Visitor:
    def visit_paragraph(self, paragraph):
        pass

    def visit_text(self, text):
        pass

# ==== STYLE CLASSES ====

class Style:
    def apply(self, text):
        pass

class InlineStyle(Style):
    def apply(self, text):
        return f"[Inline] {text}"

class ColumnStyle(Style):
    def apply(self, text):
        return f"[Column]\n" + "\n".join(text.split())

# ==== STYLE SETTER VISITOR ====

class StyleSetterVisitor(Visitor):
    def __init__(self, style):
        self.style = style

    def visit_paragraph(self, paragraph):
        paragraph.style = self.style

    def visit_text(self, text):
        pass

# ==== RENDER VISITOR ====

class RenderVisitor(Visitor):
    def visit_paragraph(self, paragraph):
        styled_text = paragraph.style.apply(paragraph.text) if paragraph.style else paragraph.text
        print(f"Paragraph: {styled_text}")

    def visit_text(self, text):
        print(f"Text: {text.content}")

# ==== DIALOG TO CHOOSE STYLE ====

def choose_style_dialog():
    root = tk.Tk()
    root.withdraw()
    choice = simpledialog.askstring("Стиль абзацу", "Виберіть стиль (inline/column):").lower()
    root.destroy()

    if choice == "inline":
        return InlineStyle()
    elif choice == "column":
        return ColumnStyle()
    else:
        messagebox.showerror("Помилка", "Невідомий стиль. Використано стиль за замовчуванням.")
        return InlineStyle()

# ==== MAIN ====

if __name__ == "__main__":
    doc = [
        Paragraph("Це приклад абзацу з кількома словами."),
        Text("Це просто звичайний текст.")
    ]

    style = choose_style_dialog()

    style_visitor = StyleSetterVisitor(style)
    for el in doc:
        el.accept(style_visitor)

    print("\n=== Вивід документа ===")
    renderer = RenderVisitor()
    for el in doc:
        el.accept(renderer)
