import Obbiettivo as obj
import Attivita as act


o1 = obj.Obbiettivo("Core", 3, 5, ["test1", "test2"])
o2 = obj.Obbiettivo("Gambe", 4, 2, ["test3", "test4"])
#print(o1.__str__())
a1 = act.Attivita("test", ["storica", "open"], 3, 3, 1,
                  5,[o1,o2],"ipsum lorem")
print(a1.__str__())
