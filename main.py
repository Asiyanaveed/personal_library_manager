import streamlit as st
import json

def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

library = load_library()

st.title("📚Personal Library App")
menu = st.sidebar.radio("Select an option", ["View Library", "Add Book","Delete Book","Search Book","Save and Quit"])
    
if menu == "View Library":
    st.sidebar.header("View Library")
    if library:
        st.table(library)
    else:
        st.write("❌No books in library. ➕Add some books!")

elif menu == "Add Book":
    st.sidebar.header("Add new Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2022, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read?")

    if st.button("Add Book"):
        library.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        })
        save_library(library)
        st.success("✅Book added successfully!")
        st.rerun()

elif menu == "Delete Book":
    st.sidebar.header("Delete Book")
    book_title = [book["title"] for book in library]

    if book_title:
        selected_book = st.selectbox("Select a book to delete", book_title)
        if st.button("Delete Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library(library)
            st.success("✅Book deleted successfully!")
            st.rerun()
    else:
        st.write("👎No books in library. ➕Add some books!")

elif menu == "Search Book":
    st.sidebar.header("Search Book")
    search_term = st.text_input("Enter title or author to search")

    if st.button("Search"):
        result = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if result:
            st.table(result)
        else:
            st.warning("😌No books found!")

elif menu == "Save and Quit":
    save_library(library)
    st.success("🎉🎊Library saved successfully!")
    st.balloons()
