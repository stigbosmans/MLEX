from os import walk

class MailLoader:
    paths=[]
    mails=[]
    folder_path="";
    def __init__(self, folder_path):
        self.folder_path=folder_path;
        for (dirpath, dirnames, filenames) in walk(folder_path):
            self.paths.extend(filenames)
            break
    
    def load_mails(self):
        for path in self.paths:
            self.mails.append(self.open_file(path))
        return self.mails;
    
    def open_file(self,file_path):
        fo = open(self.folder_path+"/"+file_path, "r");
        res=fo.read()
        fo.close()
        return res