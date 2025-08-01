from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def home(response):
     genres = ['Action','Rommance','Japaness']
     books =  [
        {'title': 'Naruto', 'image': 'naruto.jpg', 'likes': 3245},
        {'title': 'One Piece', 'image': 'onepiece.jpg', 'likes': 4521},
        {'title': 'Death Note', 'image': 'deathnote.jpg', 'likes': 3789},
        {'title': 'Attack on Titan', 'image': 'aot.jpg', 'likes': 2890}, ]
     
     return render(response,'comics/home.html',{'genres':genres,'books':books})

def genre(response):
    genres = ['Action', 'Romance', 'Comedy', 'Horror','Japaness','Korean','American','SuperHero','Fantacy']
    comics = [
        {'title': 'Naruto', 'image': 'naruto.jpg', 'likes': 3245},
        {'title': 'One Piece', 'image': 'onepiece.jpg', 'likes': 4521},
        {'title': 'Death Note', 'image': 'deathnote.jpg', 'likes': 3789},
        {'title': 'Attack on Titan', 'image': 'aot.jpg', 'likes': 2890},
     {'title': 'Naruto', 'image': 'naruto.jpg', 'likes': 3245},
    {'title': 'One Piece', 'image': 'onepiece.jpg', 'likes': 4521},
    {'title': 'Death Note', 'image': 'deathnote.jpg', 'likes': 3789},
    {'title': 'Attack on Titan', 'image': 'aot.jpg', 'likes': 2890},
    {'title': 'Bleach', 'image': 'bleach.jpg', 'likes': 3190},
    {'title': 'Demon Slayer', 'image': 'demonslayer.jpg', 'likes': 5111},
    {'title': 'My Hero Academia', 'image': 'mha.jpg', 'likes': 2899},
    {'title': 'Tokyo Ghoul', 'image': 'tokyoghoul.jpg', 'likes': 2754},
    {'title': 'Jujutsu Kaisen', 'image': 'jjk.jpg', 'likes': 3433},
    {'title': 'Dragon Ball Z', 'image': 'dbz.jpg', 'likes': 4123},
    {'title': 'Chainsaw Man', 'image': 'chainsawman.jpg', 'likes': 2356},
    {'title': 'Black Clover', 'image': 'blackclover.jpg', 'likes': 2987},
    {'title': 'Fairy Tail', 'image': 'fairytail.jpg', 'likes': 3210},
    {'title': 'Boruto', 'image': 'boruto.jpg', 'likes': 2675},
    {'title': 'Mob Psycho 100', 'image': 'mobpsycho.jpg', 'likes': 2103},
    {'title': 'Spy x Family', 'image': 'spyxfamily.jpg', 'likes': 3782},
    {'title': 'Hunter x Hunter', 'image': 'hxh.jpg', 'likes': 4582},
    {'title': 'Vinland Saga', 'image': 'vinlandsaga.jpg', 'likes': 2489},
    {'title': 'Fullmetal Alchemist', 'image': 'fma.jpg', 'likes': 4890},
    {'title': 'Blue Lock', 'image': 'bluelock.jpg', 'likes': 2945},
    {'title': 'One Punch Man', 'image': 'opm.jpg', 'likes': 4120},
    {'title': 'Erased', 'image': 'erased.jpg', 'likes': 1645},
    {'title': 'Berserk', 'image': 'berserk.jpg', 'likes': 5231},
    {'title': 'The Promised Neverland', 'image': 'tpn.jpg', 'likes': 2590},
    {'title': 'Noragami', 'image': 'noragami.jpg', 'likes': 1987},
    {'title': 'Re:Zero', 'image': 'rezero.jpg', 'likes': 2743},
    {'title': 'Sword Art Online', 'image': 'sao.jpg', 'likes': 3200},
    {'title': 'Dr. Stone', 'image': 'drstone.jpg', 'likes': 2820},
    {'title': 'Akame ga Kill', 'image': 'akamegakill.jpg', 'likes': 2390},
    {'title': 'Fire Force', 'image': 'fireforce.jpg', 'likes': 2112},
    {'title': 'Haikyuu!!', 'image': 'haikyuu.jpg', 'likes': 3650},
    {'title': 'Ao Haru Ride', 'image': 'aoharuride.jpg', 'likes': 1340},
    {'title': 'Horimiya', 'image': 'horimiya.jpg', 'likes': 1567},
    {'title': 'Love is War', 'image': 'kaguyasama.jpg', 'likes': 2034},
    {'title': 'Yona of the Dawn', 'image': 'yona.jpg', 'likes': 1976},
    {'title': 'Seraph of the End', 'image': 'seraph.jpg', 'likes': 1623},
    {'title': 'Beastars', 'image': 'beastars.jpg', 'likes': 2100},
    {'title': 'Claymore', 'image': 'claymore.jpg', 'likes': 1983},
    {'title': 'Gintama', 'image': 'gintama.jpg', 'likes': 4550},
    {'title': 'D.Gray-man', 'image': 'dgrayman.jpg', 'likes': 2671},
    {'title': 'Zom 100', 'image': 'zom100.jpg', 'likes': 1465},
    {'title': 'JoJo’s Bizarre Adventure', 'image': 'jojo.jpg', 'likes': 4700},
    {'title': 'Steins;Gate', 'image': 'steinsgate.jpg', 'likes': 2090},
    {'title': 'Parasyte', 'image': 'parasyte.jpg', 'likes': 1892},
    {'title': 'Made in Abyss', 'image': 'abyss.jpg', 'likes': 1740},
    {'title': 'Hellsing', 'image': 'hellsing.jpg', 'likes': 1532},
    {'title': 'The Rising of the Shield Hero', 'image': 'shieldhero.jpg', 'likes': 2421},
    {'title': 'Bungou Stray Dogs', 'image': 'bungou.jpg', 'likes': 2764},
    {'title': 'Ergo Proxy', 'image': 'ergoproxy.jpg', 'likes': 1100},
    {'title': 'Great Teacher Onizuka', 'image': 'gto.jpg', 'likes': 2645},
    {'title': 'Kaiji', 'image': 'kaiji.jpg', 'likes': 1253},
    {'title': 'Monster', 'image': 'monster.jpg', 'likes': 3452},
    {'title': 'Fruits Basket', 'image': 'fruitsbasket.jpg', 'likes': 1982},
    {'title': 'Inuyasha', 'image': 'inuyasha.jpg', 'likes': 2234},
    {'title': 'Trinity Seven', 'image': 'trinityseven.jpg', 'likes': 1765},
    {'title': 'No Game No Life', 'image': 'ngnl.jpg', 'likes': 2022},
    {'title': 'The Seven Deadly Sins', 'image': '7ds.jpg', 'likes': 2934},
    {'title': 'Soul Eater', 'image': 'souleater.jpg', 'likes': 2345},
    {'title': 'Elfen Lied', 'image': 'elfenlied.jpg', 'likes': 1876},
    {'title': 'Toradora!', 'image': 'toradora.jpg', 'likes': 1503},
    {'title': 'Kill la Kill', 'image': 'killlakill.jpg', 'likes': 1666},
    {'title': 'Code Geass', 'image': 'codegeass.jpg', 'likes': 4211},
    {'title': 'Psycho-Pass', 'image': 'psychopass.jpg', 'likes': 2789},
    {'title': 'Charlotte', 'image': 'charlotte.jpg', 'likes': 1988},
    {'title': 'Clannad', 'image': 'clannad.jpg', 'likes': 3001},
    {'title': 'Your Lie in April', 'image': 'yourlie.jpg', 'likes': 3500},
    ]
    return render(response, 'comics/genre.html', {'genres': genres, 'books': comics})



def about(response):     
     return render(response,'comics/AboutPage.html',{})

def book(response,name):

    config = {
         'book_name':name
    }
    return render(response,'comics/specificBook.html',config)


