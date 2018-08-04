#-*- coding:utf-8 -*-

#颜色值转换
def ToColor(r, g, b, a, base=255):
    r = r * 1.0 / base
    g = g * 1.0 / base
    b = b * 1.0 / base 
    a = a * 1.0 / base 

    color = (
        BorderValue(r, 0, 1),
        BorderValue(g, 0, 1),
        BorderValue(b, 0, 1),
        BorderValue(a, 0, 1),
    )

    print "ToColor:", color
    return color

#数值边界规范
def BorderValue(v, min, max):
    if v < min:
        return min 
    elif v > max:
        return max 
    return v