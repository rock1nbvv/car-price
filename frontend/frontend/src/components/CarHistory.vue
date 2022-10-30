<template>
  <div v-for="(car, index) in carHistory" :key="index">
    <div
      class="card"
      style="
        width: 18rem;
        float: left;
        position: relative;
        margin-left: 20px;
        margin-bottom: 10px;
      "
    >
      <div class="card-body">
        <h5 class="card-title">{{ car.brand }} {{ car.name }}</h5>
        <p class="card-text">Age: {{ car.age }}</p>
        <p>Mileage: {{ car.mileage }}</p>
        <p>Repairments: {{ car.repairments }}</p>
        <p>Evaluated Price: {{ car.est_price }}</p>
        <!--        <a href="#" class="btn btn-primary">Go somewhere</a>-->
      </div>
    </div>
    <p></p>
  </div>
</template>

<script>
export default {
  name: "CarHistory",
  data() {
    return {
      msg: "Hello, this is History",
      carHistory: [],
    };
  },
  async created() {
    await this.getCarHistory();

    this.carHistory = Array.from(this.cars);
  },
  methods: {
    async sendRequest(url, method, data) {
      const myHeaders = new Headers({
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
      });

      const response = await fetch(url, {
        method: method,
        headers: myHeaders,
        body: data,
      });

      return response;
    },
    async getCarHistory() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getCarHistory",
        "get"
      );
      this.cars = await response.json();
    },
  },
};
</script>
