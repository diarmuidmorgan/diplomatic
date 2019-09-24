Add ideas here

> make nodes, connect them up
> get all countries and sea areas connected up as in the diplomacy game map
> add simple rules for resolving country captures e.g attack/defend/support


Build skynet, **by accident**

Fun with operator overloading in little_world.py!
Example Worldbuilding with little_world.py:

from little_world import Walker, Country
england = Country("England")
scotland = Country("Scotland")
ireland = Country("Ireland")
england + ireland
england + scotland
ireland + scotland

diarmuid = Walker("Diarmuid")
kevin = Walker("Kevin")

diarmuid + kevin
diarmuid + ireland
kevin + ireland

print("at this point, the countries are connected and diarmuid and kevin are living happily in ireland")

diarmuid.step()

diarmuid.home[0].name
kevin.home[0].name
print("diarmuid moved away! traitor")
