import glob
import os
import pathlib
import shutil


class FileMgr:
    def __init__(self):
        self._path_2_docs = "../docs"
        self._root = "../"

    @staticmethod
    def clear_folder_recursively(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def clear_docs(self):
        FileMgr.clear_folder_recursively(self._path_2_docs)

    def write_file(self, sub_path, file_name, content):
        if sub_path != "":
            new_path = os.path.join(self._path_2_docs, sub_path)
        else:
            new_path = self._path_2_docs
        if not os.path.exists(new_path):
            os.makedirs(new_path, exist_ok=True)
        f = open(os.path.join(new_path, file_name), "w", encoding="utf8")
        f.write(content)
        f.close()

    def get_folder_content(self, sub_path):
        new_path = os.path.join(self._root, sub_path)
        only_files = [f for f in os.listdir(new_path) if os.path.isfile(os.path.join(new_path, f))]
        return only_files

    def get_folder_content_rek(self):
        ret = list()
        for filename in glob.iglob(self._root + "_sources/**/*.md", recursive=True):
            filename = filename.replace("\\", "/")
            ret.append(filename)
        return ret

    def get_file_content(self, sub_path, file_name):
        new_path = os.path.join(self._root, sub_path, file_name)
        f = open(new_path, "r", encoding="utf8")
        ret = f.read()
        f.close()
        return ret

    def copy_folder(self, source, destination):
        shutil.copytree(source, destination)

    def copy_file(self, source, destination):
        shutil.copyfile(source, destination)

    @staticmethod
    def get_project_folder():
        parent_folder = pathlib.Path(os.path.abspath(__file__))
        parent_folder = parent_folder.parent.absolute()
        parent_folder = parent_folder.parent.absolute()
        return parent_folder

    @staticmethod
    def get_base_name(filename: str):
        return os.path.basename(filename)
