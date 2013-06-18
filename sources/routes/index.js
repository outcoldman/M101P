
/*
 * GET home page.
 */

var mongoose = require('mongoose')
    , FunnyNumber = mongoose.model('FunnyNumber');

exports.index = function(req, res){
    FunnyNumber.find().exec(function(err, numbers){
        var magic = 0;
        for (var i = 0 ; i < numbers.length; i++) {
            if (numbers[i].value % 3 == 0) {
                magic += numbers[i].value;
            }
        }

        console.log(magic);
        res.render('index', { title: 'Express', magicNumber: magic });
    });
};