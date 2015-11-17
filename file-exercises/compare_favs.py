pk_fav_foods = open("pk_fav_foods.txt")
pk_fav = pk_fav_foods.read()
pk_fav_foods.close()


kp_fav_foods = open("kp_fav_foods.txt")
kp_fav = kp_fav_foods.read()
kp_fav_foods.close()

our_favs = "pk_fav_foods" and "kp_fav_foods"

def compare_favs(pk_fav, kp_fav):
    if pk_fav == kp_fav:
        return True
    else:
        return False

if compare_favs:
    print "Our favorite foods are the same"
else:
    print "Our favorite foods are different"
