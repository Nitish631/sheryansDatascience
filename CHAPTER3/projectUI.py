import streamlit as st
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# Game Functions
# -----------------------------
def check_winner(b):
    # Rows
    if 3 in np.sum(b, axis=0) or 3 in np.sum(b, axis=1):
        return "X"

    # Columns
    if -3 in np.sum(b, axis=0) or -3 in np.sum(b, axis=1):
        return "O"

    # Diagonals
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    # Draw
    if not 0 in b:
        return "DRAW"

    return None


def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.winner = None


# -----------------------------
# Initialize Session State
# -----------------------------
if "board" not in st.session_state:
    reset_game()


# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
    <style>

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 30px;
    }

    .player {
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        height: 100px;
        font-size: 45px;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #555;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<div class="title">🎮 TIC TAC TOE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Classic 3 × 3 Tic Tac Toe Game</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Current Player
# -----------------------------
if not st.session_state.game_over:

    if st.session_state.current == 1:
        player = "X"
    else:
        player = "O"

    st.markdown(
        f'<div class="player">Current Player: {player}</div>',
        unsafe_allow_html=True
    )


# -----------------------------
# Game Board
# -----------------------------
board = st.session_state.board

for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        value = board[row, col]

        if value == 1:
            symbol = "❌"
        elif value == -1:
            symbol = "⭕"
        else:
            symbol = " "

        # Empty cell
        if value == 0 and not st.session_state.game_over:

            if cols[col].button(
                symbol,
                key=f"cell_{row}_{col}"
            ):

                # Put current player's mark
                board[row, col] = st.session_state.current

                # Check result
                result = check_winner(board)

                if result is not None:
                    st.session_state.game_over = True
                    st.session_state.winner = result

                else:
                    # Switch player
                    if st.session_state.current == 1:
                        st.session_state.current = -1
                    else:
                        st.session_state.current = 1

                st.rerun()

        else:
            cols[col].button(
                symbol,
                key=f"cell_{row}_{col}",
                disabled=True
            )


# -----------------------------
# Game Result
# -----------------------------
if st.session_state.game_over:

    result = st.session_state.winner

    if result == "DRAW":
        st.warning("🤝 Ohoo! It's a DRAW!")

    else:
        if result == "X":
            st.success("🎉 ❌ X WINS!")
        else:
            st.success("🎉 ⭕ O WINS!")

    st.button(
        "🔄 New Game",
        on_click=reset_game
    )


# -----------------------------
# Reset Button
# -----------------------------
if not st.session_state.game_over:

    st.write("")

    st.button(
        "🔄 Reset Game",
        on_click=reset_game
    )