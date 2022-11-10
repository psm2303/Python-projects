coded = "pbatenghyngvbaf, lbh fbyirq zl yhvtv chmmyr. @ zr ba gjvggre jvgu lbhe snibhevgr qrffreg gb trg lbhe erjneq. Vg'f yvxr, abg n irel tbbq erjneq fb hu"

base = ord("a")
for i in range(1, 26):
    out = ""
    for char in coded:
        # only transpose alphanumeric characters
        if 97 <= ord(char) <= 122:
            out += chr(base + (ord(char) + i - base) % 26)
        else:
            out += char
    print(i, out)
