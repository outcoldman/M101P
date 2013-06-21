var mongoose = require('mongoose')
    , Schema = mongoose.Schema;

var FunnyNumberSchema = new Schema({
    value : Number
});

mongoose.model('FunnyNumber', FunnyNumberSchema);


var questionsSchema = new Schema({
    question : String,
    answer : String
}, { collection : 'hw1' })

mongoose.model('questions', questionsSchema)