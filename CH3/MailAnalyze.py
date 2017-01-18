from sklearn.base import BaseEstimator, TransformerMixin
import re

class MailAnalyze(BaseEstimator, TransformerMixin):
    content=""
    wordcount_dict={}
    html_tags=0
    def fit(self,X,y=None):
        self.content=X.lower()
        self.remove_html()
        self.word_count()
        print(self.wordcount_dict)
        return "ok"
    
    def transform(self,X,y=None):
        return "ok"
    
    def remove_html(self):
        results=re.findall("<\/?.*>",self.content)
        self.html_tags=len(results)
        self.content=re.sub("<\/?.*>","",self.content)

    def word_count(self):
        for word in self.content.split():
            if word not in self.wordcount_dict:
                self.wordcount_dict[word] = 1
            else:
                self.wordcount_dict[word] += 1