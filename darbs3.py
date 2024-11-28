import time
import random

username = input("Uzrakstiet savu vārdu: ")

print("SPĒLE - 3 DURVIS")

print('Laipni lūdzam,', username, '!')
print()
print('Lai turpinātu, uzrakstiet - Start')

enter = input()
if enter.lower() == "start":
    print('')
    print('')
    print('Priekšvārds:')
    print('Jūs dodaties strādāt Oriflame birojā. Bet tieši pirms ieejas birojā jūs nolaupa Sandra Vilsone un aizved uz pagrabu,')
    print('kas atrodas zem Oriflame biroja. Jūs varat izkļūt no šī pagraba, bet jums būs jāizvēlas pareizās durvis.')
    print('Jo ne visas durvis vedīs uz Oriflame biroju...')
    
    while True:
        print('')
        print('Uzrakstiet durvju numuru (1-3), kurās vēlaties ieiet')
        
        door = input()
        if door == "1":
            print('')
            print('Jūs atvērāt pirmās durvis.')
            print('Jūs tikko nodomājāt, ka jums ir paveicies, kad pēkšņi, it kā no nekurienes, izlec vampīrs un saka:')
            
            print()
            print('- Sveiks, cilvēk. Lai izkļūtu no pagraba, tev jāuzvar mani spēlē Akmens, Šķēres, Papīrs!')
            print('Ja uzvarēsi, es tevi atbrīvošu, bet, ja uzvarēšu es, tu nonāksi pie haizivīm!')
            
            print()
            print('Nu ko, mums laikam būs jāspēlē ar vampīru.')
            print()
            
            print('Ja jūs neatceraties šīs spēles noteikumus, rakstiet - Rules, ja atceraties, rakstiet - Yes')
            otvet = input()
            if otvet.lower() == 'noteikumi' or otvet.lower() == 'rules':
                print('')
                print('Spēlē Akmens - Šķēres - Papīrs, diviem spēlētājiem vienlaicīgi jāizvēlas un jāuzraksta viens no trim priekšmetiem - Akmens, Šķēres vai Papīrs. Uzvar tas, kura priekšmets ir stiprāks!')
                print(' ')
                print('PRIEKŠMETU SPĒKS')
                print('Akmens uzvar Šķēres.')
                print('Šķēres uzvar Papīru.')
                print('Papīrs uzvar Akmeni.')
            
            print('')
            print('Lai izvēlētos: Akmens, rakstiet - 1, Šķēres, rakstiet - 2, Papīrs, rakstiet - 3')
            time.sleep(2)
            
            print('')
            print('Akmens, Šķēres, Papīrs')
            time.sleep(1)
            print(3)
            time.sleep(0.5)
            print(2)
            time.sleep(0.5)
            print(1)
            time.sleep(0.5)
            
            kmn = input('Jūsu izvēle (1/2/3): ')
            if kmn == '1':
                kamenibumaga = 'Akmens'
            if kmn == '2':
                kamenibumaga = 'Šķēres'
            if kmn == '3':
                kamenibumaga = 'Papīrs'
            
            time.sleep(0.5)    
            print(username + ': Es izvēlos - ', kamenibumaga)
            
            kmnotvet = random.choice(['Šķēres', 'Papīrs', 'Akmens'])
            print('VirtuAl: Es izvēlos - ', kmnotvet)
            
            print()
            
            if kmn == '1' and kmnotvet == 'Šķēres':
                print('Apsveicam, jūs uzvarējāt!')
                print('')
                print('Vampīrs, kā solīja, izveda jūs brīvībā, un jūs veiksmīgi sākāt darbu Oriflame birojā!')
                print('')
                print('YOU WIN!!!')
                break    
            elif kmn == '2' and kmnotvet == 'Papīrs':
                print('Apsveicam, jūs uzvarējāt!')
                print('')
                print('Vampīrs, kā solīja, izveda jūs brīvībā, un jūs veiksmīgi sākāt darbu Oriflame birojā!')
                print('')
                print('YOU WIN!!!')
            elif kmn == '3' and kmnotvet == 'Akmens':
                print('Apsveicam, jūs uzvarējāt!')
                print('')
                print('Vampīrs, kā solīja, izveda jūs brīvībā, un jūs veiksmīgi sākāt darbu Oriflame birojā!')
                print('')
                print('YOU WIN!!!')
            elif kmn == '1' and kmnotvet == 'Papīrs':
                print('Vampīrs uzvarēja...')
                print('')
                print('Vampīrs met jūs pie haizivīm...')
                time.sleep(2)
                print('Jūs gājāt bojā.')
                print('Lai sāktu no jauna, rakstiet - again')
                again = input()
                if again.lower() != 'again':
                    break
            elif kmn == '2' and kmnotvet == 'Akmens':
                print('Vampīrs uzvarēja...')
                print('Vampīrs met jūs pie haizivīm...')
                time.sleep(2)
                print('Jūs gājāt bojā.')
                print('Lai sāktu no jauna, rakstiet - again')
                again = input()
                if again.lower() != 'again':
                    break
            elif kmn == '3' and kmnotvet == 'Šķēres':
                print('Vampīrs uzvarēja...')
                print('Vampīrs met jūs pie haizivīm...')
                time.sleep(2)
                print('Jūs gājāt bojā.')
                print('Lai sāktu no jauna, rakstiet - again')
                again = input()
                if again.lower() != 'again':
                    break
            elif kmn == '1' and kmnotvet == 'Akmens':
                print('Neizšķirts!')
                print('Vampīrs jūs sūta uz sākumu.')
                time.sleep(2)
            elif kmn == '2' and kmnotvet == 'Šķēres':
                print('Neizšķirts!')
                print('Vampīrs jūs sūta uz sākumu.')
                time.sleep(2)
            elif kmn == '3' and kmnotvet == 'Papīrs':
                print('Neizšķirts!')
                print('Vampīrs jūs sūta uz sākumu.')
                time.sleep(2)

                            
                           
        elif door == '2':
            
            print('')
            print('Jūs atvērāt otrās durvis.')
            print('Jūs ejat pa tumšo koridoru, briesmas nav.')
            print('Pēkšņi ceļš sadalās.')
            print('Jūs varat iet pa labi vai pa kreisi.')
            print('')
            
            print('Lai iet pa labo ceļu, uzrakstiet - Right')
            print('Lai iet pa kreiso ceļu, uzrakstiet - Left')
            rightorleft = input()
            
            if rightorleft.lower() == 'right':
                print('')
                print('Jūs pagriezāties pa labi.')
                print('Tieši aiz pagrieziena bija kraujas mala.')
                print('Jūs nokritāt un sasitāties.')
                print('')
                print('Jūs zaudējāt.')
                time.sleep(1)
                print()
                print("Lai sāktu no jauna, uzrakstiet - Again")
                print('Lai beigtu, uzrakstiet - Stop')
                atamobriv = input()
                print()
            
                if atamobriv.lower() == 'again':
                    print()
            
                else:
                    break
                            
            elif rightorleft.lower() == 'left': 
                print('')
                print('Jūs pagriezāties pa kreisi.')
                print('Aiz pagrieziena bija garš koridors.')
                print('')
                
                print('Lai turpinātu iet, uzrakstiet - Go')
                print('Lai apstāties, uzrakstiet - Stop')
                
                goorstop = input()
                if goorstop.lower() == 'go':
                    print('')
                    print('Jūs devāties tālāk.')
                    print('Jūs sasniedzāt durvis.')
                    print('')
                
                    print('Lai ieietu, uzrakstiet - Room')
                    print('Lai neieietu, uzrakstiet - Hall')
                
                    roomorhall = input()
                    if roomorhall.lower() == 'room':
                        print('')
                        print('Jūs iegājāt telpā.')
                        print('Pēkšņi jūs dzirdējāt, kā aiz jums aizcirtās durvis.')
                        print('Telpā izslēdzās gaisma.')
                        print('Pēkšņi telpa sāka piepildīties ar indīgu gāzi.')
                        print('')
                        print('Jūs zaudējāt.')
                        time.sleep(1)
                        print()
                
                        print("Lai sāktu no jauna, uzrakstiet - Again")
                        print('Lai beigtu, uzrakstiet - Stop')
                        roomihall = input()
                        print()
                
                        if roomihall.lower() == 'again':
                            print()
                
                        else:
                            break
            
                    elif roomorhall.lower() == 'hall':
                        print('')
                        print('Jūs neiegājāt telpā.')
                        print('Pēkšņi aiz jums jūs dzirdējāt soļus.')
                        print('Bet jūs nepaspējāt pagriezties.')
                        print('Jums mugurā iedūra nazi.')
                        print('')
                        print('Jūs zaudējāt.')
                        
                        time.sleep(1)
                        print()
                        print("Lai sāktu no jauna, uzrakstiet - Again")
                        print('Lai beigtu, uzrakstiet - Stop')
                        
                        hallllll = input()
                        print()
                        
                        if hallllll.lower() == 'again':
                            print()
                                        
                        else:
                            print()
                            break
                            
                elif goorstop.lower() == 'stop': 
                    print('')
                    print('Jūs negribējāt iet tālāk pa koridoru.')
                    print('Kamēr jūs stāvējāt un domājāt, ko darīt tālāk, viss grīdas segums ap jums piepildījās ar indīgiem zirnekļiem.')
                    print('Jūs mēģinājāt no tiem izbēgt.')
                    print('Bet viens no viņiem tomēr jūs sakoda.')
                    print('Jūs zaudējāt samaņu...')
                    print('')
                    print('Jūs zaudējāt.')
                    time.sleep(1)
                    print()
                    print("Lai sāktu no jauna, uzrakstiet - Again")
                    print('Lai beigtu, uzrakstiet - Stop')
                    goilistop = input()
                    print()
                                
                    if goilistop.lower() == 'again':
                            print()
                                
                    else:
                        break
                            
        elif door == "3":  
            print('')
            print('Jūs atvērāt trešās durvis.')
            print('Tieši aiz durvīm bija lifts.')
            print('Jūs iegājāt liftā.')
            print('Izvēlieties stāvu, uz kuru vēlaties doties (1-3).')
                
            print('Lai izvēlētos, uzrakstiet stāva numuru:') 
            
            viberietazhplz = input()
            if viberietazhplz == '1':
                print('')
                print('Kamēr jūs kāpāt, lifta virve pārtrūka un lifts nokrita šahtā.')
                print('Jūs neizturējāt kritienu un sasitāties.')
                print('')
                print('Jūs zaudējāt.')
                time.sleep(1)
                print()
                print("Lai sāktu no jauna, uzrakstiet - Again")
                print('Lai beigtu, uzrakstiet - Stop')
                liftupal = input()
                print()
            
                if liftupal.lower() == 'again':
                    print()
            
                else:
                    break
                                
            elif viberietazhplz == '2': 
                print('')
                print('Jūs uzkāpāt otrajā stāvā.')
                print('Pirms jums bija liela, pilnīgi balta istaba')
                print('Otrā istabas galā jūs pamanījāt divas kāpnes')
                print('Jūs varat nokāpt uz pirmo stāvu vai uzkāpt uz trešo stāvu.')
                print('')
                print('Lai kāptu lejā, uzrakstiet - Down')
                print('Lai kāptu augšā, uzrakstiet - Up')
                
                downorup = input()
                if downorup.lower() == 'down':
                    print('')
                    print('Jūs nokāpāt uz pirmo stāvu.')
                    print('Istabā ir izslēgta gaisma, un jūs neko neredzat, izņemot pēdējo pakāpienu.')
                    print('Jūs nolemjat izmēģināt savu veiksmi un iet tālāk.')
                    print('Apakšā nav grīdas.')
                    print('Jūs nokritāt uz krokodilu baseinu.')
                    print('Tie jūs apēda...')
                    print('')
                    print('Jūs zaudējāt.')
                    
                    time.sleep(1)
                    print()
                    print("Lai sāktu no jauna, uzrakstiet - Again")
                    print('Lai beigtu, uzrakstiet - Stop')
                    usholdown = input()
                    print()
                
                    if usholdown.lower() == 'again':
                        print()
                
                    else:
                        break
                
                elif downorup.lower() == 'up':  
                    print('')
                    print('Jūs uzkāpāt uz trešo stāvu.')
                    print('Uz trešā stāva jūs pamanījāt satrauktu vīrieti.')
                    print('Jūs piegājāt pie viņa, un, kad viņš jūs ieraudzīja, viņa sejā parādījās atvieglojums.')
                    print('Izrādījās, ka tas ir Oriflame darbinieks, kurš jūs meklēja.') 
                    print('Vīrietis aizveda jūs uz biroju un jūs veiksmīgi iegājāt darbā!')
                    print('')
                    print('TU UZVARĒJI!!!')
                    
                    break
                
                else:
                    print('Šāda stāva nav.')
                    
            elif viberietazhplz == '3':
                print('')
                print('Jūs uzkāpāt uz trešo stāvu')
                print('Uz trešā stāva jūs pamanījāt satrauktu vīrieti.')
                print('Jūs piegājāt pie viņa, un, kad viņš jūs ieraudzīja, viņa sejā parādījās atvieglojums.')
                print('Izrādījās, ka tas ir Oriflame darbinieks, kurš jūs meklēja.') 
                print('Vīrietis aizveda jūs uz biroju un jūs veiksmīgi iegājāt darbā!')
                print('')
                print('TU UZVARĒJI!!!')
                
                break
                
            else:
                print()
                print('Šāds stāvs nav.')
                
        else:
            print('Tādas durvis nav.')
