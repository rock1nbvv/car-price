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
            checked:'',
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
            if (this.task.title === '' || this.task === null || this.task.value === 0
                || this.age === '' || this.age === null || this.age.value === 0
                || this.mileage === '' || this.mileage === null || this.mileage.value === 0
                || this.repairments === '' || this.repairments === null || this.repairments.value === 0) {
                alert('Please fill all the fields');
            } else {
                alert(this.age + ' ' + this.mileage + ' ' + this.repairments)
                this.printCar({age: this.age, mileage: this.mileage, repairments: this.repairments})

                await this.getTasks()

                await this.sendRequest(window.location + 'create', 'post', JSON.stringify(this.task))

                await this.getTasks()

                this.task.title = ''
                this.age = ''
                this.mileage = ''
                this.repairments= ''
            }
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
        printCar(Car) {
            console.log('Car age is ' + Car.age)
            console.log('Car mileage is ' + Car.mileage)
            console.log('Car repairments number is ' + Car.repairments)

        }
    },
    delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')
