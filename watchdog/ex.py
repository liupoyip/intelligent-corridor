import os
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def monitor_folder(path_target_folder, path_recording_csv, setting_type):
    
    path_target_folder = os.path.abspath(path_target_folder)
    path_recording_csv = os.path.abspath(path_recording_csv)
    if not os.path.exists(path_recording_csv):
        open(path_recording_csv, 'a').close()
    print("[+] Start monitoring")
    print(f"   [-] Monitor folder: {path_target_folder}")
    print(f"   [-] Record csv file: {path_recording_csv}")

    class NewFileHandler(FileSystemEventHandler):

        def __init__(self, path_rec_csv=path_recording_csv, s_type=setting_type):
            self.path_rec_csv = path_rec_csv
            self.s_type = s_type

        ### 追加新功能在「檔案生成」
        def on_created(self, event):
            if not event.is_directory and "TeraCopy" not in event.src_path:
                file_path = os.path.abspath(event.src_path)
                create_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                new_line_in_csv = f"{file_path},{create_time},{self.s_type}\n"
                with open(self.path_rec_csv, 'a') as f:
                    f.write(new_line_in_csv)
                    f.close()
                print(f"[*] {datetime.datetime.now()} New file created: {file_path}")

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path_target_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
    print("Monitor STOP")

if __name__ == "__main__":
    
    path_target_folder = './monitored_folder'
    path_recording_csv = 'record.csv'
    setting_type = 3

    monitor_folder(path_target_folder, path_recording_csv, setting_type)
