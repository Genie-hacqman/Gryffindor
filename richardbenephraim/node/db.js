
const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

const uri = process.env.MONGODB_URI;

const connectDB = async() => await mongoose.connect(uri)
.then(
    () => {
        console.log("connect successfully ")
    }
).catch(
    () => {
        console.log("there is an error with your server")
    }
)