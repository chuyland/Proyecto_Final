import random

class Movie:   #Define la película

    def __init__(self,title):
        self.rank = random.randint(50,100)
        self.title = title 
        print("La película " + self.title + " ha sido evaluada por la crítica con un " + str(self.rank))

    def new_rank(self):
        return(str(self.rank))

    def get_title(self):
        return(str(self.title))

    def dislike(self):
            self.rank -= 1
            print("La nueva calificación de", self.title, " es ", self.rank)


    def like(self):
            self.gasolina +=1
            print("La nueva calificación de", self.title, " es ", self.rank)


tit = Movie("Titanic")
psi = Movie("Psicosis")
her = Movie("Her")
kan = Movie("Citizen kane")
ave = Movie("Avengers")
shi = Movie("The Shining")
mid = Movie("Midnight in Paris")
dja = Movie("Django")
bud = Movie("Budapest Hotel")
ver = Movie("Vertigo")

tit.new_rank()
psi.new_rank()
her.new_rank()
kan.new_rank()
ave.new_rank()
shi.new_rank()
mid.new_rank()
dja.new_rank()
bud.new_rank()
ver.new_rank()


