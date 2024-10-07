# The if/else statement executes a block of code if a specified condition is true
# If the condition is false, another block of code can be executed

print("You, a curious adventurer named Arin, are wandering through an ancient forest when you stumble upon a strange, glowing artifact half-buried in the ground. As you approach, you hear a faint hum, and the artifact pulses with light. It's clear that this is no ordinary object.Would you like  PICK ,LEAVE or DESTROY the artifact? \n")
pick= "The moment Arin touches the artifact, a flash of light blinds them. When their vision clears, they find themselves transported to an otherworldly realm, filled with towering structures made of crystal and light. A voice speaks to them, revealing that the artifact is a key to unlocking ancient powers, but it also binds them to a dangerous destiny.Would you    EMBRACE THE POWER or SEEK A WAY OUT?"
embrace="Having embraced the artifact’s power, Arin becomes more attuned to the forces of the otherworld. They are hailed as a potential savior by some, but others view them as a threat. Soon, Arin must decide whether to use their newfound power to unite the realms or to dominate them."
seekout = "Arin, wary of the immense power the artifact offers, decides not to embrace it fully. Instead, they search for a way to return to their world. As they wander through the alien realm, they encounter strange, ethereal beings who seem to know about the artifact and its true nature. These beings warn Arin that while escape is possible, the artifact's influence has already bound itself to them, meaning that their departure could have dire consequences."
leave = "Arin hesitates as they stand over the glowing artifact. Something about it feels wrong. Instead of touching it, they decide to back away, their instincts telling them to leave it alone. But as they do, they can't shake the feeling that they need to understand what this artifact truly is before they leave it behind completely.Would you like to have a DISTANT WATCH or RUN?"
distantWatch= "Arin watches the artifact from afar, observing its behavior. Over time, strange creatures begin to emerge from the ground around it, as though drawn by its energy. Arin realizes the artifact may be a beacon for something far more dangerous."
run= "Panicking, Arin turns and runs as the world warps around them. Behind, the rupture expands, consuming everything in its path. They flee, desperate to escape the chaos, but the fracture between realms is closing in fast."
destroy = "Arin stands over the glowing artifact, unease gnawing at them. They can't shake the feeling that this object holds immense danger. Unable to leave it intact, Arin raises their weapon and smashes the artifact with all their strength. What happens next is far worse than they imagined.Would you like to FIND THE SOURCE or ESCAPE THE RUPTURE?"
findSource="Determined to fix what they’ve broken, Arin ventures deeper into the heart of the rupture, moving toward the epicenter of the disaster"
escaperupture="Panicked, Arin turns and flees, their mind racing as they try to put as much distance as possible between themselves and the growing rupture"

choice1 = input("choice : ").lower()
if choice1 == "pick":
    print(pick)
    choice2 = input("choice : ").lower()
    if choice2 == "embrace the power":
        print(embrace)
        print("\n")
        print("Sigined out")
    elif choice2 == "seek a way out":
        print(seekout)
        print("\n")
        print("Signed out")
    else:
        print("Please choose the correct option or check spelling")
    
elif choice1 == "leave":
    print(leave)
    choice3 = input("choice : ").lower()
    if choice3 == "distant watch":
        print(distantWatch)
        print("\n")
        print("Sigined out")
    elif choice3 == "run":
        print(run)
        print("\n")
        print("Signed out")
    else:
        print("Please choose the correct option or check spelling")
    
elif choice1 == "destroy":
    print(destroy)
    choice2 = input("choice : ").lower()
    if choice2 == "find the source":
        print(findSource)
        print("\n")
        print("Sigined out")
    elif choice2 == "escape the rupture":
        print(escaperupture)
        print("\n")
        print("Sigined out")
else:
    print("Please choose the correct option or check spelling")
