import omg, sys

differ = False

def dataEqual(da,db):
    abytenum = len(da)
    bbytenum = len(db)
    if abytenum != bbytenum:
        return False
    else:
        for bval in range(abytenum):
            if da[bval] != db[bval]:
                return False
    return True

def diffDetected(s):
    global differ
    differ = True
    print(s)

if (len(sys.argv) < 3):
    print("\n    waddiff script: diff WADs\n")
    print("    Usage:")
    print("    waddiff.py input1.wad input2.wad\n")
else:
    wa = sys.argv[1]
    wb = sys.argv[2]
    a = omg.WAD(wa)
    b = omg.WAD(wb)
    differ = False
    if len(omg.WadIO(wa).entries) != len(omg.WadIO(wb).entries):
        diffDetected("Warning: Lump counts differ between the WADs.")

    for i in range(len(a.groups)):
        if len(a.groups[i]) > 0 and len(b.groups[i]) > 0:
            tocheck = []
            for x in a.groups[i]:
                if x not in b.groups[i]:
                    diffDetected(f"Lump {x} is in {wa} but not in {wb}")
                else:
                    tocheck.append(x)
            for x in b.groups[i]:
                if x not in tocheck:
                    diffDetected(f"Lump {x} is in {wb} but not in {wa}")
            for x in tocheck:
                # some are lumps, some are groups
                if isinstance(a.groups[i][x], dict):
                    # should function this but don't want to right now
                    tocheck2 = []
                    for y in a.groups[i][x]:
                        if y not in b.groups[i][x]:
                            diffDetected(f"Lump {y} within {x} is in {wa} but not in {wb}")
                        else:
                            tocheck2.append(y)
                    for y in b.groups[i][x]:
                        if y not in a.groups[i][x]:
                            diffDetected(f"Lump {y} within {x} is in {wb} but not in {wa}")
                    for y in tocheck2:
                        if not dataEqual(a.groups[i][x][y].data, b.groups[i][x][y].data):
                            diffDetected(f"Lump {y} within {x} differs between {wa} and {wb}")
                elif not dataEqual(a.groups[i][x].data, b.groups[i][x].data):
                    diffDetected(f"Lump {x} differs between {wa} and {wb}")

        elif len(a.groups[i]) == 0 and len(b.groups[i]) == 0:
            continue
        elif len(a.groups[i]) == 0:
            diffDetected(f"Lump category \'{a.groups[i]._name}\' does not exist in {wa} but exists in {wb}")
        else:
            diffDetected(f"Lump category \'{a.groups[i]._name}\' does not exist in {wb} but exists in {wa}")
sys.exit(differ)
