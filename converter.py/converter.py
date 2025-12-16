# Файл: color_converter.py
# Автор: Акоманинг
# Это файл является частью проекта "hello engineer"

def rgb_to_hex(r, g, b):
    """
    Конвертирует значения RGB (0-255) в HEX-строку
    """
    return f"#{r:02X}{g:02X}{b:02X}"

def main():
    print("Конвертер RGB в HEX")
    print("===================")
    
    try:
        r = int(input("Введите R (0-255): "))
        g = int(input("Введите G (0-255): "))
        b = int(input("Введите B (0-255): "))
        
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Ошибка: значения должны быть в диапазоне 0-255")
            return
        
        hex_color = rgb_to_hex(r, g, b)
        print(f"\nRGB({r}, {g}, {b})")
        print(f"HEX: {hex_color}")
        
        # Дополнительно: покажем представление в других системах
        print(f"\nДополнительно:")
        print(f"R = {r} DEC, {bin(r)} BIN, {hex(r)} HEX")
        print(f"G = {g} DEC, {bin(g)} BIN, {hex(g)} HEX")
        print(f"B = {b} DEC, {bin(b)} BIN, {hex(b)} HEX")
        
    except ValueError:
        print("Ошибка: введите целые числа")

if __name__ == "__main__":
    main()