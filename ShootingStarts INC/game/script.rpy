image alex = ("Alex.png")
image joshuaformal = ("Joshuaformal.png")
image elizabeth = ("Elizabeth.png")
image sam1 = ("Sam1.png")
image sam2 = ("Sam2.png")
image sam3 = ("Sam3.png")
image alicem = ("alice.png")
image cameron = ("cameron.png")
image joshua = ("joshua.png")
image nicky = ("nickie.png")
image susie = ("susie.png")

#bgs

image livingroomcouch = ("livingroomcouch.png")
image livingroomtv = ("livingroomtv.png")

define josh = Character("Joshua", image="joshuaformal.png")
define alex = Character("Alex", image="Alex.png")
define elizabeth = Character("Elizabeth", image="Elizabeth.png")
define sam = Character("Sam", image="Sam1.png")
define nicky = ("Nicky")
define t = ("test")
define who = ("???")
transform moveright:
    linear 0.3 xpos 0.80

transform pop:
    linear 0.2 yoffset -150
    linear 0.1 yoffset 0
transform zoomin:
    zoom 1.0
    linear 0.2 zoom 1.2
transform zoomout:
    zoom 1.2
    linear 0.2 zoom 1.0


# The game starts here.

label start:




    show joshua
    josh "My name is Joshua west. I am 11 years old."
    josh "I don't have a father and instead spend my days with my mom and babysitter, Nicky."
    josh "My Mom works as a ballet dancer in NYC. By the time she's done working, I'm already fast asleep."
    josh "Except on wednesdays, where the theater closes early."
    josh "Then, I'm allowed to go. I usually bring my sketchbook and draw my Mom in her dresses."
    show nicky:
        xalign 0.5
        linear 0.3 xpos 0.85
    nicky "Joshua! You ready to get in the car? It's almost time to see your mother perform."
    josh "Yeah, just a sec!"
    show nicky:
        linear 0.2 yoffset -150
        linear 0.1 yoffset 0
    nicky "Actually, today your mother has a singing role today. The theater is trying to produce musicals on top of it's ballet."
    hide nicky
    hide joshua
    "We finnaly arrived at the theater and took our seats."
    who "Ladies and gentlemen! Do we have a doozey for you tonight!"
    who "Tonight, giving our theaters first ever vocal performance..."
    who "Elizabeth...{p}West!"
    "I watched everyone perform and my mother sing. Sketbook in hand, drawing everyones outfits. Even from here, I could faintly see my mothers strawberry-shaped birthmark."
    "Finnaly, {p} mom came up to us after changing her outfit backstage."
    show joshua:
        xalign 0.1
    show elizabeth
    elizabeth "Alright. Nicky, can you drive me home?"

    show nicky:
        xalign 0.100
        linear 0.3 xpos 0.85
        linear 0.3 yoffset -150
        linear 0.3 yoffset 0
    nicky "yup"



    "She adjusts her gaze to meet mine."
    elizabeth "Right, {p} right."
    elizabeth "Did you enjoy the show honey?"
    menu:
       "yes":
        elizabeth "Good, I'm glad."
       "no":
        elizabeth "...{p}...{p}..."
    elizabeth "Come now Joshua, let's get home. It's time for bed."
    hide elizabeth
    hide joshua
    hide nicky
    "After we got home I lied down for bed and began to shut my eyes..."
    "And then a loud thud jolted me out of sleep."
    "I peered through my creeked open door..."
    "And I saw my mother picking up a box of photo's and other memories. Mom goes through them with me every now and then."
    "Usually, each box is labeled. But this one...{p}This one is scribled out."
    "I can't exactly make out the numbers.{p} All that I can make out is '19'."
    "I'll...{p}I'll look tommorow."
    "I need my sleep now."
    show nicky
    nicky "Joshua. Get up."
    show josh:
        xalign 0.1
        yoffset 50
    josh "I'm up I'm up."
    nicky "okay...I gotta go do something. {p} You, behave."
    show joshua:
        yoffset 0
    "i knew then was my chance to look through the photos..."
    hide joshua
    "So, I walked into my mother's room and found the box whoms date was scribbled out."
