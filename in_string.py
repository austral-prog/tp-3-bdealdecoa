def check_vowels():
    txt = input("> ") 
    
    print("Contiene a:", any(c in txt for c in ("a", "A")))
    print("Contiene e:", any(c in txt for c in ("e", "E")))
    print("Contiene i:", any(c in txt for c in ("i", "I")))
    print("Contiene o:", any(c in txt for c in ("o", "O")))
    print("Contiene u:", any(c in txt for c in ("u", "U")),"\n")
    
    Txt = input("> ") 
    
    print("Contiene a:", any(c in Txt for c in ("a", "A")))
    print("Contiene e:", any(c in Txt for c in ("e", "E")))
    print("Contiene i:", any(c in Txt for c in ("i", "I")))
    print("Contiene o:", any(c in Txt for c in ("o", "O")))
    print("Contiene u:", any(c in Txt for c in ("u", "U")))


    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
