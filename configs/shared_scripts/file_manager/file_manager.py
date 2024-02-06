from datetime import datetime


class FileManager:
    @classmethod
    def save_content(cls, full_file_path, content):
        try:
            with open(full_file_path, mode='w', encoding='utf-8') as file:
                file.write(content)
        except (FileNotFoundError, PermissionError) as error:
            raise error


class DataSaverBase:
    def __init__(self, html_content, text_content, folder_file_path):
        self.html_content = html_content
        self.today_date = datetime.now().strftime('%d-%m-%Y')
        self.folder_file_path = folder_file_path
        self.text_content = text_content

    def save_html(self):
        html_file_name = self.today_date + '.html'
        full_html_path = self.folder_file_path + '/' + html_file_name
        FileManager.save_content(full_file_path=full_html_path, content=self.html_content)

    def save_txt(self):
        txt_file_name = self.today_date + '.txt'
        full_txt_path = self.folder_file_path + '/' + txt_file_name
        FileManager.save_content(full_file_path=full_txt_path, content=self.text_content)


class DataSaver(DataSaverBase):
    def save_results(self):
        try:
            self.save_txt()
            self.save_html()
        except Exception as error:
            raise error
