pk_fav_foods = open("pk_fav_foods.txt")
pk_fav = pk_fav_foods.readlines()
pk_fav_foods.close()


kp_fav_foods = open("kp_fav_foods.txt")
kp_fav = kp_fav_foods.readlines()
kp_fav_foods.close()

our_favs = "pk_fav_foods" and "kp_fav_foods"

def compare_favs(pk_fav, kp_fav):
    return pk_fav[0] == kp_fav[0]

if ("compare_favs" == True):
    print "Our favorite foods are the same"
else:
    print "Our favorite foods are different"

def compare_favs2(pk_fav, kp_fav):
    for x in kp_fav:
        if x in pk_fav:
            print "We both love",x

compare_favs2(pk_fav, kp_fav)