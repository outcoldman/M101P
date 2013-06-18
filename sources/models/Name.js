var mongoose = require('mongoose')
    , Schema = mongoose.Schema;

var NameSchema = new Schema({
    name : String
});

mongoose.model('Name', NameSchema);