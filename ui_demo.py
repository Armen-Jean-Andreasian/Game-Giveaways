# streamlit run ui_demo.py

import streamlit as st
from database.cache import Cache


name = "Game Giveaways"
st.title("Game Giveaways")
st.divider()


def request_against_cache():
    result = Cache.get_all_data()
    return result


giveaways: dict[str:list[dict[str:dict]]] = request_against_cache()

for store_name, giveaway_data in giveaways.items():
    col1, col2 = st.columns(2)  # Create two columns

    for i, game_data in enumerate(giveaway_data):
        if i % 2 == 0:
            current_col = col1
        else:
            current_col = col2

        store = "Steam" if store_name == "steam_giveaways" else "Epic Games"

        current_col.text(f"Name: {game_data['title']}\nStore:{store}")
        current_col.image(image=game_data['image_url'], use_column_width="always")
        current_col.link_button(label='Open Giveaway Page', url=game_data['game_url'])

    st.divider()
