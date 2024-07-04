counter = 1
while True:
    #value error
    try:
        age = int(input("yaşınızı giriniz: "))
        #print(age + "yasındasınız") #python bunu toplayamaz hata type error

        income = 2000
        risk = income / age 
        # yaş=0 yazıldığında 0 a bölünme hatası alınır zeroDivisionError
        print(f"Risk puanınız {risk}'dir.")

    except ValueError:
        print("yanlış değer girdiniz")

    except TypeError:
        print("bir hata oluştu")

    except ZeroDivisionError:
        print("yaşınızı 0 harici bir değer giriniz")

    except Exception as exceptionObject:
        print("bir hata oluştu:", exceptionObject)
        #gelen hatasının sebebini bilmediğimizde kontrol ederiz

    else: #hata alınmazsa bu blok çalışır
        print(f"{age:.4} yasındasınız")
        break

    finally: 
        #hata alsın veya almazsın bu kod bloğu çalışır
        #dosyayı kapatmayı buraya yazarız
        print(f"döngü {counter} defa çalıştı")
        counter +=1
        if counter > 10:
            #print("çok fazla deneme yapıldı")
            #break
            raise ValueError("çok fazla deneme yapıldı") #hata üretmek

        #koşul true değilse raise olur
        assert (counter <= 10), "çok fazla deneme yapıldı" #false olunca essert çalışır raised verir


#with exit code 0 : kodun doğru çalıştığını gösterir 1 olması hatalı olduğu anlamına gelir
