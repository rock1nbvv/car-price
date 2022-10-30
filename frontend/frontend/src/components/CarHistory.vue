<template>
  <div></div>
  <div v-for="(car, index) in carHistory" :key="index">
    <p>
      For {{ car }} id is {{ car.id }} model is {{ car.name }} price is
      {{ car.price }} brand is {{ car.brand }}
    </p>
    <v-card elevation="12"></v-card>
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
