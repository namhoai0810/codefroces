name_gest = input()
name_home = input()
name_untidy = input()
if(sorted(name_home + name_gest) == sorted(name_untidy)):
    print("YES")
else:
    print("NO")