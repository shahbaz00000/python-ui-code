import tkinter as tk
from tkinter import ttk

# Main App
class DevOpsUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DevOps Engineer Dashboard")
        self.root.geometry("900x600")
        self.root.configure(bg="#0f172a")

        self.style = ttk.Style()
        self.style.theme_use('default')

        # Styling
        self.style.configure("TButton",
                             font=("Segoe UI", 10, "bold"),
                             padding=10,
                             foreground="#ffffff",
                             background="#1e293b")

        self.style.map("TButton",
                       background=[('active', '#334155')])

        # Header
        header = tk.Label(root,
                          text="⚙️ DevOps Engineer Dashboard",
                          font=("Segoe UI", 20, "bold"),
                          bg="#0f172a",
                          fg="#38bdf8")
        header.pack(pady=15)

        # Main Frame
        main_frame = tk.Frame(root, bg="#0f172a")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Left Panel
        left_panel = tk.Frame(main_frame, bg="#1e293b", width=250)
        left_panel.pack(side="left", fill="y", padx=10)

        # Buttons
        buttons = [
            "CI/CD Pipeline",
            "Docker Containers",
            "Kubernetes",
            "Monitoring",
            "Logs",
            "Settings"
        ]

        for btn in buttons:
            ttk.Button(left_panel, text=btn, command=lambda b=btn: self.update_content(b)).pack(pady=10, padx=10, fill="x")

        # Right Panel
        self.right_panel = tk.Frame(main_frame, bg="#020617")
        self.right_panel.pack(side="right", fill="both", expand=True, padx=10)

        self.content_label = tk.Label(self.right_panel,
                                     text="Welcome DevOps Engineer 🚀",
                                     font=("Segoe UI", 16),
                                     bg="#020617",
                                     fg="#e2e8f0")
        self.content_label.pack(pady=20)

        # Status Cards
        self.create_status_cards()

    def update_content(self, section):
        self.content_label.config(text=f"📌 {section} Section Loaded")

    def create_status_cards(self):
        card_frame = tk.Frame(self.right_panel, bg="#020617")
        card_frame.pack(pady=20)

        cards = [
            ("Active Containers", "12"),
            ("Deployments", "5"),
            ("CPU Usage", "68%"),
            ("Errors", "2")
        ]

        for i, (title, value) in enumerate(cards):
            card = tk.Frame(card_frame,
                            bg="#1e293b",
                            width=150,
                            height=100)
            card.grid(row=0, column=i, padx=10)

            tk.Label(card,
                     text=title,
                     font=("Segoe UI", 10),
                     bg="#1e293b",
                     fg="#94a3b8").pack(pady=5)

            tk.Label(card,
                     text=value,
                     font=("Segoe UI", 18, "bold"),
                     bg="#1e293b",
                     fg="#38bdf8").pack()

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = DevOpsUI(root)
    root.mainloop()
