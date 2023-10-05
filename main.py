import Obbiettivo as obj
import Attivita as act


o1 = obj.Obbiettivo("Core", 3, 5, ["test1", "test2"])
print(o1.__str__())
a1 = act.Attivita("test", ["storica", "open"], 3, 3, 1,
                  5,o1,"ipsum lorem")
print(a1.__str__())
