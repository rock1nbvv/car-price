<template>
  <div class="container">
    <div class="row">
      <div class="col-6 mx-auto mt-5">
        <!--        <p>{{ msg }}</p>-->
        <h1>Used Car Price Calculator</h1>
        <p>
          Get fair and unbiased price quote for your used car using our car
          valuation calculator.
        </p>
        <form @submit.prevent="evaluateCar" class="mx-auto">
          <div class="row">
            <div class="col-9">
              <div class="mb-3">
                <label for="ageInput" class="form-label"
                  >Age of the car is: {{ age }}</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="ageInput"
                  v-model="age"
                  placeholder="Enter age of the car"
                  @keypress="validateNumber"
                />
              </div>
              <div class="mb-3">
                <label for="mileage" class="form-label"
                  >Kilometers {{ mileage }}</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="mileage"
                  v-model="mileage"
                  placeholder="Enter kilometers driven"
                  @keypress="validateNumber"
                />
              </div>
              <div class="mb-3">
                <label for="repairments" class="form-label"
                  >Repairments {{ repairments }}
                </label>
                <input
                  type="text"
                  class="form-control"
                  id="repairments"
                  v-model="repairments"
                  placeholder="Enter number of repairments"
                  @keypress="validateNumber"
                />
              </div>
              <div class="mb-3">
                <!--<label for="brand" class="form-label"
                  >Brand price: { brand_price }</label
                >
                <select
                  class="form-select"
                  id="brand"
                  v-model="brand_price"
                  placeholder="Select car brand"
                >
                  <option v-for="brand in brands" :value="brand.brand">
                { brand.name }
              </option>
                </select>-->
                <div class="mb-3">
                  <label for="brand" class="form-label"
                    >Car make {{ brandName }}</label
                  >
                  <select
                    class="form-select"
                    id="brand"
                    v-model="brandName"
                    @change="getModelsFromBrands()"
                  >
                    <option :value="null" disabled selected>
                      Select car brand
                    </option>
                    <option
                      v-for="(brand, index) in brands"
                      v-bind:value="brand.brand"
                      v-bind:key="index"
                    >
                      {{ brand.brand }}
                    </option>
                  </select>
                </div>
                <div class="mb-3" v-if="brandName !== null">
                  <label for="model" class="form-label"
                    >Car model {{ modelId }}</label
                  >
                  <select
                    class="form-select"
                    id="model"
                    v-model="modelId"
                    @change="getAvgPrice()"
                  >
                    <option :value="null" disabled selected>
                      Select car model
                    </option>
                    <option
                      v-for="(model, index) in models"
                      v-bind:value="model.id"
                      v-bind:key="index"
                    >
                      {{ model.name }}
                    </option>
                  </select>
                </div>
                <div class="mb-3" v-if="selectedCarObj !== null">
                  <p>Average price of this model: {{ selectedCarObj.price }}</p>
                </div>
                <div class="mb-3" v-if="predictedPrice !== null">
                  <p>Predicted price of your car: {{ predictedPrice }}</p>
                </div>
              </div>
              <div class="mb-3">
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="checkbox"
                    v-model="areDocsInOrder"
                  />
                  <label class="form-check-label" for="checkbox">
                    All documents are in order {{ areDocsInOrder }}
                  </label>
                </div>
              </div>
              <button class="btn btn-success w-100" type="submit">
                Check Value
              </button>
            </div>
          </div>
        </form>
        <!--<div class="mt-5">
      <div class="card mb-3" v-for="(task, index) in tasks" :key="index">
        <div
          class="card-body row justify-content-between px-4"
          @dblClick="completeTask(task)"
          :class="{ completed: task.completed }"
        >
          For { task.taskTitle } car price is { task.est_price }
          <button
            type="submit"
            class="btn-close"
            @click="deleteTask(task)"
          ></button>
        </div>
      </div>
    </div>-->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarEvaluation",
  data() {
    return {
      msg: "Hello, this is Evaluation",
      task: {
        title: "",
      },
      tasks: [],
      selected: "",
      age: "",
      mileage: "",
      repairments: "",
      checked: false,
      brand_price: "",
      brands: [],
      brandName: null,
      cars: [],
      modelId: null,
      models: [],
      selectedCarObj: null,
      car: {},
      predictedPrice: null,
      areDocsInOrder: false,
    };
  },
  async created() {
    await this.getCars();

    let carsCopy = Array.from(this.cars);

    const RemoveDuplicates = (array, key) => {
      return array.reduce((arr, item) => {
        const removed = arr.filter((i) => i[key] !== item[key]);
        return [...removed, item];
      }, []);
    };

    carsCopy = RemoveDuplicates(carsCopy, "brand");

    this.brands = carsCopy;
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
    async getCars() {
      const response = await this.sendRequest(
        "http://127.0.0.1:5000/api/getBrands",
        "get"
      );
      this.cars = await response.json();
    },
    async evaluateCar() {
      if (
        this.age === "" ||
        this.age === null ||
        this.age.value === 0 ||
        this.mileage === "" ||
        this.mileage === null ||
        this.mileage.value === 0 ||
        this.repairments === "" ||
        this.repairments === null ||
        this.repairments.value === 0
      ) {
        alert("Please fill all the fields");
      } else {
        const car = {
          age: this.age,
          mileage: this.mileage,
          repairments: this.repairments,
          areDocsInOrder: this.areDocsInOrder,
          selectedCarObj: this.selectedCarObj,
        };
        console.log(JSON.stringify(car));
        const response = await this.sendRequest(
          "http://127.0.0.1:5000/api/evaluate",
          "post",
          JSON.stringify(car)
        );
        const temp = await response.json();
        this.predictedPrice = temp.price;

        this.task.title = "";
        this.age = "";
        this.mileage = "";
        this.repairments = "";
      }
    },
    getModelsFromBrands() {
      let testBrand = this.brandName;
      let newArray = this.cars.filter(function (el) {
        return el.brand == testBrand;
      });
      this.selectedCarObj = null;
      this.modelId = null;
      this.predictedPrice = null;
      this.models = newArray;
    },
    getAvgPrice() {
      let testModelId = this.modelId;
      let newArray = this.cars.filter((obj) => {
        return obj.id === testModelId;
      });
      this.predictedPrice = null;
      this.selectedCarObj = newArray[0];
    },
  },
};
</script>
