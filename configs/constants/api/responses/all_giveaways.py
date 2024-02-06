from typing import Dict

# RESPONSE KEYS
STEAM_RESPONSE_KEY = 'steam_giveaways'
EPIC_GAMES_RESPONSE_KEY = "epic_games_giveaways"
GOG_RESPONSE_KEY = "gog_giveaways"


# RESPONSE
ALL_GIVEAWAYS_DEFAULT_RESPONSE: Dict[str, list] = {

    STEAM_RESPONSE_KEY: [
        {'title': 'The Sims™ 4 My First Pet Stuff',
         'image_url': 'https://cdn.akamai.steamstatic.com/steam/apps/1235753/header.jpg',
         'game_url': 'https://store.steampowered.com/app/1235753/The_Sims_4_My_First_Pet_Stuff/?snr=1_7_7_2300_150_1'},
    ],

    EPIC_GAMES_RESPONSE_KEY: [
        {'title': "Marvel's Guardians of the Galaxy",
         'image_url': 'https://cdn1.epicgames.com/offer/d5241c76f178492ea1540fce45616757/Free-Game-17_1920x1080-5014a073a3666df3541f1913b3af38c1?h=480&quality=medium&resize=1&w=854',
         'game_url': 'https://store.epicgames.com/en-US/p/marvels-guardians-of-the-galaxy'},

        {'title': 'Sail Forth',
         'image_url': 'https://cdn1.epicgames.com/spt-assets/bf6f7c896b214dd891aa10debb6fbf50/sail-forth-1h4ru.jpg?h=480&quality=medium&resize=1&w=854',
         'game_url': 'https://store.epicgames.com/en-US/p/sail-forth-51847e'}
    ],

    GOG_RESPONSE_KEY: [
        {'title': 'Witcher 3',
         'image_url': 'https://images.gog-statics.com/ca20a040b7e7dbf11f954b4fa85e1ecdcf8f95eeba8ebf71f89455794eec80f2_product_tile_117h.jpg',
         'game_url': 'https://www.gog.com/game/the_witcher_3_wild_hunt'}
    ]
}
