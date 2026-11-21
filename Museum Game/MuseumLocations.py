#Holds the museum locations as well as the clues found in each

from Locations import location

Driveway = Location(
    "Driveway",
    "The area right behind the art gallary, it is easy for artists to unload there artwork here",
    {
        "clue1" : "There seem to be some paint brushes on the ground here",
        "clue2" : "There are fresh tire tracks, so someone was just here and it seems like they left in a rush",
        "clue3" : "The only camera back here is broken, so the thief must have known that"
    }
)

GallarySpace = Location(
    "Gallary Space",
    "The area where the painting was hanging prior to the theif that occured",
    {
        "clue1" : ""
        "clue2" : ""
        "clue3" : "There seems to be some broken glass and some small screws, the look like something from a watch"
    }
)

Lobby = Location(
    "Lobby",
    "This is the first area any patron enters when comming into the mueseum, there is also a security desk here",
    {
        "clue1" : "It seems Jason may have left his keys on the desk during all the commotion",
        "clue2" : "",
        "clue3" : ""
    }
)

Cafe = Location(
    "Cafe",
    "This is where Sam works, there is always a huge line beccause they have some of the best coffee in town"
    {
        "clue1" : "",
        "clue2" : "",
        "clue3" : "The register seems to have been closed out at 9pm"
    }    
)

StorageRoom = location(
    "Storage Room",
    "This is where any artwork is stored before it can be put on display only curators and security gaurds have access to the room"
    {
        "clue1" : "",
        "clue2" : "",
        "clue3" : ""
    }
)

SecurityOffice = location(
    "Security Office",
    "This is where the security gaurd's store their equipment and where all of the camera servers are located, the only person with a key to this room is the Security Guard Jason"
    {
        "clue1" : "There is an ",
        "clue2" : "The lock for this office seems to be working properly",
        "clue3" : ""
    }
)