

fox = "WHAT DOES THE FOX SAY?\n"


def generic_ring_lyric(ring):
    for i in range(3):
        ring = ring + "ding "
    ring = ring + "dingeringeding"
    return ring

def pow_lyric():
    pow = "Wa "
    for i in range(5):
        pow = pow + "pa "
    pow = pow + "pow!"
    return pow

def pow_lyric_multi(num_lines):
    pow = ""
    for i in range(num_lines):
        pow = pow + "Wa "
        for i in range(5):
            pow = pow + "pa "
        pow = pow + "pow!\n"
    return pow


print("Dog goes woof, cat goes meow.")
print("Bird goes tweet, and mouse goes squeak.")
print("Cow goes moo. Frog goes croak, and the elephant goes toot.")
print("Ducks say quack and fish go blub, and the seal goes OW OW OW.")
print("But there's one sound that no one knows...")
print(fox)
print(generic_ring_lyric("Ring "))
print(generic_ring_lyric("Gering "))
print(generic_ring_lyric("Gering "))
print(fox)

print(pow_lyric())
print(pow_lyric())
print(pow_lyric())