const arrows = document.querySelectorAll(".arrow");
const movieLists = document.querySelectorAll(".movie-list");

arrows.forEach((arrow, i) => {
  const itemNumber = movieLists[i].querySelectorAll("img").length;
  const itemWidth = 270; // Width of each movie item
  const itemsToShow = 6; // Number of items to show at a time
  const visibleWidth = itemWidth * itemsToShow; // Width for the visible items
  let clickCounter = 0;

  arrow.addEventListener("click", () => {
    const maxOffset = (itemNumber - itemsToShow) * itemWidth;
    clickCounter++;

    if (clickCounter * visibleWidth > maxOffset) {
      // Reset to start if reached the end
      clickCounter = 0;
      movieLists[i].style.transform = "translateX(0)";
    } else {
      // Move to next set of items
      movieLists[i].style.transform = `translateX(-${clickCounter * visibleWidth}px)`;
    }
  });

  console.log(Math.floor(window.innerWidth / 270));
});

// TOGGLE
const ball = document.querySelector(".toggle-ball");
const items = document.querySelectorAll(
  ".container,.movie-list-title,.navbar-container,.sidebar,.left-menu-icon,.toggle"
);

ball.addEventListener("click", () => {
  items.forEach((item) => {
    item.classList.toggle("active");
  });
  ball.classList.toggle("active");
});

document.addEventListener("DOMContentLoaded", function () {
  const carouselItems = document.querySelector(".carousel-items");
  const prevButton = document.querySelector(".carousel-prev");
  const nextButton = document.querySelector(".carousel-next");

  let currentIndex = 0;
  const itemCount = document.querySelectorAll(".carousel-item").length;

  function showNextSlide() {
      currentIndex = (currentIndex + 1) % itemCount;
      updateCarousel();
  }

  function showPrevSlide() {
      currentIndex = (currentIndex - 1 + itemCount) % itemCount;
      updateCarousel();
  }

  function updateCarousel() {
      const offset = -currentIndex * 100;
      carouselItems.style.transform = `translateX(${offset}%)`;
  }

  prevButton.addEventListener("click", showPrevSlide);
  nextButton.addEventListener("click", showNextSlide);

  setInterval(showNextSlide, 5000); // Change slide every 5 seconds
});
