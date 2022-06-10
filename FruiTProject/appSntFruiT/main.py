# public import
from tkinter import *
from random import *
from time import sleep
import webbrowser

# local import
from bddBrowser import *
from bddFruit import *

# general var
wb = webbrowser

''' timer = 0
check = True
while check:
    timer += 1
    sleep(2)
    print("test : {}".format(timer)) '''

print("Console log :\n")

def windowIsActive():
    window.mainloop()

def switchModeGeneralLink():
    getSearchBarButtonForLink()

def switchModeFruitlLink():
    getSearchBarButtonSpecialForFruit()

def getSearchBarButtonForLink():
    resultOfSearchBar = searchBar.get()
    if resultOfSearchBar.lower() in dataBaseFruiT:
        resultRandom = choice(dataBaseBrowser)
        wb.open_new(resultRandom)
        print("Console log : choix correct")
    else:
        print("Console log : choix incorrect")
#les bienfaits
def getSearchBarButtonSpecialForFruit():
    resultOfSearchBar = searchBar.get().lower()
    if resultOfSearchBar == "pomme":
        wb.open_new('https://sante.journaldesfemmes.fr/fiches-nutrition/2524527-les-bienfaits-de-la-pomme-pour-la-sante/#:~:text="La%20pomme%20contient%20aussi%20de,des%20sucres%20et%20des%20graisses.')
    elif resultOfSearchBar == "pastèque":
        wb.open_new('https://wikifarmer.com/fr/12-bienfaits-sante-etonnants-de-la-pasteque/')
    elif resultOfSearchBar == "abricot":
        wb.open_new('https://www.jardiner-malin.fr/sante/abricot-bienfaits-vertu.html#:~:text=C%27est%20un%20diurétique%2C%20il,efficaces%20en%20cas%20d%27%20hémorroïdes.')
    elif resultOfSearchBar == "pêche":
        wb.open_new('https://www.jardiner-malin.fr/sante/peche-bienfaits-vertus.html#:~:text=Source%20de%20fibres%20alimentaires%2C%20la,la%20prévention%20des%20maladies%20cardiovasculaires.')
    elif resultOfSearchBar == "poire":
        wb.open_new('https://sante.journaldesfemmes.fr/fiches-nutrition/2595168-poire-bienfaits-sante-calories-contre-indication/#:~:text=Elle%20booste%20les%20transits%20paresseux,la%20plus%20riche%20en%20fibres.')
    elif resultOfSearchBar == "mangue":
        wb.open_new('https://www.jardiner-malin.fr/sante/abricot-bienfaits-vertu.html#:~:text=C%27est%20un%20diurétique%2C%20il,efficaces%20en%20cas%20d%27%20hémorroïdes.')
    elif resultOfSearchBar == "ananas":
        wb.open_new('https://sante.journaldesfemmes.fr/fiches-nutrition/2537094-bienfaits-ananas-sante-minceur-foie-digestion/')
    elif resultOfSearchBar == "kiwi":
        wb.open_new('https://www.zespri.com/fr-BE/blogdetail/10-bienfaits-etonnants-du-kiwi')
    elif resultOfSearchBar == "figue":
        wb.open_new('https://sante.lefigaro.fr/mieux-etre/nutrition-aliments/figue/quels-bienfaits#:~:text=La%20figue%20est%20riche%20en,une%20quantité%20intéressante%20de%20fibres.')
    elif resultOfSearchBar == "framboise":
        wb.open_new('https://www.femmeactuelle.fr/sante/alimentation-equilibree/les-5-vertus-sante-de-la-framboise-10892#:~:text=Le%20fruit%20est%20connu%20pour,préviennent%20maladies%20cardiovasculaires%20et%20chroniques.')
    elif resultOfSearchBar == "myrtille":
        wb.open_new('https://www.topsante.com/nutrition-et-recettes/les-bons-aliments/les-supers-aliments/la-myrtille-prend-soin-de-nos-yeux-620584#:~:text=Ses%20atouts%20santé&text=Championne%20de%20la%20vision%20%3A%20elle,bonne%20vascularisation%20de%20la%20rétine.&text=Sa%20richesse%20en%20anthocyanes%20(420,g)%20combat%20le%20vieillissement%20cellulaire.&text=Peu%20calorique%20et%20peu%20sucrée,est%20un%20petit%20fruit%20minceur%20!')
    elif resultOfSearchBar == "melon":
        wb.open_new('https://www.cuisineaz.com/articles/10-bienfaits-du-melon-sur-votre-sante-1395.aspx')
    elif resultOfSearchBar == "raisin":
        wb.open_new('https://www.irbms.com/fiches-aliments-raisin/#:~:text=Bienfaits%20du%20raisin%20sur%20la,flavonoïdes%20renfermés%20dans%20les%20grains.')
    elif resultOfSearchBar == "mûre":
        wb.open_new('https://www.lacourdorgeres.com/la-mure-decouvrez-ses-nombreux-bienfaits-pour-votre-sante-,n202.html#:~:text=Un%20fruit%20bon%20pour%20la,excellente%20pour%20la%20circulation%20sanguine.')
    elif resultOfSearchBar == "alise":
        wb.open_new('https://alimentation.ooreka.fr/astuce/voir/488125/alise')
    elif resultOfSearchBar == "cassis":
        wb.open_new('https://sante.journaldesfemmes.fr/fiches-sante-du-quotidien/2657441-cassis-plante-medicinale-bienfaits-indications-contre-indications/#:~:text=Le%20cassis%20est%20connu%20aujourd,)"%2C%20décrit%20Amélie%20Mounier.')
    elif resultOfSearchBar == "groseille":
        wb.open_new('https://www.jardiner-malin.fr/sante/groseille-bienfaits-vertu.html#:~:text=Elle%20est%20efficace%20pour%20lutter,vitamines%20A%2C%20B%20et%20C.')
    elif resultOfSearchBar == "prune":
        wb.open_new('https://lemagdusenior.ouest-france.fr/dossier-587-bienfaits-prunes-sante.html#:~:text=Les%20fibres%20alimentaires%20contenues%20dans,prolifération%20de%20certaines%20cellules%20cancéreuses.')
    elif resultOfSearchBar == "cerise":
        wb.open_new('https://www.santemagazine.fr/alimentation/aliments-et-sante/fruits/8-bienfaits-de-la-cerise-337039')
    elif resultOfSearchBar == "pamplemousse":
        wb.open_new('https://www.passeportsante.net/fr/Solutions/PlantesSupplements/Fiche.aspx?doc=pamplemousse_ps#:~:text=Il%20est%20riche%20en%20vitamine,d%27eau%20et%20de%20fibres.')
    elif resultOfSearchBar == "clémentine":
        wb.open_new('https://www.santemagazine.fr/alimentation/aliments-et-sante/fruits/la-clementine-un-fruit-qui-a-la-peche-430477#:~:text=Ce%20petit%20agrume%20fournit%20regorge,fer%20nécessaire%20aux%20globules%20rouges.')
    elif resultOfSearchBar == "orange":
        wb.open_new('https://lemagdusenior.ouest-france.fr/dossier-810-bienfaits-orange-sante.html#:~:text=Grâce%20à%20tous%20les%20bienfaits,seniors%20peuvent%20souffrir%20plus%20souvent.')
    elif resultOfSearchBar == "citron":
        wb.open_new('https://www.la-vie-naturelle.com/blog/post/bienfaits-citron#:~:text=Le%20citron%20est%20notamment%20connu,et%20en%20particulier%20le%20foie.')
    elif resultOfSearchBar == "lime":
        wb.open_new('https://www.noovomoi.ca/cuisiner/aliments/lime.html#:~:text=Bienfaits%20pour%20la%20santé&text=La%20lime%20est%20une%20excellente,de%20cuivre%20et%20de%20fer.')
    elif resultOfSearchBar == "banane":
        wb.open_new('https://www.maxdegenie.com/conseils-et-astuces/les-bienfaits-des-bananes-murissement-et-conservation/#:~:text=Avec%20sa%20teneur%20en%20glucides,et%20pour%20limiter%20la%20fatigue.')
    elif resultOfSearchBar == "grenade":
        wb.open_new('https://www.lepoint.fr/sante/grenade-elle-merite-d-etre-consommee-au-naturel-plutot-qu-en-sirop-23-07-2011-1355479_40.php#:~:text=La%20grenade%20est%20l%27un,de%20prévenir%20les%20maladies%20cardiovasculaires.')
    else:
        print("Console log : choix incorrect")

def pommeSetup():
    
    window.iconbitmap("appSntFruiT/medias/pomme.ico")
    window.configure(bg="#CF0033")

    mainFrame.configure(bg="#CF0033")
    Title.configure(bg="#CF0033")
    firstUnderTitile.configure(bg="#CF0033")
    fsecondUnderTitile.configure(bg="#CF0033")
    readMeInfo.configure(bg="#CF0033")

    searchButtonOfGeneralLink.configure(bg="#460000")
    searchButtonOfFruitLink.configure(bg="#460000")

    pommeThemeButton.configure(bg="#460000")
    poireThemeButton.configure(bg="#335600")
    melonThemeButton.configure(bg="#DF9900")

    searchButtonOfGeneralLink.configure(activebackground="#CF0033")
    searchButtonOfFruitLink.configure(activebackground="#CF0033")

    pommeThemeButton.configure(activebackground="#CF0033")
    poireThemeButton.configure(activebackground="#66CC66")
    melonThemeButton.configure(activebackground="#335600")

    Title.configure(fg="#460000")
    firstUnderTitile.configure(fg="#460000")
    fsecondUnderTitile.configure(fg="#460000")
    readMeInfo.configure(fg="#460000")

    print("Console log : theme pomme activé")

def poireSetup():

    window.iconbitmap("appSntFruiT/medias/poire.ico")
    window.configure(bg="#66CC66")

    mainFrame.configure(bg="#66CC66")
    Title.configure(bg="#66CC66")
    firstUnderTitile.configure(bg="#66CC66")
    fsecondUnderTitile.configure(bg="#66CC66")
    readMeInfo.configure(bg="#66CC66")

    searchButtonOfGeneralLink.configure(bg="#335600")
    searchButtonOfFruitLink.configure(bg="#335600")

    poireThemeButton.configure(bg="#335600")
    pommeThemeButton.configure(bg="#460000")
    melonThemeButton.configure(bg="#DF9900")

    searchButtonOfGeneralLink.configure(activebackground="#66CC66")
    searchButtonOfFruitLink.configure(activebackground="#66CC66")

    poireThemeButton.configure(activebackground="#66CC66")
    pommeThemeButton.configure(activebackground="#CF0033")
    melonThemeButton.configure(activebackground="#335600")
    

    Title.configure(fg="#335600")
    firstUnderTitile.configure(fg="#335600")
    fsecondUnderTitile.configure(fg="#335600")
    readMeInfo.configure(fg="#335600")

    print("Console log : theme poire activé")

def melonSetup():

    window.iconbitmap("appSntFruiT/medias/melon.ico")
    window.configure(bg="#DF9900")

    mainFrame.configure(bg="#DF9900")
    Title.configure(bg="#DF9900")
    firstUnderTitile.configure(bg="#DF9900")
    fsecondUnderTitile.configure(bg="#DF9900")
    readMeInfo.configure(bg="#DF9900")

    searchButtonOfGeneralLink.configure(bg="#335600")
    searchButtonOfFruitLink.configure(bg="#335600")

    melonThemeButton.configure(bg="#DF9900")
    poireThemeButton.configure(bg="#335600")
    pommeThemeButton.configure(bg="#460000")

    searchButtonOfGeneralLink.configure(activebackground="#DF9900")
    searchButtonOfFruitLink.configure(activebackground="#DF9900")

    poireThemeButton.configure(activebackground="#DF9900")
    pommeThemeButton.configure(activebackground="#CF0033")
    melonThemeButton.configure(activebackground="#335600")

    Title.configure(fg="#335600")
    firstUnderTitile.configure(fg="#335600")
    fsecondUnderTitile.configure(fg="#335600")
    readMeInfo.configure(fg="#335600")

    print("Console log : theme melon activé")

window = Tk()
window.title("FruiT")
window.geometry("720x480")
window.minsize(720,480)
window.maxsize(720,480)
window.overrideredirect(0)

mainFrame = Frame(window)
Title = Label(mainFrame, text = "Bienvenue sur FruiT", font=("Courrier", 40))
firstUnderTitile = Label(mainFrame, text="Pour obtenir des informations concernant les fruits,", font=("Courrier", 20))
fsecondUnderTitile = Label(mainFrame, text="tapez un nom de fruit !", font=("Courrier", 20))
readMeInfo = Label(window, text="Infos de l'application dans le 'README.md' : app crée par Sonn Hugo ; Tolotti Keelan ; Olzack Maxime ; Steiner Lucie ; Paul Louis", font=("Courrier", 9))

searchBar = Entry(window, width=40, )
searchImage = PhotoImage(file='appSntFruiT/medias/search.png')
searchButtonOfGeneralLink = Button(window, text="Les bienfaits des fruits",command=lambda:switchModeGeneralLink())
searchButtonOfFruitLink = Button(window, text="Les bienfaits du fruit",command=lambda:switchModeFruitlLink())

pommeThemeFile = PhotoImage(file="appSntFruiT/medias/pomme.png")
pommeThemeButton = Button(window, image=pommeThemeFile,command=lambda:pommeSetup())
poireThemeFile = PhotoImage(file="appSntFruiT/medias/poire.png")
poireThemeButton = Button(window, image=poireThemeFile,command=lambda:poireSetup())
melonThemeFile = PhotoImage(file="appSntFruit/medias/melon.png")
melonThemeButton = Button(window, image=melonThemeFile,command=lambda:melonSetup())

mainFrame.pack(side=TOP)
Title.pack()
firstUnderTitile.pack()
fsecondUnderTitile.pack()

searchBar.place(relx=0.5, rely=0.45, anchor=CENTER)
searchButtonOfGeneralLink.place(relx=0.4, rely=0.52, anchor=CENTER)
searchButtonOfFruitLink.place(relx=0.607, rely=0.52, anchor=CENTER)

pommeThemeButton.place(relx = 0.1, rely = 0.9,anchor=CENTER)
poireThemeButton.place(relx = 0.9, rely = 0.9,anchor=CENTER)
melonThemeButton.place(relx = 0.5, rely = 0.9,anchor=CENTER)

readMeInfo.place(relx=0.5, rely=0.96, anchor=CENTER)

pommeSetup()
windowIsActive()