import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def get_data(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "cache-control": "no-cache",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(r.text)

    r = requests.get(
        "https://mc.yandex.ru/watch/34241905?wmode=7&page-url=https%3A%2F%2Fwww.avito.ru%2Fmoskva_i_mo%2Fchasy_i_ukrasheniya%2Fchasy-ASgBAgICAUTQAYYG&page-ref=https%3A%2F%2Fwww.avito.ru%2Fmoskva_i_mo%2Fchasy_i_ukrasheniya%2Fchasy-ASgBAgICAUTQAYYG%3Fcd%3D1%26q%3Dapple%2Bwatch%2Bse&charset=utf-8&browser-info=pv%3A1%3Avf%3Aynzjpe2ysmhyiw5vig54s%3Afp%3A1252%3Afu%3A0%3Aen%3Autf-8%3Ala%3Aru%3Av%3A933%3Acn%3A1%3Adp%3A0%3Als%3A957884211279%3Ahid%3A18746591%3Az%3A180%3Ai%3A20221205010204%3Aet%3A1670191324%3Ac%3A1%3Arn%3A890634051%3Arqn%3A514%3Au%3A1666270400532257957%3Aw%3A1260x979%3As%3A1920x1080x24%3Ask%3A1%3Awv%3A2%3Ads%3A2%2C17%2C800%2C85%2C1%2C0%2C%2C437%2C1%2C1819%2C1822%2C16%2C1346%3Aco%3A0%3Acpf%3A1%3Ans%3A1670191321943%3Aadb%3A1%3Afip%3A27310d81d8abf72408d19a5f3da1f977-1cc4db1a3d7b1837d6538ca6cabed338-a81f3b9bcdd80a361c14af38dc09b309-7950ec0297c12322859860922e071362-9adf115a84ff26f41e9d720bd31c1ffc-3ebafa6d1dc320dfc3933205199039e0-f029f500589792a0d5a0f159f332406e-4081b6d3e2740106a9c12283c2ec02b9-a81f3b9bcdd80a361c14af38dc09b309-442d4e5c08bab4e7c0516508afe0f400-4adab536de1f16d5439eaab9fc76e7a1%3Arqnl%3A1%3Ast%3A1670191324%3At%3A%D0%9A%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B5%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%20%D1%87%D0%B0%D1%81%D1%8B%20%E2%8C%9A%EF%B8%8F%20%D0%B2%C2%A0%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5%20%D0%B8%C2%A0%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8%20%D1%81%C2%A0%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%BE%D0%B9%20%7C%20%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5%20%D0%B8%C2%A0%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B5%20%D1%87%D0%B0%D1%81%D1%8B%20%7C%20%D0%90%D0%B2%D0%B8%D1%82%D0%BE&t=gdpr(14)clc(0-0-0)rqnt(1)aw(1)fip(1)ti(2)",
        headers=headers)
    print(r.text)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.find_all("div", class_="item")

    for item in items:
        itme = item.find("a").get("href")
        print(item)


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override",
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62")

    try:
        driver = webdriver.Firefox(
            service=Service(executable_path="C:\\Users\Slava\PycharmProjects\AvitoBuyBot\geckodriver.exe"),
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("index_selenium.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    items = soup.find_all("div",
                          class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")

    for item in items:
        date = item.find("div",
                         class_="date-text-KmWDf text-text-LurtD text-size-s-BxGpL text-color-noaccent-P1Rfs").get(
            "#text")
        item = "https://www.avito.ru" + item.find("a").get("href")
        print(item, date)


def main():
    # get_data("https://www.avito.ru/moskva_i_mo/chasy_i_ukrasheniya/chasy-ASgBAgICAUTQAYYG?cd=1&q=apple+watch+se&s=104")https://www.avito.ru/moskva_i_mo/chasy_i_ukrasheniya/chasy-ASgBAgICAUTQAYYG?cd=1&f=ASgBAgECAUTQAYYGAUXGmgwYeyJmcm9tIjo0MDAwLCJ0byI6MTQwMDB9&q=apple+watch+se&s=1TI2Dra6edtAq4vdEA2yJeutedGIbX0phK1724INeg
    get_data_with_selenium(
        "https://www.avito.ru/moskva_i_mo/avtomobili/vaz_lada/2107-ASgBAgICAkTgtg3GmSjitg3Omig?cd=1&s=104")


if __name__ == '__main__':
    main()
