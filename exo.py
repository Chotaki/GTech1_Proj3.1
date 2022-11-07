def add(x, y){
    return x + y
}

def sub(x, y){
    return x - y
}

def multiply(x, y){
    return x * y
}

def divide(x, y){
    return x / y
}

def modulo(x, y){
    return x % y
}

#calculer revenue par seconde sur 1 an (salaire/h, h/JourOuvrable - 5j/semaine, JO/an)

def revenuePerSecond(SH, Hjo, JOa){
    return JOa * Hjo * SH / 365 / 24 / 60 / 60
}

#convertir salaire brut en salaire net

def calculNet(SB, public){
    if public return SB * 15/100
    return SB * 23/100
}