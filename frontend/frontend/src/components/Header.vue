<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col">
        <nav class="navbar navbar-expand-lg navbar-light">
          <a class="navbar-brand" href="#">
            <img
              src="../assets/logo.svg"
              width="40"
              height="40"
              class="d-inline-block align-center"
              alt=""
            />
            <span class="logo-text d-inline-block"
              >Fuzzy Car Price Estimator</span
            >
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <router-link to="/" class="nav-item nav-link"
                >Evaluation</router-link
              >
              <router-link to="/history" class="nav-item nav-link"
                >History</router-link
              >
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
};
</script>

<style scoped>
.logo-text {
  margin-left: 0.5em;
}
</style>
