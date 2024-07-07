function addBookRow(
  bookId,
  name,
  author,
  price,
) {
  const booksList = document.querySelector("#back");
  const article = document.createElement("article");
  article.id = `book-${bookId}`;
  article.className = "book-item-v2";
  article.innerHTML = `
    <div class="producto-libro">
      <a href="#" class="link-libro">
        <img src="/static/images/${name}.jpg" alt="Tapa del libro" class="imagen-libro">
      </a>
      <p class="descripcion-libro">${name} Autor: ${author} Precio: ${price}</p>
    </div>
  `
  booksList.appendChild(article);
}

window.addEventListener("DOMContentLoaded", async () => {
  const response = await fetch("/api/books");
  const data = await response.json();
  for (const book of data) {
    addBookRow(
      book.id,
      book.name,
      book.author,
      book.price,
    );
  }
});
