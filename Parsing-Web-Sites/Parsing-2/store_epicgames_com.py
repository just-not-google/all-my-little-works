from epicstore_api import EpicGamesStoreAPI, EGSException, EGSNotFound

def parsing_store_epicgames_com(name_game):
    try:
        api = EpicGamesStoreAPI(locale="ru-RU", country="RU")
        exact_results = api.fetch_store_games(keywords=name_game, count=1)
        exact_elements = exact_results.get('data', {}).get('Catalog', {}).get('searchStore', {}).get('elements', [])
        if exact_elements:
            game = exact_elements[0]
            print(f"{game['title']}")
            print(f"ID: {game['id']}")
            print(
                f"{game.get('price', {}).get('totalPrice', {}).get('fmtPrice', {}).get('originalPrice', 'Бесплатно')}")
            product_slug = game.get('productSlug')
            if product_slug:
                print(f"https://store.epicgames.com/ru/p/{product_slug}")
            else:
                url_mapping = game.get('urlSlug') or game.get('catalogNs', {}).get('mappings', [{}])[0].get('pageSlug')
                if url_mapping:
                    print(f"https://store.epicgames.com/ru/p/{url_mapping}")
                else:
                    print(f"https://store.epicgames.com/ru/p/{game['id']}")
        else:
            print("Такой игры не найдено на данном сайте")
    except EGSNotFound as e:
        print(f"Неизвестная ошибка - {e}")
    except EGSException as e:
        print(f"Неизвестная ошибка - {e}")
    except Exception as e:
        print(f"Неизвестная ошибка - {e}")

        
if __name__ == "__main__":
    x = input(">> ")
    parsing_store_epicgames_com(x)