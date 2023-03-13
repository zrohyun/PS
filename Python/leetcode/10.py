def isMatch(s: str, p: str) -> bool:
    p_preced = ""
    s_preced = ""
    while s and p:
        # left pop from str
        c1, *s = s
        c2, *p = p

        if c2 == ".":  # matches any single character
            pass

        elif c2 == "*" and p_preced == ".":  # all matching with any character
            while s:
                c1, *s = s

        elif c2 == "*":  # matches zero or more of the preceding element

            if s_preced != p_preced:  # zero matching
                s = [c1] + s
            else:  # one or more matching
                if c1 == p_preced:
                    while s:
                        c1, *s = s
                        if c1 != p_preced:
                            s = [c1] + s
                            break
                else:
                    s = [c1] + s
            continue

        s_preced = c1
        p_preced = c2

    if s == p:
        return True

    return False


print(isMatch("missisipi", "mis*is*p*."))
