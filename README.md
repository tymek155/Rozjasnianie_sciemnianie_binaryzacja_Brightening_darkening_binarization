Go to [English version](#english-version)
# Ogólne informacje
Projekt realizuje implementację prostej aplikacji służącej do przetwarzania 
obrazów w skali szarości. Możliwe są rozjaśnianie/ściemnianie obrazu o podaną 
wartość, rozjaśnianie procentowe, rozjaśnianie krokowe (o 10-20% w trzech krokach) 
oraz binaryzacja z progiem domyślnym (127) lub wybranym przez użytkownika (0-255).

# Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
* Pillow 11.0.0
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się 
z funkcji `save`, która zapisuje obecny stan obrazu do pliku i zwiększa licznik 
konieczny do prawidłowego zapisu, `rozjasnij_sciemnij` modyfikującej jasność o stałą 
wartość z ograniczeniem do zakresu 0-255, `rozjasnij_sciemnij_proc` zmieniającej 
jasność procentowo, `binaryzacja` konwertującej obraz do skali szarości, bazując 
na progu oraz `main`, która służy do obsługi ogólnej logiki programu, umożliwia 
testowanie różnych funkcji oraz odpowiada za interakcję z użytkownikiem.

## Oryginalne zdjęcie w skali szarości
![image](https://github.com/user-attachments/assets/0e9e27b3-b7d8-4857-847b-e65ce6ce8259)
## Zdjęcie przyciemnione o 50%
![image](https://github.com/user-attachments/assets/819cb519-98c0-4130-910d-958fca56f16a)
## Seria 3 zdjęć rozjaśnianych o 15%
<img width="740" alt="image" src="https://github.com/user-attachments/assets/47f75d49-d703-42ba-8ed6-a7e2687a9b00" />

## Zdjęcie zbinaryzowane ze standardowym progiem 127
![image](https://github.com/user-attachments/assets/ac83f531-cc16-40db-afd2-da92eec51e16)


# English version

# General Information  
The project implements a simple application for processing grayscale images. 
Possible operations include brightening/darkening the image by a specified value, 
percentage-based brightening, stepwise brightening (10-20% in three steps), 
and binarization with a default threshold (127) or a user-selected threshold 
(0-255).

# Technologies  
The code uses:  
* Python 3.12
* NumPy 2.2.2
* Pillow 11.0.0

# Usage
The code was run and written in the PyCharm environment. The code structure 
consists of the `save` function, which saves the current image state to a file 
and increments the counter necessary for proper saving, `rozjasnij_sciemnij` 
modifying brightness by a constant value with a 0-255 range limit, 
`rozjasnij_sciemnij_proc` changing brightness percentage-based, `binaryzacja` 
converting the image to grayscale based on a threshold, and `main`, which handles 
the general program logic, enables testing various functions, and is responsible 
for user interaction.  

## Original grayscale photo
![image](https://github.com/user-attachments/assets/0e9e27b3-b7d8-4857-847b-e65ce6ce8259)
## Photo darkened by 50%
![image](https://github.com/user-attachments/assets/819cb519-98c0-4130-910d-958fca56f16a)
## Series of 3 photos brightened by 15%
<img width="740" alt="image" src="https://github.com/user-attachments/assets/47f75d49-d703-42ba-8ed6-a7e2687a9b00" />

## Binarized image with standard threshold 127
![image](https://github.com/user-attachments/assets/ac83f531-cc16-40db-afd2-da92eec51e16)
