# src/log_viewer.py
import tkinter as tk
from tkinter import ttk
from log_parser import parse_log
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LogViewerApp:
    def __init__(self, root, log_data):
        self.root = root
        self.root.title("Log Viewer")

        self.tree = ttk.Treeview(root, columns=('Timestamp', 'Type', 'IP', 'Method', 'URL'), show='headings')
        self.tree.heading('Timestamp', text='Timestamp')
        self.tree.heading('Type', text='Type')
        self.tree.heading('IP', text='IP')
        self.tree.heading('Method', text='Method')
        self.tree.heading('URL', text='URL')

        for log in log_data:
            try:
                self.tree.insert('', tk.END, values=(log['timestamp'], log['type'], log['ip'], log['method'], log['url']))
            except KeyError as e:
                logging.error(f"Missing key in log data: {e}")
            except Exception as e:
                logging.error(f"Error inserting log data into treeview: {e}")

        self.tree.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    log_file_path = 'http-server\\logs\\log.txt'
    try:
        log_data = parse_log(log_file_path)
        logging.info(f"Parsed {len(log_data)} log entries")
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        log_data = []
    except Exception as e:
        logging.error(f"Error parsing log file: {e}")
        log_data = []

    root = tk.Tk()
    app = LogViewerApp(root, log_data)
    root.mainloop()