function addBookRow(
  bookId,
  nombre_libro,
  autor,
  precio,
  imagen,
) {
  const booksList = document.querySelector("#back");
  const article = document.createElement("article");
  article.id = `book-${bookId}`;
  article.className = "book-item-v2";
  article.innerHTML = `
    <div class="producto-libro">
      <a href="#" class="link-libro">
        <img src="/static/img/${imagen}" alt="Tapa del libro" class="imagen-libro">
      </a>
      <p class="descripcion-libro">${nombre_libro} Autor: ${autor} Precio: ${precio}</p>
    </div>
  `
  booksList.appendChild(article);
}

window.addEventListener("DOMContentLoaded", async () => {
  const response = await fetch("/api/books");
  const data = await response.json();
  for (const book of data) {
    // console.log(book)
    addBookRow(
      book.id_libros,
      book.nombre_libro,
      book.autor,
      book.precio,
      book.imagen,
    );
  }
});
