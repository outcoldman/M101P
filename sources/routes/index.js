
/*
 * GET home page.
 */

var mongoose = require('mongoose')
    , FunnyNumber = mongoose.model('FunnyNumber');

exports.index = function(req, res){
    console.log(req.route.params.n);

    FunnyNumber
        .find()
        .limit(1)
        .skip(req.route.params.n)
        .sort('value')
        .exec(function(err, numbers){

            var result;
            for (var i = 0 ; i < numbers.length; i++) {
                result = numbers[i].value + '\n';
            }

            console.log(result);
            res.render('index', { title: 'Express', result: result });
    });
};