<template>
  <div class="main-page">
    <div class="container" style="padding-top:35px; width: 75vw;">
      <!-- <h2>Carousel Example</h2> -->
      <div
        id="myCarousel"
        class="carousel slide"
        data-ride="carousel"
        style="background-color: white;"
      >
        <!-- Indicators -->
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>

        <!-- Wrapper for slides -->
        <div class="carousel-inner carousel-border-radius">
          <div class="item active">
            <a :href="slides.first.link">
              <img
                :src="slides.first.img_src"
                :alt="slides.first.img_alt"
                style="width:100%;"
              />
            </a>
            <div class="carousel-caption">
              <h3>{{ slides.first.caption }}</h3>
              <p>{{ slides.first.txt }}</p>
            </div>
          </div>

          <div class="item">
            <a :href="slides.second.link">
              <img
                :src="slides.second.img_src"
                :alt="slides.second.img_alt"
                style="width:100%;"
              />
            </a>
            <div class="carousel-caption">
              <h3>{{ slides.second.caption }}</h3>
              <p>{{ slides.second.txt }}</p>
            </div>
          </div>

          <div class="item">
            <a :href="slides.third.link">
              <img
                :src="slides.third.img_src"
                :alt="slides.third.img_alt"
                style="width:100%;"
              />
            </a>
            <div class="carousel-caption">
              <h3>{{ slides.third.caption }}</h3>
              <p>{{ slides.third.txt }}</p>
            </div>
          </div>
        </div>

        <!-- Left and right controls -->
        <a
          class="left carousel-control carousel-border-radius"
          href="#myCarousel"
          data-slide="prev"
        >
          <span class="glyphicon glyphicon-chevron-left"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="right carousel-control carousel-border-radius"
          href="#myCarousel"
          data-slide="next"
        >
          <span class="glyphicon glyphicon-chevron-right"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    <h1 style="text-align:center; margin: 60px auto 60px auto;">
      Filtrar por categoría
    </h1>
    <div class="categories-container" id="categories-container">
      <div class="image">
        <router-link :to="`${categories.first.link}`">
          <img
            class="image__img"
            :src="categories.first.img_src"
            :alt="categories.first.img_alt"
          />

          <div class="image__overlay image__overlay--blur">
            <div class="image__title">{{ categories.first.img_title }}</div>
            <p class="image__description">
              {{ categories.first.img_description }}
            </p>
          </div>
        </router-link>
      </div>
      <div class="image">
        <router-link :to="`${categories.second.link}`">
          <img
            class="image__img"
            :src="categories.second.img_src"
            :alt="categories.second.img_alt"
          />

          <div class="image__overlay image__overlay--blur">
            <div class="image__title">{{ categories.second.img_title }}</div>
            <p class="image__description">
              {{ categories.second.img_description }}
            </p>
          </div>
        </router-link>
      </div>
      <div class="image">
        <router-link :to="`${categories.third.link}`">
          <img
            class="image__img"
            :src="categories.third.img_src"
            :alt="categories.third.img_alt"
          />

          <div class="image__overlay image__overlay--blur">
            <div class="image__title">{{ categories.third.img_title }}</div>
            <p class="image__description">
              {{ categories.third.img_description }}
            </p>
          </div>
        </router-link>
      </div>
      <div class="image">
        <router-link :to="`${categories.fourth.link}`">
          <img
            class="image__img"
            :src="categories.fourth.img_src"
            :alt="categories.fourth.img_alt"
          />

          <div class="image__overlay image__overlay--blur">
            <div class="image__title">{{ categories.fourth.img_title }}</div>
            <p class="image__description">
              {{ categories.fourth.img_description }}
            </p>
          </div>
        </router-link>
      </div>
    </div>
    <div class="main-component">
      <router-view v-on:back2login="back2login"> </router-view>
    </div>
  </div>
</template>

<script>
export default {
  // name: "App",
  name: "mainPage",
  data: function() {
    return {
      slides: {
        first: {
          link: "",
          img_src: "https://p2.piqsels.com/preview/330/534/353/seat-chair-theatre-dark.jpg",
          img_alt: "Cinematografía",
          caption: "Industria del arte cinematográfico",
          txt: "",
        },
        second: {
          link: "",
          img_src: "https://live.staticflickr.com/5025/5679417968_a86046e1e8_b.jpg",
          img_alt: "Diego Velasquez - Christ in the House",
          caption: "Christ in the House",
          txt: "by Diego Velasquez",
        },
        third: {
          link: "",
          img_src: "https://cacofoniamilano.com/woo/wp-content/uploads/2017/04/1200px-georges_seurat_031-kopia-1024x678.jpg",
          img_alt: "George Seurat",
          caption: "Una tarde de domingo en la lisla La Grande Jatte",
          txt: "George Seurat",
        },
      },
      categories: {
        first: {
          link: "/products/category/pintura",
          img_src:
            "https://i.pinimg.com/236x/ed/f4/b1/edf4b1824f7a3d61cefa8bf15f77e82a.jpg",
          img_alt: "Categoría pintura",
          img_title: "Pinturas",
          img_description: "El arte de la representación",
        },
        second: {
          link: "/products/category/escultura",
          img_src:
            "https://i.pinimg.com/236x/4e/24/0b/4e240bc4899d6831b1c64a68fb3bc6d2.jpg",
          img_alt: "Categoría escultura",
          img_title: "Esculturas",
          img_description: "El arte de modelar",
        },
        third: {
          link: "/products/category/musica",
          img_src:
            "https://i.pinimg.com/236x/f5/16/0f/f5160f91e0b23a04b4270e858fac2919.jpg",
          img_alt: "Categoría música",
          img_title: "Música",
          img_description: "El arte de las musas",
        },
        fourth: {
          link: "/products/category/cine",
          img_src:
            "https://i.pinimg.com/236x/99/72/e5/9972e549461642766930cdd3845d73f4.jpg",
          img_alt: "Categoría cine",
          img_title: "Cine",
          img_description: "El séptimo arte",
        },
      },
    };
  },
  props: {
    toCategoriesSection: {
      default: "false",
      type: String,
    },
  },
  components: {},
  methods: {},
  mounted: function() {
    if (this.toCategoriesSection === "true")
      window.scrollTo(window.scrollX, window.scrollY + 650);
  },
  created: function() {
    window.scroll(0, 0);
  },
};
</script>

<style scoped>
.main-page {
  padding-top: 90px;
  z-index: 900;
}
/* ---categories-start-- */
.categories-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin: 30px 30px 90px 30px;
}
.image {
  position: relative;
  height: 400px;
  width: 270px;
  border-radius: 15px;
}

.image__img {
  display: block;
  height: 400px;
  width: 100%;
  border-radius: 15px;
}

.image__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  color: #ffffff;
  font-family: "Quicksand", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.25s;
  border-radius: 15px;
}

.image__overlay--blur {
  backdrop-filter: blur(5px);
}

.image__overlay--primary {
  background: #009578;
}

.image__overlay > * {
  transform: translateY(20px);
  transition: transform 0.25s;
}

.image__overlay:hover {
  opacity: 1;
}

.image__overlay:hover > * {
  transform: translateY(0);
}

.image__title {
  font-size: 2em;
  font-weight: bold;
}

.image__description {
  font-size: 1.25em;
  margin-top: 0.25em;
}
/* ---categories-end--- */

.product-categories:hover {
  opacity: 0.5;
}
.carousel-border-radius {
  border-radius: 15px;
}

/* --- footer start ---*/
/* .brand {
  font-size: 20px;
}

.info-links a {
  color: white;
  margin: auto 15px auto 5px;
}
i {
  margin: auto 10px auto 10px;
  font-size: 2rem;
  color: white;
}
footer {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  align-items: center;
  text-align: center;
  display: flex;
  justify-content: space-evenly;

  color: rgb(235, 231, 231);
  padding: 25px 5px 25px 5px;
  background-color: black;
} */

/* --- footer end --- */
/* .header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 5px 5px 5px;
  background-color: black;
}

.nav {
  display: flex;
  justify-content: space-evenly;
}

.nav button {
  color: rgb(235, 231, 231);
  background-color: black;
  margin: auto 10px auto 10px;
} */
</style>
