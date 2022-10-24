const {createApp} = Vue
const TaskApp = {

    data() {
        return {
            task: {
                'title': ''
            },
            tasks: [],
            selected: '',
            age: '',
            mileage: '',
            repairments: '',
            cars: [
    {brand: 'Toyota', price: 50000},
    {brand: 'Ford', price: 80000},
    {brand: 'VW', price: 90000},
    {brand: 'Mercedes', price: 165000}
]
        }

    },
    async created() {
        await this.getTasks()
    },
    methods: {
        async sendRequest(url, method, data) {
            const myHeaders = new Headers({
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            })

            const response = await fetch(url, {
                method: method,
                headers: myHeaders,
                body: data
            })

            return response
        },
        async getTasks() {
            const response = await this.sendRequest(window.location, 'get')
            this.tasks = await response.json()

        },
        async createTask() {
            await this.getTasks()

            await this.sendRequest(window.location + 'create', 'post', JSON.stringify(this.task))

            await this.getTasks()

            this.task.title = ''
        },
        async deleteTask(task) {
            await this.sendRequest(window.location + 'delete', 'post', JSON.stringify(task))
            await this.getTasks()
        },
        async completeTask(task) {
            await this.sendRequest(window.location + 'complete', 'post', JSON.stringify(task))
            await this.getTasks()
        },
        validateNumber: (event) => {
            let keyCode = event.keyCode;
            if (keyCode < 48 || keyCode > 57) {
                event.preventDefault();
            }
        },
        warn(age, mileage, repairments) {
            if (this.age === '' || this.age === null || this.age.value === 0
                || this.mileage === '' || this.mileage === null || this.mileage.value === 0
                || this.repairments === '' || this.repairments === null || this.repairments.value === 0) {
                alert('Please fill all the fields');
            } else {
                alert(age + ' ' + mileage + ' ' + repairments)
                this.printCar({age: age, mileage: mileage, repairments: repairments})
            }
        },
        printCar(Car) {
            console.log('Car age is ' + Car.age)
            console.log('Car mileage is ' + Car.mileage)
            console.log('Car repairments number is ' + Car.repairments)

        }
    },
    delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')
