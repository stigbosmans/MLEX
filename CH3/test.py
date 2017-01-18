import MailAnalyze as a;
import os
import MailLoader as ldr;
spam_path=os.path.dirname(os.path.realpath(__file__))+"/spam";
clean_path=os.path.dirname(os.path.realpath(__file__))+"/easy_ham";

analyze = a.MailAnalyze();
mail_loader=ldr.MailLoader(spam_path)
spam=mail_loader.load_mails()

for mail in spam:
    analyze.fit(mail)
    break;