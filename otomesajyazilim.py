import os
try:
    from telethon import TelegramClient
    import time#. 
    import datetime#. 
    from telethon.tl.types import UserStatusRecently, UserStatusOnline, InputPeerChannel, InputChannel, InputPeerChat#. 
    import csv#. 
    import os#. 
    from telethon.errors import FloodError, FloodWaitError, PeerFloodError, UserPrivacyRestrictedError, UserAlreadyInvitedError, UserAlreadyParticipantError, UsernameInvalidError#. 
    from colorama import Fore, Style, init#. 
    from telethon.tl.functions.channels import InviteToChannelRequest#. 
    from telethon.tl.functions.messages import GetDialogsRequest#. 
    from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser#. 
    from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError#. 
    from telethon.tl.functions.channels import InviteToChannelRequest#. 
    import random#. 
    import pyfiglet#. 
    from telethon import functions, types#. 
    import requests#. 
except ImportError:#. 
    os.system("pip install telethon")#. 
    os.system("pip install requests")#. 
    os.system("pip install pyfiglet")#. 
    os.system("pip install csv")#. 
    os.system("pip install colorama")#. 
    os.system("pip install datetime")#. 
#. 
from telethon import TelegramClient#. 
import time#. 
from telethon import TelegramClient, sync#. 
import datetime#. 
from telethon.tl.types import UserStatusRecently, UserStatusOnline, InputPeerChannel, InputChannel, InputPeerChat#. 
import csv#. 
import os#. 
from telethon.errors import FloodError, FloodWaitError, PeerFloodError, UserPrivacyRestrictedError, UserAlreadyInvitedError, UserAlreadyParticipantError#. 
from colorama import Fore, Style, init#. 
from telethon.tl.functions.channels import InviteToChannelRequest#. 
from telethon.sync import TelegramClient#. 
from telethon.tl.functions.messages import GetDialogsRequest#. 
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser#. 
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError#. 
from telethon.tl.functions.channels import InviteToChannelRequest#. 
import random#. 
import pyfiglet#. 
import requests#. 
from telethon import functions, types#. 
#. 
def start():#. 
    clr()#. 
    banner()#. 
    print(Fore.YELLOW + "[1] Grup listesi çekin (Dm, Scraper, Tagger için)")#. 
    print(Fore.YELLOW + "[2] OTO DM başlatın")#. 
    print(Fore.YELLOW + "[3] OTO mesaj başlatın")#. 
    print(Fore.YELLOW + "[4] Üye çekici başlatın")#. 
    print(Fore.YELLOW + "[5] OTO tagger başlatın")#. 
    print(Fore.YELLOW + "[6] OTO iletme başlatın")#. 
    print(Fore.YELLOW + "[7] Bot ayarları")#. 
    try:#. 
        secim = int(input("Ne yapmak ıstersınız: "))#. 
    except ValueError:#. 
        print("yanlıs seçim")  #. 
        time.sleep(1)#. 
        start()#. 
    except IndexError:#. 
        print("yanlıs seçim")#. 
        time.sleep(1)#. 
        start()#. 
    if secim == 1:#. 
        uyecekici()#. 
    elif secim == 2:#. 
        otodm()#. 
    elif secim == 3:#. 
        otomesaj()    #. 
    elif secim == 4:#. 
        scraper()   #. 
    elif secim ==5:#. 
        etiket()#. 
    elif secim == 6:#. 
        iletme()#. 
    elif secim == 7:#. 
        ayarlar()#. 
    else:#. 
        print("yanlıs seçim")  #. 
        time.sleep(1)#. 
        start()   #. 

#. 
def clr():#. 
    if os.name == 'nt':#. 
        os.system('cls')#. 
    else:#. 
        os.system('clear')#. 
#. 
def cu():#. 
    with open('unfmembers.csv', 'r') as file_in, open('members.csv', 'w', newline='') as file_out:#. 
        reader = csv.reader(file_in)#. 
        writer = csv.writer(file_out)#. 
        for row in reader:#. 
            new_row = [cell for cell in row if cell.strip() != ""]#. 
            new_row = ['*' if cell == '' else cell for cell in row]#. 
            writer.writerow(new_row)#. 
#. 
def uyecekici():  
    clr()#. 
    banner()#. 
    print(Fore.RED + "Bu kısım sadece son görülmeleri yakında olan kullanıcıları çeker.")#. 
    time.sleep(5)#. 
    clr()#. 
    try:#. 
        with open("api.txt", "r") as f:#. 
            api_id, api_hash = f.read().split(",")#. 
        api_id = int(api_id)#. 
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")#. 
    except FileNotFoundError:#. 
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))#. 
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")#. 
        with open("api.txt", "w") as f:#. 
            f.write(f"{api_id},{api_hash}")#. 
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")#. 
    try:#. 
        client = TelegramClient("session", api_id, api_hash)#. 
        client.start()   #. 
    except:#. 
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") #. 
        time.sleep(5)#. 
        client.disconnect()#. 
        start()     #. 
    groups = []#. 
    chats = []#. 
    last_date = None#. 
    chunk_size = 200#. 
    groups=[]#. #. 
 
    result = client(GetDialogsRequest(#. 
                offset_date=last_date,#. 
                offset_id=0,#. 
                offset_peer=InputPeerEmpty(),#. 
                 limit=chunk_size,#. 
                 hash = 0#. 
             ))
    chats.extend(result.chats)#. 
 #. 
    for chat in chats:#. 
        try:
            if chat.megagroup== True:#. 
                groups.append(chat)#. 
        except:#. 
            continue#. 
    
    i=0#. #. #. #. #. #. #. 
    for group in groups:#. #. 
        print(Fore.YELLOW+'['+Fore.RED+str(i)+Fore.GREEN+']'+Fore.CYAN+' - '+group.title)#. #. #. 
        i+=1
        
    selected_group_number = int(input("\nHangi grubun üyelerini listelemek istersiniz? Numarasını girin: "))     #. 
    target_group=groups[int(selected_group_number)]#. 

    selected_group = None#. #. 
    selected_group = target_group
    
    #. 
    if selected_group is not None:
        with open('unfmembers.csv', mode='w', newline='') as file:#. 
            writer = csv.writer(file)#. 
            reader = csv.reader(file)#. 
        #. #. #. #. 
            print(f"\n{selected_group.title} grubundaki üyeler çekiliyor....")
            members = client.get_participants(selected_group)#. 
            for i, member in enumerate(members):
                if isinstance(member.status, UserStatusRecently) or isinstance(member.status, UserStatusOnline):
                    name = f"{member.first_name} {member.last_name}" if member.last_name is not None else member.first_name#. 
                    username = member.username #. 
                    if username == '':#. 
                        pass#. 
                    writer.writerow([username])#. 
    
    else:#. 
        print(Fore.RED + "geçersiz grup")#. 
    cu()#. 
    os.remove("unfmembers.csv")#. 
    client.disconnect()#. 
    print(Fore.GREEN + "Üye çekme işleni başarılı") #. 
    start() #. 



def otodm():#. 
    clr()#. 
    banner()#. 
    print(Fore.GREEN + "[+] Oto DM yardım kısmına hoşgeldiniz. Bu kısımı lütfen okumadan geçmeyiniz.\n\n[+] Yardım kanalımız: için @. e yazın\n\n[+] Soru hızlı yardım ıcın: https://t.me/.\n\n")#. 
    print(Fore.GREEN + "[+] OTO dm başlatmanız için önce üye listesi çekmelisiniz. ")#. 
    print(Fore.GREEN + "[+] Spam koruma Telegram Premium üyelerde daha iyi çalışacaktır.")#. 
    print(Fore.GREEN + "[+] Flood hatası yedıysenız OTO DM yı belırlı bır sure başlatmayın.")
    print(Fore.GREEN + "[+] Çektiğiniz üyeler members.csv dosyasına kaydedilmektedir dm atılan kullanıcıların otomatık listeden silimi bulunmamaktadır sizin el ile silmeniz gerekmektedir. Kolay sılım ıcın Botun ayarlar kısmından members.csv sil işlemini yaparak ilk 50 kullanıcıyı sılebılırsınız.")
    print(Fore.GREEN + "[+] API_ID API_HASH ayarları apı.txt dosyasına kaydedılmektedır. Dosyadan kontrollerınzı yapabılırsınız.")#. 
     
    print(Fore.RED + "[+] Bot ekranı 60 saniye sonra gelecektir.")#. 
    time.sleep(60)#. 
    clr()#. 
    try:
        with open("api.txt", "r") as f:#. 
            api_id, api_hash = f.read().split(",")#. 
        api_id = int(api_id)#. 
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")#. 
    except FileNotFoundError:#. 
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))#. 
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")#. 
        with open("api.txt", "w") as f:#. 
            f.write(f"{api_id},{api_hash}")#. 
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")#. 
    try:#. 
        client = TelegramClient("session", api_id, api_hash)#. 
        client.start()   #. 
    except:#. 
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") #. 
        time.sleep(5)#. 
        client.disconnect()#. 
        start()  #. 
    try:
        sanie = int(input("DM gönderme aralığı (saniye cinsinden) [0 = sıfır bekleme süresi]:  "))  
    except ValueError:#. 
        print(Fore.RED + "Yanşlış değer! Ana menüye dönülüyor;")  
        time.sleep(5)#. 
        client.disconnect()#. 
        start()  #. 
    except IndexError:#. .
        print(Fore.RED + "Yanşlış değer! Ana menüye dönülüyor;")  #. #. .
        time.sleep(5)#. 
        client.disconnect()#. #. .#. .
        start()      #. 
    try:#. 
        with open("message.txt", "r" , encoding="utf-8") as f:#. 
            message = f.read()#. 
    except FileNotFoundError:#. 
        print(Fore.RED + "message.txt dosyası bulunamadı lütfen adımları tekrar ızleyıp message.txt dosyasını kurun. Ana menüye dönülüyor; #. .")#. 
        time.sleep(5)#. 
        client.disconnect()#. #. .#. .
        start()    #. 
    with open("members.csv", mode="r") as file:#. 
        reader = csv.reader(file)#. 
        next(reader) #. 
        print(Fore.GREEN + "Bot başlatıldı durdurmak için Ctrl + c yapın. #. .")#. #. .
        for row in reader:#. 
            username = (row[0]) #. #. 
            try:#. 
                if "*" in username:
                    print(f"Kullanıcı adı {username} '*' karakteri içeriyor. Atlanıyor...")#
                else:#. 
                    client.send_message(username, message)#. #. .
                    time.sleep(sanie)#. #. .
                    print(Fore.BLUE + f"Mesaj {username}, li kullanıcıya gonderıldı")#. .
            except PeerFloodError:
                print(Fore.RED + "Hata! Flood sistemini devre dışı bırakan hata oluştu. Gereksinimler çalıştırılıyor... #. .")
                time.sleep(5)#. .
                hata = 0#. .
                basari = 0#. .
                try:#. .
                    client.send_message("SpamBot", "/start")#. .
                    print(Fore.GREEN + "[+] Flood adım 1 başarılı oldu.")#. .
                    basari += 1#. .
                except:
                    print(Fore.RED + "[-] Flood adım 1 başarısız oldu.") #. .
                    hata += 1#. .
                time.sleep(2)
                try:#. .
                    client.send_message("SpamBot", "/start")#. .
                    client.send_message("SpamBot", "This is a mistake")
                    client.send_message("SpamBot", "Yes")#. .
                    client.send_message("SpamBot", "No! Never did that!")#. .
                    client.send_message("SpamBot", "İm writing my family some messages and ı banned from telegram messages pls open sir")#. .
                    print(Fore.GREEN + "[+] Flood adım 2 başarılı oldu.")#. .
                    basari += 1#. .
                except:#. .
                    print(Fore.RED + "[-] Flood adım 2 başarısız oldu.") #. .
                    hata += 1
                time.sleep(5)    #. .
                print(Fore.RED + "Botu lütfen belırlı bır zaman bekledıkten sonra tekrar çalıştırın. Ana menüye dönülüyor;")#. .
                time.sleep(5)#. .
                client.disconnect()#. .
                start()#. .
            except KeyboardInterrupt:
                print(Fore.RED + "Gönderim kullanıcı tarafından durduruldu. Ana menüye dönülüyor;")#. .
                time.sleep(5)#. .
                client.disconnect()#. .
                start()    #. .
            except UsernameInvalidError:
                print(f"Kullanıcı adı {username} olan kullanıcı bulunamadı")#. .
            except Exception as e:#. .
                print(Fore.RED + f"Mesaj {username} kullanıcısına gonderılırken bır sorun olustu. Koruma çalıştırılıyor... {e}")#. .
                time.sleep(5)#. .
                client.send_message("SpamBot", "/start")#. .
                time.sleep(60)#. .
        print("Tüm gönderim bitti")#. .
        client.disconnect()#. .
    start()#. .

def otomesaj():#. .
    clr()#. .
    banner()#. .
    print(Fore.GREEN + "[+] Oto mesaj yardım kısmına hoşgeldiniz. Bu kısımı lütfen okumadan geçmeyiniz.\n\n[+] \n\n")#. .
    print(Fore.GREEN + "[+] Grupları gırdıgınız zaman gruplar bır groups.txt dosyasına kaydedılecektır. Grup ayarlamalarınızı o kısımdan yapabılırsınız.")
    print(Fore.GREEN + "[+] API_ID API_HASH ayarları apı.txt dosyasına kaydedılmektedır. Dosyadan kontrollerınzı yapabılırsınız.")#. .#. .
    print(Fore.GREEN + "[+] Botu başlatmadan önce lüfen bot dosyasının (main.py) ile aynı klasor ıcıne message.txt adında bır dosya oluşturup icine gruplara gondermek ıstedıgınız mesajı yazın.")#. .
    print(Fore.GREEN + "[+] Bu kısımları okumadan geçmeyin ")#. .
    print(Fore.RED + "[+] Bot ekranı 30 saniye sonra gelecektir.")#. .
    time.sleep(30)#. .
    clr()
    try:
        with open("api.txt", "r") as f:
            api_id, api_hash = f.read().split(",")#. .
        api_id = int(api_id)
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")#. .
    except FileNotFoundError:
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))#. .
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")#. .
        with open("api.txt", "w") as f:
            f.write(f"{api_id},{api_hash}")
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")     #. .
    try:
        with open("groups.txt", "r") as f:
            groups = f.read().splitlines()
        print("Gruplar dosyadan okundu.")
    except FileNotFoundError:#. .
        n = int(input("Kaç grup mesaj gönderilecek "))
        groups = []#. .
        for i in range(n):#. .#. .
            group_name = input(f"Lütfen {i+1}. grup ismini giriniz: ")
            groups.append(group_name)#. .#. .
        with open("groups.txt", "w") as f:#. .
            f.write("\n".join(groups))
        print("Gruplar dosyaya kaydedildi.")#. .
    try:#. .
        client = TelegramClient("session", api_id, api_hash)
        client.start()   #. .#. .
    except:#. .
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") #. .
        time.sleep(5)#. .#. .
        client.disconnect()#. .
        start()   #. .
    try:    
        beklemesuresi = float(input("Mesaj gönderme aralığı (saniye cinsinden) [0 = sürekli gönder]: "))#. .
        dongu = float(input("Tekrarlama aralıgı [kapatana kadar gondermesını ıstıyorsanız uzun bır sayı yazın]: "))#. .
    except:#. .
        print(Fore.RED + "Yanlış girim yaptınız. Ana menüye dönülüyor;")#piyasanın alla#. .hı benım .
        time.sleep(5)#. .
        client.disconnect()#. .
        start()#. .
    donguhesap = 0#. .
#. .
    try:
        with open("message.txt", "r" , encoding="utf-8") as f:
            message = f.read()#. .
    except FileNotFoundError:
        print(Fore.RED + "message.txt dosyası bulunamadı lütfen adımları tekrar ızleyıp message.txt dosyasını kurun. Ana menüye dönülüyor;")
        time.sleep(5)#. .
        client.disconnect()
        start()        #. .
    try:#. .
        clr()#. .
        print(Fore.GREEN + "Bot başlatıldı durdurmak için Ctrl + c yapın.")
        while dongu > donguhesap:
            for group in groups:
                client.send_message(group, message)#. .
                print(f"Mesaj ({group}) gönderildi.")#. .
            print(Fore.BLUE + f"Bir sonraki gönderim için {beklemesuresi} saniye bekleniyor...")
            time.sleep(beklemesuresi)
            donguhesap  += 1
        print(Fore.GREEN + "Tüm gönderim bitti. Ana menüye dönülüyor;")    #. .
        time.sleep(5)
        client.disconnect()
        start()
    except KeyboardInterrupt:
        print(Fore.RED + "Gönderim kullanıcı tarafından durduruldu. Ana menüye dönülüyor;")#. .
        time.sleep(5)
        client.disconnect()
        start()
#. .#. .
def scraper():
    clr()
    banner()
    print(Fore.GREEN + "[+] Oto scraper yardım kısmına hoşgeldiniz. Bu kısımı lütfen okumadan geçmeyiniz.\n\n[+] Yardım kanalımız: için @. e yazın\n\n[+] Soru hızlı yardım ıcın: https://t.me/.\n\n")
    print(Fore.GREEN + "[+] Çektiğiniz üyeler members.csv dosyasına kaydedilmektedir eklenen kullanıcıların otomatık listeden silimi bulunmamaktadır sizin el ile silmeniz gerekmektedir.  Kolay sılım ıcın Botun ayarlar kısmından members.csv sil işlemini yaparak ilk 50 kullanıcıyı sılebılırsınız.")
    print(Fore.GREEN + "[+] API_ID API_HASH ayarları apı.txt dosyasına kaydedılmektedır. Dosyadan kontrollerınzı yapabılırsınız.")
    print(Fore.GREEN + "[+] Bu kısımları okumadan gecmeyin İyi kullanmalar")
    print(Fore.RED + "[+] Bot ekranı 30 saniye sonra gelecektir.")#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .#. .
    time.sleep(30)
    clr()
    try:
        with open("api.txt", "r") as f:#. .
            api_id, api_hash = f.read().split(",")
        api_id = int(api_id)#. .
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")
    except FileNotFoundError:
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")#. .
        with open("api.txt", "w") as f:
            f.write(f"{api_id},{api_hash}")
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")     
    try:
        client = TelegramClient("session", api_id, api_hash)
        client.start()   
    except:
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") 
        time.sleep(5)
        client.disconnect()
        start()  
    chats = []#. .
    last_date = None
    chunk_size = 200#. .
    groups=[]
 
    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),#. .
                 limit=chunk_size,
                 hash = 0
             ))#. .#. .
    chats.extend(result.chats)
 
    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue
    i=0
    for group in groups:
        print(Fore.YELLOW+'['+Fore.RED+str(i)+Fore.GREEN+']'+Fore.CYAN+' - '+group.title)
        i+=1

    selected_group_number = int(input("\nHangi gruba üye eklemek istersiniz? Numarasını girin: "))     #. .
    target_group=groups[int(selected_group_number)]
    clr()    
    
    with open("members.csv", mode="r") as f:
        reader = csv.reader(f)
        next(reader)
        entity = InputChannel(target_group.id, target_group.access_hash)
        ns = 0
        added_users = []
        print(Fore.GREEN + "Bot başlatıldı durdurmak için Ctrl + c yapın.")
        for row in reader:
            usernames = (row)
            ns += 1
            added_users.append(usernames)#. .
            if ns % 50 == 0:
                
                print(f' Ban Riski Dolayısıyla 2 Dakika Bekleme')
                time.sleep(120)
            try:
                if "*" in usernames:
                    print(f"Kullanıcı adı {usernames} '*' karakteri veya boşluk içeriyor. Atlanıyor...")
                    time.sleep(2)
                else:    
                    # user_to_add = client.get_input_entity(username)
                    client(InviteToChannelRequest(entity, usernames))
                    print(f'{usernames} Ekleniyor...')
                    print(f'10 Saniye Bekleme')
                    time.sleep(10)#. .
            except PeerFloodError:
                print(Fore.RED + "Hesap FLOOD hatası aldı! Lütfen kodu 3-4 saat süre sonra çalıştırın. Ana menüye dönülüyor;")
                time.sleep(5)
                client.disconnect()
                start()
            except UserPrivacyRestrictedError:
                print(Fore.RED + 'Bu Kullanıcı Gruplara Eklenmeyi Engellemiş pas geçiliyor')
                time.sleep(4)
                continue
            except UserAlreadyParticipantError:
                print(Fore.RED +  "Kullanıcı zaten grupta var pas geçiliyor")
                time.sleep(3)
                continue
            except UserAlreadyInvitedError:
                print(Fore.RED + "Kullanıcı zaten grupta var pas geçiliyor")#. .#. .
                time.sleep(3)
                continue
            except KeyboardInterrupt:
                print(Fore.RED + 'Uygulama Durduruldu. Ana menüye dönülüyor;')
                time.sleep(5)
                client.disconnect()
                start()
            except Exception as e:
                print(Fore.RED + f"HATA: {e} pas geçiliyor..")
                time.sleep(3)
                continue
            
colors = [Fore.RED, Fore.GREEN, Fore.WHITE, Fore.CYAN]
rs = Fore.RESET#. .
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Seks ')
    print(random.choice(colors) + logo + rs)
    print(Fore.RED + '31 seks''\n')

def etiket():
    clr()
    banner()
    print(Fore.GREEN + "[+] Oto etiket yardım kısmına hoşgeldiniz. Bu kısımı lütfen okumadan geçmeyiniz.\n\n[+] Yardım kanalımız için . e ulaşın. \n\n[+] Soru hızlı yardım ıcın: https://t.me/.\n\n")
    print(Fore.GREEN + "[+] Bu kısmın amacı 1. secenek ile çektiğiniz kullanıcı ısımlerını ıstedıgınız grupta tek tek etıketleyerek reklam yapabılırsınız.")
    print(Fore.GREEN + "[+] API_ID API_HASH ayarları apı.txt dosyasına kaydedılmektedır. Dosyadan kontrollerınzı yapabılırsınız.")
    print(Fore.GREEN + "[+] Botu başlatmadan önce lüfen bot dosyasının (main.py) ile aynı klasor ıcıne message.txt adında bır dosya oluşturup icine gruplara gondermek ıstedıgınız mesajı yazın.")
    print(Fore.GREEN + "[+] Okumadan geçmeyin")
    print(Fore.RED + "[+] Bot ekranı 30 saniye sonra gelecektir.")
    time.sleep(30)
    clr()#. .
    try:
        with open("api.txt", "r") as f:
            api_id, api_hash = f.read().split(",")
        api_id = int(api_id)
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")
    except FileNotFoundError:
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")
        with open("api.txt", "w") as f:
            f.write(f"{api_id},{api_hash}")
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")     
    try:
        client = TelegramClient("session", api_id, api_hash)
        client.start()   
    except:
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") 
        time.sleep(5)
        client.disconnect()
        start()    
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
 
    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))#. .
    chats.extend(result.chats)
 
    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue
    i=0#. .
    for group in groups:
        print(Fore.YELLOW+'['+Fore.RED+str(i)+Fore.GREEN+']'+Fore.CYAN+' - '+group.title)
        i+=1
    try:
        selected_group_number = int(input("\nHangi gruba etiket başlatmak istersiniz? Numarasını girin: "))     
    except:
        print(Fore.RED + "Yanlış değer! Ana menüye dönülüyor;")
        time.sleep(5)
        client.disconnect()
        start()
    target_group=groups[int(selected_group_number)]
#. .
    with open('members.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        users = [row[0] for row in reader]
    try:
        with open("message.txt", "r" , encoding="utf-8") as f:
            message_ = f.read()#. .
    except FileNotFoundError:
        print(Fore.RED + "message.txt dosyası bulunamadı lütfen adımları tekrar ızleyıp message.txt dosyasını kurun. Ana menüye dönülüyor;")
        time.sleep(5)
        client.disconnect()
        start()#. .
    tagcount = 13
    print(Fore.GREEN + "Bot başlatıldı durdurmak için Ctrl + c yapın.")
    for a in range(0, len(users), tagcount):
        tagged_users = users[a:a+tagcount]
        tag_text = " ".join([f"@{user}" for user in tagged_users if user and user != '*'])
    
        text = message_ + '\n' + '\n' +  tag_text

        try:
            client.send_message(target_group, text)
            time.sleep(5)
            print('etiket mesajı gonderıldı.')
        except FloodWaitError:
            print(Fore.RED + "FLOOD hatası. Ana menüye dönülüyor;")
            time.sleep(3)
            client.disconnect()
            start()
        except KeyboardInterrupt:
            print(Fore.RED + "Gönderim kullanıcı tarafından durduruldu. Ana menüye dönülüyor;")
            time.sleep(5)
            client.disconnect()
            start()
        except Exception as e:
            print(Fore.RED + f"HATA: {e}. Ana menüye dönülüyor;")  
            time.sleep(5)
            client.disconnect()
            start() 
        
    print(Fore.GREEN + "Tüm gönderim bitti") 
    client.disconnect()  
    time.sleep(5) 
    start()

def iletme():
    clr()
    banner()
    print(Fore.GREEN + "[+] Oto iletme yardım kısmına hoşgeldiniz. Bu kısımı lütfen okumadan geçmeyiniz.\n\n[+] Yardım kanalımız için . e ulaşın. \n\n[+] Soru hızlı yardım ıcın: https://t.me/.\n\n")
    print(Fore.GREEN + "[+] Mesaj ID , Grup ID gibi bilgilerın nasıl alınacagnı bılmeyenler rehber kanalımızdan ogrenebılırler. Rehber kanalı için => @.")
    print(Fore.GREEN + "[+] Oto iletmenın temel mantığı bır mesajı bır gruptan dıger gruplara iletmesidir bu sayede mesajlarınızdaki premium çıkartmalar gruplara gonderılecektır.")
    print(Fore.GREEN + "[+] API_ID API_HASH ayarları apı.txt dosyasına kaydedılmektedır. Dosyadan kontrollerınzı yapabılırsınız.")
    print(Fore.GREEN + "[+] Bu kısımları okumadan gecmeyin İyi kullanmalar")
    print(Fore.RED + "[+] Bot ekranı 30 saniye sonra gelecektir.")
    time.sleep(30)
    clr()
    try:
        with open("api.txt", "r") as f:
            api_id, api_hash = f.read().split(",")
        api_id = int(api_id)
        print(Fore.BLUE + "API ID ve API HASH Dosyadan okundu.")
    except FileNotFoundError:
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")
        with open("api.txt", "w") as f:
            f.write(f"{api_id},{api_hash}")
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")     
    try:
        with open("groups.txt", "r") as f:
            target_groups = f.read().splitlines()
        print("Groups loaded from file.")
    except FileNotFoundError:
        n = int(input("Kaç grup mesaj gönderilecek? "))
        target_groups = []
        for i in range(n):
            group_name = input(f"Lütfen {i+1}. grup ismini giriniz: ")
        target_groups.append(group_name)
        with open("groups.txt", "w") as f:
            f.write("\n".join(target_groups))
        print("Groups saved to file.")
    try:
        client = TelegramClient("session", api_id, api_hash)
        client.start()   
    except:
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") 
        time.sleep(5)
        client.disconnect()
        start()
    try:
        source_group = int(input("İletilecek mesajın bulundugu grup İD sini girin: "))
        message_id = int(input("İletilecek mesajın İD sini girin: "))
        interval = int(input("Botun kaç saniyede bir mesaj gönderecegini yazın [saniye cinsinden]: "))
        dongu = float(input("Tekrarlama aralıgı [kapatana kadar gondermesını ıstıyorsanız uzun bır sayı yazın]: "))
    except:
        print(Fore.RED + "Yanlış değer! Ana menüye dönülüyor;")
        time.sleep(5)
        client.disconnect()
        start()
    try:
        source_entity = client.get_entity(source_group)
        target_entities = [client.get_entity(group_name) for group_name in target_groups]  
        message = client.get_messages(source_entity, ids=message_id)
        donguhesap1 = 0
    except Exception as e:
        print(Fore.RED + f"HATA!: {e}. Ana menüye dönülüyor;")
        time.sleep(4)
        client.disconnect()
        start()
    clr()
    print(Fore.RED + "Program başlatıldı çıkmak için CTRL + C yapın.")    
    try:    
        while dongu > donguhesap1:
            for target_entity in target_entities:
                try:
                    client.forward_messages(target_entity,message)
                    time.sleep(2)
                except:
                    print(f"Mesaj gönderme hatası: {source_group}")
                    continue
            if interval == 0:
                continue
            print(f"Bir sonraki gönderim için {interval} saniye bekleniyor.")
            time.sleep(interval)
            donguhesap1 += 1
        print(Fore.GREEN + "Tüm gönderim bitti: Ana menüye dönmek için Entere basın; ")
        input("")
        print(Fore.GREEN + "Ana menüye dönülüyor; ")
        time.sleep(5)
        client.disconnect()
        start()
    except KeyboardInterrupt:
        print(Fore.RED + "Program kullanıcı tarafından durduruldu. Ana menüye dönülüyor;")   
        time.sleep(4)
        client.disconnect()
        start() 
    except Exception as e:
        print(Fore.RED + f"HATA!: {e}. Ana menüye dönülüyor;")
        time.sleep(4)
        client.disconnect()
        start()



def ayarlar():
    clr()
    banner()
    print(Fore.RED + "Çıkmak için entere basın.")
    print(Fore.YELLOW + "[1] APİ İD APİ HASH dosyalarını silin.")
    print(Fore.YELLOW + "[2] Botun bağlı Hesaptan çıkış yapın.")
    print(Fore.YELLOW + "[4] Members.csv dosyasından ilk 50 satırı silin.")
    try:
        with open("api.txt", "r") as f:
            api_id, api_hash = f.read().split(",")
        api_id = int(api_id)
    except FileNotFoundError:
        api_id = int(input("Lütfen my.telegram.org'dan aldığınız api id giriniz: "))
        api_hash = input("Lütfen my.telegram.org'dan aldığınız api hash'ini giriniz: ")
        with open("api.txt", "w") as f:
            f.write(f"{api_id},{api_hash}")
        print(Fore.BLUE + "API ID ve API HASH Dosyaya Kaydedildi.")     
    try:
        client = TelegramClient("session", api_id, api_hash)
        client.start()   
    except:
        print(Fore.RED + "Telegrama bağlanirken sorun oluştu tekrar deneyin. Ana menüye dönülüyor;") 
        time.sleep(5)
        client.disconnect()
        start()
    try:
        sec = int(input("Ne yapmak ıstersınız: "))
    except ValueError:
        print("yanlıs seçim")  
        time.sleep(1)
        client.disconnect()
        start()
    except IndexError:
        print("yanlıs seçim")  
        time.sleep(1)
        client.disconnect()
        start()
    if sec == 1:
        try:
            print(Fore.RED + "APi İD APİ HASH BİLGİGERİNİZ SIFIRLANACAKTIR: ONAYLIYORMUSUNUZ?:")
            onay = input("E/H: ")
            if onay == "E":
                try:
                    os.remove("api.txt")
                    print(Fore.GREEN + "Silme işlemi başarılı. Ana menüye dönülüyor;")
                    time.sleep(4)
                    client.disconnect()
                    ayarlar()
                except:
                    print("HATA OLUŞTU. Ana menüye dönülüyor;")
                    time.sleep(4)
                    client.disconnect()
                    ayarlar()
            elif onay == "H":
                print(Fore.RED + "İşlem iptal edildi. Ana menüye dönülüyor;")
                time.sleep(4)
                client.disconnect()
                ayarlar()
            else:
                print("yanlıs seçim")  
                time.sleep(1)
                client.disconnect()
                ayarlar()      
        except:
            print("HATA OLUŞTU. Ana menüye dönülüyor;")
            time.sleep(4)
            client.disconnect()
            ayarlar()
    elif sec == 2:
        try:
            print(Fore.RED + "BAĞLI HESABINIZ SİLİNECEKTİR: ONAYLIYORMUSUNUZ?:")
            onay = input("E/H: ")
            if onay == "E":
                try:
                    client.log_out()
                    print(Fore.GREEN + "Silme işlemi başarılı. Ana menüye dönülüyor;")
                    time.sleep(4)
                    start()
                except Exception as e:
                    print(Fore.RED + f"HATA OLUŞTU.{e} Ana menüye dönülüyor;")
                    time.sleep(4)
                    client.disconnect()
                    ayarlar()
            elif onay == "H":
                print(Fore.RED + "İşlem iptal edildi. Ana menüye dönülüyor;")
                time.sleep(4)
                client.disconnect()
                ayarlar()
            else:
                print("yanlıs seçim")  
                time.sleep(1)
                client.disconnect()
                ayarlar()   
        except:
            print("HATA OLUŞTU. Ana menüye dönülüyor;")
            time.sleep(4)
            client.disconnect()
            ayarlar()
    elif sec == 3:
        print("bu kısım ucretsız surumde calısmamaktadır ")
        time.sleep(10)

    elif sec == 4:
        try:
            print(Fore.GREEN + "Siliniyor...")
            with open("members.csv", "r") as f:
                lines = f.readlines()

            with open("members.csv", "w") as f:
                f.writelines(lines[50:])
            print(Fore.GREEN + "Silme işlemi başarılı.! Ana menüye dönülüyor;")
            time.sleep(4)
            client.disconnect()
            ayarlar()
        except Exception as e:
            print(Fore.RED + f"Hata {e}.  Ana menüye dönülüyor;")  
            time.sleep(4)
            client.disconnect()
            ayarlar()
    else:
        print("yanlıs seçim")  
        time.sleep(1)
        client.disconnect()
        ayarlar()


start()  
